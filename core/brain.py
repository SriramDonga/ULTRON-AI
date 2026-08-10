from core.config import ASSISTANT_NAME


class UltronBrain:

    def __init__(self):
        self.name = ASSISTANT_NAME

    def think(self, command):
        command = command.lower()

        if "hello" in command:
            return "Hello. I am ULTRON."

        elif "who are you" in command:
            return "I am ULTRON, your personal AI assistant."

        elif "how are you" in command:
            return "All systems are operational."

        else:
            return "I don't know how to handle that command yet."