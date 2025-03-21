# Distributed Notebook System using RPC

This project implements a distributed notebook system using Remote Procedure Calls (RPC). The system allows multiple clients to interact with a server to store and retrieve notes in an XML-based database. Additionally, the server can query Wikipedia for more information on a given topic and append it to the notes.

## Features

### Basic Requirements (1-7 points)
- **Client-side functionality:**
  - Input: Users can submit a topic, text, and timestamp for a note.
  - If the topic exists in the XML database, the note is appended to the existing topic.
  - If the topic does not exist, a new entry is created in the XML database.
  - Users can retrieve the contents of the XML database based on a given topic.

- **Server-side functionality:**
  - Processes client input and stores data in a local XML database.
  - Handles multiple client requests simultaneously.

### Additional Requirements (8-10 points)
- **Client-side functionality:**
  - Users can search for terms on Wikipedia and append the results to an existing topic.

- **Server-side functionality:**
  - Queries the Wikipedia API for information related to the user's search term.
  - Appends relevant information (e.g., a link to a Wikipedia article) to the user-submitted topic.

## Technologies Used
- **Programming Language:** Python
- **RPC Framework:** XML-RPC
- **XML Handling:** `xml.etree.ElementTree`
- **Wikipedia API:** `requests` library for querying Wikipedia



### Prerequisites
- Python 3.x installed
- Required Python libraries: `xmlrpc`, `xml.etree.ElementTree`, `requests`
