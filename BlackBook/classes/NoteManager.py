class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, text):
        note = Note(text)
        self.notes.append(note)

    def edit_note(self, index, new_text):
        if 0 <= index < len(self.notes):
            self.notes[index].text = new_text

    def remove_note(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]

    def get_notes(self):
        return [str(note) for note in self.notes]
