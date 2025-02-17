"""Activity 6.2 - Customer Class
   Aarón Cortés García - A01730451
"""

import json
import os


class Customer:
    """Class representing a customer in the hotel system."""
    FILE_NAME = "customers.json"  # File where customer data is stored

    def __init__(self, customer_id, name, email, phone):
        """Initializes a customer with his fields"""
        self.customer_id = customer_id  # Unique identifier for the customer
        self.name = name  # Full name of the customer
        self.email = email  # Contact email address
        self.phone = phone  # Contact phone number

    def to_dict(self):
        """Converts the customer object into a dictionary for JSON storage."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

    @classmethod
    def save_customers(cls, customers):
        """Saves a list of customer objects to a JSON file."""
        with open(cls.FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump([customer.to_dict() for customer in customers],
                      file, indent=4)

    @classmethod
    def load_customers(cls):
        """Loads customer data from JSON file and returns a list of objects."""
        if not os.path.exists(cls.FILE_NAME):
            return []  # Return empty list if file does not exist
        try:
            with open(cls.FILE_NAME, 'r', encoding='utf-8') as file:
                return [Customer(**data) for data in json.load(file)]
        except (json.JSONDecodeError, TypeError):
            print("Error loading customers. Returning an empty list.")
            return []

    @classmethod
    def create_customer(cls, customer_id, name, email, phone):
        """Creates a new customer, adds it to the list, and saves to file."""
        customers = cls.load_customers()
        customers.append(Customer(customer_id, name, email, phone))
        cls.save_customers(customers)  # Save updated list to file

    @classmethod
    def delete_customer(cls, customer_id):
        """Deletes a customer by ID and updates the file."""
        customers = [c for c in cls.load_customers()
                     if c.customer_id != customer_id]
        cls.save_customers(customers)  # Save updated customer list

    @classmethod
    def get_customer(cls, customer_id):
        """Retrieves a customer by ID if it exists."""
        for customer in cls.load_customers():
            if customer.customer_id == customer_id:
                return customer  # Return the matching customer
        return None  # Return None if not found

    def modify_customer(self, name=None, email=None, phone=None):
        """Updates customer details such as name, email, or phone number."""
        if name:
            self.name = name  # Update name if provided
        if email:
            self.email = email  # Update email if provided
        if phone:
            self.phone = phone  # Update phone if provided
        customers = self.load_customers()
        for i, customer in enumerate(customers):
            if customer.customer_id == self.customer_id:
                customers[i] = self  # Replace old customer with updated data
                break
        self.save_customers(customers)  # Save the updated list to file
