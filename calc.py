# Your Variables
main_cash = 500
EGP= 15.73
Number_of_days = 252

# Don't miss with Above
Total_cash = main_cash
day = 0

number_with_commas1 = "{:,}".format(main_cash)
number_with_commasEG = "{:,}".format(int(int(Total_cash) * EGP))
print(f"Day {day}: {number_with_commas1} USD & {number_with_commasEG} EGP")
day +=1

for x in range(Number_of_days):
    after_1_day_per = Total_cash * 0.03
    Total_cash += after_1_day_per
    intnumber = int(Total_cash)
    number_with_commas = "{:,}".format(intnumber)
    number_with_commasEG = "{:,}".format(int(int(Total_cash) * EGP))
    #print(f"Day {day}: {number_with_commas} USD & {number_with_commasEG} EGP")
    day +=1

per_with_commas1 = "{:,}".format(int(Total_cash / main_cash))
per_with_commas2 = "{:,}".format(int(Total_cash / main_cash) * 100)

print(f"Total After {Number_of_days} days is {number_with_commas} USD & {number_with_commasEG} EGP")
print(f"Profit Margin in {Number_of_days} days is {per_with_commas2}% and {per_with_commas1} Times")
