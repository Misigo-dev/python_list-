class Plane:
    def drive(self):
        print("The plane is taxiing on the runway ✈️")

class Boat:
    def drive(self):
        print("The boat is sailing ⛵")

# Treat them all the same
for vehicle in [Plane(), Boat()]:
    vehicle.drive()
