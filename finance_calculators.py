
# ******** EDIT ********
# Thanks Logan for the re-submit, could not figure out why my values we're so incredibly high initially!
# Completely miss-read the task overview regarding conversion of the interest rate.

# Capstone project 1
# This is a program to calculate either a total investment or a home loan monthly repayment rate.

import math                                                                             # Math functions will be required for calculations.

# Short program introduction.
# User is asked to enter either 'investment' or 'bond'.
# Both options are explained in more detail to the user.
# Variable 'user_opt' is converted to lower case to negate any capitalisation issues.

print("")
print("Welcome to ABC Financing where your future is our priority.\n")
print("""Type either 'investment' or 'bond', based on the information below:
Investment:  Calculate the total interest from your chosen investment.
Bond:        Calculate your monthly home loan repayments.\n""")
user_opt = input("Please confirm your selection: ")
user_opt = (user_opt.lower())

# Assigning new variables 'invest' and 'bond'.
# Variables are either 'True' or 'False' based on value of variable 'user_opt' for use in calculation statements.

if (user_opt == "investment"):
    invest = True
    bond = False
elif (user_opt == "bond"):
    bond = True
    invest = False
else:
    bond = False
    invest = False

# Following statement will progress based on variables 'invest' and 'bond' being either 'True' or 'False'.
# In either case user is instructed how to enter follow up inputs via print output.
#
# In 'invest == True' case user is asked to enter three numerical values.
# User is then asked the choose and type either 'simple' or 'compound' as interest type stored as variable 'inv_type'.
# Based on this another sub statement is formed to calculate the investment value in either case.
# Investment total is output via print in either case.
# If an incorrect input is given for 'inv_type' an error message is printed asking user to restart program.
#
# In 'bond == True' case user is asked to enter three numerical values.
# Based on these values the monthly house loan repayment value is calculated and output via print.
#
# If the user did not initially enter either 'investment' or 'bond' program will detect both 'bond' and 'invest' as 'False'.
# This will output an error message to the user asking to restart program.

if (invest == True):
    print("\nYou have chosen the 'Investment' option, please answer the next few questions in numerical value \nand then select either 'simple' or 'compound' as your interest rate.\n")
    inv_val = float(input("What is the total amount that you are investing? R"))
    inv_rat = float(input("What is the interest rate of you investment? "))
                                                                                        # WHITE SPACING
    inv_rat_mod = float(inv_rat / 100)                                                  # Found my error! Completely forgot to add this step.
                                                                                        # WHITE SPACING
    inv_tim = float(input("What is the total number of years you are investing for? "))
    inv_type = input("Please type whether the interest is 'simple' or 'compound': ")
    inv_type = (inv_type.lower())                                                       # Variable 'inv_type' converted to lower case to negate any capitalisation issues.
                                                                                        # WHITE SPACING
    if (inv_type == "simple"):
        inv_total = (inv_val * (1 + (inv_rat_mod * inv_tim)))                           # Formula as given by task assignment.
        print(f"\nInvesting R{inv_val:.2f} at a {inv_type} interest rate of {inv_rat}% over {inv_tim:.0f} years will equate to an investment total of R{inv_total:.2f}.")
    elif (inv_type == "compound"):
        inv_total = (inv_val * math.pow((1 + inv_rat_mod), inv_tim))                    # Formula as given by task assignment.
        print(f"\nInvesting R{inv_val:.2f} at a {inv_type} interest rate of {inv_rat}% over {inv_tim:.0f} years will equate to an investment total of R{inv_total:.2f}.")
    else:
        print("\nI'm sorry, you have not chosen a valid interest rate option, please restart the program.")

elif (bond == True):
    print("\nYou have chosen the 'Bond' option, please answer the next few questions in numerical value.\n")
    prop_val = float(input("What is the current value of your house? "))
    bond_int = float(input("What is you home loan interest rate? "))
                                                                                        # WHITE SPACING
    bond_int_mod = float((bond_int / 12) / 100)                                         # Here is the step I am missing to convert correct interest rate for bond repayment.
                                                                                        # WHITE SPACING
    bond_tim = float(input("Over how many months will you be repaying your home loan? "))
    bond_total = (bond_int_mod * prop_val) / (1 - (1 + bond_int_mod) ** (-bond_tim))    # Formula as given by task assignment.
    print(f"\nYour monthly repayments on a property value of R{prop_val:.2f} at an interest rate of {bond_int}% over {bond_tim:.0f} months will be R{bond_total:.2f}.")
else:
    print("\nI'm sorry, you have typed an incorrect option, please restart the program.")






