import logging

from flask import Flask, request
from flask_cors import CORS, cross_origin

from ua_latin_kmu import text_translate_kmu
from ua_latin_dstu_a import text_translate_dstu_a

logger = logging.getLogger(__name__)


service = Flask("latin-ua-service")
CORS(service)


@service.post("/")
@cross_origin()
def translate_text_endpoint():
    source_data = request.json
    translation_method = source_data.get("translationMethod")
    source_text = source_data.get("text")

    logger.info(f"Received request: {source_text}")

    if translation_method == "KMU":
        return text_translate_kmu(source_text), 200
    elif translation_method == "DSTU_A":
        return text_translate_dstu_a(source_text), 200
    else:
        return "Translation method must be one of: 'KMU', 'DSTU_A'", 400


@service.get('/health-check')
def health_check_endpoint():
    return "healthy", 200


if __name__ == "__main__":
    service.run("0.0.0.0", port=8090)
