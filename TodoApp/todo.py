class Todo:
    def __init__(self, title: str, completed: bool = False):
        self.title = title
        self.completed = completed

class TodoApp:
    def __init__(self):
        self.todos = []

    def add_todo(self, title: str):
        todo = Todo(title)
        self.todos.append(todo)
        return todo

    def list_todos(self):
        return self.todos

    def complete_todo(self, index: int):
        if 0 <= index < len(self.todos):
            self.todos[index].completed = True
            return True
        return False

    def remove_todo(self, index: int):
        if 0 <= index < len(self.todos):
            del self.todos[index]
            return True
        return False
