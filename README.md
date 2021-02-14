# Speech Recogizer

** [Website](https://equitek.herokuapp.com) **

The aim of this project was to create a voice assistance that up recieving a voice command can execute a task.

# Features:
1. Search major search engines and websites: Google, Bing, Duckduckgo, Wikipedia and Youtube.

2. Make a Joke: Uses pyjokes to prints and recite a programming joke.

3. What if ...: Uses wikipedia to get a summary of a what is question and also recites the summary to the user.

4. Exits the program.


## The search feature:
This works on a two step process of asking 1) the website or search engine 2) the query or question. Then a webbrowser window will be opened with the engine / website output.

### Compatible website(s) and search engine(s):
* Youtube
* Google
* Duckduckgo
* Bing
* Wikipedia

### command
- Search <Search engine / Website>
	e.g. search youtube

## Make a joke feature:
Making a joke is as simple as saying **"Make a joke"**.

## What is .... feature:
Simply say **"What is <Query / Question>"** and the summary will be printed on the terminal and recited to you by the builtin Windows 10 Text to Speech system.

# Supported platform(s):
Windows 10

# Dependencies:

```
pip install -r requirements.txt
```
```
pip install PyAudio
```

## Install PyAudio
You may stuggle to install this package on python 3.+. So I suggest you use this article to install it.

[Install PyAudio on Python 3.0](https://thetechinfinite.com/2020/07/14/how-to-install-pyaudio-module-in-python-3-0-in-windows/)


# Fork this project.
You may fork this project this project if you want to use it and add other features.