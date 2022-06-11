
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import av
import time

apikey = 'cE3WuAQv6sE_Sd2QFQMZqcOI6_0VN3sraGx7Edy-IAXJ'
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/2fab6c67-335c-40fb-a2b5-d9bd56c889dc'

# Setup Service
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

def get_audio():
    if True:
        
        output_text_file = open('output_text.txt','r')
        frames: List[int] = []
        text = ""
        
        for line in output_text_file.readlines():
            text += str(line)
        if len(text):
            print(">>>>>>>>>>>>>>>>>>>>>>>>",len(text))
            file = 'audio.mp3'
            with open(file, 'wb') as audio_file:
                res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
                audio_file.write(res.content)
    #     container = av.open(file)
    #     for frame in container.decode(audio=0):
    #         print("Appending Frames")
    #         frames.append(frame)
    # print(">>>>>> Frame Length: ",len(frames))
    # return frames
