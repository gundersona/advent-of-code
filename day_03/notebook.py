import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium")


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
    return


@app.cell
def _():
    # from itertools import combinations

    # def sum_joltage_2(input):
    #     total_joltage = 0
    #     for a in input:
    #         bank_joltage = max(
    #             int("".join(a[i] for i in indices))
    #             for indices in combinations(range(len(a)), 12)
    #         )
    #         total_joltage += bank_joltage
    #         print(bank_joltage)

    #     return total_joltage
    return


@app.cell
def _(example_input):
    example_input[0].index(max(example_input[0]))
    return


@app.cell
def _():
    d = {2: "two", 1: "one"}
    d[3] = "three"
    print(d)
    return (d,)


@app.cell
def _(d):
    "".join([i[1] for i in sorted(d.items())])
    return


@app.cell
def _(example_input):
    list(example_input[0]).index(max(list(example_input[0])))
    return


@app.cell
def _():
    example_solution_list = [
        987654321111,
        811111111119,
        434234234278,
        888911112111,
    ]
    return


@app.cell
def _(jolt_dict):
    print(jolt_dict)
    return


@app.cell
def _(example_input, line):
    example_input[line]
    return


@app.cell
def _(example_input):
    line = 2

    jolt_dict = {}
    bank = list(example_input[line])
    print(bank)
    print("-" * 50)
    for i in range(12):
        # idx = bank.index(max(bank))
        idx = len(bank) - 1 - bank[::-1].index(max(bank))
        jolt_dict[idx] = max(bank)
        print(max(bank))
        bank[idx] = "0"
        print(bank)
    answer = int("".join(i[1] for i in sorted(jolt_dict.items())))
    # answer == example_solution_list[line]
    answer
    return jolt_dict, line


@app.function
def sum_joltage_2(input):
    joltage = 0
    for line in input:
        jolt_dict = {}
        bank = list(line)
        for i in range(12):
            # idx = bank.index(max(bank))
            idx = len(bank) - 1 - bank[::-1].index(max(bank))
            jolt_dict[idx] = max(bank)
            bank[idx] = "0"
        joltage += int("".join(i[1] for i in sorted(jolt_dict.items())))
    return joltage


@app.cell
def _():
    example_solution_2 = 3121910778619
    return (example_solution_2,)


@app.cell(hide_code=True)
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


if __name__ == "__main__":
    app.run()
