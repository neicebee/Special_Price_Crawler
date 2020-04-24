from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import sys

path = "C:/Python Library/chrome_driver/chromedriver"
url = "http://www.tmon.co.kr/best/1"

chrome_options = Options()

chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(path, options=chrome_options)
driver.get(url)

elements = driver.find_elements_by_css_selector("#_dealList > li")

print("상품 개수: {}".format(len(elements)))

for i in range(0, len(elements)):
    req = elements[i].get_attribute('innerHTML')
    soup = BeautifulSoup(req, 'html.parser')

    price = ""

    link = soup.a.get('href')

    info1 = soup.find('p', {'class' : 'title_name'})
    product = info1.text.strip()

    info2 = soup.find('div', {'class' : 'grade_average'})
    star = info2.get('aria-label')

    info3 = soup.find('span', {'class' : 'price'})
    pricecheck = info3.text.split()

    for j in range(0, len(pricecheck)):
        price = price + pricecheck[j] + " "

    info4 = soup.find('span', {'class' : 'buy_count'})
    count = info4.text.strip()

    print("No: {}".format(i+1))
    print("상품명: " + product)
    print("가격: " + price)
    print("평점: " + star)
    print("구매 개수: " + count)

    driver.close()
