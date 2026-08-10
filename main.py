from core.brain import UltronBrain
from voice.listener import UltronListener
from voice.speaker import UltronSpeaker


def main():
    brain = UltronBrain()
    listener = UltronListener()
    speaker = UltronSpeaker()

    speaker.speak("ULTRON voice system initialized.")

    while True:
        command = listener.listen()

        if not command:
            continue

        if command.lower() == "exit":
            speaker.speak("Goodbye.")
            break

        response = brain.think(command)

        speaker.speak(response)


if __name__ == "__main__":
    main()