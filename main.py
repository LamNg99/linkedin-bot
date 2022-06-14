# Import necessary tools
from selenium import webdriver
import os
import sys
import time

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
    fill_usr = driver.find_element_by_xpath("//input[@name='session_key']")
    fill_pass = driver.find_element_by_xpath("//input[@name='session_password']")

    fill_usr.send_keys(username)
    fill_pass.send_keys(password)
    time.sleep(1)

    login_button = driver.find_element_by_xpath("//button[@type='submit']").click()
    print('Login Successfully!')

login_bot()

def connect_bot():
    driver.get('https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=1')





