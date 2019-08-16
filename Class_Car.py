class Car:
    def __init__ (self, seats):
        self.seats = seats
        self.busy_seats = 0
        if self.seats < 0:
            raise ValueError("число мест в автомобиле не может быть отрицательным")

    def available_seats(self):
        return(self.seats - self.busy_seats)

    def add_passenger(self):
        if self.available_seats() > 0:
            self.busy_seats += 1
        else:
            raise ValueError("Все места уже заняты")

    def remove_passenger(self):
        if self.busy_seats >0:
            self.busy_seats -= 1
        else:            raise ValueError("Все места уже свободны")

    def clean_car(self):
        self.busy_seats = 0