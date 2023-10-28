import tkinter as tk
from tkinter import ttk
from src.month import getMonth
from datetime import date

class CSVViewerApp(tk.Tk):
    def __init__(self, headers, data, pendientes=0):
        super().__init__()
        self.title("Visor de CSV")
        width= self.winfo_screenwidth()               
        height= self.winfo_screenheight()               
        self.geometry("%dx%d" % (width, height))
        self.headers = headers
        self.data = data
        self.pendientes = pendientes

        self.title_label = None
        self.tree = None

        self.create_gui()

    def create_gui(self):
        # Título
        title_text = f"Cargas hoy {date.today().day} de {getMonth(date.today().month)}, pendientes: {self.pendientes}"
        self.title_label = tk.Label(self, text=title_text, font=("Helvetica", 32, "bold"), bg="cyan")
        self.title_label.pack(pady=10)  # Añadir espacio entre el título y la tabla

        # Crear un Treeview para mostrar una tabla de datos
        self.tree = ttk.Treeview(self, columns=self.headers, show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)  # Todo el ancho y alto de la pantalla
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 24, "bold"))  # Estilo del encabezado
        style.configure("Treeview.Cell", font=("Helvetica", 18))  # Estilo de cada celda
        style.configure("Treeview", rowheight=50)

        # Configurar las columnas de datos
        for header in self.headers:
            self.tree.heading(header, text=header)
            self.tree.column(header, width=100)

        # Agregar datos a la tabla
        for row in self.data:
            self.tree.insert("", "end", values=row, tags="oddrow")
            self.tree.tag_configure("oddrow", background="white", font=("Helvetica", 25))

    def update_data(self, new_headers, new_data, new_pendientes):
        self.title_label.destroy()  # Eliminar el título actual
        self.tree.destroy()  # Eliminar la tabla actual
        self.headers = new_headers
        self.data = new_data
        self.pendientes = new_pendientes
        self.create_gui()  # Crear la interfaz actualizada