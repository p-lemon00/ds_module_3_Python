import csv

# Read in csv file

csvpath = "Resources/budget_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Find
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The changes in "Profit/Losses", and then the average of those changes
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in profits (date and amount) over the entire period

    month_tot = 0
    net = 0
    change_list = []
    prev_prof = " "
    inc = 0
    dec = 0
    change = 0
    
    
    for row in csvreader:
        
        month = row[0]
        prof = int(row[1])
        month_tot = month_tot + 1
        net = net + prof
        
        if (prev_prof != " "):
            change = prof - prev_prof
            change_list.append(change)
            avg = sum(change_list)/len(change_list)

        if change > inc:
            inc = change
            inc_month = month
        
        if change < dec:
            dec = change
            dec_month = month
        
        prev_prof = int(row[1])

    # Print Results and write to a text file

    results = (f"Financial Analysis \n ---------------------------- \n Total Months:  {month_tot} \n Total: ${net} \n Average Change: ${avg} \n Greatest Increase in Profits: {inc_month} ${inc} \n Greatest Decrease in Profits:  {dec_month} ${dec}")
    print(results)
    txt = open("analysis/analysis_pybank.txt", "w")
    txt.write(results)
