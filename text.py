from gtts import gTTS
import os
myText="hariss and aviss are good frends and aviss is fighter ,singer,dancer,critical thinker.she have 3 good frend"
language='en'
output=gTTS(text=myText,lang=language,slow=False)
output.save("output.mp3")
os.system("start output.mp3")