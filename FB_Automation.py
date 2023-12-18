from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.command import Command
from selenium .webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep


s = Service("C:\\Users\\USER\\Desktop\\Karan_MINI_PROJECT\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
Browser = driver.get("https:www.facebook.com/")
driver.maximize_window()
print("opened Facebook.com")
print("            ")
sleep(2)

#entering the USERNMAE and PASSWORD
Username = driver.find_element(By.ID,"email").send_keys("9150213477")
print("Entered E-mail ID")
print("            ")
sleep(2)

Password = driver.find_element(By.ID,"pass").send_keys("Karan2424")
print("Entered password")
print("            ")
sleep(2)

Button = driver.find_element(By.NAME,"login").click()
print("logged into the facebook")
print("            ")
print("Login Successfull!!!!")
sleep(2)

#navigate the Browser in Facebook to the Birthday Events

driver.get("https:www.facebook.com/events/birthdays/")
print("            ")
print("Brthday Events!!")
sleep(2)



#To Find  The Today's BirthdayList
birthday_container = driver.find_element(By.CSS_SELECTOR,".xyamay9 ")
birthdayList = birthday_container.find_elements(By.CSS_SELECTOR,'.xamitd3')
print("            ")
print(birthdayList)
print("            ")
print("accessed")

person = 0
birthday_person={}
try:
       for b in birthdayList:
                name = b.find_element(By.TAG_NAME,"h2")
                print(name)
                print("            ")

                age = b.find_element(By.CSS_SELECTOR,".xo1l8bm")
                print(age)
                print("            ")

       
                birthday_person[person]= {'name ':name.text , 'age ':age.text}
                person = person+1


                textBox = b.find_element(By.CSS_SELECTOR,"p.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8")
                wish = " Happy Birthday!!! "
                textBox.send_keys(wish)
                sleep(5)
                textBox.send_keys(Keys.ENTER)

                
                print("            ")
                print(birthday_person)
                print("            ")
                print(" Message Sended Successfully !!")
      
     

except NoSuchElementException :
       print("there is no birthday today")

       
