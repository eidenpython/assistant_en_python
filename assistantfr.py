import pywhatkit
import speech_recognition as sr
import pyttsx3 as ttx
import datetime
import random
import wakeonlan
import webbrowser
from tkinter import *


def assitant():

    listener=sr.Recognizer()
    engine=ttx.init()
    voice=engine.getProperty('voices')
    engine.setProperty('voice', 'french')
    engine.setProperty("rate", 175)
    new_vol = 1
    engine.setProperty("volume", new_vol)

    def parler(text):
        engine.say(text)
        engine.runAndWait()


    def salutation():
        listalea = ["boujour comment allez vous?", "Bonjour comment puis je vous aider", "boujour ca va bien."]
        listindex = random.randrange(len(listalea))
        parler(listalea[listindex])

    def arret():

        listefin = ["ok j'arrêtte le système", "fin du programme", "Arrêt du système"]
        listindexi = random.randrange(len(listefin))
        parler(listefin[listindexi])


    def tv():
        listalea1 = ["J'allume la tv", "j'allume la tv pour vous.", "j'allume la tv", "la tv est allumé"]
        listindex1 = random.randrange(len(listalea1))
        parler(listalea1[listindex1])

        wakeonlan.send_magic_packet('44:ef:bf:de:fd:9b')

    def pok():
        listalea2 = ["tu veux quoi", "oui, quoi encore", "quoi", "oui quoi encore", "tu te fou de moi", "ferme la un peu"]
        listindex2 = random.randrange(len(listalea2))
        parler(listalea2[listindex2])

    def quantique():
        uri = "https://www.google.com/search?q=ordinateur+quantique&biw=1166&bih=617&tbm=nws&sxsrf=APq-WBsnWavHUN_9CLWIGXwVszz6QQA2ug%3A1643740145265&ei=8Xv5YevaD_LjsAeWk7y4Ag&oq=ordinate&gs_lcp=Cgxnd3Mtd2l6LW5ld3MQARgCMggIABCABBCxAzIICAAQgAQQsQMyCwgAEIAEELEDEIMBMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoECAAQQzoICAAQsQMQgwE6BQgAELEDUP-yAVjHvAFggdABaANwAHgAgAGSAYgBjgeSAQM2LjOYAQCgAQGwAQDAAQE&sclient=gws-wiz-news"
        webbrowser.open(uri)
        parler("je cherches sur le quantique")




    def ecouter():

        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Je vous ecoute..")
                audio = r.listen(source, timeout=1, phrase_time_limit=5)

            try:
                print("Reconnaisance...")
                Query = r.recognize_google(audio, language="fr-FR")
                print(f"Vous avez dit: {Query}")

            except Exception as e:

                return ""
            return Query

    def lancer_assistant():

        while True:
            #test

                command=ecouter()
                print(command)

                if 'mets la chanson de ' in command:
                    chanteur=command.replace("mets la chanson de", "")
                    pywhatkit.playonyt(chanteur)

                elif 'heure' in command:
                    heure=datetime.datetime.now().strftime('%H:%M')
                    parler('il est'+heure)
                elif 'Bonjour' in command:
                    salutation()

                elif 'arret'in command or 'arrêt' in command or "arrêtte "in command:

                    arret()
                    break

                elif "allume la tv" in command or "allume tv" in command or 'allume tele' in command or 'allume la télé' in command :
                    tv()

                elif "mil" in command or "émil" in command or "Emile" in command:
                    pok()


                elif "recherche Quantique " in command or "recherche quantique" in command:
                   quantique()

                else:
                    print('je ne comprends pas')

    def papi():
            exit()



    while True:

        lancer_assistant()


mainframe = Tk()
buttonimage = PhotoImage(file="humanbrain.ppm")
imagelabel = Label(image=buttonimage)

nwbutt = Button(mainframe, image=buttonimage, borderwidth=0, bg='#f2f2f2',fg="#f2f2f2", command=assitant)
nwbutt.place(x=210, y=100)

mainframe.configure(bg='#f2f2f2')
mainframe.geometry("1000x600")
mainframe.mainloop()