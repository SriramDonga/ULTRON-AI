from core.brain import UltronBrain
from voice.listener import UltronListener
from voice.speaker import UltronSpeaker
from automation.system_control import SystemController


def main():
    brain = UltronBrain()
    listener = UltronListener()
    speaker = UltronSpeaker()
    controller = SystemController()

    speaker.speak("ULTRON voice system initialized.")

    while True:
        command = listener.listen()

        if not command:
            continue

        if command.lower() == "exit":
            speaker.speak("Goodbye.")
            break

        result = brain.think(command)

        if result["type"] == "response":
            speaker.speak(result["message"])

        elif result["type"] == "action":

            if result["action"] == "open_calculator":
                response = controller.open_calculator()
                speaker.speak(response)


if __name__ == "__main__":
    main()