# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create two 
# objects from Class TV and will produce the following output:
# tv1's channel is 30 and volume level is 3
# tv2's channel is 3 and volume level is 2

from pyfiglet import Figlet
from termcolor import colored
from tqdm import tqdm 
import time
print()
print("⬜"* 88)
user_name = input("\n\n\33[1m\33[33mInput your name here ✍️  :\33[0m ")
ask_usr = input("\n\33[1m\33[33mHi " + str(user_name) + "\33[1m\33[33m, would you like to turn your TV on 🤔 ? Enter 'Y' if yes and 'N' if no: \33[0m")
if ask_usr.upper() == "Y":
# Loading bar
    print()
    for i in tqdm (range (100), desc="Opening...\U0001F973"):
        time.sleep(0.05)
        pass
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
    
    #Test TV driver
    # Assign TV 1 and TV 2' attributes (channel and volume)
    tv_1 = TV(0,0,0) # TV 1
    tv_1.power_on()
    tv_1.set_channel(30)
    tv_1.set_volume(3)
    tv_2 = TV(0,0,0) # TV 2
    tv_2.power_on()
    tv_2.set_channel(3)
    tv_2.set_volume(2)
    # Display the results
    print("\33[45m\33[1mThe TV 1's channel is", tv_1.get_channel(), "\33[45m\33[1m and volume is ", tv_1.get_volume(), "\33[0m")
    print("\33[45m\33[1mThe TV 1's channel is ", tv_2.get_channel(), "\33[45m\33[1m and volume is ", tv_2.get_volume(), "\33[0m")
    print()
    print("⬜"* 88)
    # Change channel, volume, turn off tv 1, 2, or both
    while True:
        try:
            usr_chc = input("\n\33[1m\33[92m If you don't want to change anything press '0' ; If you want to change Channel for TV 1 press '1' ; If you want to change Channel for TV 2 press '2' ; If you want to change volume for TV 1 press '3' ; If you want to change volume for TV 2 press '4' ; If you want turn TV 1 off press '5' ; If you want turn TV 1 off press '6': \33[0m")
            if usr_chc not in ["0","1","2","3","4","5","6"]:
                raise ValueError
        except ValueError:
            print("\n\33[1m\33[31mInvalid Operation. Try again.\33[0m")
            continue
        if usr_chc == "1":
                new_channel = int(input("\n\33[1m\33[7mEnter new channel: \33[0m"))
                tv_1.set_channel(new_channel)
                print("\n\33[45m\33[1mThe TV 1's channel is", tv_1.get_channel(), "\33[45m\33[1m and volume is ", tv_1.get_volume(), "\33[0m")
        if usr_chc == "2":
                new_channel = int(input("\n\33[1m\33[7mEnter new channel: \33[0m"))
                tv_2.set_channel(new_channel)
                print("\n\33[45m\33[1mThe TV 2's channel is ", tv_2.get_channel(), "\33[45m\33[1m and volume is ", tv_2.get_volume(), "\33[0m")
        if usr_chc == "3":
                new_volume = int(input("\n\33[1m\33[7mEnter new volume level: \33[0m"))
                tv_1.set_volume(new_volume)
                print("\n\33[45m\33[1mThe TV 1's channel is ", tv_1.get_channel(), "\33[45m\33[1m and volume is ", tv_1.get_volume(), "\33[0m")
        if usr_chc == "4":
                new_volume = int(input("\n\33[1m\33[7mEnter new volume level: \33[0m"))
                tv_2.set_channel(new_volume)
                print("\n\33[45m\33[1mThe TV 2's channel is ", tv_2.get_channel(), "\33[45m\33[1m and volume is ", tv_2.get_volume(), "\33[0m")
        if usr_chc == "5":
                tv_1.power_off()
                print("\n\33[45m\33[1mTV 1 is turned off")
        if usr_chc == "6":
                tv_2.power_off()
                print("\n\33[45m\33[1mTV 2 is turned off")
        else:
            usr_chc == "0"
            break
    # Close the TV