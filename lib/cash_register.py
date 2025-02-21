#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []  # List to keep track of items
        self.last_transaction = 0  # Store last transaction amount
        self.last_transaction_count = 0  # Track the quantity of the last added item

    def add_item(self, item_name, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity  # Track the last transaction
        self.last_transaction_count = quantity  # Store quantity for voiding
        self.items.extend([item_name] * quantity)  # Add item name multiple times

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount

        # Ensure proper formatting
            total_formatted = int(self.total) if self.total.is_integer() else round(self.total, 2)
            print(f"After the discount, the total comes to ${total_formatted}.")  # Added period for exact match
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:  # Ensure there are items before voiding
            self.total -= self.last_transaction  # Subtract last transaction amount
            self.items = self.items[:-self.last_transaction_count]  # Remove correct count
            self.last_transaction = 0  # Reset last transaction
            self.last_transaction_count = 0  # Reset last transaction count
