![alt text](https://secure.meetupstatic.com/photos/event/b/3/e/e/highres_494806062.jpeg)

[![PyPI](https://img.shields.io/pypi/v/virtualenv?style=flat-square)](https://pypi.org/project/virtualenv)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/virtualenv?style=flat-square)](https://pypi.org/project/virtualenv)
![Python Versions](https://img.shields.io/badge/Python-3.7-green.svg)
![Ubuntu](https://img.shields.io/badge/Ubuntu-18.04-blue.svg)
[![PyPI - License](https://img.shields.io/pypi/l/virtualenv?style=flat-square)](https://opensource.org/licenses/MIT)


# Meetup Analytics & Python 3 de Marzo: Bases para operacionalizar un modelo de ML

El siguiente repositorio contiene el código fuente oficial de la charla ***Bases para operacionalizar un modelo de ML***, dictada el día 03-03-2021 para la comunidad. La información oficial del evento se encuentra en el siguiente [link](https://www.meetup.com/Analytics-y-Python/events/276446885/).


## Herramientas utilizadas

El proyecto general se montó en el OS Ubuntu v18.04 LTS, en una VM levantada en AWS (t2.micro).

Para llevar a cabo los scrapers se utilizó Python v3.7, y creación de un ambiente virtual usando [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

En el caso de simular el navegador web para realizar el scraping interactivo se utilizó selenium, con [Chromium](https://chromedriver.chromium.org/).

Para el procesamiento de imágenes se utilizó la API de [Tesseract](https://github.com/tesseract-ocr/tesseract/wiki) en Python.


## Descripción del contenido

La configuración del ambiente virtual de Python para la replicabilidad de los resultados exhibidos se encuentra en el archivo [requirements.txt](https://github.com/moebius-analitica/meetup-webscraping/edit/master/requirements.txt)

Para aquellos que quieran obtener los datos de forma inmediata, tenemos disponible el siguiente repositorio [Drive](https://drive.google.com/drive/folders/1WRNEnmRX9uDpkg7SyhW2gd5pplM4FRA4?usp=sharing) para que accedan de forma libre.

## Estructura del repositorio

En primer lugar, realizamos la descarga de los archivos provenientes de la Dirección del Trabajo: [Nómina de empresas acogidas a la Ley 21.227](https://www.dt.gob.cl/portal/1626/w3-article-118613.html). Para este ejercicio, se utilizaron los documentos asociados a las nóminas de empresas acogidas a la "Reducción de Jornada". No obstante, el script recoge todos las nóminas. Para esto se ocupa el código [downloadDocs.py](https://github.com/moebius-analitica/meetup-webscraping/blob/master/src/downloadDocs.py)

Posteriormente, se realiza la transformación de los documentos en datos mediante el uso de [tabula-py](https://pypi.org/project/tabula-py/). El código que realiza esta transformación es [pdfToData.py](https://github.com/moebius-analitica/meetup-webscraping/blob/master/src/pdfToData.py).

Ahora, para ir nutriendo la información obtenida anteriormente, se realizan scrapers [Situación tributaria de Terceros del SII](https://zeus.sii.cl/cvc/stc/stc.html) y [Consulta pública de multas ejecutoriadas](https://ventanilla.dirtrab.cl/RegistroEmpleador/consultamultas.aspx). Para este último, el código es [multaScraper.py](https://github.com/moebius-analitica/meetup-webscraping/blob/master/src/multaScraper.py).

Y a modo de complementaridad, se disponibilizan demos para bypassear captchas numéricos mediante los métodos [SIIDemo.py](https://github.com/moebius-analitica/meetup-webscraping/blob/master/src/SIIDemo.py) y [tessDemo.py](https://github.com/moebius-analitica/meetup-webscraping/blob/master/src/tessDemo.py), con sus respectivas configuraciones.

Toda esta masividad de datos da la oportunidad para que cada uno de Uds. pueda realizar sus análisis. Así que, ¡A jugar!

## Autoría

* **Moebius Analítica** - [Webpage](https://www.moebius-analitica.cl/)
