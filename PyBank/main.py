import os
import csv

# Path to read CSV
budget_csv = os.path.join('.' , 'budget_data_1.csv')

# Lists to store data
date_list = []
rev_change_list = []

total_revenue = 0
total_months = 0
current_revenue = 0

with open(budget_csv, newline="") as csvfile:

    csvreader= csv.reader(csvfile, delimiter=",")
    
    line_after_header = next(csvreader)

    

    for row in csvreader:

        previous_revenue = current_revenue

        current_revenue = float(row[1])
        
        revenue_change = current_revenue - previous_revenue
        
        total_revenue = total_revenue + current_revenue
    
        total_months = int(total_months) + 1

        if revenue_change != current_revenue:
            rev_change_list.append(revenue_change)
            date_list.append(row[0])


average_change = round(sum(rev_change_list) / len(rev_change_list),2)
top_increase = max(rev_change_list)
top_decrease = min(rev_change_list)

top_inc_month = date_list[rev_change_list.index(top_increase)]
top_dec_month = date_list[rev_change_list.index(top_decrease)]



# Print out summary data
print(f"Financial Analysis")
print(f"__________________")
print(f"Total Months: {total_months}")
print(f"Total Revenue: {total_revenue}")
print(f"Average Revenue Change: {average_change}")
print(f"Greatest Increase in Revenue: {top_inc_month} - {top_increase}")
print(f"Greatest Decrease in Revenue: {top_dec_month} - {top_decrease}")

# Export Summary Data
csvpath = "PyBank Summary.csv"
with open(csvpath, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow([f"Financial Analysis"])
    csvwriter.writerow([f"___________________"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total Revenue: {total_revenue}"])
    csvwriter.writerow([f"Average Revenue Change: {average_change}"])
    csvwriter.writerow([f"Greatest Increase in Revenue: {top_inc_month} - {top_increase}"])
    csvwriter.writerow([f"Greatest Decrease in Revenue: {top_dec_month} - {top_decrease}"])