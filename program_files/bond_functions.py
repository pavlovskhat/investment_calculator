from validation_functions import *
from tabulate import tabulate

def bond_inputs():
    """
    Return figures for bond calculation.
    :return: figures as list
    """
    bond_total = valid_flt("Enter total bond value R")
    interest = valid_flt("Enter monthly interest: ") / 100 / 12
    duration = valid_flt("Enter duration of bond in months: ")
    return [bond_total, interest, duration]


def table_bond_result(figures, result):
    """
        Formats and displays bond results as
        a table using the tabulate module.
        :param figures: figures from user inputs
        :param result: calculation result
        """
    display = [
        ["Bond Total", f"R{figures[0]:,.2f}"],
        ["Interest Rate", f"{round(figures[1] * 12 * 100)}%"],
        ["Payment Duration", f"{int(figures[2])} months"],
        ["Monthly Payments", f"R{result:,.2f}"],
        ["Total Payable", f"R{(result * figures[2]):,.2f}"]
    ]
    print(tabulate(display, tablefmt="double_grid"))


def bond():
    """
    Calculates and displays the bond
    repayment breakdown.
    """
    figures = bond_inputs()
    bond_result = (figures[1] * figures[0]) / (1 - (1 + figures[1]) ** (-figures[2]))
    print("Bond repayment breakdown:")
    table_bond_result(
        figures,
        bond_result
    )
