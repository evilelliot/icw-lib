# Importar las librerías.
from lib.Crawler import Crawler
from lib.Downloader import Downloader
from lib.Validator import Validator

# Proveer un enlace de instagram.
link = "https://www.instagram.com/p/Bn9LJcEAP4b/?taken-by=storror"

# Creando una instancia de la clase Validator.
validate  = Validator(link)
validated = validate.Validate()

# Verificar cada uno de los enlaces en busca de enlaces invalidos.

# Creando una instancia de la clase Crawler.
crawler  = Crawler(link)
soupper  = crawler.Crawl()

# Guardar información sobre el enlace.
link     = crawler.GetLink(soupper)
account  = crawler.GetAccountname(soupper)

# Crear una instancia de la clase Downloader con los parametros de enlace y nombre del archivo a guardar.
download = Downloader(link, account)

# Usando el método de descarga e imprimiendo el resultado del proceso.
print(download.Download())	













