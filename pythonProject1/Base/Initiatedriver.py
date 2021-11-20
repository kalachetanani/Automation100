from selenium.webdriver import Chrome
from Library import Configreader


def startbrowser():
    global driver
    if(Configreader.readconfigdata('details','Browser'))=='Chrome'):
        path = "C:\\kalafolder\\chromedriver.exe"
        driver=Chrome(executable_path=path)
    elif(Configreader.readconfigdata('details','Browser'))=='Firefox'):
        path = "C:\\kalafolder\\geckodriver.exe"
        driver=Firefox(executable_path=path)
    else:
        path = "C:\\kalafolder\\chromedriver.exe"
        driver = Chrome(executable_path=path)
    driver.get(Configreader.readconfigdata('details','URL'))
    return driver





