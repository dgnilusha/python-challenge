#import the os module
import os
#import CSV file
import csv

CSV_PATH = os.path.join('Resources', 'budget_data.csv')


# initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]


# csvpath = "C:/Users/dgnil/Desktop/Classwork/python-challenge/pyBank/PyBank/Resources/budget_data.csv"
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile:

    # csv reader specifies delimiter 
    csvreader = csv.reader(csvfile,delimiter=',')

    next(csvreader) # skip header row

    # loop through each row  csv 
    for row in csvreader:
    # increment total months
        total_months =total_months+1

        # total amount of profit/losses
        current_profit_loss = int(row[1])
        total_profit_loss = total_profit_loss+ current_profit_loss

    # calculate change in profit/losses and add to list
        if total_months > 1:
            profit_loss_change = current_profit_loss - previous_profit_loss
            profit_loss_change_list.append(profit_loss_change)

           

    # set previous profit/loss to current profit/loss 
        previous_profit_loss = current_profit_loss

# calculate the average change in profit/losses
average_profit_loss_change = sum(profit_loss_change_list) / len(profit_loss_change_list)

# print the analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${round(average_profit_loss_change, 2)}")


# Export the results to a text file
with open("output.txt", "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_loss}\n")
    output_file.write(f"Average Change: ${round(average_profit_loss_change, 2)}")