# encoding: utf-8
import datetime
import json
import time
import os
import requests
import urllib
# Declare variables
DOMAIN = 'zalo_tts'
SERVICE_ZALO_TTS = 'say'
# config
CONF_TOKEN = 'token'
CONF_URL_HASS = 'url'
# data service
CONF_SPEED = 'speed'
CONF_PLAYER_ID = 'entity_id'
CONF_MESSAGE = 'message'
CONF_VOICE_NAME = 'voice_name'
CONF_RE_USE = 're_use'
# audio file path
CONF_FILE_PATH = '/config/www/tts/'
CONF_AUDIO_PATH = '/local/tts/'
def setup(hass, config):
    def tts_handler(data_call):
        # Get config
        url_hass = str(config[DOMAIN][CONF_URL_HASS])
        token = str(config[DOMAIN][CONF_TOKEN])
        # Get data service
        media_id = data_call.data.get(CONF_PLAYER_ID)
        message = str(data_call.data.get(CONF_MESSAGE)[0:2000])
        voice_name = data_call.data.get(CONF_VOICE_NAME)
        speed = data_call.data.get(CONF_SPEED)
        encode_type= 1
        re_use=data_call.data.get(CONF_RE_USE)
        if re_use:
            file_name=CONF_FILE_PATH+'zalo_'+message[:60]+'.mp3'
            if os.path.exists(file_name):
                file_url=url_hass+CONF_AUDIO_PATH+'zalo_'+message[:60]+'.mp3'
            else:
                # List voice of Google Speech Synthesis
                speaker_list = {'nu_mien_bac_01': 2, 'nam_mien_bac_01': 4, 'nu_mien_nam_01': 1,'nam_mien_nam_02': 3} 
                speaker_id = speaker_list.get(voice_name)
                #HTTP Request
                url = 'https://api.zalo.ai/v1/tts/synthesize'
                #Header Parameters
                header_parameters = {'apikey': apikey}
                # Body Parameters
                data = {'input': message.encode('utf-8'), 'speed': speed, 'encoder_type': encode_type,'speaker_id': speaker_id}
                #Get respounse from Server  
                response = requests.post(url, data = data, headers = header_parameters)
                # Get URL File
                file_url = response.json()['data']['url']
                #Save File to Local
                file_response = requests.get(file_url)
                open(file_name, "wb").write(file_response.content)         
        else:
            speaker_list = {'nu_mien_bac_01': 2, 'nam_mien_bac_01': 4, 'nu_mien_nam_01': 1,'nam_mien_nam_02': 3} 
            speaker_id = speaker_list.get(voice_name)
            #HTTP Request
            url = 'https://api.zalo.ai/v1/tts/synthesize'
            #Header Parameters
            header_parameters = {'apikey': apikey}
            # Body Parameters
            data = {'input': message.encode('utf-8'), 'speed': speed, 'encoder_type': encode_type,'speaker_id': speaker_id}
            #Get respounse from Server  
            response = requests.post(url, data = data, headers = header_parameters)
            # Get URL File
            file_url = response.json()['data']['url']
        # Play audio file with Home Assistant Service#  
        # service data for 'CALL SERVICE' in Home Assistant
        service_data = {'entity_id': media_id, 'media_content_id': file_url, 'media_content_type': 'audio/mp3'}
        # Call service from Home Assistant
        hass.services.call('media_extractor', 'play_media', service_data)
    hass.services.register(DOMAIN, SERVICE_ZALO_TTS, tts_handler)
    return True
