from pyfiglet import Figlet
from termcolor import colored
# Intro to the brand of the TV
intro_brand = Figlet( font = "doh", justify = "right")
print()
print("⬜"* 88)
print(colored(intro_brand.renderText("   AETH3R"), "cyan"))
# Create class for TV
class TV():
# Channel, Volume, and Power is the parameters- default of the TV
    def __init__(self, channel, volume, power):
        self.channel = channel
        self.volume = volume
        self.power = power
    # Set up the power and use boolean where: off = false and on = true
    # Power on
    def power_on(self):
        self.power = True
    # Power off
    def power_off(self):
        self.power = False
    # Return the channel
    def get_channel(self):
        return self.channel
    # Set a new channel
    def set_channel(self, new_channel):
        if self.power_on and 1 <= new_channel <= 120:
            self.channel = new_channel
    # Return volume
    def get_volume(self):
        return self.volume
    # Set a new volume
    def set_volume(self, new_volume):
        if self.power_on and 1 <= new_volume <= 7:
            self.volume = new_volume
    # Change Channels
    def channels_up(self):# Channel increases by 1
        if self.power_on and self.channel < 120:
            self.channel + 1
    def channels_down(self):# Channel decreases by 1
        if self.power_on and self.channel > 1:
            self.channel - 1
    # Change Volume
    def volume_up(self):# Volume increases by 1
        if self.power_on and self.volume < 7:
            self.volume + 1
    def volume_down(self):# Volume decreases by 1
        if self.power_on and self.volume > 1:
            self.volume - 1