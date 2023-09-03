import functions as fn
import PySimpleGUI as pg

label = pg.Text("Type in a todo")
entry_box = pg.InputText(tooltip="enter here", key="todo", size=(35, 1))
button_add = pg.Button("Add")
button_edit = pg.Button("Edit")
button_delete = pg.Button("Delete")
listbox = pg.Listbox(values=fn.get_todos(), key='todos', enable_events=True, size=(35, 10))
window = pg.Window('My Todo App',
                   resizable=True,
                   ttk_theme="default",
                   element_justification="center",
                   margins=(3, 3),
                   auto_size_text=True,
                   auto_size_buttons=True,
                   layout=[[label], [entry_box, button_add], [listbox, button_edit, button_delete]],
                   font=('Impact', 16),
                   background_color="yellow",
                   button_color="red",
                   use_ttk_buttons=True)
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
            # window.update_animation(time_between_frames=0.2)
        case "Delete":
            selected = values['todos'][0]
            todos = fn.get_todos()
            # ind = todos.index(selected)
            todos.remove(selected)
            fn.put_todos(todos)
            window['todos'].update(values=todos)
        case pg.WINDOW_CLOSED:
            break
window.close()
