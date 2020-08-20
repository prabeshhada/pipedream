import os
import pyttsx3

pyttsx3.speak("Welcome to my tools")


print("notepad")
print("chrome")
print("windows player")


while True:
	print("Chat with me with your choice: " , end="")
	x=input()



	if ("run" in x) and (("notepad" in x) or ("editor" in x)):

		os.system("notepad")
	elif "run" in x and "chrome" in x:
		os.system("chrome")
	elif "run" in x and "mediaplayer" in x:
		os.system("mediaplayer")
	elif "exit" in x or "quit" in x:
		break
	else:

		print("dont support")


	
