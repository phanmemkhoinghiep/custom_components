Develop based on Python orignal source code at: https://viettelgroup.ai/document/tts

#Hello
This is step by step guide to intergrated these TTS Component to your Home Assistant

### STEP1. Download to your Home Assistant Custom_Component Folder

1.1. git clone or copy row file to your Home Assistant Custom_Component Folder

### STEP2. Register and get Free Token/API from STT engines

2.1. Register Free Viettel TTS Account and get Token at: https://viettelgroup.ai/en

### STEP3. Configure these TTS Component

3.1. Create folder name tts at local home assistant: www/tts

3.2. Configure the API in your configuration.yaml

3.2.1. Configure Example for Viettel TTS
```sh
#TTS of Vietnamese Viettel TTS
viettel_tts:
 token: 'your Viettel Token' 
   #See in the /custom_components/viettel_tts/readme.txt for more detail how to create Viettel API
 url: 'your hass base URL'
 ```
3.2.2. This is a example how to use this service

```sh
script:
  viettel_reading_08:
    sequence:  
    - service: viettel_tts.say
      data_template:
        entity_id: media_player.note4    
        message: "{{ Your text here }}
        voice_type: 'nu_mien_nam_1'    
        speed: '1.0'  
```

Thank you!
