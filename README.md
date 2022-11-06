## Bot de descarga de comprobantes desde Mis Comprobantes (AFIP)
### *A partir de una planilla de excel con una lista de CUIT y claves fiscales, descarga los comprobantes emitidos y recibidos del mes anterior de cada contribuyente, en formato XLS.*
---
#### Instrucciones:
1. Si no lo tuviera instalado, descargue e instale Python 3.8.5 o superior, desde www.python.org/downloads. Durante la instalación asegúrese de agregar Python al PATH.
2. Descargue los archivos bot.py, claves.xlsx y requirements.txt del repositorio, y colóquelos en una misma carpeta.
3. Descargue ChromeDriver (según la versión que tenga de Google Chrome) desde https://chromedriver.chromium.org/downloads, y coloque en la carpeta del punto anterior.
4. Desde la línea de comandos, sitúese en la carpeta creada e instale las librerías requeridas con `pip install -r requirements.txt`
5. Modifique el archivo claves.xlsx con las CUIT y claves de preferencia, una debajo de la otra. Guarde los cambios.
6. Inicie bot.py
---

> El bot aún no resuelve cuando AFIP solicita cambio de clave.
> Dado ese caso u otro error que pudiera surgir, elimine las filas de CUIT / clave que correspondan y vuelva a correr el programa.
> El desarrollo del bot responde solo a fines educativos. El desarrollador del mismo deslinda toda responsabilidad por los daños y/o perjuicios que pudiere ocasionar su utilización, como así tampoco se hace responsable sobre el uso que puedan hacer terceros con la información brindada.

