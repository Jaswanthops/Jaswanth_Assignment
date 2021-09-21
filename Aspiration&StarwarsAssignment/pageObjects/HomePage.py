class SpendandSave:
    save_spend_link = "//header/ul[1]/li[1]/a[1]"
    aspiration_logo = "Aspiration | Green Financial Services"
    ssverifivation = "//h1[contains(text(),'Spend & Save Plans')]"
    asptagnam = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/spend-save-plans[1]/div[1]/div[1]/div[1]/div[2]/button[1]"
    aspplusnam = "//button[contains(text(),'Get Aspiration Plus')]"
    input_email_asp = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/form[1]/fieldset[1]/div[3]/div[1]/div[2]/input[1]"
    email_close_pop = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/button[1]"

    def __init__(self,driver):
        self.driver = driver

    def click_spend_save(self):
        self.driver.find_element_by_xpath(self.save_spend_link).click()

    def ssverifivation(self):
        self.driver.find_element_by_xpath(self.ssverifivation)

    def click_getasp(self):
        self.driver.find_element_by_xpath(self.asptagnam).click()

    def setemail(self,email):
        self.driver.find_element_by_xpath(self.input_email_asp).click()
        self.driver.find_element_by_xpath(self.input_email_asp).clear()
        self.driver.find_element_by_xpath(self.input_email_asp).send_keys(email)

    def click_email_close(self):
        self.driver.find_element_by_xpath(self.email_close_pop).click()

    def click_getasp_plus(self):
        self.driver.find_element_by_xpath(self.aspplusnam).click()