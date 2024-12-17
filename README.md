# Extract Metadata Tool

## Descripción

Este script en Python permite trabajar con metadatos de imágenes, incluyendo la extracción de metadatos generales, la extracción de coordenadas GPS y la eliminación de todos los metadatos de una imagen. Está diseñado para ser fácil de usar y se ejecuta desde la línea de comandos.

## Características

- **Extracción de metadatos**: Obtiene y muestra los metadatos EXIF de una imagen, incluyendo información como el fabricante de la cámara, la fecha y la hora de captura, entre otros.
- **Extracción de coordenadas GPS**: Si la imagen contiene información GPS en los metadatos, el script calcula y muestra las coordenadas (latitud y longitud).
- **Eliminación de metadatos**: Crea una nueva versión de la imagen original sin ningún metadato.

## Requisitos

- Python 3.7 o superior.
- Librería **Pillow** (Python Imaging Library). Puedes instalarla con:
  ```bash
  pip install pillow
  ```

## Uso

### Ejecución del script

1. Guarda el archivo con el nombre `extract_metadata.py`.
2. Abre una terminal o línea de comandos.
3. Ejecuta el script especificando la ruta de la imagen:
   ```bash
   python extract_metadata.py <ruta_de_la_imagen>
   ```

### Menú interactivo

Una vez iniciado, el script mostrará un menú interactivo con las siguientes opciones:

1. **Extraer metadatos**:

   - Selecciona esta opción para mostrar todos los metadatos EXIF presentes en la imagen.

2. **Extraer coordenadas GPS**:

   - Si los metadatos contienen información GPS, el script calculará y mostrará las coordenadas en formato decimal (latitud y longitud).

3. **Eliminar metadatos**:

   - Crea una copia de la imagen sin ningún metadato. La nueva imagen se guardará en el mismo directorio con el nombre `no_meta.<extensión>`.

4. **Salir**:
   - Termina la ejecución del script.

## Ejemplo de uso

Para procesar una imagen llamada `foto.jpg`, ejecuta el script:

```bash
python extract_metadata.py foto.jpg
```

En el menú interactivo, elige la opción deseada según lo que necesites realizar.

## Notas

- El script funciona con imágenes en formatos compatibles con **Pillow**, como JPG y PNG.
- Si no se encuentra información GPS en los metadatos, el script indicará que no hay datos GPS disponibles.

## Estructura del Código

1. **`get_exif`**: Extrae todos los metadatos EXIF de una imagen.
2. **`gps_extract`**: Procesa los datos GPS de los metadatos para devolver coordenadas en formato decimal.
3. **`no_meta`**: Crea una copia de la imagen sin ningún metadato.
4. **`main`**: Maneja el flujo del programa, presentando el menú y ejecutando las acciones seleccionadas.

## Contribución

Si deseas mejorar este script o agregar nuevas funcionalidades, no dudes en enviar tus sugerencias o crear un pull request en el repositorio.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [`LICENSE`](https://mit-license.org/) para más información.
