# Importar las librerías.
from lib.Crawler import Crawler
from lib.Downloader import Downloader
from lib.Validator import Validator

# Proveer enlaces de instagram.
a = "https://www.instagram.com/p/Bn9LJcEAP4b/?taken-by=storror"
b = "https://www.instagram.com/p/BntALsFBiXy/?taken-by=storror"
c = "https://www.instagram.com/p/Bln3enCgVX6/?taken-by=callumstorror"
d = "https://www.instagram.com/p/BlqXFKqgIpB/?taken-by=callumstorror"
# Creamos un array con los enlaces que queremos anotar.
links  = (a, b, c, d)


# Creamos una función en pro de tener todo un poco más ordenado.
def MultiDownload(array):
	# Iterar cada index del argumento array-
	for link in array:
		# Creando una instancia de la clase Validator.
		validate  = Validator(link)
		validated = validate.Validate()

		# Verificar cada uno de los enlaces en busca de enlaces invalidos.
		if validated == True:
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
		else: 
			print("¡Enlace invalido!")
pass

# Probando la función.
MultiDownload(links)










