import threading
import time
from playsound import playsound

#data
counter = 0
timings = {
    "stackTiming":5,
}

#audio

#create functions
def counting():
    global counter
    threading.Timer(1.0, counting).start()
    counter+=1
    print(counter)


def playAudio():
    global counter
    threading.Timer(0.5, playAudio).start()
    if counter % timings["stackTiming"] == 0:
        playsound("./assets/Glass.mp3")
    
        
        


#create threads
countingThread = threading.Thread(target=counting())
soundThread = threading.Thread(target=playAudio())


#run threads
soundThread.start()
countingThread.start()


