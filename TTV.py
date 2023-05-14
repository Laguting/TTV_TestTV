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
    # Set a new channel
    # Return volume
    # Set a new volume
    # Change Channels
    # Channel increases by 1
    # Channel decreases by 1
    # Change Volume
    # Volume increases by 1
    # Volume decreases by 1
    # Assign TV 1 and TV 2' attributes (channel and volume)
    # Display the results

    # Close the TV

