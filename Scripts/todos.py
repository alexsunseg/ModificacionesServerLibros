import os
import requests

urlBase = "https://www.conaliteg.sep.gob.mx/2023/c/"

links = [
    "P1MLA",
    "P1PAA",
    "P1PCA",
    "P1TPA",
    "P1SDA",
    "P1PEA",
    "P1LPM",
    "P2MLA",
    "P2PAA",
    "P2PCA",
    "P2PEA",
    "P2SDA",
    "P3LPM",
    "P3MLA",
    "P3PAA",
    "P3PCA",
    "P3PEA",
    "P3SDA",
    "P0SHA",
    "P0CMA",
    "P4SDA",
    "P4LPM",
    "P4PAA",
    "P4PCA",
    "P4PEA",
    "P5SDA",
    "P5LPM",
    "P5PAA",
    "P5PCA",
    "P5PEA",
    "P5MLA",
    "P6SDA",
    "P6LPM",
    "P6PAA",
    "P6PCA",
    "P6PEA",
    "P6MLA"
]


# Carpeta destino
folderDestino = os.path.join(os.getcwd(), "librosPrimaria")
os.mkdir(folderDestino)


for link in links:

    count = 0
    continuar = True

    folder = os.path.join(folderDestino, link)

    os.mkdir(folder)

    full_url = urlBase + link

    while continuar:
        imagenUrl = f"{full_url}/{count:03d}.jpg"

        response = requests.get(imagenUrl)
        if response.status_code == 200:
            imagenNombreSecuencia = f"{link}_{count:03d}.jpg"
            imagenPath = os.path.join(folder, imagenNombreSecuencia)

            with open(imagenPath, "wb") as img_file:
                img_file.write(response.content)

            print(f"Imagen {imagenNombreSecuencia} descargada")
            count += 1

        else:
            print(f"Error al descargar la imagen {imagenUrl}")
            continuar = False

print("Proceso de descarga de imágenes completado.")
