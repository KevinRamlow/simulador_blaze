from selenium.webdriver.common.by import By

def get_data(driver, url):
    driver.get(url)
    multiplier_dict = {}

    for page in range(0, 50):
        history = driver.find_element(By.ID, 'history')
        multiplier_dict['page'] = history.find_elements(By.CLASS_NAME, 'bet-amount')
        
        driver.find_element(By.XPATH, '//*[@id="crash-analytics"]/div[2]/div[2]/div/div/button[2]').click()

        page += 1

    return multiplier_dict