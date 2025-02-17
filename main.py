"""Activity 6.2 - Main menu for managing hotels,
   customers, and reservations. Aarón Cortés
   García - A01730451
"""

from hotel import Hotel
from customer import Customer
from reservation import Reservation


def display_menu():
    """Displays the main menu options."""
    print("\nHotel Management System")
    print("1. Create Hotel")
    print("2. Modify Hotel")
    print("3. Delete Hotel")
    print("4. Create Customer")
    print("5. Modify Customer")
    print("6. Delete Customer")
    print("7. Make Reservation")
    print("8. Cancel Reservation")
    print("0. Exit")


def handle_create_hotel():
    """Handles the creation of a new hotel."""
    name = input("Enter hotel name: ")
    location = input("Enter hotel location: ")
    rooms = int(input("Enter number of rooms: "))
    Hotel.create_hotel(name, location, rooms)
    print("Hotel created successfully.")


def handle_modify_hotel():
    """Handles hotel modification."""
    name = input("Enter hotel name to modify: ")
    hotel = Hotel.get_hotel(name)
    if not hotel:
        print("Hotel not found.")
        return
    new_location = input("Enter new location (leave blank to skip): ")
    hotel.modify_hotel(location=new_location if new_location else None)
    print("Hotel modified successfully.")


def handle_delete_hotel():
    """Handles hotel deletion."""
    name = input("Enter hotel name to delete: ")
    Hotel.delete_hotel(name)
    print("Hotel deleted successfully.")


def handle_create_customer():
    """Handles the creation of a new customer."""
    customer_id = int(input("Enter customer ID: "))
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone: ")
    Customer.create_customer(customer_id, name, email, phone)
    print("Customer created successfully.")


def handle_modify_customer():
    """Handles customer modification."""
    customer_id = int(input("Enter customer ID to modify: "))
    customer = Customer.get_customer(customer_id)
    if not customer:
        print("Customer not found.")
        return
    new_name = input("Enter new name (leave blank to skip): ")
    new_email = input("Enter new email (leave blank to skip): ")
    new_phone = input("Enter new phone (leave blank to skip): ")
    customer.modify_customer(
        name=new_name if new_name else None,
        email=new_email if new_email else None,
        phone=new_phone if new_phone else None
    )
    print("Customer modified successfully.")


def handle_delete_customer():
    """Handles customer deletion."""
    customer_id = int(input("Enter customer ID to delete: "))
    Customer.delete_customer(customer_id)
    print("Customer deleted successfully.")


def handle_make_reservation():
    """Handles making a reservation."""
    reserv_id = int(input("Enter reservation ID: "))
    customer_id = int(input("Enter customer ID: "))
    hotel_name = input("Enter hotel name: ")
    room_id = int(input("Enter room ID: "))
    Reservation.create_reservation(reserv_id, customer_id, hotel_name, room_id)
    print("Reservation created successfully.")


def handle_cancel_reservation():
    """Handles reservation cancellation."""
    reserv_id = int(input("Enter reservation ID to cancel: "))
    Reservation.cancel_reservation(reserv_id)
    print("Reservation canceled successfully.")


def main():
    """Main function to run the cyclic menu."""
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                handle_create_hotel()
            elif choice == 2:
                handle_modify_hotel()
            elif choice == 3:
                handle_delete_hotel()
            elif choice == 4:
                handle_create_customer()
            elif choice == 5:
                handle_modify_customer()
            elif choice == 6:
                handle_delete_customer()
            elif choice == 7:
                handle_make_reservation()
            elif choice == 8:
                handle_cancel_reservation()
            elif choice == 0:
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
