class Room:
  def __init__(self, room_type):
    self.room_type = room_type

class House:
  def __init__(self):
    self.rooms = [Room("Living Room"), Room("Bedroom")]

if __name__ == "__main__":
  h = House()
  print(f"House has {len(h.rooms)} rooms.")