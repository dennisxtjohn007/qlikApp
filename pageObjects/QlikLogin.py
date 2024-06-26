import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    textbox_email_id = "1-email"
    textbox_password_id = "1-password"
    button_login_id = "1-submit"
    img_profile_xpath = "(//img[@class='MuiAvatar-img css-1hy9t21'])[1]"
    button_logout_id = "app-switcher-logout"
    favorites_xpath = "(//span[contains(@class,'MuiTypography-root MuiTypography-body1')])[2]"
    more_menu_dots_id = "more-menu-button"
    duplicate_menu_id = "show-more-duplicate"
    # qlik_home_id = "top-bar-logo"
    qlik_home_xpath = "(//div[contains(@class,'MuiToolbar-root MuiToolbar-regular')]//div)[2]"
    welcome_user = "//h2[text()='Welcome, Dennis John.']"
    more_menu_dots_xpath = "(//button[@id='more-menu-button'])[2]"
    rename_id = "show-more-update"
    edit_name_input_id = "app-modal-name-input"
    rename_save_xpath = "//span[text()='Save']"

    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def setUsername(self,username):
        self.driver.find_element("id", self.textbox_email_id).clear()
        self.driver.find_element("id", self.textbox_email_id).send_keys(username)

        # self.driver.find_element_by_id(self.textbox_email_id).clear()
        # self.driver.find_element_by_id(self.textbox_email_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element("id", self.textbox_password_id).clear()
        self.driver.find_element("id", self.textbox_password_id).send_keys(password)

    def clickSubmit(self):
        self.driver.find_element("id", self.button_login_id).click()

    def clickFavorites(self):
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.favorites_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.favorites_xpath).click()

    def moreMenu(self):
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, self.more_menu_dots_id)))
        element.click()
        # self.driver.find_element("id", self.more_menu_dots_id).click()

    def duplicateMenu(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.duplicate_menu_id)))
        element.click()
        # self.driver.find_element("id", self.duplicate_menu_id).click()

    def clickQlikHome(self):
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, "top-bar-logo")))
        element.click()
        # self.driver.find_element("id", self.qlik_home_id).click()

    def clickUser(self):
        self.driver.find_element(By.XPATH, self.welcome_user)
    def moreMenuXpath(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.more_menu_dots_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.more_menu_dots_xpath).click()

    def clickRename(self):
        element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, self.rename_id)))
        element.click()
        # self.driver.find_element("id", self.rename_id).click()

    def editNameInput(self,newName):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.edit_name_input_id)))
        element.clear()
        element.send_keys(newName)
        # self.driver.find_element("id", self.edit_name_input_id).clear()
        # self.driver.find_element("id", self.edit_name_input_id).send_keys(newName)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.rename_save_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.rename_save_xpath).click()

    def renameSaveButton(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.edit_name_input_id)))
        element.click()
        # self.driver.find_element(By.XPATH, self.rename_save_xpath).click()
    def clickProfile(self):
        self.driver.find_element(By.XPATH, self.img_profile_xpath).click()

    def clickLogout(self):
        self.driver.find_element("id", self.button_logout_id).click()

