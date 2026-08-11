from core.brain import UltronBrain
from voice.listener import UltronListener
from voice.speaker import UltronSpeaker

from automation.system_control import SystemController
from automation.app_controller import AppController

from browser.browser_controller import BrowserController


def calculate_expression(expression):

    try:

        expression = expression.lower()

        expression = expression.replace("×", "*")
        expression = expression.replace("x", "*")
        expression = expression.replace("÷", "/")

        allowed = "0123456789+-*/(). "

        expression = "".join(
            char
            for char in expression
            if char in allowed
        )

        result = eval(
            expression,
            {"__builtins__": {}}
        )

        return f"The answer is {result}."

    except Exception:

        return "I could not calculate that expression."


def main():

    brain = UltronBrain()
    listener = UltronListener()
    speaker = UltronSpeaker()

    system = SystemController()
    app = AppController()
    browser = BrowserController()

    speaker.speak(
        "ULTRON voice system initialized."
    )

    while True:

        command = listener.listen()

        if not command:
            continue

        result = brain.think(command)

        # --------------------------------
        # NORMAL RESPONSE
        # --------------------------------

        if result["type"] == "response":

            speaker.speak(
                result["message"]
            )

        # --------------------------------
        # EXIT
        # --------------------------------

        elif result["type"] == "exit":

            speaker.speak(
                "Goodbye."
            )

            break

        # --------------------------------
        # ACTION
        # --------------------------------

        elif result["type"] == "action":

            action = result["action"]

            # Calculator
            if action == "open_calculator":

                response = app.open_calculator()

            # Calculate
            elif action == "calculate":

                response = calculate_expression(
                    result["expression"]
                )

            # Notepad
            elif action == "open_notepad":

                response = app.open_notepad()

            # Write into Notepad
            elif action == "write_notepad":

                response = app.open_notepad()

                app.type_text(
                    result["text"]
                )

                response = (
                    "I opened Notepad and typed your message."
                )

            # Browser
            elif action == "open_browser":

                response = app.open_browser()

            # Google
            elif action == "open_google":

                response = browser.open_google()

            # YouTube
            elif action == "open_youtube":

                response = browser.open_youtube()

            # Google Search
            elif action == "search_google":

                response = browser.search_google(
                    result["query"]
                )

            # YouTube Search
            elif action == "search_youtube":

                response = browser.search_youtube(
                    result["query"]
                )

            # Time
            elif action == "get_time":

                response = system.get_time()

            # Date
            elif action == "get_date":

                response = system.get_date()

            else:

                response = (
                    "I don't know how to perform "
                    "that action yet."
                )

            speaker.speak(response)


if __name__ == "__main__":
    main()