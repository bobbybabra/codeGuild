# make a store
# inventory
# checkout
# accounts
# use multiple inheritance pattern class and strive for 'dry code'
# ------------------------------------------------------------------
# idea: stock market input to generate prices
#===================================================================
#import random
#import os
#import sqlite3


class Wholesale():
    def __init__(self):
        self.delivery = delivery
        self.order = order
        self.payout = payout


class Store(object):
    def __init__(self, item):
        self.avail_items = {}
        self.customer_basket = {}

    def find(self,text):
        found_list = []
        for index, item in self.available_items.items():
            name = item.name
            position = name.find(text)
            if position <> -1:
                found_list.append(item)
        return found_list
# dict to list, pop, then add 11?
        # self.item = widgets
        # self.colors = colors
        # self.size_price = dict(zip('small, medium, large', [10, 20, 30]))


class InventoryItem():
    def __init__(self, name, on_hand, price):
        self.name = name
        self.on_hand = on_hand
        self.price = price
	self.sizes = None
	self.colors = None
	
    def __repr__(self):
        output = ""
        output = output + self.name
        output = output + " @ " + str(self.price)
        return output

sizes = ["small","medium","large"]
colors = ["black","white"]

class InventoryItemFactory():
    def make_item(self, name, sizes, colors):
        widget = InventoryItem()
        widget.name = name
        widget.sizes = sizes
        widget.colors = colors
	return widget

factory = InventoryItemFactory()
small_black = factory.make_item("widget","small","black")
print small_black

for type.color in list(types, sizes, colors):
    print(types, sizes, colors

    # def ls_inventory(self):
    #     print len(inventory)


class CartLineItems():
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity


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
        output = "Cart\n"
        for line in self.selected_items:
            output = output + str(line) + "\n"
        output = output + "\nTotal" + str(self.get_total())
        return output


class Custormer():
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def search(self, input_name):
        if input_name in self.name:
            print 'ok'
        elif:
            print 'welcome new customer %s' %input_name
            self.customer_list.append {(customer_list:-1) + 11 : 'input_name'}


# class MakeOrder(Wholesale, Store):
#     def placeOrder(self):
#         print ("how many widget do you want to order?")
#         order_input = input(">")
#         if widgets <= 20
#             print "time to order more widgets"
#             print "the store has %d items" % widgets
#
#
# class Menu(Store, Customer, Wholesale):
#     def register_menu(self):
#         print "--" * 20a
#         print '--' *20
#         print "enter number for choice"
#         print ("1 Checkout Customer")
#         print ("2 Print Inventory")
#         print ("3 Order from Wholesale")
#         print ("4 Discount Item")
#         print ("5 Search for item")
#         print ("6 Quit")
#         print ("**") * 20
#         print ("**") * 20
#         choice = int(raw_input('> '))
#             if choice == 1:
#                 checkout()
#             if choice == 2:
#                 ls_inventory()
#             if choice == 3:
#                 wholesale_order()
#             if choice == 4:
#                 manual_discount()
#             if choice == 5:
#
#             if choice == 6:
#                 quit()
#
# class Accounts(Store):
#     def __init__(self):
#         self.name = none
#         self.code = code
#         self.company = company
#         self.money = money
#         self.payable = payable
#         self.expense = expense
#         self.credit = credit
#         self.taxes.taxes
#
#
# class Import(Accounts):
#     pass
#
#
# class Export(Accounts):
#     pass
#
#
# class Checkout(Accounts):
#     def out(self):
#         barcode = Accounts.barcode()
#         register = []
#
#
# class Employees(Accounts):
#     def __init__(self):
#         self.ft = fulltime
#         self.pt = parttime
#         self.shift = [1, 2, 3]
#
#
# class SaleItems(Checkout):
#     def __init__(self):
#         self.specials = specials

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
