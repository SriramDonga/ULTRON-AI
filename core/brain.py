from core.config import ASSISTANT_NAME
from core.command_parser import CommandParser


class UltronBrain:

    def __init__(self):
        self.name = ASSISTANT_NAME
        self.parser = CommandParser()

    def think(self, command):

        command_lower = command.lower()

        parsed = self.parser.parse(command)

        # EXIT
        if parsed["intent"] == "exit":
            return {
                "type": "exit"
            }

        # GREETING
        if (
            "hello" in command_lower
            or command_lower == "hi"
            or "hey" in command_lower
        ):
            return {
                "type": "response",
                "message": "Hello. I am ULTRON."
            }

        # IDENTITY
        if "who are you" in command_lower:
            return {
                "type": "response",
                "message": "I am ULTRON, your personal AI assistant."
            }

        # STATUS
        if "how are you" in command_lower:
            return {
                "type": "response",
                "message": "All systems are operational."
            }

        # CALCULATE
        if parsed["intent"] == "calculate":
            return {
                "type": "action",
                "action": "calculate",
                "expression": parsed["expression"]
            }

        # OPEN
        if parsed["intent"] == "open":

            return {
                "type": "action",
                "action": f"open_{parsed['target']}"
            }

        # WRITE
        if parsed["intent"] == "write":

            return {
                "type": "action",
                "action": "write_notepad",
                "text": parsed["text"]
            }

        # SEARCH
        if parsed["intent"] == "search":

            return {
                "type": "action",
                "action": f"search_{parsed['target']}",
                "query": parsed["query"]
            }

        # INFORMATION
        if parsed["intent"] == "get":

            return {
                "type": "action",
                "action": f"get_{parsed['target']}"
            }

        return {
            "type": "response",
            "message": "I don't know how to handle that command yet."
        }