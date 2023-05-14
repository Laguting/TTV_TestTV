# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create two 
# objects from Class TV and will produce the following output:
# tv1's channel is 30 and volume level is 3
# tv2's channel is 3 and volume level is 2

print()
print("⬜"* 88)
user_name = input("\n\n\33[1m\33[33mInput your name here ✍️  :\33[0m ")
ask_usr = input("\n\33[1m\33[33mHi " + str(user_name) + "\33[1m\33[33m, would you like to turn your TV on 🤔 ? Enter 'Y' if yes and 'N' if no: \33[0m")
if ask_usr.upper() == "Y":
# Loading bar
    print()
    from tqdm import tqdm 
    import time
    for i in tqdm (range (100), desc="Opening...\U0001F973"):
        time.sleep(0.05)
        pass
# Intro to the brand of the TV
    from pyfiglet import Figlet
    from termcolor import colored
    intro_brand = Figlet( font = "doh", justify = "right")
    print()
    print("⬜"* 88)
    print(colored(intro_brand.renderText("AETH3R"), "cyan"))
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
        def channels_up(self):# Channel decreases by 1
            if self.power_on and self.channel > 1:
                self.channel - 1
    # Change Volume
    # Volume increases by 1
    # Volume decreases by 1
    
    #Test TV driver
    # Assign TV 1 and TV 2' attributes (channel and volume)
    tv_1 = TV(30,0,True)
    tv_1.set_volume(3)
    # Display the results
    print("The TV 1's channel is ", tv_1.get_channel(), " and volume is ", tv_1.get_volume())
    # Close the TV

