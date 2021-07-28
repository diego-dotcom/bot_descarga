## Bot de descarga desde Mis Comprobantes
### *A partir de una planilla de excel con CUIT y clave fiscal, descarga los comprobantes emitidos y recibidos del mes anterior, en formato XLS.*
---
#### Instrucciones:
1. Si no lo tuviera instalado, descargar e instalar Python 3.8.5 o superior, desde www.python.org/downloads
2. Descargar los archivos del repositorio y colocar en la misma carpeta
3. Descargar ChromeDriver (según la versión que tenga de Google Chrome) desde https://chromedriver.chromium.org/downloads y colocar en la carpeta del punto anterior
4. Desde la línea de comandos, sitúese en la carpeta creada e instale las librerías requeridas con `pip install -r requirements.txt`
5. Modifique el archivo claves.xlsx con las CUIT y claves de preferencia, una debajo de la otra. Guarde los cambios
6. Inicie bot.py
---

> El bot aún no resuelve cuando AFIP solicita cambio de clave.
> Dado ese caso u otro error que pudiera surgir, elimine las filas de CUIT / clave que correspondan y vuelva a correr el programa.

