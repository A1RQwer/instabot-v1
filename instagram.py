from selenium import webdriver
from helium import *
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import os
#collor print
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def instagram(): #This is loading browser
    global ig
    choption = webdriver.ChromeOptions()
    choption.add_argument("lang=en-US")
    choption.add_argument("--start-fullscreen")
    ig = start_chrome(options=choption)
    ig.get("https://www.instagram.com")
    wait_until(Text("Allow the use of cookies from Instagram on this browser?").exists)
    click("Only allow essential cookies")
    ig.find_element(By.CLASS_NAME, value="_9dls").send_keys(F11)

def login(): #This is login
    global name,passw
    name = input(bcolors.OKBLUE+"Put you're username:")
    passw = input(bcolors.OKBLUE+"Put you're password:")
    ig.find_element(By.CSS_SELECTOR, value="input[name='username']").send_keys(name)
    ig.find_element(By.CSS_SELECTOR, value="input[name='password']").send_keys(passw)
    sleep(6)
    ig.find_element(By.XPATH, value="//div[contains(text(),'Log in')]").click()

def goodlog(): #verifi login, if text password incorrect
    sleep(2)
    if Text("Sorry, your password was incorrect. Please double-check your password.").exists():
        print(bcolors.FAIL+"You¸re put bad login details!!")
        print(bcolors.WARNING+"Now loading again login")
        ig.refresh()
        login()

def loadingacc():
    sleep(0.6)
    wait_until(Text("Save Your Login Info?").exists)
    click("Not Now")
    
    click("Not Now")
    print(bcolors.OKGREEN+"Logged")

def action(aktiv):
    if aktiv=="1":#acc info
        ig.find_element(By.CSS_SELECTOR, value=".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._aak1._a6hd").click()
        wait_until(Text("Edit profile").exists)
        posts = ig.find_element(By.CSS_SELECTOR, value="body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(2) > main:nth-child(2) > div:nth-child(1) > header:nth-child(1) > section:nth-child(2) > ul:nth-child(3) > li:nth-child(1) > div:nth-child(1)").text
        followers= ig.find_element(By.CSS_SELECTOR, value="body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(2) > main:nth-child(2) > div:nth-child(1) > header:nth-child(1) > section:nth-child(2) > ul:nth-child(3) > li:nth-child(2) > a:nth-child(1) > div:nth-child(1)").text
        following = ig.find_element(By.CSS_SELECTOR, value="body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(2) > main:nth-child(2) > div:nth-child(1) > header:nth-child(1) > section:nth-child(2) > ul:nth-child(3) > li:nth-child(3) > a:nth-child(1) > div:nth-child(1)").text
        print(posts+" "+followers+" "+following)
        print(bcolors.OKGREEN+"Complete")
        ig.get("https://www.instagram.com")
    
    if aktiv=="2": #follow
        see_all = ig.find_element(By.XPATH, value="//div[@class='_aacl _aacn _aacw _aacx _aad6']").click()
        n = int(input(bcolors.OKBLUE+"Koľko ľudí chceš sledovať?"+" 10-100:"))
        wait_until(Text("Suggested").exists)
        with open("following_list.txt", "a") as f:
            for x in range(n):
                sleep(3)
                user = ig.find_element(By.CSS_SELECTOR, value="body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1) > span:nth-child(1) > div:nth-child(1)").text
                f.write('\n'+user)
                print(bcolors.HEADER+user+" start followed")
                follow = ig.find_element(By.CSS_SELECTOR, value="body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
                ig.refresh()
            f.close()
        print(bcolors.OKGREEN+"Complete")
    ig.get("https://www.instagram.com")
    
    if aktiv=="3": #unfollow
        if Text("Suggestions For You").exists():
            ig.find_element(By.CSS_SELECTOR, value=".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._aak1._a6hd").click()
            wait_until(Text("Edit profile").exists)
            click("following")
            wait_until(Text("People").exists)
            with open("Unfollowing_list.txt", "a") as g:
                j= int(input("How much you unfollow:"))
                for i in range(j):
                    
                    sleep(3)
                    a = ig.find_element(By.CSS_SELECTOR, value="body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1) > span:nth-child(1) > div:nth-child(1)").text
                    ig.find_element(By.CSS_SELECTOR, value="body > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)").click()
                    if Text("Unfollow").exists():
                        click("Unfollow")
                    print(bcolors.HEADER+a+" unfollowed")
                    g.write("\n"+a)
                    ig.refresh()
                g.close()
            ig.get("https://www.instagram.com")
        print(bcolors.OKGREEN+"Completed")
def welcome():
    print(bcolors.HEADER+"This is demo. Have action follow, unfollow and acc information")
    sleep(2)
    print(bcolors.OKBLUE+"For more info")
    sleep(2)
    print(bcolors.OKCYAN+"contact me on instagram")
    sleep(2)
    print(bcolors.WARNING+"pyth.onsk")

welcome()                     
instagram()
login()
goodlog()
loadingacc()

for i in range(5):
    if __name__=="__main__":
        action(input(bcolors.OKBLUE+"put number 1.account info 2.follow, 3=unfollow:"))



    
            
