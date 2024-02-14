from operations import AddOperation, ListOperation, DeleteOperation

def main():
    while True:
        print("Выберите операцию:")
        print("1. Добавить заметку")
        print("2. Показать список заметок")
        print("3. Удалить заметку")
        print("4. Выход")

        choice = input("Введите номер операции: ")

        if choice == '1':
            AddOperation().execute()
        elif choice == '2':
            ListOperation().execute()
        elif choice == '3':
            DeleteOperation().execute()
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
