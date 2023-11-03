from .Command import Command


class PrintNotesWithTagsCommand(Command):
    def execute(self, address_book, note_book, args):
        notes_with_tags = [
            str(note) for note in note_book.data if hasattr(note, 'tags') and note.tags
        ]
        return "\n".join(notes_with_tags) if notes_with_tags else "No notes with tags."
