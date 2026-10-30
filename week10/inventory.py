# Reflection 1:
# The most suprising thing about lists is how easy it is to change, add, or remove items without having to create a whole new list.

# Reflection 2:
# In a business situation, a Python list could help organize daily sales numbers and calculate totals/averages. This would save time compared to using Excel.

# Exercise 1:
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory, "|", len(inventory))

# Exercise 2:
print(inventory[0], "|", inventory[-1], "|", inventory[len(inventory) // 2])

# Exercise 3:
print(inventory[:3], "|", inventory[-2:], "|", inventory[::2])

# Exercise 4:
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5:
coords =(40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed, which makes them useful for coordinates that should stay the same.")

print(coords)

# Exercise 6:
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count
best = max(sales)
worst = min(sales)

print("Total:", total, "|", "Average:", average, "|", "Best:", best, "|", "Worst:", worst)

# Exercise 7:
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print(prices)
print(discounted)

# Exercise 8:
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))
