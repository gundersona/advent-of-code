import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Read input data
    """)
    return


@app.cell
def _():
    with open("example_input.txt", "r") as _f:
        example_input = _f.read().split(sep=",")
    example_input
    return (example_input,)


@app.cell
def _():
    with open("input.txt", "r") as _f:
        input = _f.read().split(sep=",")
    input
    return (input,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 1
    """)
    return


@app.function
def sum_invalid_IDs_1(input):
    invalid_id_sum = 0
    for line in input:
        start, end = map(int, line.split("-"))
        for id in range(start, end + 1):
            id = str(id)
            num_digits = len(id)
            if num_digits % 2 == 0:
                if id[0 : num_digits // 2] == id[num_digits // 2 : num_digits]:
                    invalid_id_sum += int(id)
    return invalid_id_sum


@app.cell
def _():
    example_solution_1 = 1227775554
    return (example_solution_1,)


@app.cell
def _(example_input, example_solution_1, mo):
    mo.md(rf"""
    Example solution 1 is correct: {sum_invalid_IDs_1(example_input) == example_solution_1}
    """)
    return


@app.cell
def _(input, mo):
    mo.md(rf"""
    Part 1 Solution: {sum_invalid_IDs_1(input)}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Test Case
    """)
    return


@app.cell
def _():
    a = "123123123123"
    return (a,)


@app.cell
def _(a):
    factors = [i for i in range(1, len(a) // 2 + 1) if len(a) % i == 0]
    factors
    return (factors,)


@app.cell
def _(a, factors):
    for f in factors:
        id_chunked = [a[i : i + f] for i in range(0, len(a), f)]
        print(f"id is invalid: {len(set(id_chunked)) == 1}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**Warning:** It's important to break out of the factor loop immediately after encountering an invalid ID to avoid double-counting it!"
        ),
        kind="warn",
    )
    return


@app.function
def sum_invalid_IDs_2(input):
    invalid_id_sum = 0
    for line in input:
        start, end = map(int, line.split("-"))
        for id in range(start, end + 1):
            id = str(id)
            factors = [
                i for i in range(1, len(id) // 2 + 1) if len(id) % i == 0
            ]
            for f in factors:
                # break id into equal length chunks
                id_chunked = [id[i : i + f] for i in range(0, len(id), f)]
                # if all chunks are equal, id is invalid
                if len(set(id_chunked)) == 1:
                    invalid_id_sum += int(id)
                    break  # avoid double counting invalid id's
    return invalid_id_sum


@app.cell
def _():
    example_solution_2 = 4174379265
    return (example_solution_2,)


@app.cell(hide_code=True)
def _(example_input, example_solution_2, mo):
    mo.md(rf"""
    Example solution 2 is correct: {sum_invalid_IDs_2(example_input) == example_solution_2}
    """)
    return


@app.cell(hide_code=True)
def _(input, mo):
    mo.md(rf"""
    Part 2 Solution: {sum_invalid_IDs_2(input)}
    """)
    return


@app.cell
def _(
    mo,
    total_invalid_actual_part1,
    total_invalid_actual_part2,
    total_invalid_example_part1,
    total_invalid_example_part2,
):
    mo.md(f"""
    ### Invalid ID counts summary

    - Example Input:
      - Total invalid IDs (Part 1): {total_invalid_example_part1}
      - Total invalid IDs (Part 2): {total_invalid_example_part2}

    - Actual Input:
      - Total invalid IDs (Part 1): {total_invalid_actual_part1}
      - Total invalid IDs (Part 2): {total_invalid_actual_part2}
    """)
    return


@app.cell
def _(alt, example_counts):
    chart_example = alt.Chart(example_counts).transform_fold(
        ["count_part1", "count_part2"], as_=["part", "count"]
    ).mark_bar().encode(
        x=alt.X("line_index:O", title="Line Index"),
        y=alt.Y("count:Q", title="Invalid ID Count"),
        color=alt.Color("part:N", title="Part", scale=alt.Scale(scheme="tableau10")),
        tooltip=[
            alt.Tooltip("line_index:O", title="Line"),
            alt.Tooltip("start:Q", title="Start"),
            alt.Tooltip("end:Q", title="End"),
            alt.Tooltip("part:N", title="Part"),
            alt.Tooltip("count:Q", title="Invalid Count"),
        ]
    ).properties(title="Example Input: Invalid ID Counts by Line").interactive()

    chart_example
    return


@app.cell
def _(actual_counts, alt):
    chart_actual = alt.Chart(actual_counts).transform_fold(
        ["count_part1", "count_part2"], as_=["part", "count"]
    ).mark_bar().encode(
        x=alt.X("line_index:O", title="Line Index"),
        y=alt.Y("count:Q", title="Invalid ID Count"),
        color=alt.Color("part:N", title="Part", scale=alt.Scale(scheme="tableau10")),
        tooltip=[
            alt.Tooltip("line_index:O", title="Line"),
            alt.Tooltip("start:Q", title="Start"),
            alt.Tooltip("end:Q", title="End"),
            alt.Tooltip("part:N", title="Part"),
            alt.Tooltip("count:Q", title="Invalid Count"),
        ]
    ).properties(title="Actual Input: Invalid ID Counts by Line").interactive()

    chart_actual
    return


if __name__ == "__main__":
    app.run()
