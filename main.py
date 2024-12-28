class Orbit:
    def __init__(self, change_from, change_to, take_off_delta, low_orbit=None, total_delta=None):
        self.change_from = change_from
        self.change_to = change_to
        self.take_off_delta = take_off_delta
        self.low_orbit = low_orbit
        self.total_delta = total_delta

    def display_orbit_details(self):
        print(f"TakeOff from {self.change_from}: {self.take_off_delta} m/s")
        if self.low_orbit:
            print(f"Transit from {self.change_from} low orbit to {self.change_to} low orbit: {self.low_orbit} m/s")
        if self.total_delta:
            print(f"Transit from {self.change_from} to {self.change_to} total: {self.total_delta} m/s")


class SpaceMission:
    def __init__(self):
        self.orbit_data = {
            ('kerbin', 'kerbin'): Orbit('kerbin', 'kerbin', 3400, total_delta=3400),
            ('kerbin', 'mun'): Orbit('kerbin', 'mun', 3400, low_orbit=1170, total_delta=4570),
            ('kerbin', 'minmus'): Orbit('kerbin', 'minmus', 3400, low_orbit='1090-1430', total_delta = '4490-4830'),
            ('kerbin', 'duna'): Orbit('kerbin', 'duna', 3400, low_orbit='1690-1700', total_delta = '5090-5100'),
            ('kerbin', 'ike'): Orbit('kerbin','ike',3400,low_orbit= 4940, total_delta='4940-4950'),
            ('kerbin', 'dres'): Orbit('kerbin', 'dres', 3400, low_orbit= '2850-3860', total_delta = '6250-7260'),
            ('kerbin', 'jool'): Orbit('kerbin', 'jool', 3400, low_orbit=4940, total_delta='4940-4950'),














        }

    def make_orbit(self):
        change_from = input('From: ').lower()
        change_to = input('To: ').lower()

        key = (change_from, change_to)
        if key in self.orbit_data:
            self.orbit_data[key].display_orbit_details()
        else:
            print(f"No data available for orbit from {change_from} to {change_to}.")

    def landing(self):
        change_from = input('Change from: ').lower()
        change_to = input('Change to: ').lower()
        print(f"Landing functionality for {change_from} to {change_to} not yet implemented.")

    def main_menu(self):
            print('1. Make Orbit')
            print('2. Landing')
            print('3. Aerobraking')
            print('4. Return')
            print('5. Exit')

            command = input('Enter Command: ')

            if command == '1':
                self.make_orbit()
            elif command == '2':
                self.landing()
            elif command == '3':
                print("Aerobraking functionality not yet implemented.")
            elif command == '4':
                print("Return functionality not yet implemented.")
            elif command == '5':
                print("Exiting program. Goodbye!")
            else:
                print("Invalid command. Please try again.")


if __name__ == '__main__':
    mission = SpaceMission()
    mission.main_menu()
