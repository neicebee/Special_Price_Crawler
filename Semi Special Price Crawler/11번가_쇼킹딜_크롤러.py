from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import sys

path = "C:/Python Library/chrome_driver/chromedriver"
url = "http://deal.11st.co.kr/html/nc/deal/main.html"

chrome_options = Options()

# WebDriver를 브라우저 없이 실행 옵션 => headless
chrome_options.add_argument('--headless')

# Chrome 브라우저의 로그 레벨 낮춤 옵션 = > log-level=3
chrome_options.add_argument('--log-level=3')

# 콘솔에 로그를 남기지 않는 옵션 => disable-logging
chrome_options.add_argument('--disable-logging')
# Gui를 제공하지 않는 환경에서는 no-sandbox와 disable-gpu 옵션을 추가해야함

driver = webdriver.Chrome(path, options=chrome_options)
driver.get(url)

elements = driver.find_elements_by_css_selector("#emergencyPrd > div > ul > li")

print("상품 개수: {}".format(len(elements)))

# 상품명, 하이퍼링크, flag, 세일가, 남은 시간, 현재 구매 개수, 가격 리스트
product = []
href = []
flag = []
sale = []
time = []
count = []
price = []

for i in range(0, len(elements)-1):
    req = elements[i].get_attribute('innerHTML')
    soup = BeautifulSoup(req, 'html.parser')

    info1 = soup.find('div', {'class':'box_pd'})
    href.append(info1.a.get("href"))

    info2 = soup.find('div', {'class' : 'prd_info'})
    productcheck = info2.find_next('span', {'class': 'fs_16'})
    product.append(productcheck.text.strip())

    info3 = soup.find('div', {'class' : 'info_flag'})
    flagcheck = info3.text.strip()
    flag.append(flagcheck)

    info4 = soup.find('span', {'class' : 'chgTime'})
    timecheck = info4.text.strip()
    time.append(timecheck)

    info5 = info2.find_next('span', {'class' : 'price_detail'})
    pricecheck = info5.text.strip()
    price.append(pricecheck)

    info6 = soup.find('div', {'class' : 'price_info'})
    classcheck = info6.span.get('class')

    if classcheck[0] == "sale":
        sale.append(info6.span.text.strip())
    elif classcheck[0] == "sp_price":
        sale.append(info6.span.text.strip())

    info7 = soup.find('span', {'class' : 'puchase_num'})
    countcheck = info7.text.strip()
    count.append(countcheck)

if len(product) == len(href) == len(flag) == len(sale) == len(time) == len(count) == len(price):
    for i in range(0, len(product)):
        print("11번가 쇼킹딜 긴급공수 {}번째 상품".format(i+1))
        print("상품명: " + product[i])
        print("상품 flag: " + flag[i])
        print("가격: " + price[i])
        print("쇼킹딜: " + sale[i])
        print("현재까지 구매 개수: " + count[i])
        print("남은 시간: " + time[i])
        print("링크: " + href[i])
        print("================================")

    driver.close()
else:
    print("Error!")
    driver.close()
    sys.exit(1)