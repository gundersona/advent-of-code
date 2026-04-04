import marimo

__generated_with = "0.21.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Day 6
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

    return (Path,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 1
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Read Inputs
    """)
    return


@app.cell
def _(Path, mo):
    example_solution_part1 = 4277556


    def read_file(f):
        lines = Path(f).read_text().splitlines()
        return [row.split() for row in lines]


    example = read_file(mo.notebook_location() / "example.txt")
    input = read_file(mo.notebook_location() / "input.txt")
    return example, example_solution_part1, input


@app.cell(hide_code=True)
def _(example, input, mo):
    mo.accordion({"Example Input": example, "Actual Input": input})
    return


@app.function
def solve_problem(worksheet):
    grand_total = 0
    for i in range(len(worksheet[0])):
        math_operation = worksheet[-1][i]
        column_total = int(worksheet[0][i])
        for j in range(1, len(worksheet) - 1):
            if math_operation == "+":
                column_total += int(worksheet[j][i])
            if math_operation == "*":
                column_total *= int(worksheet[j][i])
        grand_total += column_total
    return grand_total


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 example check
    """)
    return


@app.cell
def _(example, example_solution_part1):
    solve_problem(example) == example_solution_part1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 solution
    """)
    return


@app.cell
def _(input):
    solve_problem(input)
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
    ### Read Inputs
    """)
    return


@app.cell
def _(Path, mo):
    example_solution_part2 = 3263827


    def read_file_part2(f):
        return Path(f).read_text().splitlines()


    example_part2 = read_file_part2(mo.notebook_location() / "example.txt")
    input_part2 = read_file_part2(mo.notebook_location() / "input.txt")
    return (example_part2,)


@app.cell
def _(example_part2):
    example_part2
    return


app._unparsable_cell(
    r"""
    try:
        pass
    except(ValueError):
        continue
    """,
    name="_"
)


@app.cell
def _():
    int(' ')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 example
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 Solution
    """)
    return


if __name__ == "__main__":
    app.run()
