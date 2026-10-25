class Order:
  def __init__(self, order_id):
    self.order_id = order_id

class Customer:
  def __init__(self, name):
    self.name = name
    self.orders = []

  def add_order(self, order):
    self.orders.append(order)

if __name__ == "__main__":
  cust = Customer("Ziggy")
  ord_item = Order(101)
  cust.add_order(ord_item)
  print(f"Customer {cust.name} has order ID: {cust.orders[0].order_id}")