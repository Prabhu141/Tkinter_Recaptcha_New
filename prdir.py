# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 10:01:10 2020


"""
import tkinter as tk
from tkinter import ttk

import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
# system libraries
import os
import sys
import urllib
import pydub
import speech_recognition as sr
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
from datetime import datetime
import requests
import json
import stem.process
from stem import Signal
from stem.control import Controller

# custom patch libraries
from patch import download_latest_chromedriver, webdriver_folder_name


win = tk.Tk()
win.minsize(800, 600)
win.title("Maximized Window")

# Maximize the window
win.attributes("-alpha", True)
win.title("Python GUI App")

ttk.Label(win, text="Selenium Automation").pack()

# Define the dropdown options
options = [
    "|   |___Programming",
    "|   |___Developers and Publishers",
    "|   |___Web Development"

]

# Create the combobox widget
combobox = ttk.Combobox(win, values=options)
combobox.pack()

driver = webdriver.Chrome()
def delay(waiting_time=5):
    driver.implicitly_wait(waiting_time)
def delay(waiting_time=5):            
    driver.implicitly_wait(waiting_time)

def create_tor_proxy(socks_port,control_port):
    TOR_PATH = os.path.normpath(os.getcwd()+"\\tor\\tor.exe")
    try:
        tor_process = stem.process.launch_tor_with_config(
          config = {
            'SocksPort': str(socks_port),
            'ControlPort' : str(control_port),
            'MaxCircuitDirtiness' : '300',
          },
          init_msg_handler = lambda line: print(line) if re.search('Bootstrapped', line) else False,
          tor_cmd = TOR_PATH
        )
        print("[INFO] Tor connection created.")
    except:
        tor_process = None
        print("[INFO] Using existing tor connection.")
    
    return tor_process

def renew_ip(control_port):
    print("[INFO] Renewing TOR ip address.")
    with Controller.from_port(port=control_port) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
        controller.close()
    print("[INFO] IP address has been renewed! Better luck next try~")  
    
if __name__ == "__main__":
    SOCKS_PORT = 41293
    CONTROL_PORT = 41294
    USER_AGENT_LIST = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                    ]
    activate_tor = False
    tor_process = None
    user_agent = random.choice(USER_AGENT_LIST)
    if activate_tor:
        print('[INFO] TOR has been activated. Using this option will change your IP address every 60 secs.')
        print('[INFO] Depending on your luck you might still see: Your Computer or Network May Be Sending Automated Queries.')
        tor_process = create_tor_proxy(SOCKS_PORT,CONTROL_PORT)
        PROXIES = {
            "http": f"socks5://127.0.0.1:{SOCKS_PORT}",
            "https": f"socks5://127.0.0.1:{SOCKS_PORT}"
        }
        response = requests.get("http://ip-api.com/json/", proxies=PROXIES)
    else:
        response = requests.get("http://ip-api.com/json/")
    result = json.loads(response.content)
    print('[INFO] IP Address [%s]: %s %s'%(datetime.now().strftime("%d-%m-%Y %H:%M:%S"), result["query"], result["country"]))
    
    # download latest chromedriver, please ensure that your chrome is up to date
    # while True:
def open_website():
    if True:
        try:
            # create chrome driver
            chrome_options = webdriver.ChromeOptions()
            path_to_chromedriver = os.path.normpath(
                os.path.join(os.getcwd(), webdriver_folder_name, "chromedriver.exe")
            )
            if activate_tor:
                chrome_options.add_argument(f"--proxy-server=socks5://127.0.0.1:{SOCKS_PORT}")
            chrome_options.add_argument(f"user-agent={user_agent}")
            driver = webdriver.Chrome(executable_path=path_to_chromedriver,options=chrome_options)
            delay()
            # go to website
            #-------------------------------------------------------------------------------
            # Setup
            Username = 0
            Email = 1
            URL = 2

            with open('data.csv', 'r') as csv_file:

                csv_reader = csv.reader(csv_file)

            #-------------------------------------------------------------------------------
            # Web Automation

                for line in csv_reader:


                    # driver = webdriver.Chrome()
                    driver.get('http://prdirectory.com.ar/submit.php')
                    driver.maximize_window()
                    time.sleep(5)

                    
                    element = driver.find_elements(By.NAME, 'CATEGORY_ID')
                    print('ok')
                    drp = Select(element[0])
                    selected_option = combobox.get()  # Get the selected option from the combobox
                    drp.select_by_visible_text(selected_option)
                    time.sleep(4)

                    goto = driver.find_elements(By.XPATH, '//*[@id="ok"]')
                    goto[0].click()

                    freelink = driver.find_element("xpath", '//*[@id="submitForm"]/table/tbody/tr/td/div/div[1]/table/tbody/tr[3]/td[1]/input')
                    freelink.click()
                    time.sleep(5)

                    goto = driver.find_elements(By.XPATH, '//*[@id="submitForm"]/table/tbody/tr/td/div/div[1]/table/tbody/tr[4]/td/center/input')
                    goto[0].click()

                    Title_field = driver.find_element("xpath", '//*[@id="TITLE"]')
                    Title_field.send_keys(line[3])
                    time.sleep(3)


                    Description_field = driver.find_element("xpath", '//*[@id="DESCRIPTION"]')
                    Description_field.send_keys(line[4])
                    time.sleep(3)

                    Ownername_field = driver.find_element("xpath", '//*[@id="OWNER_NAME"]')
                    Ownername_field.send_keys(line[0])
                    time.sleep(3)

                    Email_field = driver.find_element("xpath", '//*[@id="OWNER_EMAIL"]')
                    Email_field.send_keys(line[1])
                    time.sleep(3)




                    #recaptcha process
                     # main program
                    # auto locate recaptcha frames
                    try:
                        delay()
                        frames = driver.find_elements_by_tag_name("iframe")
                        recaptcha_control_frame = None
                        recaptcha_challenge_frame = None
                        for index, frame in enumerate(frames):
                            if re.search('reCAPTCHA', frame.get_attribute("title")):
                                recaptcha_control_frame = frame
                                
                            if re.search('recaptcha challenge', frame.get_attribute("title")):
                                recaptcha_challenge_frame = frame
                        if not (recaptcha_control_frame and recaptcha_challenge_frame):
                            print("[ERR] Unable to find recaptcha. Abort solver.")
                            sys.exit()
                        # switch to recaptcha frame
                        delay()
                        frames = driver.find_elements_by_tag_name("iframe")
                        driver.switch_to.frame(recaptcha_control_frame)
                        # click on checkbox to activate recaptcha
                        driver.find_element_by_class_name("recaptcha-checkbox-border").click()
                    
                        # switch to recaptcha audio control frame
                        delay()
                        driver.switch_to.default_content()
                        frames = driver.find_elements_by_tag_name("iframe")
                        driver.switch_to.frame(recaptcha_challenge_frame)
                    
                        # click on audio challenge
                        time.sleep(10)
                        driver.find_element_by_id("recaptcha-audio-button").click()
                    
                        # switch to recaptcha audio challenge frame
                        driver.switch_to.default_content()
                        frames = driver.find_elements_by_tag_name("iframe")
                        driver.switch_to.frame(recaptcha_challenge_frame)
                    
                        # get the mp3 audio file
                        delay()
                        src = driver.find_element_by_id("audio-source").get_attribute("src")
                        print(f"[INFO] Audio src: {src}")
                    
                        path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), "sample.mp3"))
                        path_to_wav = os.path.normpath(os.path.join(os.getcwd(), "sample.wav"))
                    
                        # download the mp3 audio file from the source
                        urllib.request.urlretrieve(src, path_to_mp3)
                    except:
                        # if ip is blocked.. renew tor ip
                        print("[INFO] IP address has been blocked for recaptcha.")
                        if activate_tor:
                            renew_ip(CONTROL_PORT)
                        sys.exit()    

                    # load downloaded mp3 audio file as .wav
                    try:
                        sound = pydub.AudioSegment.from_mp3(path_to_mp3)
                        sound.export(path_to_wav, format="wav")
                        sample_audio = sr.AudioFile(path_to_wav)
                    except Exception:
                        sys.exit(
                            "[ERR] Please run program as administrator or download ffmpeg manually, "
                            "https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/"
                        )

                    # translate audio to text with google voice recognition
                    delay()
                    r = sr.Recognizer()
                    with sample_audio as source:
                        audio = r.record(source)
                    key = r.recognize_google(audio)
                    print(f"[INFO] Recaptcha Passcode: {key}")

                    # key in results and submit
                    delay()
                    driver.find_element_by_id("audio-response").send_keys(key.lower())
                    driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
                    time.sleep(5)
                    driver.switch_to.default_content()
                    time.sleep(5)
                    # driver.find_element_by_id("recaptcha-demo-submit").click()
                    if (tor_process):
                        tor_process.kill()
                   
                    freelink = driver.find_element("xpath", '/html/body/center/div/div[2]/div/div[4]/form/div[7]/div[2]/div[7]/input')
                    freelink.click()
                    time.sleep(5)

                    agree = driver.find_elements(By.NAME, 'AGREERULES')
                    agree[0].click()
                    time.sleep(10)

                    submit = driver.find_elements(By.XPATH, '//*[@id="submitForm"]/table/tbody/tr[12]/td/input')
                    submit[0].click()
                    print("completed")

            # continue     
            # break
        except Exception:
            # patch chromedriver if not available or outdated
            try:
                driver
            except NameError:
                is_patched = download_latest_chromedriver()
            else:
                is_patched = download_latest_chromedriver(
                    driver.capabilities["version"]
                )
                if not is_patched:
                   sys.exit(
                    "[ERR] Please update the chromedriver.exe in the webdriver folder according to your chrome version:"
                    "https://chromedriver.chromium.org/downloads"
                   )
            print("we are facing error please update chorme driver ")
    return 'Helloworld' 

button = ttk.Button(win, text="Open Website", command=open_website)
button.pack()
win.mainloop()   
    # # main program
    # # auto locate recaptcha frames
    # try:
    #     delay()
    #     frames = driver.find_elements_by_tag_name("iframe")
    #     recaptcha_control_frame = None
    #     recaptcha_challenge_frame = None
    #     for index, frame in enumerate(frames):
    #         if re.search('reCAPTCHA', frame.get_attribute("title")):
    #             recaptcha_control_frame = frame
                
    #         if re.search('recaptcha challenge', frame.get_attribute("title")):
    #             recaptcha_challenge_frame = frame
    #     if not (recaptcha_control_frame and recaptcha_challenge_frame):
    #         print("[ERR] Unable to find recaptcha. Abort solver.")
    #         sys.exit()
    #     # switch to recaptcha frame
    #     delay()
    #     frames = driver.find_elements_by_tag_name("iframe")
    #     driver.switch_to.frame(recaptcha_control_frame)
    #     # click on checkbox to activate recaptcha
    #     driver.find_element_by_class_name("recaptcha-checkbox-border").click()
    
    #     # switch to recaptcha audio control frame
    #     delay()
    #     driver.switch_to.default_content()
    #     frames = driver.find_elements_by_tag_name("iframe")
    #     driver.switch_to.frame(recaptcha_challenge_frame)
    
    #     # click on audio challenge
    #     time.sleep(10)
    #     driver.find_element_by_id("recaptcha-audio-button").click()
    
    #     # switch to recaptcha audio challenge frame
    #     driver.switch_to.default_content()
    #     frames = driver.find_elements_by_tag_name("iframe")
    #     driver.switch_to.frame(recaptcha_challenge_frame)
    
    #     # get the mp3 audio file
    #     delay()
    #     src = driver.find_element_by_id("audio-source").get_attribute("src")
    #     print(f"[INFO] Audio src: {src}")
    
    #     path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), "sample.mp3"))
    #     path_to_wav = os.path.normpath(os.path.join(os.getcwd(), "sample.wav"))
    
    #     # download the mp3 audio file from the source
    #     urllib.request.urlretrieve(src, path_to_mp3)
    # except:
    #     # if ip is blocked.. renew tor ip
    #     print("[INFO] IP address has been blocked for recaptcha.")
    #     if activate_tor:
    #         renew_ip(CONTROL_PORT)
    #     sys.exit()    

    # # load downloaded mp3 audio file as .wav
    # try:
    #     sound = pydub.AudioSegment.from_mp3(path_to_mp3)
    #     sound.export(path_to_wav, format="wav")
    #     sample_audio = sr.AudioFile(path_to_wav)
    # except Exception:
    #     sys.exit(
    #         "[ERR] Please run program as administrator or download ffmpeg manually, "
    #         "https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/"
    #     )

    # # translate audio to text with google voice recognition
    # delay()
    # r = sr.Recognizer()
    # with sample_audio as source:
    #     audio = r.record(source)
    # key = r.recognize_google(audio)
    # print(f"[INFO] Recaptcha Passcode: {key}")

    # # key in results and submit
    # delay()
    # driver.find_element_by_id("audio-response").send_keys(key.lower())
    # driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
    # time.sleep(5)
    # driver.switch_to.default_content()
    # time.sleep(5)
    # driver.find_element_by_id("recaptcha-demo-submit").click()
    # if (tor_process):
    #     tor_process.kill()
    