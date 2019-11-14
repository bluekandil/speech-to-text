import speech_recognition as sr
import pyaudio
from pydub import AudioSegment
from os import path
import sys
import os

r=sr.Recognizer()

#---convert  mp3 to wav
# sound = AudioSegment.from_mp3("demo.mp3")
# sound.export("demo.wav", format="wav")

# r= sr.Recognizer()
audiofilename='female.wav'

convertedTextFile=os.path.splitext(audiofilename)[0]


currentAudioClip = sr.AudioFile("audiosource/"+audiofilename)
with currentAudioClip as source:
    audio = r.record(source)
# output to textfile
def saveToFile(text):
    sys.stdout=open("transcribes/"+convertedTextFile,"w")
    print (text)
    sys.stdout.close()
 

r.recognize_google(audio)
print(r.recognize_google(audio))
saveToFile(r.recognize_google(audio))


# mysource=sr.Microphone();
# print(mysource)


# # p = pyaudio.PyAudio()
# # info = p.get_host_api_info_by_index(0)
# # numdevices = info.get('deviceCount')
# # for i in range(0, numdevices):
# #     if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
# #         print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))


# with sr.Microphone() as source:
#     print("SAY SOMETHING");
#     audio = r.listen(source)
#     print("time over,Thanks")

# try:
#     print("Text"+r.recognize_google(audio));
# except:
#     pass;
