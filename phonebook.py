import os

# константы
DATA_FILE = "phonebook.txt"
RECORD_FIELDS = ["last_name", "first_name", "patronymic", "organization", "work_phone", "personal_phone"]

# загрузка данных с файла
def load_phonebook():
    phonebook = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            for line in file:
                entry = dict(zip(RECORD_FIELDS, line.strip().split(',')))
                phonebook.append(entry)
    return phonebook

# сохранение данных в файле
def save_phonebook(phonebook):
    with open(DATA_FILE, "w") as file:
        for entry in phonebook:
            line = ','.join([entry[field] for field in RECORD_FIELDS])
            file.write(line + '\n')

# показать контакты
def display_entries(phonebook, page, entries_per_page):
    start_idx = (page - 1) * entries_per_page
    end_idx = start_idx + entries_per_page
    for entry in phonebook[start_idx:end_idx]:
        print(', '.join([f"{field}: {entry[field]}" for field in RECORD_FIELDS]))

# добавить контакт
def add_entry(phonebook, entry):
    phonebook.append(entry)
    save_phonebook(phonebook)
    print("Entry added successfully.")

# изменить запись
def edit_entry(phonebook, index, updated_entry):
    if 0 <= index < len(phonebook):
        phonebook[index] = updated_entry
        save_phonebook(phonebook)
        print("Entry updated successfully.")
    else:
        print("Invalid index.")

# поиск контактов
def search_entries(phonebook, query):
    results = []
    for entry in phonebook:
        if any(query.lower() in entry[field].lower() for field in RECORD_FIELDS):
            results.append(entry)
    return results

if __name__ == "__main__":
    phonebook = load_phonebook()

    while True:
        print("\nMenu:")
        print("1. Display entries")
        print("2. Add entry")
        print("3. Edit entry")
        print("4. Search entries")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            page = int(input("Enter page number: "))
            entries_per_page = int(input("Enter entries per page: "))
            display_entries(phonebook, page, entries_per_page)

        elif choice == "2":
            new_entry = {field: input(f"Enter {field}: ") for field in RECORD_FIELDS}
            add_entry(phonebook, new_entry)

        elif choice == "3":
            index = int(input("Enter the index of the entry to edit: "))
            updated_entry = {field: input(f"Enter updated {field}: ") for field in RECORD_FIELDS}
            edit_entry(phonebook, index, updated_entry)

        elif choice == "4":
            search_query = input("Enter search query: ")
            results = search_entries(phonebook, search_query)
            if results:
                print("Search results:")
                for entry in results:
                    print(', '.join([f"{field}: {entry[field]}" for field in RECORD_FIELDS]))
            else:
                print("No matching entries found.")

        elif choice == "5":
            break

    print("Program terminated.")
