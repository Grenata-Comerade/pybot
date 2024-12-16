import speech_recognition as srec
import pyttsx3 as pyt
import pywhatkit
import wikipedia
import subprocess
from gtts import gTTS
from time import sleep
import os
import openai
openai.api_key = '' # Your Token!

engine = pyt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def salam():
    salamKamerad = 'lib/salam.mp3'
    os.system(f'start {salamKamerad}')
    print('Kamerad! Saya adalah grenata.ai yang hadir dalam revolusi industri 5.0, katakan dan saya nyatakan.')
    sleep(3)

def perintah():
  mendengar = srec.Recognizer() # mengambil atribut objek 'srec'
  with srec.Microphone() as source: # memasukan suara sebagai perintah
    print('Mendengar...')
    mendengar.pause_threslod = 0.9
    suara = mendengar.listen(source, phrase_time_limit=5)
    try: 
      print('Wait Tuanku...')
      Layanan = mendengar.recognize_google(suara, language='id-ID')
      print(Layanan)
    except:
      pass 
    return Layanan

def bicara(self):
    teks = (self)
    bahasa = 'id'
    namafile = bicara.mp3
    def reading():
        suara = gTTS
        suara.save(namafile)
        os.system(f'start {namafile}')
    reading


def talk(audio):
      engine.say(audio)
      engine.runAndWait

def grenata_ai():
      Layanan = perintah()
      print(Layanan)
      bicara(Layanan)
      if 'open' in Layanan:
          video = Layanan.replace('open', '')
          pyt.speak('opening' + video)
          print(video + 'opening...')
          pywhatkit.playonty(video)
      if 'find out' in Layanan:
          wiki = Layanan.replace('find out', '')
          hasil = wikipedia.summary(wiki, sentences = 4)
          print(hasil)
          pyt.speak(hasil)
      if 'belajar' in Layanan:
          subprocess.call(['r'])
          Layanan = perintah()
      if 'keluar' in Layanan:
          keluar = 'lib/keluar.mp3'
          os.system(f'start {keluar}')
          print('hari yang menyenangkan kamerad, terimkasih...')
          sleep(4)
          exit()

      elif 'selesai' in Layanan:
          selesai = 'lib/keluar.mp3'
          os.system(f'start {selesai}')
          pyt.speak('hari yang menyenangkan kamerad, terimkasih...')
          sleep(4)
          exit()

      else:
          responegpt = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = Layanan,
            max_tokens=200
          )

          answergpt = responegpt.choices[0].text.strip()
          print(answergpt)
          print(Layanan)



while True:
    salam()
    grenata_ai()


