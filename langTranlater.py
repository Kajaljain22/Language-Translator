# Python app to translate any text into 100+ Languages
from googletrans import Translator, LANGUAGES


# # To print sample_text in all languages
# sample_text1 = "This is my house"

# for language in LANGUAGES:
#     tranlated_text = Translator().translate(sample_text1, dest = language)    #we can specify 'src' attribute as well
#     print(LANGUAGES[language] + " : " + tranlated_text.text)

# # LANGUAGES is a dictionary of len 106
# # {'af' : 'afrikaans','it':'italian'} and so on.....
# # Thus for printing the name of language in print statement we used LANGUAGES[language]



# # When sample_text has errors...
# # Extra-data helps to point that out
# sample_text2 = "This is my hous"
# tranlated_text = Translator().translate(sample_text2, dest = 'fr')
# print('French' + " : " + tranlated_text.text)
# print(tranlated_text.extra_data['confidence'])
# print(tranlated_text.extra_data['possible-mistakes'])


# # To detect sample_text is in which language
# sample_text3 = "Mouse"
# print(Translator().detect(sample_text3))


# Translate text into our specified languages only
sample_text4 = '''
In your eyes, there's a heavy blue
One to love and one to lose
Sweet divide, a heavy truth
Water or wine, don't make me choose
'''
my_lang_list = ['en', 'fr', 'hi']
for language in my_lang_list:
    tranlated_text = Translator().translate(sample_text4, dest = language) 
    print(LANGUAGES[language] + " : " + tranlated_text.text)
    print()
