"""
virtualenv -p python3 env
source env/bin/activate
pip install SpeechRecognition
brew install portaudio
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
https://realpython.com/python-speech-recognition/
"""

import speech_recognition as sr
sr.__version__
r = sr.Recognizer()
print (sr.Microphone.list_microphone_names())
## device index of the microphone is the index of its name in the list returned by list_microphone_names()
with sr.Microphone(device_index=0) as source:
	print ("say something");
	r.adjust_for_ambient_noise(source)
	audio = r.listen(source)
	print("time over thanks")
	try:
	   print("TEXT: "+r.recognize_google(audio));    
	except:
	   pass;

