import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class XSSProtectionTest(unittest.TestCase):
    def setUp(self):
        """Test için WebDriver başlatma ve web sitesini açma."""
        self.driver = webdriver.Chrome()
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm')

    def test_xss_in_login(self):
        """Giriş formunda XSS açığını test et."""
        xss_payload = '<script>alert("XSS")</script>'

        try:
            # Kullanıcı adı ve parola alanına XSS payload'ı gönder
            self.driver.find_element(By.NAME, 'username').send_keys(xss_payload)
            self.driver.find_element(By.NAME, 'password').send_keys('password' + Keys.RETURN)

            # XSS açığını kontrol et
            try:
                WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                alert_text = alert.text
                alert.accept()
                self.fail("Test Failed: XSS attack was not prevented.")
            except:
                print("Test Passed: XSS attack was prevented.")
            
        except Exception as e:
            print(f"Test Error: {str(e)}")

    def tearDown(self):
        """Test bitiminde WebDriver'ı kapat."""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
