import marimo

__generated_with = "0.19.8"
app = marimo.App(width="medium")


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


if __name__ == "__main__":
    app.run()
