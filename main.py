from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from win10toast import ToastNotifier

# Connect to local Chrome instance with imported Metamask wallet
option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
element = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div[2]/div[2]/span/div[5]/div[3]"
                                    "/div/p"))
)

# desktop notification init
toaster = ToastNotifier()
LastPrice = ''
while True:
    if element.text != '0' and element.text != LastPrice:
        LastPrice = element.text
        toaster.show_toast("MIM Availability Alert", "Number of MIM available: "
                           + element.text, threaded=True, icon_path=None, duration=10)


