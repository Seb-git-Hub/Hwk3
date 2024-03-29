# create file path across operating systems
import os
# Module for reading csv files
import csv
csvpath = os.path.join('budget_data.csv')
# lists to be analyzed/reported
months = []
net_income = []
net_income_average = 0
months_months_change = []
date = []
writefile ='w'
readfile ='r'
# read csv and parse data into lists
with open(csvpath, newline='') as csvfile:
   csvreader = csv.reader(csvfile)
   next(csvreader, None)
   for row in csvreader:
       months.append(row[0])
       net_income.append(int(row[1]))
# find total months
total_months = len(months)
# create greatest increase and decrease in profits as a variable
greatest_inc = net_income[1] - net_income[0]
greatest_dec = net_income[0]
totalnet_income = 0
# loop through profits indices and compare to find greatest increase and decrease
for r in range(len(net_income)):
   if net_income[r] >= greatest_inc:
       greatest_inc = net_income[r]
       great_inc_month = months[r]
   elif net_income[r] <= greatest_dec:
       greatest_dec = net_income[r]
       great_dec_month = months[r]
   totalnet_income += net_income[r]
#calculate average_change
average_change = round(totalnet_income/len(months), -1)
#sets path for output file
output_pybank = os.path.join('pybank_output.csv')
# opens the output destination in write mode and prints the summary
with open(output_pybank, 'w') as writefile:
   writefile.writelines('Financial Analysis\n')
   writefile.writelines('----------------------------' + '\n')
   writefile.writelines('Total Months: ' + str(total_months) + '\n')
   writefile.writelines('Total Net_income: $' + str(totalnet_income) + '\n')
   writefile.writelines('Average Net_income Change: $' + str(average_change) + '\n')
   writefile.writelines('Greatest Increase in Net_income: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
   writefile.writelines('Greatest Decrease in Net_income: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')
#opens the output file in r mode and prints to terminal
with open(output_pybank, 'r') as readfile:
   print(readfile.read())
# Close file
   writefile.close()
