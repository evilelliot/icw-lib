# icw-lib
[![PyPI version](https://badge.fury.io/py/icw-lib.svg)](https://badge.fury.io/py/icw-lib)

Libreria python creada para descargar datos de una fotografía de Instagram.


## Instalación 
Para instalar la última versión desde [PyPi](https://pypi.org/manage/project/icw-lib/), utiliza:
```
pip3 install icw-lib
```

O instala la última versión manualmente desde Github:
```
git clone https://github.com/Haneawa/icw-lib
cd icw-lib
python setup.py install
```

## Uso básico
```python
from icw-lib.Crawler import Crawler
from icw-lib.Download import Download
from icw-lib.Validator import Validator
 
# Crea las instancias de las clases importadas
validator = Validator()
crawler   = Crawler()
download  = Download()

# Crea una variable con el enlace de Instagram.
link = "https://www.instagram.com/p/Bl7-bMwgSNn/"

# Valida el enlace utilizando un método de la clase Validator.
validated = validator.Validate(link)
if validated is True:
  # Comienza el procesado del enlace y su posterior descarga.
  process = crawler.Crawl(link)
  
  # Puedes obtener los siguientes datos directo del enlace.
  link    = crawler.GetLink(process)
  account = crawler.GetAccountname(process)
  
  # Inicia la descarga con el método download de la clase Download.
  # La imagen se habrá descargado en el directorio por defecto (images).
  download.Download(link, account)
  
 else:
  print("¡El link no es valido!")
  
```

## Clases
| Nombre de clase | Descripción simple | 
| :---            | :---               |
| Download        | Realiza la conexión con el codigo fuente y guarda la información requerida. |
| Validator       | Valida los enlaces mediante la comparación con una expresión regular. |
| Crawler | Obtiene el código fuente y lo filtra según los requerimentos dados. |

### Download Class
| Nombre del método | Sintaxis de método | Argumentos requeridos | Descripción |
| :--- | :--- | :--- | :--- |
| Download | *Downloader()* | **string** (link de la imagen) | Inicializador de la clase. |
| Download* | *Download()* | **null** (no requiere) | Método de descarga del enlace, utiliza el enlace provisto en la creación de la instancia. |
| Saver | *Saver()* | **null** (no requiere) | Este método maneja el nombre del archivo y evita una sobreescritura renombrando sí se da el caso. |
| Sufix | *AddSufix()* | **null** (no requiere) | Método que añade un subfijo de archivo al filename. |

> *Download: hace referencia a el nombre duplicado, pertenece un método de la clase con el mismo nombre.


### Validator Class
| Nombre del método | Sintaxis de método | Argumentos requeridos | Descripción |
| :--- | :--- | :--- | :--- |
| Validator | *Validator()* | **string** (link de la imagen) | Inicializador de la clase. |
| Validate | *Validate()* | **null** (requiere) | Valida si el enlace proviene de una imagen de Instagram mediante el match con una expresión regular. |


### Crawler Class
| Nombre del método | Sintaxis de método | Argumentos requeridos | Descripción |
| :--- | :--- | :--- | :--- |
| Crawler | *Crawler()* | **string** (link de la imagen) | Inicializador de la clase crawler. |
| Crawl | *Crawl()* | **null** (no requiere) | Obtiene el codigo fuente directo del enlace provisto en el constructor de la clase crawler. |
| Get link | *GetLink()* | **BeautifulSoup plain text** (código fuente del enlace) | Filtra la información que contiene el código fuente y encuentra el link a la página web que contiene la imagen solamente. |
| Get account name | *GetAccountname()* | **BeautifulSoup plain text** (código fuente del enlace) | Filtra la información que contiene el código fuente y encuentra el nombre de la cuenta solamente. |



## Requerimientos.
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![BeautifulSoup](https://badge.fury.io/py/BeautifulSoup.svg)](https://badge.fury.io/py/BeautifulSoup)
