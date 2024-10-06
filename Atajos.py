import tkinter as tk
from tkinter import messagebox, Listbox, StringVar, END


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")

        # Variable para la nueva tarea
        self.task_var = StringVar()

        # Creación de la interfaz gráfica
        self.create_widgets()

        # Atajos de teclado
        self.root.bind('<Return>', self.add_task)
        self.root.bind('<Delete>', self.delete_task)
        self.root.bind('<c>', self.complete_task)
        self.root.bind('<Escape>', self.close_app)

    def create_widgets(self):
        # Campo de entrada para añadir tareas
        self.entry = tk.Entry(self.root, textvariable=self.task_var, width=50)
        self.entry.pack(pady=10)

        # Botón para añadir tarea
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Lista para mostrar tareas
        self.task_listbox = Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(self.root, text="Marcar Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self, event=None):
        task = self.task_var.get()
        if task:
            self.task_listbox.insert(END, task)
            self.task_var.set('')  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def complete_task(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            # Marcar la tarea completada
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, task + " (Completada)")
            self.task_listbox.itemconfig(selected_index, {'fg': 'gray'})  # Cambiar color a gris
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

    def delete_task(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

    def close_app(self, event=None):
        self.root.destroy()


# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
