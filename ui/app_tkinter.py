import tkinter as tk

class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Lista de Tareas")

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.entry.bind("<Return>", self.agregar_tarea)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Añadir Tarea", command=self.agregar_tarea).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Marcar Completada", command=self.marcar_completada).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self.eliminar_tarea).grid(row=0, column=2, padx=5)

        self.lista = tk.Listbox(root, width=50)
        self.lista.pack(pady=10)

        self.lista.bind("<Double-1>", self.marcar_completada)

    def agregar_tarea(self, event=None):
        descripcion = self.entry.get()
        if descripcion:
            tarea = self.servicio.agregar_tarea(descripcion)
            self.lista.insert(tk.END, f"{tarea.id}. {tarea.descripcion}")
            self.entry.delete(0, tk.END)

    def marcar_completada(self, event=None):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.servicio.obtener_tareas()[index]
            self.servicio.completar_tarea(tarea.id)

            self.lista.delete(index)
            self.lista.insert(index, f"{tarea.id}. [Hecho] {tarea.descripcion}")
            self.lista.itemconfig(index, fg="gray")

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.servicio.obtener_tareas()[index]
            self.servicio.eliminar_tarea(tarea.id)
            self.lista.delete(index)
