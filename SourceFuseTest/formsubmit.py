from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        baseURL = "http://sfwebhtml:t63KUfxL5vUyFLG4eqZNUcuRQ@sfwebhtml.sourcefuse.com/automation-form-demo-for-interview/"
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Ishan\\Desktop\\Test\\driver\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(baseURL)

    def test_TC_01(self):
        driver=self.driver
        driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
        time.sleep(3)
        elements = driver.find_elements(By.XPATH, "//form//div/div/label")
        for i in elements:
            print(i.text)

    def test_TC_02(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//div[@id='fnameInput']/input[@type='text']").is_enabled()
        driver.find_element(By.XPATH, "//div[@id='lnameInput']/input[@type='text']").is_displayed()
        driver.find_element(By.XPATH, "//div[@id='emailInput']/input[@type='email']").is_displayed()
        driver.find_element(By.XPATH, "//div[@id='curCompanyInput']/input[@type='text']").is_enabled()
        driver.find_element(By.XPATH, "//div[@id='mobInput']/input[@type='tel']").is_displayed()
        driver.find_element(By.XPATH, "//div[@id='DOBInput']//input[@type='text']").is_enabled()
        driver.find_element(By.XPATH, "//div[@id='positionInput']/input[@type='text']").is_enabled()
        driver.find_element(By.XPATH, "//div[@id='portfolioInput']/input[@value='http://']").is_enabled()
        driver.find_element(By.XPATH, "//div[@id='salaryInput']/input[@type='text']").is_displayed()
        driver.find_element(By.XPATH, "//div[@id='whenStartInput']/input[@type='text']").is_displayed()
        driver.find_element(By.XPATH, "//textarea[@id='address']").is_displayed()
        driver.find_element(By.XPATH, "//input[@id='resume']").is_enabled()
        driver.find_element(By.XPATH, "//div[@id='relocateInput']/div/label[2]").is_displayed()
        driver.find_element(By.XPATH, "//form/button[@type='reset']").click

    def test_TC_03(self):
        driver = self.driver
        fname = driver.find_element(By.XPATH, "//div[@id='fnameInput']/input[@type='text']")
        self.assertTrue(fname)
        lname = driver.find_element(By.XPATH, "//div[@id='lnameInput']/input[@type='text']")
        self.assertTrue(lname)
        email = driver.find_element(By.XPATH, "//div[@id='emailInput']/input[@type='email']")
        self.assertTrue(email)
        ccompany = driver.find_element(By.XPATH, "//div[@id='curCompanyInput']/input[@type='text']")
        self.assertIsNotNone(ccompany)
        phone = driver.find_element(By.XPATH, "//div[@id='mobInput']/input[@type='tel']")
        self.assertIsNotNone(phone)
        dob = driver.find_element(By.XPATH, "//div[@id='DOBInput']//input[@type='text']")
        self.assertIsNotNone(dob)
        position = driver.find_element(By.XPATH, "//div[@id='positionInput']/input[@type='text']")
        self.assertIsNotNone(position)
        prof = driver.find_element(By.XPATH, "//div[@id='portfolioInput']/input[@value='http://']")
        self.assertTrue(prof)
        sal = driver.find_element(By.XPATH, "//div[@id='salaryInput']/input[@type='text']")
        self.assertIsNotNone(sal)
        join = driver.find_element(By.XPATH, "//div[@id='whenStartInput']/input[@type='text']")
        self.assertTrue(join)
        add = driver.find_element(By.XPATH, "//textarea[@id='address']")
        self.assertIsNotNone(add)
        cv = driver.find_element(By.XPATH, "//input[@id='resume']")
        self.assertTrue(cv)
        relo =driver.find_element(By.XPATH, "//div[@id='relocateInput']/div/label[2]")
        self.assertTrue(relo)
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click

    def test_TC_04(self):
        driver = self.driver
        fname = driver.find_element(By.XPATH, "//div[@id='fnameInput']/input[@type='text']")
        fname.send_keys("Ishan")
        lname = driver.find_element(By.XPATH, "//div[@id='lnameInput']/input[@type='text']")
        lname.send_keys("P L")
        email = driver.find_element(By.XPATH, "//div[@id='emailInput']/input[@type='email']")
        email.send_keys("ishanpl2294@gmail.com")
        ccompany = driver.find_element(By.XPATH, "//div[@id='curCompanyInput']/input[@type='text']")
        ccompany.send_keys("Coextrix Technologies Pvt.Ltd")
        phone = driver.find_element(By.XPATH, "//div[@id='mobInput']/input[@type='tel']")
        phone.send_keys("7975808302")
        dob = driver.find_element(By.XPATH, "//div[@id='DOBInput']//input[@type='text']")
        dob.send_keys("01/22/1994")
        position =driver.find_element(By.XPATH, "//div[@id='positionInput']/input[@type='text']")
        position.send_keys("Automation Testing")
        prof = driver.find_element(By.XPATH, "//div[@id='portfolioInput']/input[@value='http://']")
        prof.send_keys("www.Google.com")
        sal = driver.find_element(By.XPATH, "//div[@id='salaryInput']/input[@type='text']")
        sal.send_keys("500000")
        join = driver.find_element(By.XPATH, "//div[@id='whenStartInput']/input[@type='text']")
        join.send_keys("Immediate")
        add = driver.find_element(By.XPATH, "//textarea[@id='address']")
        add.send_keys("Address")
        cv = driver.find_element(By.XPATH, "//input[@id='resume']")
        cv.send_keys("C:\\Users\\Ishan\\Desktop\\Test\\resume\\Ishan_CV.pdf")
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='relocateInput']/div/label[2]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//form/button[@type='submit']").click()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)