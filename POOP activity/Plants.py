class Plant:
    def __init__(self, name, green, non_green):
        self.name = name
        self.green = green
        self.non_green = non_green

    def display_info(self):
        print(f"Plant: {self.name}, Green: {self.green}, Non-Green: {self.non_green}")

plant1 = Plant("Fern", True, False)
plant2 = Plant("Cactus", False, True)

plant1.display_info()
plant2.display_info()