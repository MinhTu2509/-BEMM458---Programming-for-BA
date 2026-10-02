#######################################################################
# Activity 1 – Lists in Action (Solutions)
#######################################################################

# 1) Define a list of monthly sales (Jan–Jun)
sales = [12000, 15000, 17000, 16000, 18000, 17500]
print(sales)
print("First month:", sales[0], "Last month:", sales[-1])  # OUTPUT: 12000 17500

# 2) Modify: correct March’s value, add July, and remove last entry
sales[2] = 16500
print(sales)
# OUTPUT: March from 17000 to 16500
sales.append(19000)
print(sales)
# Add July = 19000
removed = sales.pop() # Function = .pop() -> Remove last entry
print(sales)

print("Corrected + added + removed:", sales, "Removed:", removed)
# OUTPUT: [12000, 15000, 16500, 16000, 18000, 17500] Removed: 19000

# 3) Slice quarters and compare totals
q1 = sales[:3] # Sum from 0 -> 2 (<3): Jan + Feb + Mar = 12000 + 15000 + 16500
q2 = sales[3:6] # Sum from 3 -> 5 (<6):  = 16000 + 18000 + 17500
print("Q1 total:", sum(q1), "Q2 total:", sum(q2))  
# OUTPUT: Q1 total: 43500 Q2 total: 51500