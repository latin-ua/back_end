from flask import Flask, request
from flask_cors import CORS, cross_origin

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


def word_translate(word):
    translated_word = []

    for i in word:
        if i in dictionary:
            translated_word.append(dictionary[i])
        else:
            translated_word.append(i)

    translated_word = "".join(translated_word)
    return translated_word


service = Flask("latin-ua-service")
CORS(service)


@service.get("/")
@cross_origin()
def translate_text():
    source_text = request.data.decode("utf8")
    print(f"Received request: {source_text}")
    return word_translate(source_text), 200


@service.get('/health-check')
def health_check():
    return "healthy", 200


if __name__ == "__main__":
    service.run("0.0.0.0", port=8090)
