from flask import Flask, request
from flask_cors import CORS, cross_origin

import logging
from ua_latin_standard_transliteration import text_translate
from ua_latin_system_a import text_translate

logger = logging.getLogger(__name__)


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
