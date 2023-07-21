from flask import Flask, request
from flask_cors import CORS, cross_origin

import logging
from ua_latin_kmu import text_translate_kmu
from ua_latin_dstu_a import text_translate_dstu_a

logger = logging.getLogger(__name__)


service = Flask("latin-ua-service")
CORS(service)


# @service.post("/")
# @cross_origin()
# def translate_text_endpoint():
#     source_text = request.data.decode("utf8")
#     logger.error(f"Received request: {source_text}")
#     return text_translate_system_a(source_text), 200


@service.post("/json")
@cross_origin()
def translate_text_endpoint():
    sourse_data = request.json
    translationMethod = sourse_data.get("translationMethod")
    received_text = sourse_data.get("text")
    source_text = received_text.decode("utf8")

    if translationMethod == "KMU":
        logger.error(f"Received request: {source_text}")
        return text_translate_kmu(source_text), 200
    elif translationMethod == "DSTU_A":
        logger.error(f"Received request: {source_text}")
        return text_translate_dstu_a(source_text), 200
    else:
        logger.error(f"Received request: {source_text}")
        return "Translation method must be one of: 'KMU', 'DSTU_A'", 400


@service.get('/health-check')
def health_check_endpoint():
    return "healthy", 200


if __name__ == "__main__":
    service.run("0.0.0.0", port=8090)
