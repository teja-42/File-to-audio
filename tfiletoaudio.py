from gtts import gTTS
import os

text=open('audiosample.txt','r').read()

language='en'
output=gTTS(text=text,lang=language,slow=False)
output.save("fileoutput.mp3")
os.system("start fileoutput.mp3")