### Hello

This is step by step guide to intergrated Google Cloud TTS Component to your Home Assistant

### STEP1. Download to your Home Assistant Custom_Component Folder

1.1. git clone or copy row file to your Home Assistant Custom_Component Folder

### STEP2. Register to get Free API from Google

2.1. Register API:

Follow this guide: https://zalo.ai/user-profile

2.2. Write down the API:

### STEP3. Configure ZaLo TTS Component

3.1. Create folder name tts at local home assistant: www/tts

3.2. Configure the API in your configuration.yaml

```sh
#Zalo TTS
zalo_tts:
 token: 'your ZALO API at Step 2' 
 url: '192.168.1.10:8123'

```
3.3. Restart your hass to active these TTS Component

### STEP4. Configure these TTS Component
```sh
script:
  zalo_reading_01:  #May be from your script name
    sequence:  
    - service: zalo_tts.say
      data_template:
        entity_id: media_player.van_phong
        message: "Your text input here" #May be from your input_text
        speed: '1.0' #May be from your input_number
        voice_name: 'nu_mien_nam_01' #May be from your input_select
        re_use: True #Set True if the content is constance, you'd like to re use in the next time, set False if the content is variable, cant not use in the next time 
```
### STEP5.  Enjoy with the TTS voice
