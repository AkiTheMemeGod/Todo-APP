import functions as fn
import PySimpleGUI as pg
from tkinter import messagebox as mb


label = pg.Text("Type in a todo")
entry_box = pg.InputText(tooltip="enter here", key="todo", size=(35, 1))
button_add = pg.Button("Add")
button_edit = pg.Button("Edit")
button_delete = pg.Button("Complete")
exit_button = pg.Button("Exit")
reminder_button = pg.Button("Email me ;)")
listbox = pg.Listbox(values=fn.get_todos(), key='todos', enable_events=True, size=(35, 10),
                     background_color="#2b2d30",
                     text_color="#ebebeb")
window = pg.Window('My Todo App',
                   resizable=True,
                   element_justification="center",
                   margins=(3, 3),
                   auto_size_text=True,
                   layout=[[label],
                           [entry_box, button_add],
                           [listbox, button_edit, button_delete],
                           [reminder_button,exit_button]],
                   font=('Impact', 16),
                   background_color="#1e1f22",
                   button_color="#64778d")
while True:
    event, values = window.read()
    # print(event)
    # print(values)
    match event:
        case "Add":
            todos = fn.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            fn.put_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            selected = values['todos'][0]
            new_todo = values['todo']
            todos = fn.get_todos()
            ind = todos.index(selected)
            todos[ind] = new_todo + "\n"
            fn.put_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            selected = values['todos'][0]
            todos = fn.get_todos()
            todos.remove(selected)
            fn.put_todos(todos)
            window['todos'].update(values=todos)
        case "Exit":
            window.close()
        case "Email me ;)":
            selected = values['todos'][0]

            fn.send_mail(selected)
            mb.showinfo(title="TODO APP",
                        message="Email has been sent")
        case pg.WINDOW_CLOSED:
            break
window.close()
