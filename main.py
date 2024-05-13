from bs4 import BeautifulSoup
import requests
from googletrans import Translator
def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()
        return {
            'english_words' : english_words,
            'word_definition' : word_definition
        }
    except:
       print('Произошла ошибка')

def word_game():
    print('Добро пожаловать в игру')
    while True:
        translator = Translator()
        word_dict = get_english_words()
        word = word_dict.get('english_words')
        word_definition = word_dict.get('word_definition')
        translation = translator.translate(text=word_definition, dest='ru')
        result_text = translation.text
        print(f'Значение слова - {result_text}')

        user = input('Что это за слово? ')
        translation = translator.translate(text=user, dest='en')
        result_word = translation.text
        if result_word == word:
            print('Все верно!')
        else:
            print(f'Ответ неверный, было загадано слово - {word}')

        play_again = input('хотите сыграть еще раз? y/n')
        if play_again != 'y':
            print('Спасибо за игру!')
            break

word_game()
