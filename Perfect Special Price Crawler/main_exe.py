from crawler import web_driver
from crawler.special_price_parser import st11_parser
from crawler.special_price_parser import tmon_parser
from pprint import pprint
import sys

path = 'C:/Python Library/chrome_driver/chromedriver'

parser_targets = {
    "11st": {
        "url": 'http://deal.11st.co.kr/html/nc/deal/main.html',
        "parser": "st11_parser"
    },

    "tmon": {
        "url": 'http://www.tmon.co.kr/best/1',
        "parser": "tmon_parser"
    }
}

def targets_run(target):
    req = web_driver.sel_req(driver_path=path)

    info = parser_targets[target]
    print(info)

    url = info['url']
    print(url)

    # eval() 함수 : 문자열로 표현된 파이썬 식을 인수로 받아 파이썬 컴파일 코드로 변환
    # 즉, eval(info["parser"])은 문자열 "st11_parser"이 아닌 코드 st11_parser이 된다.
    callback = eval(info["parser"])
    print(callback)

    data = req.get_req(url, callback=callback)

    return data

if __name__ == '__main__':
    try:
        check = int(input("크롤링할 사이트를 선택하세요...\n1. 11번가\t/\t2. 티몬\n>>> "))

        if check == 1:
            data = targets_run("11st")
        elif check == 2:
            data = targets_run("tmon")
        else:
            print("Error!")
            sys.exit(1)

        pprint(data)
    except ValueError:
        print("Error!")
        sys.exit(1)
    except:
        pass

