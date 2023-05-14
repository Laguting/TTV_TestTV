# Laguting, Maricon Jane G.
# BSCpE 1-4
# Task: Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that will create two 
# objects from Class TV and will produce the following output:
# tv1's channel is 30 and volume level is 3
# tv2's channel is 3 and volume level is 2

# Turn om the  TV
print("⬜"* 88)
user_name = input("\n\n\33[1m\33[33mInput your name here ✍️  :\33[0m ")
ask_usr = input("\n\33[1m\33[33mHi " + str(user_name) + "\33[1m\33[33m, would you like to turn your TV on 🤔 ? Enter 'Y' if yes and 'N' if no: \33[0m")
print(ask_usr.upper)
if ask_usr.upper == "Y":
# Intro to the brand of the TV
    from pyfiglet import Figlet
    from termcolor import colored
    intro_brand = Figlet( font = "doh", justify = "right")
    print()
    print("⬜"* 88)
    print(colored(intro_brand.renderText("AETHER"), "cyan"))
    # Create class for TV
    # Channel, Volume, and Power is the parameters- default of the TV
    # Set up the power and use boolean where: off = false and on = true
    # Power on
    # Power off
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
else: 
    quit
