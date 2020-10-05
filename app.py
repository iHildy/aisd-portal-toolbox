from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


#input username and password.
username = input("Username:")
password = input("Password:")

class Login:

    #replace "C:/webdrivers/Chromedriver.exe" with the path to your webdriver.
    #webdriver.Chrome can be replaced with any other webdriver you would prefer to use.
    driver = webdriver.Chrome(executable_path=r"C:/webdrivers/Chromedriver.exe")
    driver.get("https://portal.austinisd.org")
    sleep(1)
    driver.find_element_by_xpath("//*[@id='identification']").send_keys(username)
    driver.find_element_by_xpath("//*[@id='authn-go-button']").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@id='ember525']").send_keys(password)
    driver.find_element_by_xpath("//*[@id='authn-go-button']").click()
    sleep(3)
    driver.find_element_by_xpath('//*[@id="ember1165"]').click()
    sleep(.5)
    driver.find_element_by_xpath('//*[@id="ember1167"]').click()
    sleep(3.5)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
    
    
    #hitting enter will close off your program. Will not check for enter unless you are in the command console/python window.
    input("Close Program")



Login()
