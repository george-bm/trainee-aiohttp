import base64
import json
import os

import settings
from aiohttp import web

# key for Google Speech To Text
speech_key = os.environ.get('SPEECH_KEY', None)


async def speech_view(request):
    # retrieving data from client
    body = await request.post()
    languageCode = body['lang']
    encoding = 'FLAC'
    input_file = body['file'].file
    content = input_file.read()

    # converting to base64 string
    audio_bytes = base64.b64encode(content)
    audio_str = audio_bytes.decode('utf-8')

    # data to speech api
    speech_data = {
        "audio": {
            "content": audio_str
        },
        "config": {
            "languageCode": languageCode,
            "encoding": encoding
        }
    }

    # sending to speech apy
    http_client = request.app['external_api']
    response = await http_client.post(settings.URL.format(speech_key), data=json.dumps(speech_data))
    json_response = await response.json()

    # returnint text to client
    return web.Response(text=str(json_response['results'][0]['alternatives'][0]['transcript']))
