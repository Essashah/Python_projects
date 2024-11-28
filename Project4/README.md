Vehicle Rental System
A simple Python-based system for renting and returning vehicles. The system allows users to view available vehicles, rent them, and return them.

Features:
View Available Vehicles: Displays vehicles available for rent.
Rent a Vehicle: Rent a vehicle and mark it as unavailable.
Return a Vehicle: Return a rented vehicle and make it available again.
Menu-driven Interface: Easy-to-use menu for interacting with the system.
Algorithms Used
Filtering Vehicles: Uses loops to display only available vehicles.
Renting & Returning: Updates vehicle availability (True or False) based on user actions.
Validation: Ensures valid input when selecting vehicles to rent or return.
How to Use
Clone or download the repository.

Run the script:
Copy code
python vehicle_rental_system.py
Choose options from the menu:

View available vehicles.
Rent a vehicle by selecting it.
Return a rented vehicle.
Installation
Python 3.7 or higher is required. No additional libraries needed.
Example:
python
# Start the rental system
rental_system = RentalSystem()
rental_system.menu()
