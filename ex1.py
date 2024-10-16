from gtts import gTTS
import speech_recognition as sr
import os

def get_accent():
    print("Choose an accent type:")
    print("1. US English (en-US)")
    print("2. UK English (en-GB)")
    print("3. Spanish (es)")
    print("4. French (fr)")
    print("5. Indian English (en-IN)")
    print("6. Canadian English (en-CA)")
    print("7. Chinese (zh)")
    print("8. Japanese (ja)")

    choice = input("Enter the number corresponding to the accent type: ")

    accent_mapping = {
        "1": "en-US",
        "2": "en-GB",
        "3": "es",
        "4": "fr",
        "5": "en-IN",
        "6": "en-CA",
        "7": "zh",
        "8": "ja"
    }

    return accent_mapping.get(choice, "en-US")

def speech_to_text(file_path):
    # Get the accent type from the user
    accent_type = get_accent()

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(file_path) as source:
        print("Processing the audio file...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Listen to the audio until there's silence
        audio_data = recognizer.record(source)
        

    try:
        # Recognize the speech using Google Speech Recognition
        text = recognizer.recognize_google(audio_data)
        print("You said: " + text)

        # Convert the recognized text to speech in the chosen accent
        language = accent_type
        speech = gTTS(text=text, lang=language, slow=False)
        speech.save("uploads/texttospeech2.mp3")


        # Play the generated audio on the command prompt
        os.system("start texttospeech2.mp3")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    file_path = "C:/Users/venka/OneDrive/Downloads/american_s01_713.wav"



    speech_to_text(file_path)