"""Activity 6.2 - Reservation Class
   Aarón Cortés García - A01730451
"""

import json
import os
from hotel import Hotel
from customer import Customer


class Reservation:
    """Class representing a reservation in the hotel system."""
    FILE_NAME = "reservations.json"  # File where reservation data is stored

    def __init__(self, reserv_id, customer, hotel, room_id):
        """Initializes a reservation with customer, hotel, and room ID."""
        self.reserv_id = reserv_id  # Unique ID for reservation
        self.customer = customer  # Customer object who made the reservation
        self.hotel = hotel  # Hotel object where the reservation is made
        self.room_id = room_id  # ID of the reserved room

    def to_dict(self):
        """Converts the reservation object into a dict. for JSON storage."""
        return {
            "reserv_id": self.reserv_id,
            "customer_id": self.customer.customer_id,
            "hotel_name": self.hotel.name,
            "room_id": self.room_id
        }

    @classmethod
    def save_reservations(cls, reservations):
        """Saves a list of reservation objects to a JSON file."""
        with open(cls.FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump([reservation.to_dict() for reservation in reservations],
                      file, indent=4)

    @classmethod
    def load_reservations(cls):
        """Loads reservation data from JSON and returns a list of objects."""
        if not os.path.exists(cls.FILE_NAME):
            return []  # Return empty list if file does not exist
        try:
            with open(cls.FILE_NAME, 'r', encoding='utf-8') as file:
                return [Reservation(
                    data["reserv_id"],
                    Customer.get_customer(data["customer_id"]),
                    Hotel.get_hotel(data["hotel_name"]),
                    data["room_id"]
                ) for data in json.load(file)]
        except (json.JSONDecodeError, TypeError):
            print("Error loading reservations. Returning an empty list.")
            return []

    @classmethod
    def create_reservation(cls, reserv_id, customer_id, hotel_name, room_id):
        """Creates a new reserv., adds it to the list, and saves to file."""
        customer = Customer.get_customer(customer_id)
        hotel = Hotel.get_hotel(hotel_name)

        if customer is None or hotel is None:
            print("Customer or Hotel not found. Reservation not created.")
            return

        if hotel.reserve_room(room_id):
            reservation = Reservation(reserv_id, customer, hotel, room_id)
            reservations = cls.load_reservations()
            reservations.append(reservation)
            cls.save_reservations(reservations)
            print(f"Reservation {reserv_id} created successfully.")
        else:
            print(f"Room {room_id} at {hotel_name} is not available.")

    @classmethod
    def cancel_reservation(cls, reserv_id):
        """Cancels an existing reservation and frees the room."""
        reservations = cls.load_reservations()
        reserv_to_cancel = None

        for reservation in reservations:
            if reservation.reserv_id == reserv_id:
                reserv_to_cancel = reservation
                break

        if reserv_to_cancel:
            reserv_to_cancel.hotel.cancel_reservation(reserv_to_cancel.room_id)
            reservations.remove(reserv_to_cancel)
            cls.save_reservations(reservations)
            print(f"Reservation {reserv_id} cancelled successfully.")
        else:
            print(f"Reservation with ID {reserv_id} not found.")

    @classmethod
    def get_reservation(cls, reserv_id):
        """Retrieves a reservation by ID if it exists."""
        for reservation in cls.load_reservations():
            if reservation.reserv_id == reserv_id:
                return reservation
        return None  # Return None if not found
