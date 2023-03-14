import Model
import View


def main_menu():
    while True:
        View.menu()
        match View.choice:
            case 0:
                Model.show_notes()
            case 1:
                Model.show_date()
            case 2:
                Model.open_note()
            case 3:
                Model.add()
            case 4:
                Model.re()
            case 5:
                Model.delete()
            case 6:
                Model.exit_notes()
                break


def start():
    Model.start_notes()
    main_menu()
