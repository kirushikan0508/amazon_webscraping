import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("dell laptops")
driver.find_element(By.ID, "nav-search-submit-button").click()

driver.find_element(By.XPATH, "//span[text()='Dell']").click()

laptops = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

final_list = []

for laptop in laptops: 
    # name
    try:
        name = laptop.find_element(By.XPATH, ".//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']").text
    except:
        name = "N/A"
    
    # price
    try:
        price = laptop.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
    except:
        price = "0"
    
    # reviews
    try:
        review = laptop.find_element(By.XPATH, ".//span[@class='a-size-base s-underline-text']").text
    except:
        review = "0"
    
    # append structured data
    final_list.append({
        "Name": name,
        "Price": price,
        "Reviews": review
    })

# save to JSON file
with open("amazon_dell_laptops.json", "w", encoding="utf-8") as f:
    json.dump(final_list, f, indent=4, ensure_ascii=False)

print("✅ Data saved to amazon_dell_laptops.json")
