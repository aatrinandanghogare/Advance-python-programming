class Vehicle:
    def __init__(self, vehicle_no, brand, price, category):
        self.vehicle_no = vehicle_no
        self.brand = brand
        self.price = price
        self.category = category 

    def display(self):
        print(f"Vehicle No: {self.vehicle_no}")
        print(f"Brand  : {self.brand}")
        print(f"Price   : ₹{self.price}")
        print(f"Category  : {self.category}")
        print(f"\n")
  

class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print("Vehicle added successfully!\n")

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles available.")
        else:
            print("\nVehicle Details")
            for vehicle in self.vehicles:
                vehicle.display()

showroom = Showroom()

while True:

    print("1. Add Vehicle")
    print("2. Display All Vehicles")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        vehicle_no = input("Enter Vehicle Number: ")
        brand = input("Enter Brand: ")
        price = float(input("Enter Price: "))

        print("Category:")
        print("1. Luxury")
        print("2. Economy")
        cat_choice = int(input("Enter category choice: "))

        if cat_choice == 1:
            category = "Luxury"
        else:
            category = "Economy"

        vehicle = Vehicle(vehicle_no, brand, price, category)
        showroom.add_vehicle(vehicle)

    elif choice == 2:
        showroom.display_vehicles()

    elif choice == 3:
        print("Thank you for using Vehicle Showroom Management System.")
        break

    else:
        print("Invalid choice! Please try again.")
