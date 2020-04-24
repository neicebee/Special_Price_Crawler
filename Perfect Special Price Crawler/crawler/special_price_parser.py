from bs4 import BeautifulSoup

# response : webdriver가 get한 페이지
def st11_parser(response=None):
    datas = list()

    # 11번가 쇼킹딜 요소 css_selector로 찾기
    elements = response.find_elements_by_css_selector("#emergencyPrd > div > ul > li")

    print("상품 개수: {}".format(len(elements)))

    # 상품명, 하이퍼링크, flag, 세일가, 남은 시간, 현재 구매 개수, 가격 저장 후 dict화
    for i in range(0, len(elements) - 1):
        req = elements[i].get_attribute('innerHTML')
        soup = BeautifulSoup(req, 'html.parser')

        info1 = soup.find('div', {'class': 'box_pd'})
        href = info1.a.get("href")

        info2 = soup.find('div', {'class': 'prd_info'})
        productcheck = info2.find_next('span', {'class': 'fs_16'})
        product = productcheck.text.strip()

        info3 = soup.find('div', {'class': 'info_flag'})
        flagcheck = info3.text.strip()
        flag = flagcheck

        info4 = soup.find('span', {'class': 'chgTime'})
        timecheck = info4.text.strip()
        time = timecheck

        info5 = info2.find_next('span', {'class': 'price_detail'})
        pricecheck = info5.text.strip()
        price = pricecheck

        info6 = soup.find('div', {'class': 'price_info'})
        classcheck = info6.span.get('class')

        if classcheck[0] == "sale":
            sale = info6.span.text.strip()
        elif classcheck[0] == "sp_price":
            sale = info6.span.text.strip()
        else:
            sale = None

        info7 = soup.find('span', {'class': 'puchase_num'})
        countcheck = info7.text.strip()
        count = countcheck

        data = {
            "no" : i+1,
            "product" : product,
            "flag" : flag,
            "price" : price,
            "sale" : sale,
            "count" : count,
            "time" : time,
            "href" : href
        }

        datas.append(data)

    response.close()

    return datas

def tmon_parser(response=None):
    datas = list()

    elements = response.find_elements_by_css_selector("#_dealList > li")

    print("상품 개수: {}".format(len(elements)))

    for i in range(0, len(elements)):
        req = elements[i].get_attribute('innerHTML')
        soup = BeautifulSoup(req, 'html.parser')

        price = ""

        link = soup.a.get('href')

        info1 = soup.find('p', {'class': 'title_name'})
        product = info1.text.strip()

        info2 = soup.find('div', {'class': 'grade_average'})
        star = info2.get('aria-label')

        info3 = soup.find('span', {'class': 'price'})
        pricecheck = info3.text.split()

        for j in range(0, len(pricecheck)):
            price = price + pricecheck[j] + " "

        info4 = soup.find('span', {'class': 'buy_count'})
        count = info4.text.strip()

        data = {
            "no" : i+1,
            "product" : product,
            "price" : price.strip(),
            "star" : star,
            "count" : count,
            "link" : link
        }

        datas.append(data)

    response.close()

    return datas