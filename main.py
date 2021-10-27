import speech_recognition
import playsound as ps
from gtts import gTTS

recognizer = speech_recognition.Recognizer()
recognize_exit = ['stop', 'udahan', 'berhenti']

def dengerin():
  with speech_recognition.Microphone() as mic:
    recognizer.adjust_for_ambient_noise(mic, 0.2)
    audio = recognizer.listen(mic)
    text = recognizer.recognize_google(audio, language="id")
    print(text.lower())
  return text.lower()

def bilang(text):
  tts = gTTS(text=text, lang="id")
  filename = "rekaman.mp3"
  tts.save(filename)
  ps.playsound(filename)


while True:
  try:
    text = dengerin()
    bilang(text)
    if text in recognize_exit:
      text = 'Makasih udah pake Voice Recognition Bahasa Indonesia!, Sampai Jumpa!'
      print(text)
      bilang(text)
      break
  except:
    recognizer = speech_recognition.Recognizer()
    continue