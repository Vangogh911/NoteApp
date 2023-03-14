import json
import datetime


notes = {}


def open_note():
    # вывод текста заметки
    global notes
    title = input("Введите заголовок заметки: ")
    if notes.get(title) is not None:
        for x in notes.get(title):
            print(x)
    else:
        print("Отсутствует заметка с таким заголовком.")


def add():
    # добавление заметок
    global notes
    title = input("Введите заголовок заметки: ")
    if notes.get(title) is None:
        text = input("Введите текст заметки: ")
        time_stamp = datetime.datetime.now()
        note = {text: time_stamp.strftime('%H:%M %m.%d.%Y')}
        notes.update({title: note})
    else:
        print("Заметка с таким заголовком уже существует.\n"
              "Отредактируйте существующую заметку или создайте новую.")


def delete():
    # удаление заметок
    global notes
    title = input("Введите заголовок заметки: ")
    try:
        notes.pop(title)
    except KeyError:
        print("Отсутствует заметка с таким заголовком.")


def re():
    # редактирование заметок
    global notes
    title = input("Введите заголовок заметки: ")
    if title is not None:
        for x in notes.get(title):
            print("Оригинальный текст заметки:")
            print(x)
        print('Для отмены введите "/Отмена"')
        text = input("Введите новый текст заметки: ")
        if text != "/Отмена":
            time_stamp = datetime.datetime.now()
            note = {text: time_stamp.strftime('%H:%M %d.%m.%Y')}
            notes.pop(title)
            notes.update({title: note})
    else:
        print("Отсутствует заметка с таким заголовком.")


def show_notes():
    # показать весь список заметок
    global notes
    for x in notes:
        for y in notes[x]:
            print(x, '-', notes[x][y])


def exit_notes():
    # выгружает заметки в json-файл при выходе из приложения
    global notes
    with open("data.json", "w") as fh:
        json.dump(notes, fh)


def start_notes():
    # загружает заметки из json-файла при входе в приложение
    global notes
    with open("data.json", "r") as fh:
        notes = json.load(fh)


def show_date():
    global notes
    date = input('Введите дату в формате "31.01.1970": ')
    count = 0
    for x in notes:
        for y in notes[x]:
            if notes[x][y][-10:] == date:
                print(x, '-', notes[x][y])
                count += 1
    if count == 0:
        print("В этот день не было заметок.")
