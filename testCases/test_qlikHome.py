import time

import pytest
from selenium import webdriver
from pageObjects.QlikLogin import Login

class Test001_Qlik_Login:
    baseUrl = "https://ireueql9bi2m9ji.us.qlikcloud.com/"
    username = "dennisj@logandata.com"
    password = "Logandata_2024"
    newName = "_perf"

    def test_qlikLogin(self, setup):
        # try:
            self.driver = setup
            self.driver.implicitly_wait(10)
            self.driver.get(self.baseUrl)
            self.driver.maximize_window()
            self.driver.implicitly_wait(15)
            self.login = Login(self.driver)
            act_title = self.driver.title
            # if act_title == "Sign in to your Qlik account":
            #     assert True
            # else:
            #     assert False
            self.login.setUsername(self.username)
            self.login.setPassword(self.password)
            self.login.clickSubmit()
            self.driver.implicitly_wait(10)
            time.sleep(2)
            self.login.clickFavorites()
            self.driver.implicitly_wait(5)

            count = 1
            while count < 5001:
                self.login = Login(self.driver)
                self.driver.implicitly_wait(10)
                # self.login.clickUser()
                time.sleep(2)
                # self.login.clickFavorites()
                # self.driver.implicitly_wait(5)
                self.login.moreMenu()
                self.driver.implicitly_wait(3)
                time.sleep(2)
                self.login.duplicateMenu()
                self.driver.implicitly_wait(10)
                time.sleep(2)
                # self.login.clickQlikHome()
                # self.driver.back()
                # time.sleep(3)
                # self.driver.implicitly_wait(10)
                # self.login.clickUser()
                # self.login.moreMenuXpath()
                # time.sleep(3)
                # self.login.clickRename()
                # self.driver.implicitly_wait(5)
                # time.sleep(2)
                # self.login.editNameInput(f"{self.newName}_{count}")
                # time.sleep(3)
                print(count)
                count += 1

            self.login.clickProfile()
            self.login.clickLogout()
        # except Exception as e:
        #     print(f"An error occurred: {str(e)}")
        # finally:
        #     self.driver.quit()