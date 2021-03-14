import requests
import json
import time
import itertools
from selenium import webdriver
from selenium import common
from selenium.webdriver.common.keys import Keys
import os

items = 2000
url = f"https://clouddata.scratch.mit.edu/logs?projectid=498215146&limit={items}&offset=0"

filename = "data.json"

chars ='abcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()-=_+{}[]|\:";' + "'?,./"

#driver = webdriver.Chrome(os.path.dirname(os.path.realpath(__file__)) + "/chromedriver")

def decode(input):
    output = ""
    i = 0
    for l in range(1, int(round((len(input)/2)+1))):
        if(int(input[i] + input[i+1]) == 99):
            output = output + "\n"
            i += 2
            continue
        print(int(input[i] + input[i+1]))
        output = output + chars[int(input[i] + input[i+1]) - 1]
        i += 2
    return output


def add_data():
    new_data = requests.get(url).json()
    with open(filename) as a:
        data = json.load(a)

    for s in new_data:
        alreadyThere = -1
        for index, a in enumerate(data):
            if s["user"] == a["user"]:
                alreadyThere = index
                break
        if alreadyThere != -1:
            data[alreadyThere] = s
        else:
            data.append(s)
        del s["verb"]
        s["value"] = decode(s["value"])

    if(len(data) >= 600):
        data = data[200:]

    with open(filename, "w") as a:
        json.dump(data, a, indent=4)

def answer(answer):
    answerbox = driver.find_element_by_xpath("//input[@class='input_input-form_l9eYg']")
    answerbox.send_keys(answer)
    answerbox.send_keys(Keys.RETURN)

def start():
    driver.get("https://scratch.mit.edu/projects/498215146/")
    while True:
        time.sleep(0.01)
        try:
            go = driver.find_element_by_xpath("//img[@title='Go']")
        except common.exceptions.NoSuchElementException:
            print("You failed")
        else:
            print("You passed")
            go.click()
            break

while True:
    time.sleep(1)
    add_data()
    #answer("Chocolate Potato Man")
