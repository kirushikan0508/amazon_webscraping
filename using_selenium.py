import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()

search_box= driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("dell laptop")
driver.find_element(By.ID, "nav-search-submit-button").click()

driver.find_element(By.XPATH, "//span[text()='Dell']").click()

laptop_name = []
laptop_price= []
laptop_reviews=[]


#allitem
all_products= driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

for product in all_products:
    #name
    names = product.find_elements(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
    for name in names:
        laptop_name.append(name.text)

    #price
    prices= product.find_elements(By.XPATH, ".//span[@class='a-price-whole']")
    for price in prices:
        laptop_price.append(price.text)

    #review
    try:
        if len(product.find_elements(By.XPATH,".//span[@class='a-price-whole']"))>0:
            prices= product.find_elements(By.XPATH,".//span[@class='a-price-whole']")
            for price in prices:
                # print('the lenght is ===>',len(price.text))
                laptop_price.append(price.text)
        else:
            laptop_price.append("0")
    except:
        pass
    




print('name=', len(laptop_name))
print('price=', len(laptop_price))
print('review=', len(laptop_reviews))