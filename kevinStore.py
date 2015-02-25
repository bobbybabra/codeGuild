__author__ = 'kevin'


class Store():
    def __init__(self):
        self.available_items = []
        self.customer_list = []


class InventoryItem():
    def __init__(self, name, on_hand, price):
        self.name = name
        self.on_hand = on_hand
        self.price = price

    def __repr__(self):
        output = ""
        output = output + self.name
        output = output + " @ " + str(self.price)
        return output


class CartLineItem():
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def __repr__(self):
        output = ""
        output = output + str(self.quantity)
        output = output + " x "
        output = output + str(self.item)
        output = output + " is "
        output = output + str(self.quantity * self.item.price)
        return output


class Cart():
    def __init__(self):
        self.selected_items = []

    def get_total(self):
        total = 0.0
        for line in self.selected_items:
            line_total = line.quantity * line.item.price
            total = total + line_total
        return total

    def __repr__(self):
        output = "Cart:\n"
        for line in self.selected_items:
            output = output + str(line) + "\n"
        output = output + "\nTotal: " + str(self.get_total())
        return output


class Customer():
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

from store import *

# TEST
amazon = Store()

amazon.available_items = {
    111: InventoryItem("Farenheit 451", 10, 4.99),
    222: InventoryItem("World According to Garp", 5, 4.99),
    333: InventoryItem("Stranger in a Stange Land.", 1, 4.99),
}
amazon.customer_list = {
    11: Customer("Bob"),
    22: Customer("Carol"),
}


# ##
# TEST
# ##

# who are you? select a customer.
bob = amazon.customer_list[11]

# what do you want to buy?
item = amazon.available_items[333]

#how many?
qty = 2

#add to cart
bob.cart.selected_items.append(CartLineItem(item, qty))

#what do you want to buy?
item = amazon.available_items[222]

#how many?
qty = 3

#add to cart
bob.cart.selected_items.append(CartLineItem(item, qty))

#add more? if no then checkout and print cart
print bob.cart
