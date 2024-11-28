class Vehicle:
    def __init__(self, name, price_per_day):
        """
        Initialize a vehicle with a name and rental price per day.
        """
        self.name = name  # Vehicle name (e.g., "Honda Civic", "Yamaha R15")
        self.price_per_day = price_per_day  # Rental price per day
        self.is_available = True  # Availability status (True = available, False = rented)

class RentalSystem:
    def __init__(self):
        """
        Initialize the rental system with a list of vehicles.
        """
        self.vehicles = [
            Vehicle("Honda Civic", 50),
            Vehicle("Toyota Corolla", 40),
            Vehicle("Yamaha R15", 20),
            Vehicle("Suzuki Gixxer", 15),
        ]

    def display_available_vehicles(self):
        """
        Display all vehicles that are available for rent.
        """
        print("\n--- Available Vehicles ---")
        for i, vehicle in enumerate(self.vehicles):
            if vehicle.is_available:  # Only show available vehicles
                print(f"{i + 1}. {vehicle.name} - ${vehicle.price_per_day} per day")
        print("--------------------------")

    def rent_vehicle(self):
        """
        Allow the user to rent a vehicle.
        """
        self.display_available_vehicles()
        try:
            choice = int(input("Enter the number of the vehicle you want to rent: "))
            if 1 <= choice <= len(self.vehicles):
                vehicle = self.vehicles[choice - 1]
                if vehicle.is_available:
                    vehicle.is_available = False  # Mark the vehicle as rented
                    print(f"You have successfully rented the {vehicle.name} for ${vehicle.price_per_day} per day.")
                else:
                    print(f"Sorry, the {vehicle.name} is already rented.")
            else:
                print("Invalid choice. Please select a valid vehicle number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def return_vehicle(self):
        """
        Allow the user to return a rented vehicle.
        """
        print("\n--- Rented Vehicles ---")
        rented_vehicles = [vehicle for vehicle in self.vehicles if not vehicle.is_available]
        if not rented_vehicles:
            print("No vehicles are currently rented.")
            return

        for i, vehicle in enumerate(rented_vehicles):
            print(f"{i + 1}. {vehicle.name}")
        
        try:
            choice = int(input("Enter the number of the vehicle you want to return: "))
            if 1 <= choice <= len(rented_vehicles):
                vehicle = rented_vehicles[choice - 1]
                vehicle.is_available = True  # Mark the vehicle as available
                print(f"You have successfully returned the {vehicle.name}.")
            else:
                print("Invalid choice. Please select a valid vehicle number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def menu(self):
        """
        Display the menu and allow the user to interact with the system.
        """
        while True:
            print("\n--- Vehicle Rental System ---")
            print("1. View Available Vehicles")
            print("2. Rent a Vehicle")
            print("3. Return a Vehicle")
            print("4. Exit")
            try:
                choice = int(input("Choose an option (1-4): "))
                if choice == 1:
                    self.display_available_vehicles()
                elif choice == 2:
                    self.rent_vehicle()
                elif choice == 3:
                    self.return_vehicle()
                elif choice == 4:
                    print("Thank you for using the Vehicle Rental System. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please choose a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# Main program
rental_system = RentalSystem()
rental_system.menu()
