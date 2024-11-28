# 🐍 Repositorio de Monitoreo de Estado de URL

Este repositorio contiene un par de scripts en Python que permiten monitorear el estado de una URL específica. Utiliza la biblioteca `requests` para realizar solicitudes HTTP y verificar si la página está disponible o no.

## 📁 Archivos del Repositorio

- `main.py`: Archivo principal que ejecuta el ciclo de monitoreo.
- `req.py`: Contiene la función que realiza la solicitud HTTP y verifica el estado de la URL.

## 📜 Descripción de los Archivos

### `main.py`

Este archivo es el núcleo del programa. Ejecuta un bucle infinito que llama a la función `send()` cada 2 segundos, con un intervalo de 1 segundo entre cada llamada. Si ocurre un error durante la ejecución, se captura y se imprime en la consola.

```python
from search import *
import time

exe = True
try:
    while exe:
        time.sleep(1)
        send()
        time.sleep(2)
except Exception as e:
    print(f"Error: {e}")
```
### `req.py`

Este archivo contiene la función send(), que realiza una solicitud GET a la URL especificada. Dependiendo del código de estado de la respuesta, imprime si la URL fue encontrada o no.

```python
import requests

url = "https://www.vicinityclo.de/products/akimbo-lows-pristina-moss"

def send():
    res = requests.get(url)
    status = res.status_code
    print(res)
    if status == 404:
        print("NO encontrado")
    elif status == 200:
        print("Encontrado")
```
## 🚀 Cómo Ejecutar el Proyecto
#### 1. Clona este repositorio en tu máquina local:
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
```
#### 2. Navega al directorio del repositorio:
```bash
cd ReqScript
```
#### 3. Asegúrate de tener instalada la biblioteca requests. Si no la tienes, puedes instalarla usando pip:
```bash
pip install requests
```
#### 4. Ejecuta el archivo main.py:
```bash
python main.py
```

## ⚠️ Advertencias
- El script está diseñado para ejecutarse indefinidamente. Asegúrate de tener un mecanismo para detenerlo si es necesario (como Ctrl+C).
- Asegúrate de respetar los términos de servicio del sitio web que estás monitoreando.

## 📄 Licencia
Este proyecto está bajo la Licencia MIT.

## 🤝 Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, no dudes en abrir un issue o enviar un pull request.
