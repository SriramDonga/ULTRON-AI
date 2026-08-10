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

        if command.lower().strip() == "exit":
            speaker.speak("Goodbye.")
            break

        result = brain.think(command)

        if result["type"] == "response":
            speaker.speak(result["message"])

        elif result["type"] == "action":

            if result["action"] == "open_calculator":
                response = controller.open_calculator()

            elif result["action"] == "open_notepad":
                response = controller.open_notepad()

            elif result["action"] == "open_browser":
                response = controller.open_browser()

            elif result["action"] == "get_time":
                response = controller.get_time()

            elif result["action"] == "get_date":
                response = controller.get_date()

            else:
                response = "I don't know how to perform that action yet."

            speaker.speak(response)


if __name__ == "__main__":
    main()