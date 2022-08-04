from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#opens google chrome and removes the accept all button
driver = webdriver.Chrome("/Users/aarabi_d/Downloads/chromedriver-4")
driver.get("https://www.google.com")
time.sleep(3)
button = driver.find_element(By.ID, "L2AGLb")
#only clicks on the button if it is there
if button: 
    button.click()

#list of phrases, here only three as example but can also contain 100 phrases    
phrases = ["Amazon Ratenzahlung", "Amazon Rechnungskauf", "Asos Ratenzahlung", "H&M Ratenzahlung", "Mediamarkt Ratenzahlung"]
for phrase in phrases:
    driver.get("https://www.google.com")
    time.sleep(3)
    
    #finds the search tab, clears it and enters the phrases in the order of the list
    elem = driver.find_element(By.NAME, 'q')
    elem.clear()
    elem.send_keys(phrase)
    elem.send_keys(Keys.RETURN)

    #assert "No results found." not in driver.page_source
    #div is a block element and contains the url link("a") and the headtitle ("h3")
    time.sleep(3)
    div_a = driver.find_element(By.XPATH, "//div[@class='yuRUbf']/a")
    div_h3 = driver.find_element(By.XPATH, "//div[@class='yuRUbf']/a/h3") 
    
  
    print(phrase + "---") #adding this line is more clear and seperates the different phrases
    print(div_h3.text) #prints the headline
    print(div_a.get_attribute("href")) #prints the link and href specifies the URL of the page
    
 
time.sleep(5)
driver.close()

