import os
import glob
import random
import speech_recognition as sr
from playsound import playsound


def get_audio_list(audio_type):
    audio_list = glob.glob(os.path.join(base_dir, 'mp3', audio_type, '*.mp3'))
    return(audio_list)


def speech():
    # 音声入力
    while True:
        text = ''
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('コバブル「僕に話しかけてね」')
            audio = r.listen(source)
    
        try:
            # Google Web Speech APIで音声認識
            text = r.recognize_google(audio, language='ja-JP')
        except sr.UnknownValueError:
            print('コバブル「何て言ってるか分からなかったよ」')
        except sr.RequestError as e:
            print(f'GoogleWeb Speech APIに音声認識を要求できませんでした。 {e}')
        else:
            print(text)

        if 'おはよう' in text:
            playsound(random.choice(ohayo_list))
        elif 'こんにちは' in text:
            playsound(random.choice(konnichiha_list))
        elif 'こんばんは' in text:
            playsound(random.choice(konbanha_list))
        elif 'おやすみ' in text:
            playsound(random.choice(oyasumi_list))
        elif 'よろしく' in text:
            playsound(random.choice(yoroshiku_list))
        elif text == 'バイバイ':
            playsound(random.choice(bye_list))
            print('コバブル「じゃあね」')
            break


if __name__ == '__main__':
    base_dir = os.path.dirname(__file__)

    ohayo_list      = get_audio_list('ohayo')
    konnichiha_list = get_audio_list('konnichiha')
    konbanha_list   = get_audio_list('konbanha')
    oyasumi_list    = get_audio_list('oyasumi')
    yoroshiku_list  = get_audio_list('yoroshiku')
    bye_list        = get_audio_list('bye')
    speech()
