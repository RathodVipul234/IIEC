import pyttsx3
engin = pyttsx3.init()

voices = engin.getProperty('voices')
# here 0is for man voice and 1 for women voice
engin.setProperty('voice',voices[1].id)
# engin.setProperty('rate1',130)

engin.say("How Are You!!")
engin.runAndWait()

#Also we can use speak function for text to speech
#import pyttsx3
#pyttsx.speak("hello")
