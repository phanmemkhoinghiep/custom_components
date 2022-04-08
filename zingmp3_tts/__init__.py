# encoding: utf-8
import datetime
import json
import time
import requests
import re
import urllib
# Declare variables
DOMAIN = 'zingmp3_tts'
SERVICE_ZINGMP3_TTS = 'say'
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
        mp3_link=''
        try:
            resp = requests.get('http://ac.mp3.zing.vn/complete/desktop?type=song&query='+urllib.parse.quote(message))
            resultJson = json.dumps(resp.json())
            obj = json.loads(resultJson)
            songID = obj["data"][0]['song'][0]['id']
            songUrl= "https://mp3.zing.vn/bai-hat/"+songID+".html"
            # print(songUrl)
            resp = requests.get(songUrl)
            # print(resp.text)
            key = re.findall('data-xml="\/media\/get-source\?type=audio&key=([a-zA-Z0-9]{20,35})', resp.text)
            # key = re.findall('data-xml="\/media\/get-source\?type=video&key=([a-zA-Z0-9]{20,35})', resp.text)
            songApiUrl = "https://mp3.zing.vn/xhr/media/get-source?type=audio&key="+key[0]
            resp = requests.get(songApiUrl)
            resultJson = json.dumps(resp.json())
            obj = json.loads(resultJson)
            # print(str(obj))
            mp3_link = str(obj["data"]["source"]["128"])            
            # service data for 'CALL SERVICE' in Home Assistant
            service_data = {'entity_id': media_id, 'media_content_id': mp3_link, 'media_content_type': 'audio/mp3'}
            # Call service from Home Assistant
            hass.services.call('media_extractor', 'play_media', service_data)
        except (IndexError, ValueError):
            pass

    hass.services.register(DOMAIN, SERVICE_ZINGMP3_TTS, tts_handler)
    return True

