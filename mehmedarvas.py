from selenium import webdriver;
from selenium.webdriver.support.ui import Select;

driver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe";
driver = webdriver.Chrome(executable_path=driver_path);


driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account");




email = input ("Enter your email address: ");


inputElement = driver.find_element_by_id("email_create");

inputElement.send_keys(email);






inputElement.submit() 

import time 
time.sleep(4)

inputElement1 = driver.find_element_by_name("customer_firstname");
inputElement1.send_keys("testname");


inputElement2 = driver.find_element_by_name("customer_lastname");
inputElement2.send_keys("testlastname");


inputElement3 = driver.find_element_by_name("passwd");
inputElement3.send_keys("test123");


inputElement4 = driver.find_element_by_name("address1");
inputElement4.send_keys("marmara mah 4h 7");



inputElement5 = driver.find_element_by_name("city");
inputElement5.send_keys("Istanbul");


select = Select(driver.find_element_by_id('id_state'))

select.select_by_value('5');

inputElement6 = driver.find_element_by_name("postcode");
inputElement6.send_keys("92630");

inputElement7 = driver.find_element_by_name("phone_mobile");
inputElement7.send_keys("5055135116");

inputElement8 = driver.find_element_by_name ("submitAccount")
inputElement8.click();



import time 
time.sleep(3)


driver.get("http://automationpractice.com/index.php?id_category=5&controller=category");


import time 
time.sleep(3)

driver.get("http://automationpractice.com/index.php?id_product=1&controller=product");


import time 
time.sleep(3)

inputElement9 = driver.find_element_by_name ("Submit")
inputElement9.click();


import time 
time.sleep(3)

driver.get("http://automationpractice.com/index.php?controller=order");

import time 
time.sleep(3)

driver.get("http://automationpractice.com/index.php?controller=order&step=1");


import time

time.sleep(3)


inputElement10 = driver.find_element_by_name("processAddress");
inputElement10.click();


import time 
time.sleep(3)

inputElement11 = driver.find_element_by_name ("cgv")
inputElement11.click();





driver.get("http://automationpractice.com/index.php?fc=module&module=cheque&controller=payment");


import time 
time.sleep(3)


driver.find_element_by_xpath("//*[text()='I confirm my order']").click();
















