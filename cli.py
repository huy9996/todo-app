#import
import funcions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Nhap lenh: ")
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:]

        # Đọc tất cả các dòng từ tệp và tạo danh sách todos
        todos = funcions.get_todo()

        todos.append(todo + '\n')

        # Ghi danh sách todos vào tệp
        funcions.write_todo(todos)
    elif user_action.startswith('show'):
        todos = funcions.get_todo()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = funcions.get_todo()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            funcions.write_todo(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = funcions.get_todo()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            funcions.write_todo(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Sai cu phap")


print("Bye")