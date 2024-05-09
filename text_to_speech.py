from gtts import gTTS
import os
hj=open("poem.txt","r")
myText=hj.read().replace("\n"," ")
language='en'
output=gTTS(text=myText,lang=language,slow=False)
output.save("output.mp3")
os.system("start output.mp3")