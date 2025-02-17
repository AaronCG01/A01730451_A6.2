"""Activity 6.2 - Unit test cases
   Aarón Cortés García - A01730451
"""

import unittest
import os
from hotel import Hotel
from customer import Customer
from reservation import Reservation

class TestHotelSystem(unittest.TestCase):
    """Unit tests for the Hotel, Customer, and Reservation classes."""

    def setUp(self):
        """Setup test environment by clearing JSON files."""
        for file in [Hotel.FILE_NAME, Customer.FILE_NAME, Reservation.FILE_NAME]:
            if os.path.exists(file):
                os.remove(file)
    
    def test_create_hotel(self):
        """Test creating and retrieving a hotel."""
        Hotel.create_hotel("FiestaInn", "Puebla", 10)
        hotel = Hotel.get_hotel("FiestaInn")
        self.assertIsNotNone(hotel)
        self.assertEqual(hotel.name, "FiestaInn")
        self.assertEqual(hotel.location, "Puebla")
        self.assertEqual(len(hotel.rooms), 10)

    def test_modify_hotel(self):
        """Test modifying a hotel's details."""
        Hotel.create_hotel("Grand Americana", "CDMX", 8)
        hotel = Hotel.get_hotel("Grand Americana")
        hotel.modify_hotel(location="Monterrey")
        hotel = Hotel.get_hotel("Grand Americana")
        self.assertEqual(hotel.location, "Monterrey")

    def test_delete_hotel(self):
        """Test deleting a hotel."""
        Hotel.create_hotel("Linda Vista", "Tlaxcala", 5)
        Hotel.delete_hotel("Linda Vista")
        self.assertIsNone(Hotel.get_hotel("Linda Vista"))

    def test_reserve_room(self):
        """Test reserving a room in a hotel."""
        Hotel.create_hotel("Amanecer", "Yucatán", 20)
        hotel = Hotel.get_hotel("Amanecer")
        self.assertTrue(hotel.reserve_room(2))
        self.assertFalse(hotel.reserve_room(2))  # Should not allow double booking

    def test_create_customer(self):
        """Test creating and retrieving a customer."""
        Customer.create_customer(1, "Lili Sosa", "lsosa7@gmail.com", "2211837274")
        customer = Customer.get_customer(1)
        self.assertIsNotNone(customer)
        self.assertEqual(customer.name, "Lili Sosa")
        self.assertEqual(customer.email, "lsosa7@gmail.com")
        self.assertEqual(customer.phone, "2211837274")

    def test_modify_customer(self):
        """Test modifying a customer's details."""
        Customer.create_customer(2, "Emmanuel Reyes", "mane_r@hotmail.com", "2216730964")
        customer = Customer.get_customer(2)
        customer.modify_customer(name="Alejandro Flores", phone="2528713275")
        customer = Customer.get_customer(2)
        self.assertEqual(customer.name, "Alejandro Flores")
        self.assertEqual(customer.phone, "2528713275")

    def test_delete_customer(self):
        """Test deleting a customer."""
        Customer.create_customer(3, "Alice", "alice@gmail.com", "2489009898")
        Customer.delete_customer(3)
        self.assertIsNone(Customer.get_customer(3))

    def test_create_reservation(self):
        """Test creating and retrieving a reservation."""
        # Create a hotel and a customer
        Hotel.create_hotel("Plaza Hotel", "Monterrey", 10)
        hotel = Hotel.get_hotel("Plaza Hotel")
        Customer.create_customer(10, "Sergio Martínez", "sergio@gmail.com", "5566778899")
        customer = Customer.get_customer(10)

        # Create a reservation for a valid room and customer
        Reservation.create_reservation(1, customer.customer_id, hotel.name, 1)
        reservation = Reservation.get_reservation(1)

        self.assertIsNotNone(reservation)
        self.assertEqual(reservation.reserv_id, 1)
        self.assertEqual(reservation.customer.customer_id, customer.customer_id)
        self.assertEqual(reservation.hotel.name, hotel.name)
        self.assertEqual(reservation.room_id, 1)

    def test_cancel_reservation(self):
        """Test canceling a reservation and freeing the room."""
        # Create a hotel and a customer
        Hotel.create_hotel("Vista Bella", "Guadalajara", 8)
        hotel = Hotel.get_hotel("Vista Bella")
        Customer.create_customer(30, "Margarita Pérez", "margarita@gmail.com", "5544336677")
        customer = Customer.get_customer(30)

        # Create and cancel a reservation
        Reservation.create_reservation(3, customer.customer_id, hotel.name, 7)
        self.assertTrue(hotel.reserve_room(7))  # Ensure the room is reserved
        Reservation.cancel_reservation(3)
        self.assertFalse(hotel.reserve_room(7))  # Room should be freed after cancellation

    def test_create_reservation_invalid_customer_or_hotel(self):
        """Test creating a reservation for a non-existent customer or hotel."""
        # Try creating a reservation with an invalid customer and/or hotel
        self.assertIsNone(Customer.get_customer(99))  # Non-existent customer
        self.assertIsNone(Hotel.get_hotel("NonExistentHotel"))  # Non-existent hotel
        Reservation.create_reservation(2, 99, "NonExistentHotel", 1)
        reservation = Reservation.get_reservation(2)
        self.assertIsNone(reservation)  # No reservation should be created

    def test_get_reservation(self):
        """Test retrieving an existing reservation by its ID."""
        # Create a hotel and a customer
        Hotel.create_hotel("Grand Plaza", "Veracruz", 12)
        hotel = Hotel.get_hotel("Grand Plaza")
        Customer.create_customer(40, "Raúl Sánchez", "raul@webmail.com", "2215667788")
        customer = Customer.get_customer(40)

        # Create a reservation
        Reservation.create_reservation(4, customer.customer_id, hotel.name, 10)
        reservation = Reservation.get_reservation(4)
        self.assertIsNotNone(reservation)
        self.assertEqual(reservation.reserv_id, 4)

    def tearDown(self):
        """Clean up JSON files after tests."""
        for file in [Hotel.FILE_NAME, Customer.FILE_NAME, Reservation.FILE_NAME]:
            if os.path.exists(file):
                os.remove(file)

if __name__ == "__main__":
    unittest.main()
