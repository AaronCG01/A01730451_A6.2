"""Activity 6.2 - Hotel Class
   Aarón Cortés García - A01730451
"""

import json
import os


class Hotel:
    """Class representing a hotel with room management capabilities."""
    FILE_NAME = "hotels.json"  # File where hotel data is stored

    def __init__(self, name, location, rooms):
        """Initializes a hotel with a name, location, and a set of room IDs."""
        self.name = name  # Hotel name
        self.location = location  # Hotel location
        self.rooms = {i: False for i in range(1, rooms+1)}  # Rooms with status

    def to_dict(self):
        """Converts the hotel object into a dictionary for JSON storage."""
        return {
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms  # Dictionary of room statuses
        }

    @classmethod
    def save_hotels(cls, hotels):
        """Saves a list of hotel objects to a JSON file."""
        with open(cls.FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump([hotel.to_dict() for hotel in hotels], file, indent=4)

    @classmethod
    def load_hotels(cls):
        """Loads hotel data from JSON file and returns a list of objects."""
        if not os.path.exists(cls.FILE_NAME):
            return []
        try:
            with open(cls.FILE_NAME, 'r', encoding='utf-8') as file:
                return [Hotel(data["name"], data["location"],
                        len(data["rooms"])) for data in json.load(file)]
        except (json.JSONDecodeError, TypeError):
            print("Error loading hotels. Returning an empty list.")
            return []

    @classmethod
    def create_hotel(cls, name, location, rooms):
        """Creates a new hotel, adds it to the list, and saves it to a file."""
        hotels = cls.load_hotels()
        hotels.append(Hotel(name, location, rooms))  # Append new hotel
        cls.save_hotels(hotels)

    @classmethod
    def delete_hotel(cls, name):
        """Deletes a hotel by name and updates the file."""
        hotels = [hotel for hotel in cls.load_hotels() if hotel.name != name]
        cls.save_hotels(hotels)

    @classmethod
    def get_hotel(cls, name):
        """Retrieves a hotel by name if it exists."""
        for hotel in cls.load_hotels():
            if hotel.name == name:
                return hotel
        return None

    def modify_hotel(self, location=None):
        """Updates hotel details while preserving room availability."""
        if location:
            self.location = location  # Update only the location

        # Load all hotels, find the current one, and update it
        hotels = self.load_hotels()
        for i, hotel in enumerate(hotels):
            if hotel.name == self.name:
                hotels[i] = self  # Replace with updated instance
                break

        self.save_hotels(hotels)  # Save changes to file

    def reserve_room(self, room_id):
        """Reserves a specific room by ID if available."""
        if room_id in self.rooms and not self.rooms[room_id]:
            self.rooms[room_id] = True  # Mark room as reserved
            self.modify_hotel()
            return True
        return False  # Room is already reserved or does not exist

    def cancel_reservation(self, room_id):
        """Cancels a reservation for a specific room by ID."""
        if room_id in self.rooms and self.rooms[room_id]:
            self.rooms[room_id] = False  # Mark room as available
            self.modify_hotel()
            return True
        return False  # Room is not reserved or does not exist
