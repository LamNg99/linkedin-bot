# Import necessary tools
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time
import random

# Open the Chrome driver and go to Linkedin login page
driver = webdriver.Chrome('/Users/lamnguyen/Desktop/Projects/linkedin-bot/chromedriver')
driver.get('https://www.linkedin.com')
time.sleep(1)

def login_bot():
    '''
    This bot is used to login into your Linkedin profile
    '''

    # Get username and password in the config.txt file
    try:
        with open('config.txt', mode='r') as config_file:
            config = config_file.readlines()
            username = config[0].split(' ')[-1]
            password = config[1].split(' ')[-1]   
    except FileNotFoundError as error:
        print('Check your file existance and path!')
    
    # Login into Linkedin Profile
    fill_usr = driver.find_element(By.XPATH, "//input[@name='session_key']")
    fill_pass = driver.find_element(By.XPATH, "//input[@name='session_password']")

    fill_usr.send_keys(username)
    fill_pass.send_keys(password)
    time.sleep(1)

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print('Login Successfully!')

login_bot()

def connect_bot():
    page = random.randint(1,100)
    driver.get(f'https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page={page}')
    time.sleep(1)

    all_buttons = driver.find_elements(By.TAG_NAME, 'button')
    connect_buttons = [btn for btn in all_buttons if btn.text == 'Connect']
    count = 0

    for btn in connect_buttons:
        driver.execute_script('arguments[0].click()', btn)
        time.sleep(1)

        send_button = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
        driver.execute_script('arguments[0].click()', send_button)
        close_button = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
        driver.execute_script('arguments[0].click()', close_button)
        time.sleep(1)
        count += 1
    
    print(f'You have sent {count} connect invitations')

connect_bot()
        





