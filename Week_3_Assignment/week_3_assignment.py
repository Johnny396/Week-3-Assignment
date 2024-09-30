"""Week 3 Assignment"""

def calculate_discount():
    """Final price for a commodity"""
    price = int(input("Enter Original price of the comodity > "))
    discount_percent = int(input("Enter the discounted percentage > "))
    final_price = price - (price * (discount_percent / 100))
    if discount_percent >= 20:
        return f"The final price is {final_price}"
    else:
        return f"The final price is {price}"


print(calculate_discount())
