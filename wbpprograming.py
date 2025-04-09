import threading
import requests
import time



urls=[
      "http://www.exmple.com",
      "http://www.python.org",
      "http://www.wikipedia.org"
      ]
def page(url):  
    print (f"dowloding {url}")
    try:
        responce=requests.get(url)
        print (f"finish {url}- satas:{responce.status_code}Bytes:{len(response.content)}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=page, args=(url,))
    t.start()
    threads.append(t)
for t in threads:
 t.join()

 print(f"All downloads completed  {round(time.time() - start, 2)}seconds.") 
