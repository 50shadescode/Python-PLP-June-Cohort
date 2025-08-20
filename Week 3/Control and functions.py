def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price


# Get user input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Print result with explanation
if discount_percent >= 20:
    print(f"Discount applied! Final price: ${final_price:.2f}")
else:
    print(f"No discount applied. Price remains: ${final_price:.2f}")
