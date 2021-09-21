from selenium import webdriver
from pageObjects.HomePage import SpendandSave
import time
from behave import *
from utilities.readProperties import ReadConfig

class click_sslink:
    baseURL = ReadConfig.getAppUrl()
    prodUrl = ReadConfig.getProdUrl()
    email = ReadConfig.getemail()

@given('Launch browser navigates to aspiration.com home page')
def test_homePageTitle(self):
    self.driver = webdriver.Chrome()
    self.driver.get(click_sslink.baseURL)
    aspiration_title=self.driver.title
    if aspiration_title == SpendandSave.aspiration_logo:
        assert True
    else:
        assert False

@when('User clicks on Spend and Save link')
def spendandsave(self):
    self.ss = SpendandSave(self.driver)
    self.ss.click_spend_save()

@when('Click on Get Aspiration button')
def asp_click(self):
    self.getasp = SpendandSave(self.driver)
    self.getasp.click_getasp()
    time.sleep(3)

@then('Verify that a modal containing input field for an email address to sign up appears')
def ent_email(self):
   self.enteml = SpendandSave(self.driver)
   self.enteml.setemail(click_sslink.email)
   time.sleep(3)

@then('Close the email modal box check that Two products are shown again')
def close_eml(self):
    self.eml_clo = SpendandSave(self.driver)
    self.eml_clo.click_email_close()
    time.sleep(3)

@then('Click on Get Aspiration Plus button')
def aspplus_click(self):
    self.getaspplus = SpendandSave(self.driver)
    self.getaspplus.click_getasp_plus()
    time.sleep(3)
