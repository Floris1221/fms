from selenium import webdriver
import sys,time,random, getpass
from menu import User
from selenium.webdriver.common.keys import Keys



def findByXpath(xpath):
    global driver
    element = driver.find_elements_by_xpath(xpath)
    while len(element) == 0:
        time.sleep(1)
        element = driver.find_elements_by_xpath(xpath)
    return element[0]


def log_in():
    print("Enter login")
    login = input()
    print("Enter Pasword")
    password = getpass.getpass()
    global user
    user = User(login, password)
    print("enter to whom you want to send message")
    addressee = input()
    user.to_whom(addressee)
    print("How many message you want to send")
    try:
        nbr = int(input())
        user.numbers_of_message(nbr)
    except:
        print("Format error")
    user.message()

try:
    log_in()

    driver = webdriver.Chrome()
    url = "https://www.facebook.com/"
    driver.get(url)
    time.sleep(1)


    # zaakceptowanie
    findByXpath('/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]').click()
    time.sleep(random.randint(2, 4))
    # wpisanie loginu
    findByXpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys(user.login)
    time.sleep(random.randint(2, 4))
    # wpisanie hasła
    findByXpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys(user.pasword)
    time.sleep(random.randint(2, 4))
    #wciśnięcie zaloguj
    findByXpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
    time.sleep(random.randint(2,4))
    #wciśniecie szukaj w messanger
    findByXpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/span/div/div[2]/div/div[2]/div/div/div/span[2]/div/div').click()
    time.sleep(random.randint(2,4))
    #wybranie do kogo
    findByXpath('/html/body/div[1]/div/div[1]/div/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]/div/div/label/input').send_keys(user.addressee)
    time.sleep(random.randint(2,4))
    #wybranie 1 z listy
    driver.get(findByXpath('/html/body/div[1]/div/div[1]/div/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div/div[1]/ul/li[1]/ul/li[1]/div/a').get_attribute('href'))
    time.sleep(random.randint(2,4))
    #wpisanie wiadomości
    for i in range(user.nbr):
        findByXpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div').send_keys(user.list_of_message[i]+Keys.ENTER)
        time.sleep(random.randint(2,4))
except Exception as e:
    print("Błąd logowania")
driver.close()
sys.exit()