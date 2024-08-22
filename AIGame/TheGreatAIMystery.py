from Scenes import *

Intro = """ \n\n\nThe soft rain patters against the window of the cafe, the lights softly glowing in the fog.  
'What a strange night.' You think to yourself.  This town seemed so quiet, that was why you chose it as your home, after all. 
Yet the murder of Alfred McDonald yesterday had thrown the town into shambles. 
Now, as the only detective and investigator in the city, it is up to you to uncover the mystery, and 
bring justice back to this small town you call home"""

print(Intro)
input("Press enter to continue")

Intro2 = """ \nThere are 4 main suspects in the case.  Bill Smith, an introverted, frail, grumpy old carpenter who lived down the street from where the murder took place.
John Butcher, an honest young farmer with a solid build who moved in from Kansas just a year ago, but was known to have disputes with Alfred McDonald
Sarah McDonald, The widow of the murdered suspect.  A quiet, introverted chemist, she has seemed mysterious even to 
McDonald himself at times
and Rebecca Stanford, a mysterious wild card whose career was unknown.  She was bold and outgoing, yet a mysterious figure all the same\n"""

loopOptions = True
print(Intro2)
input("Press enter to continue")

Options="""
Type one of the following options:
Visit the crime scene: "Crime"
Visit Smith: "Smith"
Visit Butcher: "Butcher"
Visit McDonald: "McDonald"
Visit Stanford: "Stanford"
Solve the mystery: "Solve" 
Read suspect descriptions again: "Suspects" 
Hear Intro again: "Intro" 
"""
print(Options)

while (loopOptions):
    playerResponse = input("Please choose an option. Type Help to hear suspects and choices again.\n")
    if (playerResponse == "Crime"):
        crime_scene()
    elif (playerResponse == "Smith"):
        Smith("Test")
    elif (playerResponse == "Butcher"):
        Butcher("Test")     
    elif (playerResponse == "McDonald"):
        McDonald("Test")
    elif (playerResponse == "Stanford"):
        Stanford("Test")
    elif (playerResponse == "Solve"):
        Solve()
    elif (playerResponse == "Intro"):
        print(Intro)
    elif (playerResponse == "Suspects"):
        print(Intro2)
    elif (playerResponse == "Help"):
        print(Options)
    else:
        print ("Please enter a valid option!")