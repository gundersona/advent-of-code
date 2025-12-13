import marimo

__generated_with = "0.18.4"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    # Imports and Helper Functions
    """)
    return


@app.cell
def _():
    import marimo as mo
    import polars as pl
    from pathlib import Path
    return Path, mo


@app.cell
def _(Path):
    example_path = Path("01_example.txt")
    example_doc = example_path.read_text().splitlines()
    example_doc
    return (example_doc,)


@app.cell
def _(Path):
    input_path = Path("01_input.txt")
    input_doc = input_path.read_text().splitlines()
    input_doc
    return (input_doc,)


@app.cell
def _(input_doc, mo):
    mo.md(rf"""
    Biggest Number of Clicks: {max(int(c[1:]) for c in input_doc)}
    """)
    return


@app.function
def extract_number(input):
    if input[0] == "L":
        out = -int(input[1:])
    else:
        out = int(input[1:])
    return out


@app.function
def find_zero_landings(doc):
    value = 50
    zero_count = 0
    for clicks in doc:
        value = (value + extract_number(clicks)) % 100
        zero_count += value == 0
    return zero_count


@app.function
def find_zero_crossings(doc):
    location = 50
    crossings = 0

    for clicks in doc:
        n = location + extract_number(clicks)
        if n < 0:
            crossings += abs(int(n / 100)) + 1
            if location is 0:
                crossings -= 1

        location = (location + extract_number(clicks)) % 100

        if n > 99:
            crossings += int(n / 100)
            if location is 0:
                crossings -= 1
    return crossings


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    # Part 1
    """)
    return


@app.cell(hide_code=True)
def _(example_doc, mo):
    mo.md(f"""
    ## Example Solution: {find_zero_landings(example_doc)}
    """)
    return


@app.cell(hide_code=True)
def _(input_doc, mo):
    mo.md(rf"""
    ## Actual Solution: {find_zero_landings(input_doc)}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Part 2
    """)
    return


@app.cell(hide_code=True)
def _(example_doc, mo):
    mo.md(rf"""
    ## Example Solution: {find_zero_landings(example_doc) + find_zero_crossings(example_doc)}
    """)
    return


@app.cell(hide_code=True)
def _(input_doc, mo):
    mo.md(rf"""
    ## Actual Solution: {find_zero_landings(input_doc) + find_zero_crossings(input_doc)}
    """)
    return


if __name__ == "__main__":
    app.run()
