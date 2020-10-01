import pyttsx3
import os
print("Rv Assistance ")
pyttsx3.speak("Welcome To Rv Assistance ")
pyttsx3.speak("How Can I Help You!")

# Only Open Some App Which I declare I'm here
#if bellow app will not open in your machine then just add path of your app in Environment Variable

while True:
    x = input("User Input:")
    # for chrome browser
    if (("run" in x) or ("execute" in x) or ("launch" in x) or ("open" in x)) and (("chrome" in x) or ("browser" in x) or ("google" in x)):
        pyttsx3.speak("Opening Browser please Wait..")
        os.system("Chrome")

    #open window media player
    elif (("run" in x) or ("execute" in x) or ("launch" in x) or ("open" in x)) and (("wmplayer" in x) or ("window media player" in x) or ("music app" in x)):
        pyttsx3.speak("Opening windows media player please Wait..")
        os.system("wmplayer")

    #opening notepade
    elif (("run" in x) or ("execute" in x) or ("launch" in x) or ("open" in x)) and (("notepad" in x) or ("text editor" in x):
        pyttsx3.speak("Opening Notepad please Wait..")
        os.system("notepad")


    #paint
    elif (("run" in x) or ("execute" in x) or ("launch" in x) or ("open" in x)) and (("paint" in x) or ("drawing app" in x)):
        pyttsx3.speak("Opening Paint please Wait..")
        os.system("mspaint")

    #power point presentation
    elif (("run" in x) or ("execute" in x) or ("launch" in x) or ("open" in x)) and (("ppt" in x) or ("power point" in x) or ("power point presentation" in x)):
        pyttsx3.speak("Opening power point presentation please Wait..")
        os.system("powerpnt")

    # exit from rv assistance
    elif ("close" in x) or ("exit" in x) or("stop" in x):
        pyttsx3.speak("Rv Assistance closed.. I really Feeling Good To Help You..Thank You")
        quit()


    else:
        pyttsx3.speak("I don't understand what u say..I'm still learning ")
