class TrainCarriage:
    def __init__(self, num_seats):
        self.num_seats = num_seats
        self.reserved_seats = []

    def add_reservation(self, seat_number):
        if seat_number not in self.reserved_seats:
            self.reserved_seats.append(seat_number)
            print(f"Seat {seat_number} reserved.")
        else:
            print(f"Sorry ,Seat {seat_number} is already reserved.")
    
    def remove_reservation(self, seat_number):
        if seat_number in self.reserved_seats:
            self.reserved_seats.remove(seat_number)
            print(f"Reservation for seat {seat_number} removed.")
        else:
            print(f"Seat {seat_number} was not reserved.")
    
    def is_full(self):
        if len(self.reserved_seats) == self.num_seats:
            print("The carriage is full.")
        else:
            print(f"{self.num_seats - len(self.reserved_seats)} seats available.")
    
    def get_report(self):
        print("Reserved seats:", self.reserved_seats)
        print("Available seats:", [x for x in range(1, self.num_seats+1) if x not in self.reserved_seats])


# Example usage:
train = TrainCarriage(10)  # 10 seats in the carriage

train.add_reservation(1)
train.add_reservation(2)
train.add_reservation(3)

train.remove_reservation(2)

train.is_full()

train.get_report()
