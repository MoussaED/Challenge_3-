import os 
import csv 

CSV_PATH = os.path.join("Resources", "budget_data.csv")
MONTH_IDX = 0 
PROFIT_IDX = 1
month_ls = []
profit_ls = []
change_ls = []
Increase_ls = []
Decrease_ls = []
previous_profit = 0
greatest_count = 0 
greatest_count_month = ""
lowest_count = 0
lowest_count_month = ""
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
       #code for month'
       current_month = row[MONTH_IDX]
       month_ls.append(current_month)

        #code for profit'
       current_profit = int(row[PROFIT_IDX])
       profit_ls.append(current_profit)

       if previous_profit != 1:
            change = current_profit - previous_profit
            change_ls.append(change)

       if change > greatest_count:
            greatest_count = change
            greatest_count_month = row[0]
            
        
       if change < lowest_count:
           lowest_count = change
           lowest_count_month = row[0]
            
       

    previous_profit = current_profit
        
        
change_avg = sum(change_ls) / len(change_ls)



f = open("PyBnk_anlys.txt", "w")
f.write("Financial Analysis")
f.write("\n ------------------------")
f.write("\n")
f.write("Greatest Increase in profits:" + greatest_count_month +  "(${:.2f})\n".format(greatest_count)) 
f.write("\n")
f.write("Greatest Decrease in profits:" + lowest_count_month +  "(${:.2f})\n" .format(lowest_count))
f.write("\n")
f.write("Average Change: ${:.2f}\n" .format((change_avg)))
f.write("\n")
f.write("Total: ${:.2f}\n" .format(sum(profit_ls)))
f.write("\n")
f.write("Total Months: {}\n" .format(str(len(month_ls))))


f.close()

f = open("PyBnk_anlys.txt", "r")
print(f.read())        







