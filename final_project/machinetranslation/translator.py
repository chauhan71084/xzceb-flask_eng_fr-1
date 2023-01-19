"""Module providingFunction printing python version."""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def englishtofrench(englishtext):
    frenchtext = language_translator.translate(
    text = englishtext,
    model_id = 'en-fr').get_result()
    return json.dumps(frenchtext, indent=2, ensure_ascii=False)

def frenchtoenglish(frenchtext):
    englishtext = language_translator.translate(
    text = frenchtext,
    model_id = 'fr-en').get_result()
    return json.dumps(englishtext, indent=2, ensure_ascii=False)
