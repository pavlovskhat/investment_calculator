from bond_functions import *
from investment_functions import *

# Global variables.
MAIN_MENU = """
==============================
WELCOME TO THE CALCULATOR APP
==============================
1> Calculate investment return
2> Calculate bond repayment
3> Exit
"""
INVEST_MENU = """
===================
INVESTMENT OPTIONS
===================
1> Simple interest model
2> Compound interest model
3> Return to main menu
"""


def investment():
    """
    Sub menu with additional investment options.
    :return: back to main menu
    """
    while True:
        print(INVEST_MENU)
        invest_choice = input("Select option >_")
        match invest_choice:
            case "1":
                figures = invest_inputs()
                print("Simple interest return:")
                table_invest_result(
                    figures,
                    simple_interest(figures)
                )
            case "2":
                figures = invest_inputs()
                print("Compound interest return:")
                table_invest_result(
                    figures,
                    compound_interest(figures)
                )
            case "3":
                return
            case _:
                print("!!! ERROR: INCORRECT CHOICE !!!")


def main():
    """
    Main menu logic
    """
    while True:
        print(MAIN_MENU)
        choice = input("Select option >_")
        match choice:
            case "1":
                investment()
            case "2":
                bond()
            case "3":
                print("Goodbye")
                exit()
            case _:
                print("!!! ERROR: INCORRECT CHOICE !!!")

# Program start point.
if __name__ == "__main__":
    main()
