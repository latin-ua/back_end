from flask import Flask, request
from flask_cors import CORS, cross_origin

import logging


logger = logging.getLogger(__name__)


dictionary = {
    'А': 'A',
    'а': 'a',
    'Б': 'B',
    'б': 'b',
    'В': 'V',
    'в': 'v',
    'Г': 'H',
    'г': 'h',
    'Ґ': 'G',
    'ґ': 'g',
    'Д': 'D',
    'д': 'd',
    'Е': 'E',
    'е': 'e',
    'Є': 'Ye',
    'є': 'ie',
    'Ж': 'Zh',
    'ж': 'zh',
    'З': 'Z',
    'з': 'z',
    'И': 'Y',
    'и': 'y',
    'І': 'I',
    'і': 'i',
    'Ї': 'Yi',
    'ї': 'i',
    'Й': 'Y',
    'й': 'i',
    'К': 'K',
    'к': 'k',
    'л': 'l',
    'М': 'M',
    'м': 'm',
    'Н': 'N',
    'н': 'n',
    'О': 'O',
    'о': 'o',
    'П': 'P',
    'п': 'p',
    'Р': 'R',
    'р': 'r',
    'С': 'S',
    'с': 's',
    'Т': 'T',
    'т': 't',
    'У': 'U',
    'у': 'u',
    'Ф': 'F',
    'ф': 'f',
    'Х': 'Kh',
    'х': 'kh',
    'Ц': 'Ts',
    'ц': 'ts',
    'Ч': 'Ch',
    'ч': 'ch',
    'Ш': 'Sh',
    'ш': 'sh',
    'Щ': 'Shch',
    'щ': 'shch',
    'Ю': 'Yu',
    'ю': 'iu',
    'Я': 'Ya',
    'я': 'ia',
    'ь': '',
    "'": '',
}

dictionary_first_letter = {
    'Є': 'Ye',
    'є': 'ye',
    'Ї': 'Yi',
    'ї': 'yi',
    'Й': 'Y',
    'й': 'y',
    'Ю': 'Yu',
    'ю': 'yu',
    'Я': 'Ya',
    'я': 'ya',
}

def text_translate(text):
    word_list = text.split()
    translated_text = []
    for word in word_list:
        translated_word = word_translate(word)
        translated_text.append(translated_word)
    translated_text = " ".join(translated_text)
    return translated_text


def word_translate(word):
    translated_word = []

    for index, letter in enumerate(word):
        if index == 0 and letter in dictionary_first_letter:
            translated_word.append(dictionary_first_letter[letter])
        elif letter in dictionary:
            translated_word.append(dictionary[letter])
        else:
            translated_word.append(letter)

    translated_word = "".join(translated_word)
    return translated_word


service = Flask("latin-ua-service")
CORS(service)


@service.post("/")
@cross_origin()
def translate_text_endpoint():
    source_text = request.data.decode("utf8")
    logger.error(f"Received request: {source_text}")
    return text_translate(source_text), 200


@service.get('/health-check')
def health_check_endpoint():
    return "healthy", 200


if __name__ == "__main__":
    service.run("0.0.0.0", port=8090)
