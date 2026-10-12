class Node:
    def __init__(self, name, age, source, destination, seat):
        self.name = name
        self.age = age
        self.source = source
        self.destination = destination
        self.seat = seat
        self.next = None

 
class ReservationSystem:
    def __init__(self):
        self.head = None

    def book_ticket(self):
        print("\n----- BOOK TICKET -----")

        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        source = input("Enter source: ")
        destination = input("Enter destination: ")
        seat = int(input("Enter seat number (1-20): "))

        if seat < 1 or seat > 20:
            print("Invalid seat number!")
            return

        current = self.head

        while current is not None:
            if current.seat == seat:
                print("Sorry! Seat already booked.")
                return
            current = current.next

        new_node = Node(name, age, source, destination, seat)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        print("\nTicket booked successfully!")
        print("Passenger:", name)
        print("Seat:", seat)

    def display_reservations(self):
        print("\n----- ALL RESERVATIONS -----")

        if self.head is None:
            print("No reservations found.")
            return

        current = self.head

        while current is not None:
            print("----------------------------")
            print("Name        :", current.name)
            print("Age         :", current.age)
            print("Source      :", current.source)
            print("Destination :", current.destination)
            print("Seat Number :", current.seat)

            current = current.next

    def search_ticket(self):
        print("\n----- SEARCH TICKET -----")

        name = input("Enter passenger name: ")

        current = self.head

        while current is not None:
            if current.name.lower() == name.lower():
                print("\nReservation Found!")
                print("Name        :", current.name)
                print("Age         :", current.age)
                print("Source      :", current.source)
                print("Destination :", current.destination)
                print("Seat Number :", current.seat)
                return

            current = current.next

        print("Reservation not found.")

    def cancel_ticket(self):
        print("\n----- CANCEL TICKET -----")

        seat = int(input("Enter seat number to cancel: "))

        current = self.head
        previous = None

        while current is not None:

            if current.seat == seat:

                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                print("Ticket cancelled successfully!")
                return

            previous = current
            current = current.next

        print("No reservation found for this seat.")

    def display_seats(self):
        print("\n----- SEAT STATUS -----")

        for seat in range(1, 21):
            current = self.head
            booked = False

            while current is not None:
                if current.seat == seat:
                    booked = True
                    break
                current = current.next

            if booked:
                print(f"Seat {seat}: Booked")
            else:
                print(f"Seat {seat}: Available")


system = ReservationSystem()

while True:

    print("\n===================================")
    print("   BUS / TRAIN RESERVATION SYSTEM")
    print("===================================")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Search Ticket")
    print("4. Display Reservations")
    print("5. Display Seat Status")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.book_ticket()

    elif choice == "2":
        system.cancel_ticket()

    elif choice == "3":
        system.search_ticket()

    elif choice == "4":
        system.display_reservations()

    elif choice == "5":
        system.display_seats()

    elif choice == "6":
        print("\nThank you for using the system!")
        break

    else:
        print("Invalid choice!")
