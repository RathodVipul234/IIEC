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
    if (("start" in x) or ("execute" in x) or ("launch" in x) or ("open" in x)) and (("chrome" in x) or ("browser" in x) or ("google" in x)):
        print("Rv Assistance : ", end = '')
        pyttsx3.speak("Opening Browser please Wait..")
        os.system("Chrome")

    #open window media player
    elif (("start" in x) or ("execute" in x) or ("launch" in x) or ("open" in x)) and (("wmplayer" in x) or ("window media player" in x) or ("music app" in x)):
        print("Rv Assistance : ", end = '')
        pyttsx3.speak("Opening window media player please Wait..")
        os.system("wmplayer")

    #opening notepade
    elif (("start" in x) or ("execute" in x) or ("launch" in x) or ("open" in x)) and (("notepade" in x)):
        print("Rv Assistance : ")
        pyttsx3.speak("Opening Notepade please Wait..")
        os.system("notepade")


    #paint
    elif (("start" in x) or ("execute" in x) or ("launch" in x) or ("open" in x)) and (("paint" in x) or ("drawing app" in x)):
        print("Rv Assistance : ")
        pyttsx3.speak("Opening Paint please Wait..")
        os.system("paint")

    #power point presentation
    elif (("start" in x) or ("execute" in x) or ("launch" in x) or ("open" in x)) and (("ppt" in x) or ("power point" in x) or ("ms office" in x) or ("power point presentation" in x)):
        print("Rv Assistance : ")
        pyttsx3.speak("Opening power point presentation please Wait..")
        os.system("powerpnt")

    # exit from rv assistance
    elif ("close" in x) or ("exit" in x) or("stop" in x):
        print("Rv Assistance : ")
        pyttsx3.speak("Rv Assistance closed.. I really Felling Good To Help You..Thank You")
        quit()


    else:
        pyttsx3.speak("i don't understand what u say..am still learning ")