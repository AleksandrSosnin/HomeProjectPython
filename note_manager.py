import json

class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_notes(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_notes(self, notes):
        with open(self.file_path, 'w') as f:
            json.dump(notes, f, indent=4)

    def add_note(self, note):
        notes = self.load_notes()
        notes.append(note.to_dict())
        self.save_notes(notes)

    def delete_note_by_index(self, index):
        notes = self.load_notes()
        if 0 <= index < len(notes):
            del notes[index]
            self.save_notes(notes)
            return True
        return False
