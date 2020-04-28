import keyboard
import time
import speech_recognition as sr
import pyaudio

writeString = ""

writeString = input("Please input text to be written: ")

if writeString.__eq__("54321"):
    print("Congratulations! You have found the hidden speech to text mode!")
    r = sr.Recognizer()
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            text = r.recognize_google(audio)  # use recognizer to convert our audio into text part.
            print("You said : {}".format(text))
            writeString = text
        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly

if writeString != "":
    print("Thank you for your input. Parsing input now...")
    writeString = writeString.replace("\n", "")
    print("New lines removed and ready to split...")
    spaceSplit = writeString.split()
    print("Please select text box in the next 10 seconds. Ready to write!")
    for i in range(0, 10):
        print(str(i))
        time.sleep(1)
    for word in spaceSplit:
        keyboard.write(word + "\n")






