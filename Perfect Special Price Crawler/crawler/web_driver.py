from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# class 생성
class sel_req(object):

    # 초기값
    driver = None
    chrome_options = Options()

    # __init__ : 생성자 함수, class 객체를 생성할 때 실행됨
    # req = sel_req(chromedriver 경로, options=옵션) 객체 생성 시 __init__ 함수 실행
    def __init__(self, driver_path, options=None):

        # 초기값
        self.driver_path = driver_path

        # WebDriver를 브라우저 없이 실행 옵션 => headless / Chrome 브라우저의 로그 레벨 낮춤 옵션 = > log-level=3 / 콘솔에 로그를 남기지 않는 옵션 => disable-logging
        # Gui를 제공하지 않는 환경에서는 no-sandbox와 disable-gpu 옵션을 추가해야함. (Linux Server 환경)
        self.options = ['--headless', '--log-level=3', '--disable-logging', '--no-sandbox', '--disable-gpu']
        self.make_chrome_options(options)

        # webdriver 객체 생성
        self.driver = webdriver.Chrome(self.driver_path, options=self.chrome_options)

    # 배열에 저장된 옵션들을 webdriver options 객체로 만들어주는 함수
    def make_chrome_options(self, options):
        if options is not None:
            self.options += options

        self.chrome_options = Options()
        for opt in set(self.options):
            self.chrome_options.add_argument(opt)

    # url을 object로 받고 req를 요청하고 결과값을 return하는 함수
    # callback 매개변수는 결과값을 파싱하는 함수로 인자값 받음. callback에 response 매개변수에는 페이지가 변경된 webdriver를 인자값으로 전달.
    def get_req(self, url, callback=None):
        self.driver.get(url)
        return callback(response=self.driver)