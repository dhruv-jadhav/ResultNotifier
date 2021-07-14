from selenium import webdriver

def Scrape():
    driver_path = "C:/Users/dhruvjadhav/PycharmProjects/chromedriver.exe"
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    option.add_argument("--incognito")
    option.add_argument("--headless")
    option.add_argument("--log-level=3")


    # Create new Instance of Chromed
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
    browser.get("https://cbseresults.nic.in/CBSEResults/Page/Page?PageId=19&LangId=P")
    result = browser.find_elements_by_xpath("//a[contains(text(), 'CENTRAL TEACHER ELIGIBILITY TEST (CTET) JANUARY - 2021')]")

    if len(result) > 0:
        link = result[0].get_attribute('href')
        return True, link
    else:
        print("Gotta wait for more time")
        return False


print(Scrape())
