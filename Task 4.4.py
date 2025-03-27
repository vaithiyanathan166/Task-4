#convert the UML diagram into a python class and its methods.

class TV:
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.price = price
        self.inches = inches
        self.channel = 1
        self.volume = 50
        self.is_on = False

    def power(self):
        self.is_on = not self.is_on
        state = "ON" if self.is_on else "OFF"
        print(f"The TV is now {state}.")

    def increase_volume(self):
        if self.is_on:
            if self.volume < 100:
                self.volume += 1
                print(f"Volume increased to {self.volume}.")
            else:
                print("Volume is already at maximum.")
        else:
            print("TV is OFF. Please turn it ON to adjust volume.")

    def decrease_volume(self):
        if self.is_on:
            if self.volume > 0:
                self.volume -= 1
                print(f"Volume decreased to {self.volume}.")
            else:
                print("Volume is already at minimum.")
        else:
            print("TV is OFF. Please turn it ON to adjust volume.")

    def set_channel(self, channel):
        if self.is_on:
            if 1 <= channel <= 50:
                self.channel = channel
                print(f"Channel set to {self.channel}.")
            else:
                print("Invalid channel. Please select a channel between 1 and 50.")
        else:
            print("TV is OFF. Please turn it ON to change channels.")

    def reset(self):
        if self.is_on:
            self.channel = 1
            self.volume = 50
            print("TV has been reset to channel 1 and volume 50.")
        else:
            print("TV is OFF. Please turn it ON to reset.")

    def status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"{self.brand} TV is {state}, at channel {self.channel}, volume {self.volume}.")

class LedTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return "Wide viewing angle."

    def backlight(self):
        return "LED backlight."

    def display_details(self):
        print(f"LED TV Details:\n"
              f"Brand: {self.brand}\n"
              f"Price: ${self.price}\n"
              f"Size: {self.inches} inches\n"
              f"Screen Thickness: {self.screen_thickness} mm\n"
              f"Energy Usage: {self.energy_usage} watts\n"
              f"Lifespan: {self.lifespan} hours\n"
              f"Refresh Rate: {self.refresh_rate} Hz\n"
              f"{self.viewing_angle()}\n"
              f"{self.backlight()}")

class PlasmaTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return "Very wide viewing angle."

    def backlight(self):
        return "No backlight needed."

    def display_details(self):
        print(f"Plasma TV Details:\n"
              f"Brand: {self.brand}\n"
              f"Price: ${self.price}\n"
              f"Size: {self.inches} inches\n"
              f"Screen Thickness: {self.screen_thickness} mm\n"
              f"Energy Usage: {self.energy_usage} watts\n"
              f"Lifespan: {self.lifespan} hours\n"
              f"Refresh Rate: {self.refresh_rate} Hz\n"
              f"{self.viewing_angle()}\n"
              f"{self.backlight()}")
