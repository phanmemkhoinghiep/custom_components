# encoding: utf-8
import datetime
import json
import time
import requests

# Declare variables
DOMAIN = 'youtube_tts'
SERVICE_YOUTUBE_TTS = 'say'
# config
# CONF_API_KEY = 'api_key'
# data service
CONF_PLAYER_ID = 'entity_id'
CONF_MESSAGE = 'message'


def setup(hass, config):

    def tts_handler(data_call):
        # Get config
        # api_key = str(config[DOMAIN][CONF_API_KEY])      
        # Get data service
        media_id = data_call.data.get(CONF_PLAYER_ID)
        message = str(data_call.data.get(CONF_MESSAGE)[0:2000])
        url = "http://vietbot.xyz:5000/api"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        payload = {'data': 'phát bài '+message, 'smh_url':'fdfd', 'smh_token1': 'sfsdfsd', 'smh_name':'hass','private_location':'105.804817,21.028511'}
        song_url=''
        try:
            response = requests.post(url, headers=headers, data= json.dumps(payload))
            # print(str(response.json()))
            payload = response.json()
            song_url=payload['answer_link']
            # service data for 'CALL SERVICE' in Home Assistant
            service_data = {'entity_id': media_id, 'media_content_id': song_url, 'media_content_type': 'audio/mp3'}
            # Call service from Home Assistant
            hass.services.call('media_extractor', 'play_media', service_data)
        except:
            pass

    hass.services.register(DOMAIN, SERVICE_YOUTUBE_TTS, tts_handler)
    return True

