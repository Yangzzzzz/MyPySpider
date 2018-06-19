from selenium import webdriver

if __name__ == '__main__':
    brower = webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver_win32/chromedriver.exe')
    brower.get("https://www.baidu.com")
    key = brower.find_element_by_id('kw')
    key.send_keys('Python')
    key.send_keys('\ue007')
    print(brower.page_source)