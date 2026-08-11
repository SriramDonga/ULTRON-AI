import re


class CommandParser:

    def parse(self, command):

        original = command
        command = command.lower().strip()

        command = re.sub(
            r"^(hey\s+)?ultron[\s,]*",
            "",
            command
        )

        # EXIT
        if command in {
            "exit",
            "quit",
            "goodbye",
            "bye",
            "stop"
        }:
            return {
                "intent": "exit"
            }

        # CALCULATOR + CALCULATION
        calculation = self.extract_calculation(command)

        if calculation:
            return {
                "intent": "calculate",
                "expression": calculation
            }

        # OPEN CALCULATOR
        if "calculator" in command:
            return {
                "intent": "open",
                "target": "calculator"
            }

        # NOTEPAD + TEXT
        if "notepad" in command or "text editor" in command:

            write_text = self.extract_write_text(command)

            if write_text:
                return {
                    "intent": "write",
                    "target": "notepad",
                    "text": write_text
                }

            return {
                "intent": "open",
                "target": "notepad"
            }

        # YOUTUBE SEARCH
        if "youtube" in command and self.is_search_command(command):

            query = self.extract_search_query(
                command,
                "youtube"
            )

            if query:
                return {
                    "intent": "search",
                    "target": "youtube",
                    "query": query
                }

        # GOOGLE SEARCH
        if self.is_search_command(command):

            query = self.extract_search_query(
                command,
                "google"
            )

            if query:
                return {
                    "intent": "search",
                    "target": "google",
                    "query": query
                }

        # OPEN YOUTUBE
        if "youtube" in command:
            return {
                "intent": "open",
                "target": "youtube"
            }

        # OPEN GOOGLE
        if "google" in command:
            return {
                "intent": "open",
                "target": "google"
            }

        # OPEN BROWSER
        if (
            "browser" in command
            or "web browser" in command
            or "internet" in command
        ):
            return {
                "intent": "open",
                "target": "browser"
            }

        # TIME
        if "time" in command:
            return {
                "intent": "get",
                "target": "time"
            }

        # DATE
        if (
            "date" in command
            or "today" in command
            or "what day is it" in command
        ):
            return {
                "intent": "get",
                "target": "date"
            }

        return {
            "intent": "unknown",
            "original_command": original
        }

    # --------------------------------------------------
    # CALCULATION
    # --------------------------------------------------

    def extract_calculation(self, command):

        if re.search(
            r"\d+\s*[\+\-\*\/x×÷]\s*\d+",
            command
        ):
            return command

        calculation_phrases = [
            "what is",
            "calculate",
            "work out",
            "how much is",
            "solve"
        ]

        if any(
            phrase in command
            for phrase in calculation_phrases
        ):

            expression = command

            replacements = {
                "multiplied by": "*",
                "divided by": "/",
                "plus": "+",
                "minus": "-",
                "times": "*",
                "over": "/"
            }

            for word, symbol in replacements.items():
                expression = expression.replace(
                    word,
                    symbol
                )

            expression = re.sub(
                r"^(what is|calculate|work out|how much is|solve)\s+",
                "",
                expression
            )

            if re.search(
                r"\d+\s*[\+\-\*\/]\s*\d+",
                expression
            ):
                return expression

        return None

    # --------------------------------------------------
    # SEARCH
    # --------------------------------------------------

    def is_search_command(self, command):

        words = [
            "search",
            "find",
            "look for",
            "look up",
            "show me"
        ]

        return any(
            word in command
            for word in words
        )

    def extract_search_query(self, command, target):

        query = command

        query = re.sub(
            rf"\b{target}\b",
            "",
            query
        )

        phrases = [
            "search for",
            "search",
            "find me",
            "find",
            "look for",
            "look up",
            "show me",
            "can you",
            "please",
            "could you",
            "would you",
            "open",
            "and"
        ]

        for phrase in phrases:
            query = query.replace(
                phrase,
                ""
            )

        query = re.sub(
            r"\b(on|in|from|using|the web|online)\b",
            "",
            query
        )

        query = re.sub(
            r"\s+",
            " ",
            query
        ).strip()

        return query

    # --------------------------------------------------
    # NOTEPAD TEXT
    # --------------------------------------------------

    def extract_write_text(self, command):

        patterns = [
            r"write (.+)",
            r"type (.+)",
            r"write down (.+)",
            r"make a note saying (.+)",
            r"create a note saying (.+)"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                command
            )

            if match:
                return match.group(1).strip()

        return None