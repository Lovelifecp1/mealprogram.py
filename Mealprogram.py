

# Meal Total Calculator
meal_cost   =   float(input("Enter the cost of your meal: $"))

# Calculate tip and tax
tip = meal_cost * 0.18
tax = meal_cost * 0.07

# Calculate Total
total = meal_cost + tip + tax

#  Display results
print("n---- Meal Summary - - - -")
print(f"Tip (18%: ${tip:.2f}")
print(f"Tip (7%: ${tip:.2f}")
print(f"Total: ${total:2f}")
