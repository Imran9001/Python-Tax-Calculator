def national_insurance(gross_salary):
    """""
    This function is for working out the national insurance that has to be paid 
    for the salary inputted. It takes in the parameter "gross salary" which is an
    integer. Uses if else statements to determine which national insurance band the salary is in.
    The function returns a single float which is the value of the national insurance for the salary entered. 
    """""
    if 12576 < gross_salary <= 50268:  # This if statement targets a salary that is over £12 576 and below or equal to £50 268.
        # 12 percent band for national insurance
        twelve_percent_amount = gross_salary - 12576  # The amount of money that is not affected by national insurance is subtracted from the salary entered.
        twelve_percent_tax = twelve_percent_amount * 0.12  # This works out 12 percent of the remaining amount which is the national insurance.
        return twelve_percent_tax  # This returns the value of national insurance that has been worked out.

    elif gross_salary > 50268:  # This else if statement targets a salary that is over £50 268.
        # 2 percent band for national insurance
        twelve_percent_amount = 50269 - 12576  # This is the amount that is taxed at 12 percent.
        twelve_percent_tax = twelve_percent_amount * 0.12
        two_percent_amount = gross_salary - 50268
        two_percent_tax = two_percent_amount * 0.02
        total = twelve_percent_tax + two_percent_tax
        return total
    elif gross_salary <= 12576:  # salary in 0 percent band for national insurance
        return 0


def student_loans(gross_salary, student_loan_input):
    """""
        This function is for working out the student loan payment. It takes into its parameters the salary and
        the remaining amount of student loan debt. It works out the amount by comparing the salary with the 
        student loan repayment threshold and the payment amount with the total remaining debt. Returns value of
        student loan payment. 
        """""
    if gross_salary >= 22015:  # Above student loan repayment threshold
        student_loan_value = gross_salary * 0.09  # student loan yearly payment is 9 percent of yearly salary
        if student_loan_input < student_loan_value:  # This if statement triggers when the student loan payment is
            # higher than the actual student loan debt remaining
            student_loan_value = student_loan_input  # value of student loan payment becomes the value of student loan debt
        return student_loan_value
    elif gross_salary < 22015:
        return 0  # Below student loan repayment threshold



def pay_calculator(gross_salary, student_loan_input, user_input, national_input):
    """""
        This function is for working out salary after tax. The salary after national insurance and student loan
        contributions can also be worked out. It uses a series of if else statements to determine which tax bracket
        the salary is in and then does the appropriate calculations. At this point depending on what the user chose,
        functions are called to work out the value of national insurance and student loan payment which are subtracted
        from the final total which is outputted. 
        """""
    tax_free = 12570

    if gross_salary <= tax_free:  # This if statement triggers when the salary is below or equal to the tax-free amount
        print("salary after tax is ", gross_salary)
        if user_input == "Y":
            print(
                "Salary under student loan repayment amount")  # a salary below or equal to the personal allowance will
            # also be below the student loan repayment amount
        if national_input == "Y":
            print("National insurance is 0")
    elif 12570 < gross_salary < 50271:  # This elif statement triggers when the salary is above £12 570 and below £50 271.
        # This is the range where the salary is in the 20 percent tax band.
        personal_allowance_deducted = gross_salary - tax_free
        tax = personal_allowance_deducted * 0.2  # Taxed at 20 percent
        if national_input == "Y":
            take_home = gross_salary - tax - national_insurance(gross_salary)  # Works the amount the user takes home
            # after subtracting the total tax and national insurance from the salary entered.
        else:
            take_home = gross_salary - tax
        print("salary after tax is")
        print(take_home)
        if national_input == "Y":
            print("National insurance is", national_insurance(gross_salary))
        if student_loans(gross_salary, student_loan_input) != 0:
            student_loan_deducted = take_home - student_loans(gross_salary, student_loan_input)
            print("After student loan fee applied, salary is", student_loan_deducted)
        elif user_input == "Y":
            print("Student loan fee not applied, salary is below repayment threshold")  # For this trigger the
            # student loan payment must equal 0 while the user has a student loan which means that the salary is lower
            # than the repayment threshold

    elif 50271 <= gross_salary <= 125140:  # This is the range where the salary is in the 40 percent tax band.
        if gross_salary > 100000:
            allowance = gross_salary - 100000  # Personal allowance goes down £1 for every £2 above £100 000. Value of
            # allowance becomes the amount that gross salary is above 100 000
            allowance2 = allowance / 2  # Divide by 2 to get every £2 above instead of every £1 above
            tax_free = tax_free - allowance2  # New personal allowance
        personal_allowance_deducted = gross_salary - tax_free
        forty_percent_amount = personal_allowance_deducted - 37700  # amount to be taxed at 20 percent is subtracted
        # from the total.
        forty_percent_tax = forty_percent_amount * 0.4
        twenty_percent_tax = 37700 * 0.2
        total_tax = twenty_percent_tax + forty_percent_tax
        if national_input == "Y":  # If statement that will choose to subtract the national insurance from the take
            # home depending on if the user picked to include the national insurance.
            take_home = gross_salary - total_tax - national_insurance(gross_salary)
        else:
            take_home = gross_salary - total_tax
        print("salary after tax is")
        print(take_home)
        if national_input == "Y":
            print("National insurance is", national_insurance(gross_salary))
        if user_input == "Y":  # Triggers if user said that they have a student loan
            student_loan_deducted = take_home - student_loans(gross_salary, student_loan_input)  # student_loans
            # function is called, the salary and amount of student loan debt is passed into it. The function works
            # out the student loan payment amount, this is then subtracted from take home.
            print("After student loan fee applied, salary is", student_loan_deducted)


    elif gross_salary > 125140:  # This is the range where the salary is in the 45 percent band.
        twenty_percent_amount_deducted = gross_salary - 37700
        forty_five_percent_amount = twenty_percent_amount_deducted - 87440  # amount to be taxed at 40 percent is subtracted
        forty_five_percent_tax = forty_five_percent_amount * 0.45
        twenty_percent_tax = 37700 * 0.2
        forty_percent_tax = 87440 * 0.4
        total_tax = twenty_percent_tax + forty_percent_tax + forty_five_percent_tax
        if national_input == "Y":
            take_home = gross_salary - total_tax - national_insurance(gross_salary)  # national_insurance function is
            # called, the salary is passed into it. The function works out the national insurance amount,
            # this is then subtracted from the gross salary along with the total tax.
        else:
            take_home = gross_salary - total_tax  # if user chooses not to include national insurance then only
            # the tax will be taken away from the gross salary
        print("salary after tax is")
        print(take_home)
        if national_input == "Y":
            print("National insurance is", national_insurance(gross_salary))
        if user_input == "Y":
            student_loan_deducted = take_home - student_loans(gross_salary, student_loan_input)
            print("After student loan fee applied, salary is", student_loan_deducted)


print("Enter your Salary")
input_salary = input()  # Value of input_salary is whatever the user inputs into the console.
while input_salary.isdigit() is not True:  # while loop triggers if previous input is not all digits so not an integer,
    # it will keep looping until an integer is entered.
    print("Please enter a whole number")
    input_salary = input()
input_salary = int(input_salary)  # digit string converts into an integer

print("Do want to include national insurance, enter Y or N")
national_input = input().upper()  # upper function makes any letters inputted into capital letters
while national_input != "Y" and national_input != "N":  # while loop, keeps looping until national_input is either Y or N
    print("Please enter only Y or N")
    national_input = input().upper()

print("Do you have a student loan, enter Y or N")
user_input = input().upper()
while user_input != "Y" and user_input != "N":
    print("Please enter only Y or N")
    user_input = input().upper()

loan_input = 0

if user_input == 'Y':
    print("what is your total remaining student loan debt")
    loan_input = input()
    while loan_input.isdigit() is not True:
        print("Please enter a whole number")
        loan_input = input()
    loan_input = int(loan_input)

pay_calculator(input_salary, loan_input, user_input, national_input)  # pay_calculator function called
