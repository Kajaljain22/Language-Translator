# Python app to translate any text into 100+ Languages
#google trans is a google API for translating text between languages
from googletrans import Translator, LANGUAGES

# # LANGUAGES is a dictionary of len 106
# # {'af' : 'afrikaans','it':'italian'} and so on.....
# # Thus for printing the name of language in print statement we used LANGUAGES[language]

def show_languages():
    for language in LANGUAGES:
        print(language," " * (8 - len(language)),LANGUAGES[language])

def find_errors():
    text = input("Let's have a look at your text.. ")
    while(text.isspace()):
        text = input("Invalid input received. Try again! ")

    tranlated_text = Translator().translate(text)
    print()
    l = tranlated_text.extra_data['possible-mistakes']
    if(l == None):
        print("No errors")
        return
    print("Have a look at possible errors..")
    for i in range(len(l)):
        print(i," = ",l[i])

def detect_language():
    text = input("Let's have a look at your text.. ")
    while(text.isspace()):
        text = input("Invalid input received. Try again! ")
    
    print("Yay!! Language detected")
    res = Translator().detect(text)
    print(LANGUAGES[res.lang])
    print("Interpreter is ",res.confidence * 100,"percent confident!")

def translate():
    print("Please choose what you want to do")
    print("Press 1 for translating your text to a specific language")
    print("Press 2 for translating your text to all languages")
    print("Press 3 to go back")
    print()

    choice = 0
    while(choice>3 or choice<1):
        choice = int(input("Enter your choice :: "))
        if(choice not in [1,2,3]):
            print("Oops!! You entered invalid number.. Try again! ")
    
    print()
    if(choice == 1):
        translate_to_language()
    elif(choice == 2):
        translate_to_all()
    elif(choice == 3):
        return

def translate_to_all():
    text = input("What do you want me to translate for you? ")
    while(text.isspace()):
        text = input("Invalid input received. Try again! ")

    for language in LANGUAGES:
        tranlated_text = Translator().translate(text, dest = language)
        print("Translation in",LANGUAGES[language])
        print(tranlated_text.text)
        print()

def translate_to_language():
    text = input("What do you want me to translate for you? ")
    while(text.isspace()):
        text = input("Invalid input received. Try again! ")
    
    print("Which language should i translate it to? ")
    dest_lang = input("Enter code of the language or press 0 to see list of languages with their codes ")
    if(dest_lang == "0"):
        show_languages()
    else:
        while(dest_lang not in LANGUAGES):
            dest_lang = input("Invalid code. Try Again!! ")

        tranlated_text = Translator().translate(text, dest = dest_lang) 
        print()
        print("This is how we say it in",LANGUAGES[dest_lang])
        print(tranlated_text.text)

print()
print("*"*50,"LANGUAGE TRANSLATOR" ,"*"*50)
print()
print("Welcome to my language translator.. Let's start with your details.. ")
name = " "
while(not(name.isalpha())):
    name = input("My name is = ")

print()
print("Hey",name,"!!")
session_on = True
while(session_on):
    print("Please choose what you want to do")
    print()
    print("Press 1 to display the list of languages")
    print("Press 2 for translating your text")
    print("Press 3 for detecting the language of your text")
    print("Press 4 for finding possible errors in your text")
    print("Press 5 to quit")
    print()

    choice = 0
    while(choice>5 or choice<1):
        choice = int(input("Enter your choice :: "))
        if(choice not in [1,2,3,4,5]):
            print("Oops!! You entered invalid number.. Try again!")

    print()
    if(choice == 1):
        show_languages()
    elif(choice == 2):
        translate()
    elif(choice == 3):
        detect_language()
    elif(choice == 4):
        find_errors()
    elif(choice == 5):
        print("Bye",name)
        print("Hope to meet again!")
        session_on = False

    print()
           
    
