import pyttsx3
engine=pyttsx3.init()
engine.setProperty("rate",125)
engine.setProperty("volume",0.8)
engine.save_to_file("hii guys love u all","test.mp3")
engine.runAndWait()