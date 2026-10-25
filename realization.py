from abc import ABC, abstractmethod

class Payable(ABC):
  @abstractmethod
  def pay(self, amount):
    pass

class Payment(Payable):
  def pay(self, amount):
    print(f"Paid ${amount} successfully.")

if __name__ == "__main__":
  p = Payment()
  p.pay(500)