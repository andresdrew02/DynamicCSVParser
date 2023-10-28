from src.csv_parser import CSVParser
from src.constants import *
from src.gui import CSVViewerApp
from tkinter import filedialog

csv_file_route = 'c:/Users/andre/Desktop/Proyectos/PythonDynamicCSVParser/data/sample.csv' # Cambia esta ruta para que sea una ruta por defecto

tiempo_para_actualizar = 5000 # En milisegundos, por defecto, cada 5000ms (5 segundos)

def seleccionar_archivo():
    ruta_archivo = filedialog.askopenfilename()
    if ruta_archivo:
        # Actualiza la ruta del archivo CSV con la ruta seleccionada
        global csv_file_route
        csv_file_route = ruta_archivo
        print(f"Archivo seleccionado: {csv_file_route}")

def actualizar_interfaz():
    print("CSV Cargado")
    parser = CSVParser(csv_file_route)
    if parser.check_file_permissions() == FILE_PERMISSIONS_OK:
        parser.parse_file()
        headers = parser.file.headers
        data = parser.file.data
        app.update_data(headers, data, parser.get_numero_pendientes())
    
    app.after(tiempo_para_actualizar, actualizar_interfaz)  # Programar la próxima actualización cada 5000 ms (5 segundos)

if __name__ == '__main__':
    app = CSVViewerApp([], [])  # Inicializa la aplicación con encabezados y datos vacíos

    seleccionar_archivo()

    # Iniciar el proceso de actualización
    actualizar_interfaz()

    app.mainloop()
