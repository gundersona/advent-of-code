import marimo

__generated_with = "0.19.7"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    from pathlib import Path
    return Path, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Read input data
    """)
    return


@app.cell(hide_code=True)
def _(Path, mo):
    example_input = Path("example_input.txt").read_text().splitlines()
    input = Path("input.txt").read_text().splitlines()
    mo.accordion({"Example Input": example_input, "Actual Input": input})
    return example_input, input


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 1
    """)
    return


@app.function
def sum_joltage_1(input):
    joltage = 0
    for a in input:
        joltage += max(
            int(a[i] + a[j])
            for i in range(len(a))
            for j in range(i + 1, len(a))
        )
    return joltage


@app.cell
def _():
    example_solution_1 = 357
    return (example_solution_1,)


@app.cell
def _(example_input, example_solution_1, mo):
    mo.md(rf"""
    Example solution 1 is correct: {sum_joltage_1(example_input) == example_solution_1}
    """)
    return


@app.cell
def _(input, mo):
    mo.md(rf"""
    Part 1 Solution: {sum_joltage_1(input)}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Part 2
    """)
    return


@app.function
def sum_joltage_2(input):
    joltage = 0
    for line in input:
        bank = list(line)
        idx = -1
        num_batteries = 12
        answer = []
        for i in range(num_batteries):
            if num_batteries == 1:
                sub_bank = bank[idx + 1 :]
            else:
                sub_bank = bank[idx + 1 : 1 - num_batteries]
            idx = bank.index(max(sub_bank))
            answer.append(bank[idx])
            num_batteries -= 1
            bank[0 : idx + 1] = "0" * len(bank[0 : idx + 1])
        joltage += int("".join(answer))
    return joltage


@app.cell
def _():
    example_solution_2 = 3121910778619
    return (example_solution_2,)


@app.cell
def _(example_input, example_solution_2, mo):
    mo.md(rf"""
    Example solution 2 is correct: {sum_joltage_2(example_input) == example_solution_2}
    """)
    return


@app.cell(hide_code=True)
def _(input, mo):
    mo.md(rf"""
    Part 2 Solution: {sum_joltage_2(input)}
    """)
    return


@app.cell
def _():
    # Nathan's solution
    bank = "234234234234278"
    answer = 434234234278
    joltage = ""

    last_position = None

    for i in range(12):
        # search right after the previous position
        start_index = 0 if (last_position is None) else (last_position + 1)
        # look for most significant first, which must have space for all
        # the following digits
        end_index = len(bank) - (11 - i)
        bank_to_search = bank[start_index:end_index]

        max_joltage = max(bank_to_search)
        joltage = joltage + max_joltage
        idx = bank_to_search.index(max_joltage)
        last_position = idx + start_index

    print("we got", joltage)
    print("correct?", int(joltage) == answer)
    return


if __name__ == "__main__":
    app.run()
