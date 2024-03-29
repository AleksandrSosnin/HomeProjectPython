## Класс Note в файле note.py:

Этот класс представляет собой основу для объектов заметок.

- **Атрибуты:**
    - `title`: Заголовок заметки.
    - `body`: Содержимое заметки.
    - `timestamp`: Время создания/редактирования заметки.

- **Методы:**
    - `to_dict()`: Преобразует объект заметки в словарь для последующей сериализации в JSON.
    - `__str__()`: Переопределен для удобного вывода информации о заметке.

## Класс NoteManager в файле note_manager.py:

Этот класс отвечает за управление заметками и их хранение в файле.

- **Методы:**
    - `load_notes()`: Загружает заметки из файла.
    - `save_notes()`: Сохраняет заметки в файл.
    - `add_note()`: Добавляет новую заметку в список заметок и сохраняет его.
    - `delete_note_by_index()`: Удаляет заметку по индексу из списка заметок и сохраняет изменения.

## Модуль operations.py:

В этом модуле содержатся классы для выполнения операций с заметками.

- **Класс Operation:**

    Абстрактный базовый класс для всех операций с заметками.

- **Классы конкретных операций:**

    - **Класс AddOperation:**

        Выполняет операцию добавления новой заметки.

    - **Класс ListOperation:**

        Выполняет операцию просмотра списка всех заметок.

    - **Класс DeleteOperation:**

        Выполняет операцию удаления заметки.

## Файл main.py:

Этот файл содержит основной код для запуска приложения.

- **Функция main():**

    Пользователю предлагается выбрать операцию.

    В зависимости от выбора вызывается соответствующий метод соответствующего класса операции.