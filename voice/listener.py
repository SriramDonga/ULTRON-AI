import speech_recognition as sr


class UltronListener:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("ULTRON: Listening...")

            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=8)

                print("ULTRON: Processing...")

                command = self.recognizer.recognize_google(audio)

                print(f"You: {command}")

                return command

            except sr.WaitTimeoutError:
                print("ULTRON: I didn't hear anything.")
                return ""

            except sr.UnknownValueError:
                print("ULTRON: I couldn't understand that.")
                return ""

            except sr.RequestError:
                print("ULTRON: Speech recognition service is unavailable.")
                return ""