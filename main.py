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

class SpaceMission:
    def __init__(self):
        self.orbit_data = {
            ('kerbin', 'moho'): Orbit('kerbin', 'moho', 3400, low_orbit=4120),
            ('kerbin', 'eve'): Orbit('kerbin', 'eve', 3400, low_orbit=2450),
            ('kerbin', 'gilly'): Orbit('kerbin', 'gilly', 3400, low_orbit=1800),
            ('kerbin', 'kerbin'): Orbit('kerbin', 'kerbin', 3400),
            ('kerbin', 'mun'): Orbit('kerbin', 'mun', 3400, low_orbit=1170),
            ('kerbin', 'minmus'): Orbit('kerbin', 'minmus', 3400, low_orbit=1090),
            ('kerbin', 'duna'): Orbit('kerbin', 'duna', 3400, low_orbit=1690),
            ('kerbin', 'ike'): Orbit('kerbin','ike',3400,low_orbit = 1540),
            ('kerbin', 'dres'): Orbit('kerbin', 'dres', 3400, low_orbit = 2850),
            ('kerbin', 'jool'): Orbit('kerbin', 'jool', 3400, low_orbit= 4900),
            ('kerbin', 'laythe'): Orbit('kerbin', 'laythe', 3400, low_orbit=7490),
            ('kerbin', 'vall'): Orbit('kerbin', 'vall', 3400, low_orbit=7020),
            ('kerbin', 'tylo'): Orbit('kerbin', 'tylo', 3400, low_orbit=6990),
            ('kerbin', 'bop'): Orbit('kerbin', 'bop', 3400, low_orbit=6610),
            ('kerbin', 'pol'): Orbit('kerbin', 'pol', 3400, low_orbit=3040),
            ('kerbin', 'eeloo'): Orbit('kerbin', 'eeloo', 3400, low_orbit=3460),
            ('kerbin', 'kerbol'): Orbit('kerbin', 'kerbol', 3400, low_orbit=20650),


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
