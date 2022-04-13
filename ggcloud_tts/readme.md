### Hello

This is step by step guide to intergrated Google Cloud TTS Component to your Home Assistant

### STEP1. Download to your Home Assistant Custom_Component Folder

1.1. git clone or copy row file to your Home Assistant Custom_Component Folder

### STEP2. Register or get Free API from Google

2.1. Register API:

Follow this guide: https://support.google.com/googleapi/answer/6158862?hl=en

2.2. Get Free API:

2.2.1.
Access this page by Google Chrome
```sh
https://www.gstatic.com/cloud-site-ux/text_to_speech/text_to_speech.min.html
```

2.2.2.
Press F12

Press Ctrl + R

2.2.3. 
Press SPEAK IT Button

2.2.4.
Complete Capcha

2.2.5.
Click Network Tab at Right Windows

2.2.6.
Click Fetch/XHR Tab at Right Windows

Click line: proxy?url= at Left Column at Right Windows

Read value of this line by Tab Header at Right Sub Windows

If they like 
```sh
https://cxl-services.appspot.com/proxy?url=https://texttospeech.googleapis.com/v1beta1/text:synthesize&token=03AGdBq27QjGOUzzA33Xye3C4mpOK7xnEblcNFBDMHXbzP6X1IRtD_TtT0fKsXRQzpzkQF0JpKxaLRsVcY-NdHWO6XOlV0ZjQCCVMzHsGwk_PHgQVMEiwn-C8YI_BfN3H7kWfw-6HdY0j2TVWD-lPZz5l_hS8sL2hdr3XAP7O0p-Wd7t4r2ggnBtq-e9cYN1laVPBt12oxWHTOhLGn9UlRUQX03O-I7BF2nDlpkLWqhbKO9a9kPfqSfJsa6wOZgy1fQxAvd9fhf3hwwJuQ1KNZaCb6U7pv6FBepyoJtvst8-gyzIJ8QgF8bBUAVmQJ3rB6tWauGK3yRFihaSUdxy8mLdutmCkZ7M6DxNtG-KiVC-08lb2sJM7prZnX7RwSQh8ZLxpfI9cjcNsg5KFEJD22qbIO4aFI3t981R_JPt2j7Q3IHFGCqZEzy6ibdbM0xrRkZtTPX8i7uyAxXZ7dxuWQeu-NanquwMHR7g
```
the api will be
```sh
03AGdBq27QjGOUzzA33Xye3C4mpOK7xnEblcNFBDMHXbzP6X1IRtD_TtT0fKsXRQzpzkQF0JpKxaLRsVcY-NdHWO6XOlV0ZjQCCVMzHsGwk_PHgQVMEiwn-C8YI_BfN3H7kWfw-6HdY0j2TVWD-lPZz5l_hS8sL2hdr3XAP7O0p-Wd7t4r2ggnBtq-e9cYN1laVPBt12oxWHTOhLGn9UlRUQX03O-I7BF2nDlpkLWqhbKO9a9kPfqSfJsa6wOZgy1fQxAvd9fhf3hwwJuQ1KNZaCb6U7pv6FBepyoJtvst8-gyzIJ8QgF8bBUAVmQJ3rB6tWauGK3yRFihaSUdxy8mLdutmCkZ7M6DxNtG-KiVC-08lb2sJM7prZnX7RwSQh8ZLxpfI9cjcNsg5KFEJD22qbIO4aFI3t981R_JPt2j7Q3IHFGCqZEzy6ibdbM0xrRkZtTPX8i7uyAxXZ7dxuWQeu-NanquwMHR7g
```
Write down it to use at Step 3

### STEP3. Configure Google Cloud TTS Component

3.1. Create folder name tts at local home assistant: www/tts

3.2. Configure the API in your configuration.yaml

```sh
#TTS of Google Cloud TTS
ggcloud_tts:
 token: 'your Gooogle API at Step 2' 
 url: '192.168.1.10:8123'

```
3.3. Restart your hass to active these TTS Component

### STEP4. Configure these TTS Component
```sh
script:
  gg_reading_01:  #May be from your script name
    sequence:  
    - service: ggcloud_tts.say
      data_template:
        entity_id: media_player.van_phong
        message: "Your text input here" #May be from your input_text
        speed: '1.0' #May be from your input_number
        pitch: '0' #May be from your input_number
        language: "vi-VN" #May be from your input_select
        voice_name: "Google_Voice_1"' #May be from your input_select
```
### STEP5.  Enjoy with the TTS voice
