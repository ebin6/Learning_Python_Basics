from gtts import gTTS
import os
import gtts
s=input("Enter your text : ")
c=gTTS(text=s,lang='en',slow=False)

c.save("test_audio.mp3")

os.system("start test_audio.mp3")

print(dir(gtts))