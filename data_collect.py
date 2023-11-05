from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)
base_url = "https://zakupki.okmot.kg/popp/view/order/list.xhtml"

all_data = []

try:
    driver.get(base_url)
    
    while True:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tr[class^="ui-widget-content"]')))

        rows = driver.find_elements(By.CSS_SELECTOR, 'tr[class^="ui-widget-content"]')
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, 'td')
            row_data = [col.text for col in cols]
            all_data.append(row_data)
        
        next_page_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.ui-paginator-next')))
        if "ui-state-disabled" in next_page_btn.get_attribute("class"):
            break
        else:
            next_page_btn.click()
            time.sleep(2)
        
        print(f"Обработана страница {len(all_data) // 10}")
finally:
    driver.quit()

df = pd.DataFrame(all_data)  
df.to_excel('tenders.xlsx', index=False)

