import speech_recognition as sr
import webbrowser as wb
import pyjokes as jokes
import wikipedia 
import time
import sys, os

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

searchEngines = {"google" : "https://www.google.com/search?client=firefox-b-d&q=", 
				 "duckduckgo": "https://duckduckgo.com/?t=ffnt&atb=v1-1&ia=web&q=", 
				 "youtube": "https://www.youtube.com/results?search_query=", 
				 "bing" : "https://www.bing.com/search?form=MOZLBR&pc=MOZI&q=",
				 "wikipedia": "https://en.wikipedia.org/wiki/"
				}



# speech to text conversion using google api.
def speechToText():

	command = sr.Recognizer()
	google_recognizer = sr.Recognizer()
	audioCommand = None

	with sr.Microphone() as source:
			
			
		audioCommand = command.listen(source)
		
		# use google api to convert to text.		
		try:
			audioCommandText = google_recognizer.recognize_google(audioCommand)
			
			return audioCommandText
		except:
			return None



# open the browser
def openBrowser(url , query, name):

	wb.get().open_new(url + query)

	print("Searching for " + query + " on " + name )
	print("=================================================================================================\n\n")
	speak.Speak("Searching for " + query + " on " + name )

	time.sleep(3)




# get the query for the choose engine.
def getQuery(name, url):

	is_valid = False # determines whether the audio is in google's repository or not.
	
	while is_valid == False:
		print("What would you like to search on " + name + "\n")
		speak.Speak("What would you like to search on " + name)
		
		# convert to text
		audioQueryText = speechToText()

		if audioQueryText is not None:
			
			#openBrowser(url, audioQueryText, name)

			return {"url":url, "query": audioQueryText, "name":name}

		else:
			print("\nPlease say something.\nNo query provided.")
			print("=========================================================================================\n\n")
			speak.Speak("Please say something.")



# execute the given command.
def ExecuteCommand(audioCommandText):
	
	queryDict = None
	# search google.
	if  "search google" in audioCommandText.lower():
		queryDict = getQuery("GOOGLE", searchEngines['google'])
		openBrowser(queryDict['url'], queryDict['query'], queryDict['name'])
		

	# seach duckduckgo
	elif "search go" in audioCommandText.lower():

		queryDict = getQuery("Duckduckgo", searchEngines["duckduckgo"])
		openBrowser(queryDict['url'], queryDict['query'], queryDict['name'])

	# search youtube
	elif "search youtube" in audioCommandText.lower():
		queryDict = getQuery("Youtube", searchEngines["youtube"])
		openBrowser(queryDict['url'], queryDict['query'], queryDict['name'])

	# seach bing
	elif "search bing" in audioCommandText.lower():
		queryDict = getQuery("Bing", searchEngines["bing"])
		openBrowser(queryDict['url'], queryDict['query'], queryDict['name'])

	# search wikipedia
	elif "search wiki" in audioCommandText.lower():

		queryDict = getQuery("Wikipedia", searchEngines["wikipedia"])
		openBrowser(queryDict['url'], queryDict['query'], queryDict['name'])

	# make a joke: using pyjokes
	elif "make a joke" in audioCommandText.lower():

		joke = jokes.get_joke()
		print("\nJOKE:\n"+ joke )
		print("\n===============================================================================================\n\n")
		speak.Speak(joke)

	# ask wikipedia a question.
	elif "what is " in audioCommandText.lower():
		audioCommandText = audioCommandText.replace("what is ", " ")
		summary = wikipedia.summary(audioCommandText)
		
		# printing the summary 
		print("\n")
		print(summary)
		speak.Speak(summary)

		print("\n\n==============================================================================================\n\n")


	# return false only if the person want to exit program.
	elif "exit" in audioCommandText.lower():

		speak.Speak("\nExiting program.")
		sys.exit("\nExiting program.")

	else:

		print("\nInvalid choice. Please try again")
		print("==============================================================================================\n\n")
		speak.Speak("Invalid choice. Please  try again.")


def main():

	print("\nAvailable commands: \n1) Search GOOGLE, BING, WIKI (Wikipedia), GO (Duckduckgo) or search Youtube \n2) Make a joke \n3) What is ..... \n4) Exit")
	speak.Speak("Available commands:. 1) Search GOOGLE, BING, WIKI (Wikipedia), GO (Duckduckgo) or search Youtube . 2)Make a joke  . 3) What is ..... . 4) Exit")
	speak.Speak("You may Speak!!")

	while True:
		
		is_valid = False # determines whether the audio is in google's repository or not.
		
		print("\nListening ..........................")
		commandText = speechToText()


		# only execute if the command / words are in google api's repository.
		if commandText is not None:
			speak.Speak(commandText)
			ExecuteCommand(commandText)
			
		else:
			print("\nPlease say something.")
			print("============================================================================================\n")
			
		time.sleep(5)
		os.system('cls')
		print("\nAvailable commands: \n1) Search GOOGLE, BING, WIKI (Wikipedia), GO (Duckduckgo) or search Youtube \n2) Make a joke \n3) What is ..... \n4) Exit")


if __name__ == '__main__':
	main()