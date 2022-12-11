from googletrans import Translator
import all_language
import os

language = all_language.LANGUAGES
translator = Translator()

def titles():
    os.system('clear')
    print("{:-^30}".format("-"))
    print("{:^30}".format("Translator Cui"))
    print("{:-^30}".format("-"))


def all_symbol():
    for key, value in language.items():
        print(key, ':', value)


def pair_language():
    print("Contoh : ")
    print("en : English, de : Germany, \nid : Indonesia")
    print('\a')
    texts = input("Ketik untuk menterjemahkan : ")
    destination = (input("Pilih Bahasa : ")).lower()

    try:
        translate = translator.translate(texts, dest=destination)
        print("\a")
        print("Bahasa yang di terjemahkan : ", translate.text)
    except:
        print("Pilihan bahasa tidak ada, Jangan cemazzz")
        print("Silahkan pilih kembali ngab!")


def menu():
    while True:
        print('\a')
        print("{:-^30}".format("-"))
        print("Pilih :")
        print("1. Menterjemahkan bahasa")
        print("2. Bahasa yang ada")
        print("3. Keluar")
        print("{:-^30}".format("-"))
        print("\a")
        choose = input("Pilihan anda: ")

        if choose == "1":
            titles()
            pair_language()
        elif choose == "2":
            titles()
            all_symbol()
        elif choose == "3":
            print("Terima Kasih!")
            exit()
        else:
            print("Pilihan tidak ada")


titles()
menu()
