from selenium import webdriver
from pageObjects.HomePage import SpendandSave
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
    spsv = self.ss.click_spend_save()
    assert spsv is True

@when('Click on Get Aspiration button')
def asp_click(self):
    self.getasp = SpendandSave(self.driver)
    gasp = self.getasp.click_getasp()
    assert gasp is True

@then('Verify that a modal containing input field for an email address to sign up appears')
def ent_email(self):
   self.enteml = SpendandSave(self.driver)
   self.enteml.setemail(click_sslink.email)

@then('Close the email modal box check that Two products are shown again')
def close_eml(self):
    self.eml_clo = SpendandSave(self.driver)
    self.eml_clo.click_email_close()

@then('Click on Get Aspiration Plus button')
def aspplus_click(self):
    self.getaspplus = SpendandSave(self.driver)
    self.getaspplus.click_getasp_plus()

@then('Verify that Get Aspiration Plus have A modal with monthly and yearly plans')
def Mon_Year_Ver(self):
    self.getaspplus = SpendandSave(self.driver)
    self.getaspplus.ver_mon_yer()
    assert self.driver.find_element_by_names(["Yearly","Monthly"]) is True

@then('Verify that Yearly plan shows $71.88 as a price per Year')
def Year_Ver(self):
    self.getaspplus = SpendandSave(self.driver)
    self.getaspplus.year_ver()
    assert self.driver.find_element_by_xpath("71.88").text() is True

@then(u'Verify that Yearly plan shows $7.99 as a price per Month')
def Mon_Ver(self):
    self.getaspplus = SpendandSave(self.driver)
    self.getaspplus.mon_ver()
    assert self.driver.find_element_by_xpath("7.99").text() is True
    self.driver.close()