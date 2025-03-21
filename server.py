from xmlrpc.server import SimpleXMLRPCServer
import xml.etree.ElementTree as ET
import requests
from datetime import datetime
import os

XML_FILE = "notebook.xml"

class NotebookServer:
    def __init__(self):
        if not os.path.exists(XML_FILE):
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(XML_FILE)

    def add_note(self, topic_name, text):
        """Add a note to a topic, creating the topic if it doesn't exist."""
        timestamp = datetime.now().strftime("%m/%d/%y - %H:%M:%S")  
        tree = ET.parse(XML_FILE)
        root = tree.getroot()

        topic_element = root.find(f"./topic[@name='{topic_name}']")
        if topic_element is None:
            topic_element = ET.SubElement(root, "topic", name=topic_name)

        note = ET.SubElement(topic_element, "note")
        ET.SubElement(note, "text").text = text
        ET.SubElement(note, "timestamp").text = timestamp
        
        tree.write(XML_FILE)
        return True

    def get_notes(self, topic_name):
        """Retrieve notes for a given topic."""
        tree = ET.parse(XML_FILE)
        root = tree.getroot()
        topic_element = root.find(f"./topic[@name='{topic_name}']")
        if topic_element is not None:
            notes = []
            for note in topic_element.findall("note"):
                notes.append({
                    "text": note.find("text").text,
                    "timestamp": note.find("timestamp").text
                })
            return notes
        return []

    def fetch_wikipedia(self, topic_name):
        """Fetch summary from Wikipedia for a given topic."""
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic_name}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            summary = data.get("extract", "No summary available.")
            link = data.get("content_urls", {}).get("desktop", {}).get("page", "No link available.")
            return f"Wikipedia Summary: {summary}\nMore info: {link}"
        else:
            return "Wikipedia lookup failed."

    def add_note_with_wikipedia(self, topic_name):
        """Add a note with data fetched from Wikipedia."""
        # Fetch Wikipedia data
        wikipedia_data = self.fetch_wikipedia(topic_name)
        if wikipedia_data:
            self.add_note(topic_name, wikipedia_data)
            return f"Note added with Wikipedia data for topic: {topic_name}"
        return "Failed to add note with Wikipedia data."

# Start the server
if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
    server.register_instance(NotebookServer())
    print("Server is running on port 8000...")
    server.serve_forever()