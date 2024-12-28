import tkinter as tk
from tkinter import ttk, messagebox

class Orbit:
    def __init__(self, change_from, change_to, take_off_delta, low_orbit=None):
        self.change_from = change_from
        self.change_to = change_to
        self.take_off_delta = take_off_delta
        self.low_orbit = low_orbit

    def display_orbit_details(self):
        total_delta = self.take_off_delta + self.low_orbit if self.low_orbit else self.take_off_delta
        details = (
            f"TakeOff from {self.change_from}: {self.take_off_delta} m/s\n"
            f"Transit from {self.change_from} low orbit to {self.change_to} low orbit: {self.low_orbit} m/s\n"
            f"Transit from {self.change_from} to {self.change_to} total: {total_delta} m/s"
        )
        return details


class SpaceMissionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Mission Control")
        self.root.geometry("500x400")
        self.root.configure(bg="#2E4053")  # Темный фон

        self.orbit_data = {
            ('kerbin', 'moho'): Orbit('kerbin', 'moho', 3400, low_orbit=4120),
            ('kerbin', 'eve'): Orbit('kerbin', 'eve', 3400, low_orbit=2450),
            ('kerbin', 'gilly'): Orbit('kerbin', 'gilly', 3400, low_orbit=1800),
            ('kerbin', 'kerbin'): Orbit('kerbin', 'kerbin', 3400),
            ('kerbin', 'mun'): Orbit('kerbin', 'mun', 3400, low_orbit=1170),
            ('kerbin', 'minmus'): Orbit('kerbin', 'minmus', 3400, low_orbit=1090),
            ('kerbin', 'duna'): Orbit('kerbin', 'duna', 3400, low_orbit=1690),
            ('kerbin', 'ike'): Orbit('kerbin', 'ike', 3400, low_orbit=1540),
            ('kerbin', 'dres'): Orbit('kerbin', 'dres', 3400, low_orbit=2850),
            ('kerbin', 'jool'): Orbit('kerbin', 'jool', 3400, low_orbit=4900),
            ('kerbin', 'laythe'): Orbit('kerbin', 'laythe', 3400, low_orbit=7490),
            ('kerbin', 'vall'): Orbit('kerbin', 'vall', 3400, low_orbit=7020),
            ('kerbin', 'tylo'): Orbit('kerbin', 'tylo', 3400, low_orbit=6990),
            ('kerbin', 'bop'): Orbit('kerbin', 'bop', 3400, low_orbit=6610),
            ('kerbin', 'pol'): Orbit('kerbin', 'pol', 3400, low_orbit=3040),
            ('kerbin', 'eeloo'): Orbit('kerbin', 'eeloo', 3400, low_orbit=3460),
            ('kerbin', 'kerbol'): Orbit('kerbin', 'kerbol', 3400, low_orbit=20650),
        }

        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        title_label = tk.Label(self.root, text="Space Mission Control", font=("Helvetica", 20, "bold"), fg="#F1C40F", bg="#2E4053")
        title_label.pack(pady=20)

        # Рамка для выбора "From" и "To"
        frame = tk.Frame(self.root, bg="#34495E", bd=5, relief=tk.RIDGE)
        frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Поле "From"
        tk.Label(frame, text="From:", font=("Arial", 14), fg="white", bg="#34495E").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.from_combobox = ttk.Combobox(frame, values=list({key[0] for key in self.orbit_data.keys()}), state="readonly", font=("Arial", 12))
        self.from_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Поле "To"
        tk.Label(frame, text="To:", font=("Arial", 14), fg="white", bg="#34495E").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.to_combobox = ttk.Combobox(frame, values=list({key[1] for key in self.orbit_data.keys()}), state="readonly", font=("Arial", 12))
        self.to_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Кнопка для расчета орбиты
        orbit_button = tk.Button(self.root, text="Make Orbit", font=("Arial", 14), bg="#27AE60", fg="white", command=self.make_orbit)
        orbit_button.pack(pady=20)

    def make_orbit(self):
        change_from = self.from_combobox.get().lower()
        change_to = self.to_combobox.get().lower()

        key = (change_from, change_to)
        if key in self.orbit_data:
            details = self.orbit_data[key].display_orbit_details()
            messagebox.showinfo("Orbit Details", details)
        else:
            messagebox.showerror("Error", f"No data available for orbit from {change_from} to {change_to}.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SpaceMissionApp(root)
    root.mainloop()
