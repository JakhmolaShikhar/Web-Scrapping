from selenium import webdriver, By


driver = webdriver.Chrome();
driver.get('https://amazon.com');


driver.implicitly_wait(5);
driver.find_element(By.id, )