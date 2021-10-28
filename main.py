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
  try:
    ps.playsound(filename)
  except:
     print('Maaf lagi sariawan, gabisa ngomong dulu')
     print(text)


pesanan = {
  'pemesan': "",
  'makanan': ""
}

def tampil_menu():
  print("1. Bakso Bakar ")
  print("2. Ayam Geprek sedap")
  print("3. Pepes Ikan Kerapu")
  text = "Mau Pesan apa?. Kami sedia Bakso Bakar, Ayam Geprek Sedap dan Pepes Ikan Kerapu"
  bilang(text)
  makanan = dengerin()
  if makanan == "Bakso Bakar":
    pesanan['makanan'] 
    bilang("Oke, pesan bakso bakar yaa")
  tanya_nama("Atas Nama siapa?")
  bilang(f"Oke {pesanan['nama'],} dengan pesanan {pesanan['makanan']} yaa. Mohon ditunggu yaa")

def tanya_nama(text):
  tts = gTTS(text=text, lang="id")
  filename = "tanya_nama.mp3"
  print(text)
  tts.save(filename)
  try:
    ps.playsound(filename)
  except:
     print('Maaf lagi sariawan, gabisa ngomong dulu')

  nama = dengerin()
  pesanan['pemesan'] = nama


# def pesan_makanan():
#   tampil_menu()
#   makanan = dengerin()
#   if makanan == "Bakso Bakar":
#     print("Bakso Bakar")

  




while True:
  try:
    text = dengerin()
    if text in recognize_exit:
      text = 'Makasih udah pake Voice Recognition Bahasa Indonesia!, Sampai Jumpa!'
      print(text)
      bilang(text)
      break
    else:
      tampil_menu()
  except:
    recognizer = speech_recognition.Recognizer()
    continue