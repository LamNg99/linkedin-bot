# Import necessary tools
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time
import random

def performance(func):
    '''
    This function measures our bots' performance 
    '''
    def wrapper(*args, **kwargs):
        print('\n****************************************************************')
        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()
        print(f'Running time: {finish_time - start_time} (s)')
        print('****************************************************************\n')
        return result
    return wrapper

@performance
def login_bot(driver, bot_name='login_bot'):
    '''
    This bot is used to login into your Linkedin profile using 
    username and password from config.txt file
    '''
    print(f'{bot_name} is running ...')
    driver.get('https://www.linkedin.com')
    time.sleep(1)
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
    print('Successfully Logged In!')

@performance
def connect_bot(driver, bot_name='connect_bot'):
    '''
    This bot will send connect invitations to people with 2nd connections randomly between page 1 and 100. 
    '''
    print(f'{bot_name} is running ...')

    page = random.randint(1,100)
    driver.get(f'https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page={page}')
    time.sleep(2)

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
    
    print(f'You have sent {count} connect invitation(s)')

@performance
def accept_bot (driver, bot_name='accept_bot'):
    '''
    This bot will accept any new connect invitations from people on LinkedIn
    '''
    print(f'{bot_name} is running ...')

    driver.get('https://www.linkedin.com/mynetwork/invitation-manager/?invitationType=ALL')
    time.sleep(2)

    all_buttons = driver.find_elements(By.TAG_NAME, 'button')
    accept_buttons = [btn for btn in all_buttons if btn.text == 'Accept']
    
    if accept_buttons:
        count = 0 
        for btn in accept_buttons:
            driver.execute_script('arguments[0].click;', btn)
            time.sleep(2)
            count += 1
        print(f'You have accepted {count} connect invitation(s)')
    else:
        print('You don\'t have any new connect invitation!')


def run_bot(driver):
    login_bot(driver)
    for bot in sys.argv[1:]:
        if bot == 'connect_bot':
            connect_bot(driver)
        elif bot == 'accept_bot':
            accept_bot(driver)
        else:
            print(f'Invalid Command: {bot}')

    print('All bot(s) completed their tasks!')

if __name__ == "__main__":
    driver = webdriver.Chrome('/Users/lamnguyen/Desktop/Projects/linkedin-bot/chromedriver')
    run_bot(driver)
    driver.close()




        





