Task 02 - Expense Tracker

Description:

A basic python expense tracker program that tracks the daily expenses of a user. It stores a record of the expense date, category, and amount in a CSV file
It validates the date format to be in "DD-MM-YYYY" format and also validates the amount to be a positive number. It also handles exceptions for non numeric values and asks the user to enter a valid amount for such cases.

The user can enter multiple expenses at once and the program will sum the total expenses for each category and store it in another CSV file. Both CSV files can be viewed using spreadsheet software such as microsoft excel or google sheets.

Features:
It records the date, category, and amount of each expense.
It validates the date and checks if it is a valid calendar date.
It does not allow empty category or amount.
It does not allow non numeric values for amount.
It stores the expenses in a CSV file using dictionaries.

It calculates the total amount spent per category and stores it in another CSV file.
The totals.csv file retains the previous values and appends new values to it for multiple usages.
Technologies Used:
Python 3
csv module
datetime module

Files used :
task_2.py - It is the main program file
expenses.csv - This file stores the individual expense records.
totals.csv - This file stores the total amount spent in each category.
The CSV files are created or edited as the program runs. The CSV file expenses.csv should have the first row as date,category,amount
How to Run
Make sure you have python 3 installed in your system. If not, install it from https://www.python.org/downloads/
Download or clone the repository to your local machine.
Open terminal in the directory where the files are located.
Run the following command
python task_2.py
Provide the input for date in DD-MM-YYYY format, category, and amount for the expense
Enter whether you want to add another expense or not.
See the results in the terminal and the CSV files. The totals.csv file will have the totals for each category.

Learning Outcomes :

I have learned how to use various python functions, dictionaries, loops, conditions, error handling, date validations, file handling, and csv functions. I also learned how to calculate the category totals and store them in another CSV file.