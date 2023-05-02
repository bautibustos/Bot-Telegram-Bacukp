import zipfile
import os
import datetime 

def zipeo():
    Nom= str ('MomentoZip\\ISPC Backup - '+
        datetime.datetime.now().strftime('%d-%m-%Y')+ " "+
        datetime.datetime.now().strftime('%H;%M')+'.zip')

    with open("Utilidad\\name.txt", "w") as archivo:
        archivo.write(Nom.replace("MomentoZip\I","I"))

    ruta='C:\\Users\\Bauti\\Desktop\\ISPC'
    archivo_zip = zipfile.ZipFile(Nom, "w")
    for carpeta_actual, subcarpetas, archivos in os.walk(ruta):# Recorremos la carpeta principal y sus subcarpetas y añadimos cada archivo a nuestro archivo zip
        archivo_zip.write(carpeta_actual)# Añadimos la carpeta actual al archivo zip
        for archivo in archivos:    # Recorremos los archivos de la carpeta actual y los añadimos al archivo zip
            ruta_completa = os.path.join(carpeta_actual, archivo)
            archivo_zip.write(ruta_completa)
    archivo_zip.close()# Cerramos el archivo zip