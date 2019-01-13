from time import sleep

import clipboard
from platinum import Chromium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from user_agent import generate_user_agent


def login_weibo(ACCOUNT, PASSWORD):    
    options = webdriver.ChromeOptions()
    options.add_argument('user-agent="{}"'.format(generate_user_agent(device_type='smartphone')))
    options.add_argument(Chromium.DISABLE_INFOBARS)
    prefs = {
        'profile.default_content_setting_values': {
            'images': 2
        }
    }
    options.add_experimental_option('prefs', prefs)
    chrome = webdriver.Chrome(options=options)

    chrome.get("https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F")

    sleep(3)
    chrome.find_element_by_id("loginName").send_keys(ACCOUNT)
    chrome.find_element_by_id("loginPassword").send_keys(PASSWORD)
    chrome.find_element_by_id("loginAction").click()
    sleep(3)

    return chrome


def post_weibo(chrome, word):
    chrome.get('https://m.weibo.cn/compose/')
    sleep(5)
    
    clipboard.copy(word)
    chrome.find_element_by_tag_name('textarea').send_keys(Keys.CONTROL, 'V')
    sleep(10)
    
    chrome.find_element_by_class_name('m-send-btn').click()
    sleep(45)
