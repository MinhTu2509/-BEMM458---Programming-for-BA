#######################################################################
# Activity 3 – Loops and Comprehensions (Solutions)
#######################################################################

sales = [12000, 15000, 17000, 16000, 18000, 17500, 21000, 20500, 22000, 21500, 23000, 24000]
print(sales)

# 1) Loop
growth_rates = []
for i in range(1, len(sales)):
    growth = (sales[i] - sales[i-1]) / sales[i-1] * 100
    print(sales) # (sales[1] - sales[0]) / sales[0]
    print(growth)
    growth_rates.append(round(growth, 2)) # rounding to 2 decimals
    print(growth_rates)
print("Growth rates (loop):", growth_rates)
# OUTPUT: [25.0, 13.33, -5.88, 12.5, -2.78, 20.0, -2.38, 7.32, -2.27, 6.98, 4.35]

# 2) Comprehension -> Similar to loop but with shorter formula
growth_rates_comp = [round((sales[i] - sales[i-1]) / sales[i-1] * 100, 2) for i in range(1, len(sales))]
print("Growth rates (comprehension):", growth_rates_comp)
# OUTPUT: [25.0, 13.33, -5.88, 12.5, -2.78, 20.0, -2.38, 7.32, -2.27, 6.98, 4.35]

# 3) Filter >= 20k
high_months = [s for s in sales if s >= 20000] # Comprehensive function
print("High months:", high_months)
# OUTPUT: [21000, 20500, 22000, 21500, 23000, 24000]
