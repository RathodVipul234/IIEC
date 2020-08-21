import os
print("#######My Pc Applications#######")
print("1.Notepade \n2.Paint \n3.PowerPoint \n4.Chrome \n5.Sublime Text3 ")
UserInput =int(input("Choose anyone To Open Right now :"))

if UserInput == 1:
    os.system("notepad")
elif UserInput == 2:
    os.system('mspaint')
elif UserInput == 3:
    os.system("POWERPNT")
elif UserInput == 4:
    os.system("chrome")
elif UserInput == 5:
    os.system("sublime_text")
else:
    print("Invalid Input!")
