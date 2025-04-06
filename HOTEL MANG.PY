# Hotel Management System with Room Booking & Payment

class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Room {self.room_number} ({self.room_type}) - ${self.price}/night - {status}"


class Customer:
    def __init__(self, customer_id, name, phone, email):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class Booking:
    def __init__(self, booking_id, customer, room, check_in_date, check_out_date):
        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.room.is_booked = True

    def __str__(self):
        return f"Booking ID: {self.booking_id}, Customer: {self.customer.name}, Room: {self.room.room_number}, Check-In: {self.check_in_date}, Check-Out: {self.check_out_date}"


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.customers = []
        self.bookings = []
        self.initialize_rooms()

    def initialize_rooms(self):
        """Dynamically add rooms (1-50 Single, 51-100 Double)."""
        for i in range(1, 51):
            self.add_room(Room(i, "Single", 100))  # Single rooms priced at $100
        for i in range(51, 101):
            self.add_room(Room(i, "Double", 150))  # Double rooms priced at $150

    def add_room(self, room):
        self.rooms.append(room)

    def add_customer(self, customer):
        self.customers.append(customer)

    def book_room(self, customer, room, check_in_date, check_out_date):
        if not room.is_booked:
            booking_id = len(self.bookings) + 1
            booking = Booking(booking_id, customer, room, check_in_date, check_out_date)
            self.bookings.append(booking)
            return booking
        else:
            return None

    def list_rooms(self, room_type=None):
        """Lists available rooms, filtered by type if specified."""
        available_rooms = [room for room in self.rooms if not room.is_booked]
        for room in available_rooms:
            if room_type is None or room.room_type == room_type:
                print(room)


class Payment:
    VALID_METHODS = ["UPI", "Card", "PhonePe", "Credit Card", "PayPal"]

    def __init__(self, method, amount):
        self.method = method
        self.amount = amount

    def process_payment(self):
        if self.method in Payment.VALID_METHODS:
            print(f"\n💳 Processing {self.method} payment of ₹{self.amount}...")
            print("✅ Payment successful!")
        else:
            print("❌ Invalid payment method! Please try again.")
            return False
        return True


def main():
    hotel = Hotel("Python Hotel")

    print("\n🚪 Welcome to SHARAD Hotel! 🚪\n")

    # Display available rooms categorized
    print("🏨 **Available Single Rooms (1-50):**")
    hotel.list_rooms("Single")

    print("\n🏨 **Available Double Rooms (51-100):**")
    hotel.list_rooms("Double")

    # Get customer details
    print("\n📋 **Please enter your details to book a room:**")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    customer_id = len(hotel.customers) + 1
    customer = Customer(customer_id, name, phone, email)
    hotel.add_customer(customer)

    # Get room selection
    room_type = int(input("\n🔹 Select Room Type:\n1️⃣ for Single Room\n2️⃣ for Double Room\n➡ Enter choice: "))

    if room_type == 1:
        print("\n✅ **Available Single Rooms (1 - 50):**")
        hotel.list_rooms("Single")
    elif room_type == 2:
        print("\n✅ **Available Double Rooms (51 - 100):**")
        hotel.list_rooms("Double")
    else:
        print("❌ Invalid room type! Exiting.")
        return

    # Room selection
    room_number = int(input("\n🔢 Enter the room number you want to book: "))
    selected_room = next((room for room in hotel.rooms if room.room_number == room_number), None)

    if not selected_room:
        print("❌ Invalid room number. Please try again.")
        return

    if selected_room.is_booked:
        print("❌ Sorry, this room is already booked.")
        return

    # Get booking dates
    check_in_date = input("\n📅 Enter check-in date (YYYY-MM-DD): ")
    check_out_date = input("📅 Enter check-out date (YYYY-MM-DD): ")

    # Book the room
    booking = hotel.book_room(customer, selected_room, check_in_date, check_out_date)
    if booking:
        print("\n✅ **Booking successful!** 🎉")
        print(booking)
    else:
        print("\n❌ Booking failed. Please try again.")

    # Process payment
    print("\n💳 **Payment Options:**")
    print("1️⃣ UPI\n2️⃣ Card\n3️⃣ PhonePe\n4️⃣ Credit Card\n5️⃣ PayPal")
    
    # Ensuring valid payment method selection
    while True:
        choice = int(input("➡ Select a payment method (1-5): "))
        payment_methods = {
            1: "UPI",
            2: "Card",
            3: "PhonePe",
            4: "Credit Card",
            5: "PayPal"
        }
        if choice in payment_methods:
            selected_method = payment_methods[choice]
            break
        else:
            print("❌ Invalid selection! Please enter a valid option.")

    payment = Payment(selected_method, selected_room.price)
    payment.process_payment()

    print("\n📌 **Current Bookings:**")
    for booking in hotel.bookings:
        print(booking)


if __name__ == "__main__":
    main()
