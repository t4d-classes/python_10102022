


class WishList:

  # items = []

  def __init__(self):
    self.items = []

  def add_item(self, item_name):
    self.items.append(item_name)

  def print_items(self):
    print(self.items)


john_wish_list = WishList();
john_wish_list.add_item("fish")
john_wish_list.add_item("radio controlled car")
john_wish_list.print_items()

joy_wish_list = WishList();
joy_wish_list.add_item("phone")
joy_wish_list.add_item("puppy")
joy_wish_list.print_items()

john_wish_list.print_items()