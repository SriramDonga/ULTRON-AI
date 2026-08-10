from core.config import ASSISTANT_NAME


class UltronBrain:

    def __init__(self):
        self.name = ASSISTANT_NAME

    def think(self, command):
        command = command.lower()

        if "hello" in command:
            return {
                "type": "response",
                "message": "Hello. I am ULTRON."
            }

        elif "who are you" in command:
            return {
                "type": "response",
                "message": "I am ULTRON, your personal AI assistant."
            }

        elif "how are you" in command:
            return {
                "type": "response",
                "message": "All systems are operational."
            }

        elif "open calculator" in command or "open calculator" in command:
            return {
                "type": "action",
                "action": "open_calculator"
            }

        else:
            return {
                "type": "response",
                "message": "I don't know how to handle that command yet."
            }