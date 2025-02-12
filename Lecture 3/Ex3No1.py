class Train:
    """
    Initializes a train with a list of carriages, each containing reserved seats.
    Uses departure and destination locations.
    A train must have at least one carriage and a unique identifier.
    """

    def __init__(self, destination, departure, train_id, num_seats):
        self.destination = destination
        self.departure = departure
        self.train_id = train_id
        self.num_seats = num_seats
        self.carriages = [{}]  # First carriage is an empty dictionary (to track reserved seats)

    """ Adding new carriage """
    def add_carriage(self):
        self.carriages.append({})
        print("A new carriage has been added.")

    """ Removing a carriage """
    def remove_carriage(self, index):
        if len(self.carriages) > 1:
            del self.carriages[index]
            print(f"The carriage at position {index + 1} has been removed.")
        else:
            print("The carriage cannot be removed because it is the last one.")

    """ Reserving a seat """
    def reserve_seat(self, seat_number):
        """Reserves a seat in the first available carriage."""
        for carriage in self.carriages:
            if seat_number not in carriage and len(carriage) < self.num_seats:
                carriage[seat_number] = "Reserved"
                print(f"Seat {seat_number} reserved.")
                return
        print(f"Sorry, Seat {seat_number} is already reserved or no space available.")

    """ Displaying free and reserved seats """
    def report(self):
        print(f"Train {self.train_id}: {self.departure} to {self.destination}")
        for i, carriage in enumerate(self.carriages, start=1):
            print(f"Carriage {i}: {carriage}")

    """ Removing a reservation """
    def remove_reservation(self, seat_number):
        for carriage in self.carriages:
            if seat_number in carriage:
                del carriage[seat_number]
                print(f"Reservation for seat {seat_number} removed.")
                return
        print(f"Seat {seat_number} was not reserved.")


# Example usage:
train = Train("Turku", "Tampere", "TT789", 10)

train.reserve_seat(1)
train.reserve_seat(2)
train.reserve_seat(3)

train.add_carriage()
train.reserve_seat(5)
train.remove_reservation(2)

train.report()
