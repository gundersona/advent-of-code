# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
#     "polars==1.38.1",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Day 5
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    from pathlib import Path
    import polars as pl

    return Path, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Read Inputs
    """)
    return


@app.cell
def _(Path):
    example_solution_1 = 3

    example = Path("example.txt").read_text().splitlines()
    example_fresh_ranges = example[: example.index("")]
    example_available_ingredients = example[example.index("") + 1 :]

    input = Path("input.txt").read_text().splitlines()
    input_fresh_ranges = input[: input.index("")]
    input_available_ingredients = input[input.index("") + 1 :]
    return (
        example_available_ingredients,
        example_fresh_ranges,
        example_solution_1,
        input_available_ingredients,
        input_fresh_ranges,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 1
    """)
    return


@app.function
def check_fresh(ranges, id):
    fresh = False
    for range in ranges:
        lower, upper = range.split("-")
        if int(id) >= int(lower) and int(id) <= int(upper):
            fresh = True
            break
    return fresh


@app.function
def count_fresh_ids(ranges, ids):
    total = 0
    for id in ids:
        total += check_fresh(ranges, id)
    return total


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 example check
    """)
    return


@app.cell
def _(example_available_ingredients, example_fresh_ranges, example_solution_1):
    count_fresh_ids(
        example_fresh_ranges, example_available_ingredients
    ) == example_solution_1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 solution
    """)
    return


@app.cell
def _(input_available_ingredients, input_fresh_ranges):
    count_fresh_ids(input_fresh_ranges, input_available_ingredients)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.function
def count_all_fresh_ids(id_ranges):
    ids = 0
    for id_range in id_ranges:
        lower, upper = id_range.split("-")
        ids += int(upper) - int(lower) + 1
        if (int(upper) - int(lower)) < 0:
            print("NEGATIVE RANGE")
    return ids


@app.cell
def _(pl):
    def count_fresh_id_duplicates(id_ranges):

        ids = 0
        data = []
        ranges = [
            row for row in id_ranges
        ]  # deep copy to avoid modifying original

        for i, id_range in enumerate(ranges):
            if id_range == "0-0":
                continue
            lower, upper = map(int, id_range.split("-"))

            for j, id_range_to_compare in enumerate(ranges[i + 1 :]):
                k = i + j + 1
                lower_compare, upper_compare = map(
                    int, id_range_to_compare.split("-")
                )

                # Case 1: entire range overlaps, nothing unique
                if lower_compare >= lower and upper_compare <= upper:
                    overlap_count = upper_compare - lower_compare + 1
                    ids += overlap_count
                    new_range = "0-0"
                    data.append(
                        {
                            "Case": 1,
                            "Range": id_range,
                            "Comparison Range": id_range_to_compare,
                            "ID Count": overlap_count,
                            "New Range": new_range,
                            "New Range End": None,
                        }
                    )
                    ranges[k] = new_range

                # Case 2: top part of range overlaps, bottom part unique
                elif (
                    lower_compare < lower
                    and upper_compare <= upper
                    and upper_compare >= lower
                ):
                    overlap_count = upper_compare - lower + 1
                    ids += overlap_count
                    new_range = f"{lower_compare}-{lower - 1}"
                    data.append(
                        {
                            "Case": 2,
                            "Range": id_range,
                            "Comparison Range": id_range_to_compare,
                            "ID Count": overlap_count,
                            "New Range": new_range,
                            "New Range End": None,
                        }
                    )
                    ranges[k] = new_range

                # Case 3: bottom part of range overlaps, top part unique
                elif (
                    upper_compare > upper
                    and lower_compare >= lower
                    and lower_compare <= upper
                ):
                    overlap_count = upper - lower_compare + 1
                    ids += overlap_count
                    new_range = f"{upper + 1}-{upper_compare}"
                    data.append(
                        {
                            "Case": 3,
                            "Range": id_range,
                            "Comparison Range": id_range_to_compare,
                            "ID Count": overlap_count,
                            "New Range": new_range,
                            "New Range End": None,
                        }
                    )
                    ranges[k] = new_range

                # Case 4: entire range overlaps, top and bottom part unique
                elif lower_compare < lower and upper_compare > upper:
                    overlap_count = upper - lower + 1
                    ids += overlap_count
                    new_range = f"{lower_compare}-{lower - 1}"
                    new_range_end = f"{upper + 1}-{upper_compare}"
                    data.append(
                        {
                            "Case": 4,
                            "Range": id_range,
                            "Comparison Range": id_range_to_compare,
                            "ID Count": overlap_count,
                            "New Range": new_range,
                            "New Range End": new_range_end,
                        }
                    )
                    ranges[k] = new_range
                    ranges.append(new_range_end)

                # Case 5: no overlap
                else:
                    data.append(
                        {
                            "Case": 5,
                            "Range": id_range,
                            "Comparison Range": id_range_to_compare,
                            "ID Count": 0,
                            "New Range": id_range_to_compare,
                            "New Range End": None,
                        }
                    )

        df = pl.DataFrame(
            data,
            schema={
                "Case": pl.Int64,
                "Range": pl.Utf8,
                "Comparison Range": pl.Utf8,
                "ID Count": pl.Int64,
                "New Range": pl.Utf8,
                "New Range End": pl.Utf8,
            },
        )
        return ids, df

    return (count_fresh_id_duplicates,)


@app.cell
def _(count_fresh_id_duplicates):
    def count_all_fresh_ids_no_duplicates(id_ranges):
        a = count_all_fresh_ids(id_ranges)
        b, _ = count_fresh_id_duplicates(id_ranges)
        return a - b

    return (count_all_fresh_ids_no_duplicates,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 example
    """)
    return


@app.cell
def _():
    example_solution_2 = 16
    return


@app.cell
def _(count_all_fresh_ids_no_duplicates, example_fresh_ranges):
    count_all_fresh_ids_no_duplicates(example_fresh_ranges)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 additional example from reddit
    https://www.reddit.com/r/adventofcode/comments/1pf0g8l/2025_day_5_part_2_request_for_additional_sample/
    """)
    return


@app.cell
def _():
    example_fresh_ranges_2 = """
    200-300
    100-101
    1-1
    2-2
    3-3
    1-3
    1-3
    2-2
    50-70
    10-10
    98-99
    99-99
    99-99
    99-100
    1-1
    100-100
    100-100
    100-101
    200-300
    201-300
    202-300
    250-251
    98-99
    100-100
    100-101
    1-101
    """.split()
    return (example_fresh_ranges_2,)


@app.cell
def _(count_fresh_id_duplicates, example_fresh_ranges_2):
    _, _df = count_fresh_id_duplicates(example_fresh_ranges_2)
    _df
    return


@app.cell
def _():
    example_solution_2_2 = 202
    return


@app.cell
def _(count_all_fresh_ids_no_duplicates, example_fresh_ranges_2):
    count_all_fresh_ids_no_duplicates(example_fresh_ranges_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 Solution
    """)
    return


@app.cell
def _(count_all_fresh_ids_no_duplicates, input_fresh_ranges):
    count_all_fresh_ids_no_duplicates(input_fresh_ranges)
    return


if __name__ == "__main__":
    app.run()
