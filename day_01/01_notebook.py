import marimo

__generated_with = "0.18.4"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    # Imports and Functions
    """)
    return


@app.cell
def _():
    import marimo as mo
    from pathlib import Path
    return Path, mo


@app.cell
def _(Path):
    example_path = Path("01_example.txt")
    example_doc = example_path.read_text().splitlines()
    return (example_doc,)


@app.cell
def _(Path):
    input_path = Path("01_input.txt")
    input_doc = input_path.read_text().splitlines()
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
        n = extract_number(clicks)
        if n > 0:
            for i in range(n):
                location += 1
                if location == 100:
                    location = 0
                    if i != (n - 1):
                        crossings += 1
        if n < 0:
            for i in range(abs(n)):
                location -= 1
                if location == -1:
                    location = 99
                    if i != 0:
                        crossings += 1
    return crossings


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    # Part 1
    """)
    return


@app.cell(hide_code=True)
def _(example_doc, input_doc, mo):
    mo.md(f"""
    ## Example Solution: {find_zero_landings(example_doc)}
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


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""
    # Alternate Solution Found Online
    """)
    return


@app.cell
def _():
    position: int = 50
    zero_count: int = 0
    with open(f"01_input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            dir = line[0]
            val = int(line[1:])
            if dir == "L":
                position = (position - val) % 100
            else:
                position = (position + val) % 100

            if position == 0:
                zero_count += 1
    print(zero_count)

    position: int = 50
    zero_count: int = 0

    for line in lines:
        line = line.strip()
        dir = line[0]
        val = int(line[1:])

        full, partial = divmod(val, 100)
        zero_count += full

        delta = -partial if dir == "L" else partial
        next_position = position + delta

        if position != 0:
            if dir == "L" and next_position <= 0:
                zero_count += 1
            elif dir == "R" and next_position >= 100:
                zero_count += 1

        position = next_position % 100

    print(f"final count: {zero_count}")
    return (lines,)


@app.cell
def _(lines):
    lines
    return


if __name__ == "__main__":
    app.run()
