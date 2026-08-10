from core.config import ASSISTANT_NAME


class UltronBrain:

    def __init__(self):
        self.name = ASSISTANT_NAME

    def think(self, command):
        command = command.lower().strip()

        # Greetings
        if "hello" in command or "hi" in command:
            return {
                "type": "response",
                "message": "Hello. I am ULTRON."
            }

        # Identity
        elif "who are you" in command:
            return {
                "type": "response",
                "message": "I am ULTRON, your personal AI assistant."
            }

        # Status
        elif "how are you" in command:
            return {
                "type": "response",
                "message": "All systems are operational."
            }

        # Calculator
        elif "calculator" in command:
            return {
                "type": "action",
                "action": "open_calculator"
            }

        # Notepad
        elif "notepad" in command or "note" in command:
            return {
                "type": "action",
                "action": "open_notepad"
            }

        # Browser
        elif "browser" in command or "google" in command:
            return {
                "type": "action",
                "action": "open_browser"
            }

        # Time
        elif "time" in command:
            return {
                "type": "action",
                "action": "get_time"
            }

        # Date
        elif "date" in command or "today" in command:
            return {
                "type": "action",
                "action": "get_date"
            }

        # Unknown command
        else:
            return {
                "type": "response",
                "message": "I don't know how to handle that command yet."
            }