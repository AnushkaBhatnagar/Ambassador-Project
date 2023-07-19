# Speech recognition
import os
import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY='8c14f348f0244e99a75ddc316a4dcc74'
SPEECH_REGION='eastasia'

def recognize_from_microphone():
   
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)


    audio_config = speechsdk.audio.AudioConfig(filename="YourAudioFile.wav")

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    

recognize_from_microphone()