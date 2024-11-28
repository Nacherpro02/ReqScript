import requests

url = "https://www.vicinityclo.de/products/akimbo-lows-pristina-moss"
url2 = "https://www.vicinityclo.de/products/akimbo-lows-asphalt-black?variant=49460835942666"
def send():
   res = requests.get(url)
   status = res.status_code
   print(res)
   if status == 404:
      print("NO encontrado")
   elif status == 200:
      print("Encontrado")
