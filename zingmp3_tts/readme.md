Service TTS cho phép phát bài hát zingmp3 dựa trên từ khóa

Khai báo trong configuration.yaml như sau:

```sh

zingmp3_tts:

media_extractor:
```   
Khai báo gọi dịch vụ như sau:

```sh
service: zingmp3_tts.say
data: 
 entity_id: media_player.rmx2025_105
 message: 'Ai chung tình được mãi'
```      
