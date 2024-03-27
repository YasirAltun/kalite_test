import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ParaBankFunctionalityTest(unittest.TestCase):
    def setUp(self):
        """Test için WebDriver başlatma ve web sitesini açma."""
        self.driver = webdriver.Chrome()
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm')

    def test_signup_form(self):
        """Kayıt formunu doldur ve formu gönder."""
        try:
            # Kayıt sayfasına git
            self.driver.find_element(By.LINK_TEXT, "Register").click()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "customerForm"))
            )

            # Form alanlarını doldur
            self.driver.find_element(By.ID, 'customer.firstName').send_keys('John')
            self.driver.find_element(By.ID, 'customer.lastName').send_keys('Doe')
            self.driver.find_element(By.ID, 'customer.address.street').send_keys('123 Main St')
            self.driver.find_element(By.ID, 'customer.address.city').send_keys('Anytown')
            self.driver.find_element(By.ID, 'customer.address.state').send_keys('CA')
            self.driver.find_element(By.ID, 'customer.address.zipCode').send_keys('12345')
            self.driver.find_element(By.ID, 'customer.phoneNumber').send_keys('123-456-7890')
            self.driver.find_element(By.ID, 'customer.ssn').send_keys('123-45-6789')
            self.driver.find_element(By.ID, 'customer.username').send_keys('john___doe')#  test yapmadan önce bu kısmı değiştirmemiz lazım
            self.driver.find_element(By.ID, 'customer.password').send_keys('password')
            self.driver.find_element(By.ID, 'repeatedPassword').send_keys('password')
            
            # Formu gönder
            self.driver.find_element(By.XPATH, "//input[@value='Register']").click()

            # Başarılı kayıt işlemini kontrol et
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[text()='Welcome john___doe']"))#  test yapmadan önce bu kısmı değiştirmemiz lazım
            )
            print("Test Passed: Registration successful.")

        except Exception as e:
            print(f"Test Failed: {str(e)}")

    def tearDown(self):
        """Test bitiminde WebDriver'ı kapat."""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



