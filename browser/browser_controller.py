import webbrowser
from urllib.parse import quote


class BrowserController:

    def open_google(self):
        webbrowser.open("https://www.google.com")
        return "Google opened."

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com")
        return "YouTube opened."

    def open_browser(self):
        webbrowser.open("https://www.google.com")
        return "Browser opened."

    def search_google(self, query):
        search_url = "https://www.google.com/search?q=" + quote(query)
        webbrowser.open(search_url)
        return f"Searching Google for {query}."

    def search_youtube(self, query):
        search_url = (
            "https://www.youtube.com/results?search_query="
            + quote(query)
        )
        webbrowser.open(search_url)
        return f"Searching YouTube for {query}."