class Orbit:
    def __init__(self, change_from, change_to, take_off_delta, low_orbit=None):
        self.change_from = change_from
        self.change_to = change_to
        self.take_off_delta = take_off_delta
        self.low_orbit = low_orbit


    def display_orbit_details(self):
        total_delta = self.low_orbit + self.take_off_delta
        print(f"TakeOff from {self.change_from}: {self.take_off_delta} m/s")
        print(f"Transit from {self.change_from} low orbit to {self.change_to} low orbit: {self.low_orbit} m/s")
        print(f"Transit from {self.change_from} to {self.change_to} total: {total_delta} m/s")
