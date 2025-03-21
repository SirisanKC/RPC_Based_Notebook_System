import xmlrpc.client

# Connect to the server
client = xmlrpc.client.ServerProxy("http://localhost:8000")

def add_note():
    topic_name = input("Enter topic name: ")
    text = input("Enter note text: ")
    
    if client.add_note(topic_name, text):
        print("Note added successfully!")
    else:
        print("Failed to add note.")

def get_notes():
    topic_name = input("Enter topic name to retrieve notes: ")
    notes = client.get_notes(topic_name)
    if notes:
        print(f"Notes for topic '{topic_name}':")
        for note in notes:
            print(f"Text: {note['text']}")
            print(f"Timestamp: {note['timestamp']}\n")
    else:
        print(f"No notes found for topic '{topic_name}'.")

def add_note_with_wikipedia():
    topic_name = input("Enter topic name: ")
    
    if client.add_note_with_wikipedia(topic_name):
        print("Note added with Wikipedia data successfully!")
    else:
        print("Failed to add note.")

def main():
    while True:
        print("\n1. Add Note")
        print("2. Retrieve Notes")
        print("3. Add Note with Wikipedia Data")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            get_notes()
        elif choice == "3":
            add_note_with_wikipedia()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()