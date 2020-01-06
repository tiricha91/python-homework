from pathlib import Path
import csv

print(f'Current Directory:{Path.cwd()}')

csvpath = Path('Pybank/budget_csv/budget_data.csv')

total_months = 0
p_l = []
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(f'Financial Analysis')
    
    print(f'-----------------------')
    
    header = next(csvreader)
   
    print(header)

    months = []
    
    for row in csvreader:
        total_months += 1
        months.append(row[0])
        plstring = int(row[1])
        p_l.append(plstring)
    print(f'Total Months: {total_months}')

    total_p_l = 0

    for plstring in p_l:
        total_p_l += plstring
    final_number = '${:,.2f}'.format(total_p_l) 
    print(f'Total: {final_number}')
 


    j = 0
    monthly_difference = []
    while j < len(p_l)-1:
        variance = p_l[j+1] - p_l[j]

        monthly_difference.append(variance)

        j += 1
        
    final_number_2 = '${:,.2f}'.format(sum(monthly_difference)/len(monthly_difference))
    print(f'Average Change: {final_number_2}')

    # to get the min and max values from monthly difference
    min_variance_val = min(monthly_difference)
    max_variance_val = max(monthly_difference)

  

    # to get the index of the min and max values in the list
    min_val_index = monthly_difference.index(min_variance_val)
    max_val_index = monthly_difference.index(max_variance_val)

#using min_val_index find p_l & months values by adding 1 to get the max & min val
    min_month = months[min_val_index+1]
    max_month = months[max_val_index+1]
print(f'Greatest Increase in Profits: {max_month} ({max_variance_val})')
print(f'Greatest Decrease in Profits: {min_month} ({min_variance_val})')

output_path = 'PyBank/output.txt'

with open(output_path,'w') as file:
    file.write(f'Financial Analysis\n')
    file.write(f'-------------------\n')
    file.write(f'Total Months: {total_months}\n')
    file.write(f'Total: {final_number}\n')
    file.write(f'Average Change: {final_number_2}\n')
    file.write(f'Greatest Increase in Profits: {max_month} ({max_variance_val})\n')
    file.write(f'Greatest Decrease in Profits: {min_month} ({min_variance_val})\n')



#----- Stuff ----

#     greatest_increase = 0
#     greatest_decrease = 0

#     for dollar_amount in monthly_difference:
#         if greatest_decrease == 0:
#             greatest_decrease = dollar_amount
#         elif dollar_amount > greatest_increase:
#             greatest_increase = dollar_amount
#         elif dollar_amount < greatest_decrease:
#             greatest_decrease = dollar_amount
    
#     print(greatest_increase)
#     print(greatest_decrease)           
        

#     print(monthly_difference)
# print(monthly_difference.index(greatest_increase))
# print(monthly_difference.index(greatest_decrease))