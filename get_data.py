from selenium.webdriver.common.by import By
from time import sleep

def get_data(driver, url):
    driver.get(url)
    multiplier_list = []
    history = driver.find_element(By.ID, 'history')

    for page in range(0, 20):
        multiplier_dict = history.find_elements(By.CLASS_NAME, 'bet-amount')
        
        for element in multiplier_dict:
            element = (element.text)
            multiplier_list.append(element)
            

        driver.find_element(By.XPATH, '//*[@id="crash-analytics"]/div[2]/div[2]/div/div/button[2]').click()
        sleep(3.5)
        page += 1 

    return multiplier_list