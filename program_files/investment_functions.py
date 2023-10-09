from validation_functions import *
import math
from tabulate import tabulate

def invest_inputs():
    """
    Returns figures required to calculate investment return.
    :return: list of figures
    """
    principal = valid_flt("Enter principal investment value R")
    interest = valid_flt("Enter interest rate: ") / 100
    duration = valid_flt("Enter number of years you intend to invest: ")
    return [principal, interest, duration]


def simple_interest(figures: list):
    """
    Calculates and returns simple interest return.
    :param figures: list of required figures
    :return float result return
    """
    return figures[0] * (1 + (figures[1] * figures[2]))


def compound_interest(figures: list):
    """
    Calculates and returns compound interest return.
    :param figures: list of required figures
    :return: float result value
    """
    return figures[0] * math.pow((1 + figures[1]), figures[2])


def table_invest_result(figures, result):
    """
    Formats and displays investment results as
    a table using the tabulate module.
    :param figures: figures from user inputs
    :param result: calculation result
    """
    display = [
        ["Principal Amount", f"R{figures[0]:,.2f}"],
        ["Interest Rate", f"{round(figures[1] * 100)}%"],
        ["Duration", f"{int(figures[2])} years"],
        ["Gross Return", f"R{result:,.2f}"],
        ["Nett Return", f"R{(result - figures[0]):,.2f}"]
    ]
    print(tabulate(display, tablefmt="double_grid"))
