import marimo

__generated_with = "0.19.11"
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
    from pathlib import Path

    return Path, mo


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


@app.cell
def _(example_fresh_ranges):
    lower, upper = example_fresh_ranges[0].split("-")
    upper
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
    ## Part 1 example check
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
    ## Part 1 solution
    """)
    return


@app.cell
def _(input_available_ingredients, input_fresh_ranges):
    count_fresh_ids(input_fresh_ranges, input_available_ingredients)
    return


@app.cell
def _():
    example_solution_2 = 14
    return (example_solution_2,)


@app.function
def count_all_fresh_ids(id_ranges):
    ids = 0
    for id_range in id_ranges:
        lower, upper = id_range.split("-")
        ids += int(upper) - int(lower) + 1
    return ids


@app.function
def count_fresh_id_duplicates(id_ranges):
    ids = 0
    ranges = [
        row for row in id_ranges
    ]  # deep copy to avoid modifying original
    for i, id_range in enumerate(ranges):
        lower, upper = map(int, id_range.split("-"))
        for id_range_to_compare in ranges[i + 1 :]:
            lower_compare, upper_compare = map(
                int, id_range_to_compare.split("-")
            )
            # Case 1: entire range overlaps, nothing unique
            if lower_compare >= lower and upper_compare <= upper:
                ids += upper_compare - lower_compare + 1
                ranges.remove(id_range_to_compare)
            # Case 2: top part of range overlaps, bottom part unique
            elif (
                lower_compare < lower
                and upper_compare <= upper
                and upper_compare >= lower
            ):
                ids += upper_compare - lower + 1
                ranges[i] = f"{lower_compare}-{lower - 1}"
            # Case 3: bottom part of range overlaps, top part unique
            elif (
                upper_compare > upper
                and lower_compare >= lower
                and lower_compare <= upper
            ):
                ids += upper - lower_compare + 1
                ranges[i] = f"{upper + 1}-{upper_compare}"
            # Case 4: entire range overlaps, top and bottom part unique
            elif lower_compare < lower and upper_compare > upper:
                ids += upper - lower + 1
                ranges[i] = f"{lower_compare}-{lower - 1}"
                ranges.append(f"{upper + 1}-{upper_compare}")

    return ids


@app.function
def count_all_fresh_ids_no_duplicates(id_ranges):
    return count_all_fresh_ids(id_ranges) - count_fresh_id_duplicates(
        id_ranges
    )


@app.cell
def _(example_fresh_ranges):
    count_all_fresh_ids_no_duplicates(example_fresh_ranges)
    return


@app.cell
def _(example_fresh_ranges, example_solution_2):
    count_all_fresh_ids_no_duplicates(example_fresh_ranges) == example_solution_2
    return


@app.cell
def _(input_fresh_ranges):
    count_all_fresh_ids_no_duplicates(input_fresh_ranges)
    return


if __name__ == "__main__":
    app.run()
