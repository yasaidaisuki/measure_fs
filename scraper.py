from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://peqdb.com/graphs/?share=PEQdB_Target") # loading webpage

action = ActionChains(driver)

try:
    responses = driver.find_elements(
        By.XPATH, "(//*[contains(@class, 'phone-item')])[position() <= 5]"      # limit certain scraping
    ) 
    
    len_responses = len(responses)

    for response in responses:
        response.click()

        # download button
        dload = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'button-saveSquig')]")))

        wait = WebDriverWait(driver, 20) # wait for time to load

        dload.click()
except Exception as e:
    print("error: ", e)


driver.quit()
