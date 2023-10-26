import requests as re
import base64

voiceoverDir = "Voiceovers"


def create_voice_over(path, text):
    print(len(text))
    try:
        url = 'https://tiktok-tts.weilnet.workers.dev/api/generation'
        data = {"text": text, "voice": "en_us_007"}
        raw = re.post(url=url, json=data)
        input = raw.json()['data']
        print(raw.status_code)
        audio_data = base64.b64decode(input)
        filePath = f"{voiceoverDir}/{path}.mp3"
        # print(input)
        with open(filePath, "wb") as output_file:
            output_file.write(audio_data)
        return filePath
    except:
        print("Error in Voice over")
        exit(0)
