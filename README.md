# Python Dynamic CSV Viewer

Este proyecto es un visor dinámico de archivos CSV construido en Python utilizando la biblioteca Tkinter para la interfaz gráfica y CSV para el procesamiento de datos. La aplicación permite cargar y mostrar datos desde archivos CSV de manera dinámica en una interfaz de usuario.

## Características

- Carga y muestra datos desde archivos CSV.
- Actualiza la interfaz de usuario automáticamente cada 5 segundos con los datos más recientes.
- Permite al usuario seleccionar un archivo CSV en tiempo real para visualizar diferentes conjuntos de datos.

## Requisitos

- Python 3.x
- Biblioteca Tkinter (normalmente incluida en la instalación de Python)
- Biblioteca CSV (normalmente incluida en la instalación de Python)

## Uso

1. Ejecute el archivo `main.py` para iniciar la aplicación.
2. La aplicación cargará automáticamente un archivo CSV ubicado en la ruta predeterminada.
3. La interfaz se actualizará automáticamente cada 5 segundos con los datos más recientes del archivo.
4. Si desea seleccionar un archivo CSV diferente, haga clic en el botón "Seleccionar archivo" y elija el archivo deseado.

## Configuración

Puede personalizar la ruta del archivo CSV predeterminado modificando la variable `csv_file_route` en el archivo `main.py`. Además, puede ajustar el tiempo de actualización en la variable `tiempo_para_actualizar`.

## Contribuciones

Las contribuciones son bienvenidas. Si desea mejorar este proyecto o agregar nuevas características, no dude en crear un pull request.
