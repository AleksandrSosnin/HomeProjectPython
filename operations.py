from note_manager import NoteManager
from note import Note

class Operation:
    def execute(self):
        pass

class AddOperation(Operation):
    def execute(self):
        title = input("Введите заголовок заметки: ")
        body = input("Введите тело заметки: ")
        note = Note(title, body)
        NoteManager("notes.json").add_note(note)
        print("Заметка успешно сохранена")

class ListOperation(Operation):
    def execute(self):
        notes = NoteManager("notes.json").load_notes()
        for note_data in notes:
            note = Note(**note_data)
            print(note)
            print()

class DeleteOperation(Operation):
    def execute(self):
        index = int(input("Введите индекс заметки для удаления: "))
        if NoteManager("notes.json").delete_note_by_index(index):
            print("Заметка успешно удалена")
        else:
            print("Неверный индекс заметки")
