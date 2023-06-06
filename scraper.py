from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/p/pl?d=gpu"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
strong = []

for i in range(len(prices)):    
    priceParent = prices[i].parent
    strong.append(priceParent.find("strong").string)

cardName = doc.find_all(class_="item-open-box-italic")
gpuName = []

for i in range(len(cardName)):
    name = cardName[i].parent
    gpuName.append(name.text.strip())
    
for i in range(len(gpuName)):
        print(f'Gpu Description: {gpuName[i]}\nPrice: ${strong[i]}\n')