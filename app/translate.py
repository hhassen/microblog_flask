from tkinter import E
from app import app
import boto3
from flask_babel import _
aws_translate = boto3.client(service_name='translate', region_name=app.config['AWS_DEFAULT_REGION'],
    aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'], aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'], use_ssl=True)


def translate(text, source_language, dest_language):
    if 'AWS_SECRET_ACCESS_KEY' not in app.config or \
            not app.config['AWS_SECRET_ACCESS_KEY']:
        return _('Error: the translation service is not configured.')
    try:
        result = aws_translate.translate_text(Text=text, 
            SourceLanguageCode=source_language, TargetLanguageCode=dest_language)
    except Exception as e:
        # print(e)
        return _('Error: the translation service failed.')
    return result.get('TranslatedText')