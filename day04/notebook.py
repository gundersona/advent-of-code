import marimo

__generated_with = "0.19.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    return mo, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Read Inputs
    """)
    return


@app.cell
def _(mo, pl):
    example_solution_1 = 13

    with open("example.txt", "r") as f:
        example = [list(line.strip()) for line in f]
    df_example = pl.DataFrame(example)

    with open("input.txt", "r") as f:
        input = [list(line.strip()) for line in f]
    df_input = pl.DataFrame(input)

    # mo.accordion({"Example Input": df_example, "Puzzle Input": df_input})
    mo.accordion({"Example Input": example, "Puzzle Input": input})
    return example, example_solution_1, input


@app.function
def safe_get(mat, r, c):
    """
    Get mat[r][c] with explicit bounds checks.
    Disallows negative indices. Raises IndexError on out-of-range.
    Works for rectangular or jagged (ragged) matrices.
    """
    # Check row
    if r < 0 or r >= len(mat):
        raise IndexError(f"Row index out of range: r={r}, rows={len(mat)}")
    row = mat[r]

    # Check column (row may have its own length if jagged)
    if c < 0 or c >= len(row):
        raise IndexError(
            f"Col index out of range: c={c}, cols_in_row={len(row)}"
        )

    return row[c]


@app.function
def num_rolls_adjacent(matrix, row, col):
    num_rolls = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not (i == 0 and j == 0):
                try:
                    num_rolls += safe_get(matrix, row + i, col + j) == "@"
                except IndexError:
                    continue
    return num_rolls


@app.function
def check_all_locations(input):
    num_accessible_rolls = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            roll = input[i][j]
            if roll == "@":
                num_accessible_rolls += num_rolls_adjacent(input, i, j) < 4
    return num_accessible_rolls


@app.cell
def _(example, example_solution_1):
    check_all_locations(example) == example_solution_1
    return


@app.cell
def _(input):
    check_all_locations(input)
    return


if __name__ == "__main__":
    app.run()
