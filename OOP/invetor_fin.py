# item.py (or whatever you name your file)

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def display_item(self):
        print(f"Name: {self.name}, Quantity: {self.quantity}, Price: ${self.price:.2f}")

    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Quantity cannot be negative.")

    def update_price(self, new_price):
        if new_price >= 0:
            self.price = new_price
        else:
            print("Price cannot be negative.")

# --- Test your Item class (you can put this outside the class, temporarily) ---
if __name__ == "__main__":
    apple = Item("Apple", 10, 1.50)
    apple.display_item() # Should output: Name: Apple, Quantity: 10, Price: $1.50

    apple.update_quantity(15)
    apple.display_item() # Should output: Name: Apple, Quantity: 15, Price: $1.50

    apple.update_quantity(-5) # Should print: Quantity cannot be negative.
    apple.display_item() # Should still be: Name: Apple, Quantity: 15, Price: $1.50

    apple.update_price(1.75)
    apple.display_item() # Should output: Name: Apple, Quantity: 15, Price: $1.75