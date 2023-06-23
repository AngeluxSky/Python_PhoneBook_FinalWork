import text
import view
import model


def start():
    pb = model.PhoneBook()
    while True:
        select = view.menu()
        match select:
            case 1:
                if pb.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if pb.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(pb.get(), text.empty_book)
            case 4:
                new = view.add_contact()
                pb.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                word = view.view_input(text.search_word)
                result = pb.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                view.show_contacts(pb.get(), text.empty_book)
                index = view.view_input(text.index_edit)
                new_data = view.add_contact()
                if pb.edit_contact(index, new_data):
                    view.print_message(text.edit_successful)
            case 7:
                word = view.view_input(text.search_word)
                result = pb.search(word)
                view.show_contacts(result, text.empty_search(word))
                index = view.view_input(text.index_remove)
                name = pb.remove(index)
                view.print_message(text.remove_contact(name))

            case 8:
                if pb.check_on_exit():
                    answer = view.view_input(text.change_confirm)
                    if answer != 'n':
                        pb.save_file()
                view.print_message(text.goodbay)
                break