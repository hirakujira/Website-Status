#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

class Status:
    Test1OK = False;
    Test2OK = False;
    Test3OK = False;
    Text = ""

class RunTest():

    @classmethod
    def get_config(cls, config_path):
        with open(config_path, 'r') as f:
            return json.loads(f.read())

    @classmethod
    def run_test_1(cls, config):
        Status.Text += "Test1 - Web Host: "
        if config["RunTest1"] == True:
            r = requests.get(config["Test1URL"])
            if r.text.find("<p>Test1: OK</p>") == 89:
                Status.Test1OK = True
                Status.Text += "Success\n"
            else:
                Status.Text += "Failed\n"
        else:
            Status.Text += "Passed\n"

    @classmethod
    def run_test_2(cls, config):
        Status.Text += "Test2 - Simple PHP: "
        if config["RunTest2"] == True:
            r = requests.get(config["Test2URL"])
            if r.text.find("<p>Test2: OK</p>") == 89:
                Status.Test2OK = True
                Status.Text += "Success\n"
            else:
                Status.Text += "Failed\n"
        else:
            Status.Text += "Passed\n"

    @classmethod
    def run_test_3(cls, config):
        Status.Text += "Test3 - Wordpress: "
        if config["RunTest3"] == True:
            r = requests.get(config["Test3URL"])
            if r.text.find("<p>Test3: OK</p>") > 0:
                Status.Test3OK = True
                Status.Text += "Success"
            else:
                Status.Text += "Failed"
        else:
            Status.Text += "Passed"

    @classmethod
    def push_notification(cls, config):
        body = {"value1": Status.Text}
        url = "https://maker.ifttt.com/trigger/" + config["ifttt_trigger"] +"/with/key/" + config["ifttt_key"]
        print(url)
        r = requests.post(url=url, data=body)

if __name__ == '__main__':
    config = RunTest.get_config("config.json")
    RunTest.run_test_1(config)
    RunTest.run_test_2(config)
    RunTest.run_test_3(config)

    print("Website status check done.")

    if Status.Test1OK == True and Status.Test2OK == True and Status.Test3OK == True:
        if config["nofity_only_when_failed"] == False:
            print("Push notification...")
            RunTest.push_notification(config)
    else:
        print("Push notification...")
        RunTest.push_notification(config)
