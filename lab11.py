import sys
from collections import Counter

# Телефонна книга
phonebook = [
    {"ім'я": "Іван", "прізвище": "Петренко", "телефон": "123456789", "місто": "Київ"},
    {"ім'я": "Олена", "прізвище": "Іванова", "телефон": "987654321", "місто": "Харків"},
    {"ім'я": "Сергій", "прізвище": "Коваль", "телефон": "555444333", "місто": "Київ"},
    {"ім'я": "Марія", "прізвище": "Шевченко", "телефон": "111222333", "місто": "Львів"},
    {"ім'я": "Анна", "прізвище": "Мельник", "телефон": "999888777", "місто": "Одеса"},
]

def display_phonebook(contacts):
    if not contacts:
        print("Контакти не знайдено.")
        return
    
    headers = ["Ім'я", "Прізвище", "Телефон", "Місто"]
    row_format = "{:<12} {:<15} {:<12} {:<12}"
    print(row_format.format(*headers))
    print("-" * 55)
    for c in contacts:
        print(row_format.format(c["ім'я"], c["прізвище"], c["телефон"], c["місто"]))

def search_contacts(phonebook, field):
    value = input(f"Введіть {field}: ").strip()
    if not value:
        print("Помилка: порожній ввід.")
        return
    results = [contact for contact in phonebook if contact[field].lower() == value.lower()]
    display_phonebook(results)

def update_contact(phonebook):
    phone = input("Введіть телефон контакту для оновлення: ").strip()
    for contact in phonebook:
        if contact["телефон"] == phone:
            print("Контакт знайдено:")
            display_phonebook([contact])
            confirm = input("Оновити контакт? (так/ні): ").strip().lower()
            if confirm == "так":
                for key in ["ім'я", "прізвище", "телефон", "місто"]:
                    new_val = input(f"Нове {key} (залишити пустим для збереження): ").strip()
                    if new_val:
                        contact[key] = new_val
                print("Контакт оновлено.")
            return
    print("Контакт не знайдено.")

def delete_contact(phonebook):
    phone = input("Введіть телефон для видалення контакту: ").strip()
    for contact in phonebook:
        if contact["телефон"] == phone:
            print("Контакт знайдено:")
            display_phonebook([contact])
            confirm = input("Видалити контакт? (так/ні): ").strip().lower()
            if confirm == "так":
                phonebook.remove(contact)
                print("Контакт видалено.")
            return
    print("Контакт не знайдено.")

def analyze_contacts(phonebook):
    cities = {c["місто"] for c in phonebook}
    print(f"Унікальні міста: {', '.join(cities)}")
    
    city_counts = Counter([c["місто"] for c in phonebook])
    print("Кількість контактів по містах:")
    for city, count in city_counts.items():
        print(f"{city}: {count}")

    if city_counts:
        most_common = city_counts.most_common(1)[0]
        print(f"Місто з найбільшою кількістю контактів: {most_common[0]} ({most_common[1]})")

# Меню
def main():
    while True:
        print("\nМеню:")
        print("1. Показати всі контакти")
        print("2. Пошук за іменем")
        print("3. Пошук за прізвищем")
        print("4. Пошук за містом")
        print("5. Оновити контакт")
        print("6. Видалити контакт")
        print("7. Аналітика")
        print("8. Вийти")
        choice = input("Оберіть опцію: ").strip()

        if choice == "1":
            display_phonebook(phonebook)
        elif choice == "2":
            search_contacts(phonebook, "ім'я")
        elif choice == "3":
            search_contacts(phonebook, "прізвище")
        elif choice == "4":
            search_contacts(phonebook, "місто")
        elif choice == "5":
            update_contact(phonebook)
        elif choice == "6":
            delete_contact(phonebook)
        elif choice == "7":
            analyze_contacts(phonebook)
        elif choice == "8":
            print("Завершення програми.")
            sys.exit()
        else:
            print("Невірна опція. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
