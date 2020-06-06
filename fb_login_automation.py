# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:15:06 2020

@author: kingslayer
"""

from selenium import webdriver
from getpass import getpass

usr=input("username:")
psw=getpass('Password:')

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

user_bar=driver.find_element_by_id("email")
user_bar.send_keys(usr)

pass_bar=driver.find_element_by_id("pass")
pass_bar.send_keys(psw)


login_button=driver.find_elements_by_id("u_0_b")[0]
login_button.submit()