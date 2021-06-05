import db_operations
import tkinter


def show_all(label):
    contents = []
    for content in db.show_all():
        contents.append(content)
    label['text'] = contents
    label.grid()


def send_content(edit_box):
    value = edit_box.get()
    db.insert(value)
    db.commit()


if __name__ == '__main__':
    db = db_operations.Interaction('./data/test.db')
    db.do_connect()
    db.delete_table(table_name='test') # develop
    db.create_tabel(table_name='test')

    root = tkinter.Tk()
    root.title('MyToDo')
    root.geometry('400x400')

    label = tkinter.Label(text='show list here')
    label.grid()

    edit_box = tkinter.Entry()
    edit_box.grid()

    button = tkinter.Button(text='register',
                            command=lambda: (send_content(edit_box),
                                            show_all(label))
    )
    button.grid()

    root.mainloop()
    db.do_disconnect()