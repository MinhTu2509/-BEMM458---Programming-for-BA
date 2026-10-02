#######################################################################
# Activity 2 – Organising and Summarising (Solutions)
#######################################################################

sales = [12000, 15000, 17000, 16000, 18000, 17500, 21000, 20500, 22000, 21500, 23000, 24000]
print(sales)

# 1) Sort
print("Temporary sort:", sorted(sales)) # Just print it, not save the printed values)
# OUTPUT: [12000, 15000, 16000, 17000, 17500, 18000, 20500, 21000, 21500, 22000, 23000, 24000]

# Saved function -> save values in the global variable: Sales
sales.sort()
print("Permanent sort:", sales)  
# OUTPUT: [12000, 15000, 16000, 17000, 17500, 18000, 20500, 21000, 21500, 22000, 23000, 24000]

# 2) Reverse + stats
sales.reverse()
print("Reversed:", sales)  
# OUTPUT: [24000, 23000, 22000, 21500, 21000, 20500, 18000, 17500, 17000, 16000, 15000, 12000]
print("Min:", min(sales), "Max:", max(sales), "Average:", sum(sales)/len(sales))  
# OUTPUT: Min: 12000 Max: 24000 Average: 18916.67

# 3) Slices and best quarter
q_totals = [sum(sales[i:i+3]) for i in range(0, 12, 3)]
# For i = 0 -> sum(sales[0:3]) -> sum (Jan -> Mar) = 
# For i = 12 -> sum(sales[3:])

print("Quarter totals:", q_totals, "Best Q:", q_totals.index(max(q_totals))+1)  
# OUTPUT: Quarter totals: [69000, 63000, 52500, 43000] Best Q: 1
