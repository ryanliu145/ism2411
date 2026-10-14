# 1. The first bug I spotted in Exercise 5 was the missing colon and I found it only after asking AI. This shows my current debugging instincts need some improvement.
# 2. The apply_discount(price, tier) takes an item's price and the tier of the customer's membership, and returns the price after applying the discount assigned to there tier. The inputs are price, which is the original price before the discount, tier, which is a string naming the customer's membership level. Then, it returns the discounted price based on the tier of the customer's membership. I think a colleague could use it wihout reading the body based on the name and parameter names.
# 3. I did use AI and I feel like it walked me through whole process, making it easier to understand.

#---Exercise 1---
def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1: .2f}")
print(f"Tax on $250 at 8%: ${tax2: .2f}")

assert abs(tax1 - 7.00) < 1e-9, f"Expected 7.00, got {tax1}"
assert abs(tax2 - 20.00) <1e-9, f"Expected 20.00, got {tax2}"

#---Exercise 2---
def apply_discount(price,tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0.0
    return price * (1 - discount)

price = 200

print(f"gold: ${apply_discount(price, 'gold'): .2f}")
print(f"silver: ${apply_discount(price, 'silver'): .2f}")
print(f"bronze: ${apply_discount(price, 'bronze'): .2f}")
print(f"none: ${apply_discount(price, 'none'): .2f}")

#---Exercise 3---
def calculate_tax(price, rate):
    return price * rate

def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0.0
    return price * (1 - discount)

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

start = 200
discounted = apply_discount(start, "gold")
print(f"After gold discount: ${discounted: .2f}")

total = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${total: .2f}")

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07): .2f}')

#---Exercise 4---
def calculate_tax(price, rate):
    return price * rate

def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0.0
    return price * (1 - discount)

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

#---Exercise 5---

#---Exercise 6---
#Scope is a variable created in a function that is only accessible within that function. Even if a global variable has the same name, the function's x is a seperate box, so changing it inside the function never changes the global x outside.