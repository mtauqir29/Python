"""  Mohammad Zaid Tauqir
     PSID: 1900570
"""
# Type code for classes here
class ItemToPurchase:
    def __init__(self, items_name = "none", items_price = 0, items_quantity = 0):
        self.item_name = items_name
        self.item_price = items_price
        self.item_quantity = items_quantity
    def print_item_cost(self):
        print(self.item_name, self.item_quantity, '@ $' + str(self.item_price), '= $' + str((self.item_price * self.item_quantity)))


if __name__ == "__main__":

    print("Item 1")

    first_item = ItemToPurchase()

    second_item = ItemToPurchase()

    # prompt and Read item1 details from the user
    first_item.item_name = input("Enter the item name:\n")
    first_item.item_price = int(input("Enter the item price:\n"))
    first_item.item_quantity = int(input("Enter the item quantity:\n"))

    print("\nItem 2")

    # prompt and Read item2 details from the user
    second_item.item_name = input("Enter the item name:\n")
    second_item.item_price = int(input("Enter the item price:\n"))
    second_item.item_quantity = int(input("Enter the item quantity:\n"))

    print("\nTOTAL COST")

    first_item.print_item_cost()
    second_item.print_item_cost()

    # Calculate the cost of items
    total = (first_item.item_price * first_item.item_quantity) + (second_item.item_price * second_item.item_quantity)

    # Display the total cost
    print("\nTotal: $" + str(total))
