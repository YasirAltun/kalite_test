import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ParaBankIntegrationTest(unittest.TestCase):
    def setUp(self):
        """Test için WebDriver başlatma ve web sitesini açma."""
        self.driver = webdriver.Chrome()
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm')

    def test_login_and_navigate(self):
        """Kullanıcı girişi yap ve hesap özeti sayfasına git."""
        try:
            # Giriş bilgilerini gir
            username_input = self.driver.find_element(By.NAME, 'username')
            password_input = self.driver.find_element(By.NAME, 'password')
            username_input.send_keys('john')
            password_input.send_keys('demo')

            # Giriş butonuna bas
            login_button = self.driver.find_element(By.XPATH, "//input[@value='Log In']")
            login_button.click()

            # Hesap özeti sayfasına yönlendirilmiş mi kontrol et
            WebDriverWait(self.driver, 10).until(
                EC.url_to_be("https://parabank.parasoft.com/parabank/overview.htm")
            )

            # URL'nin beklenen değere sahip olup olmadığını doğrula
            current_url = self.driver.current_url
            self.assertEqual(current_url, "https://parabank.parasoft.com/parabank/overview.htm", "URL did not match expected value.")
            print("Test Passed: Login and navigation successful.")
            
        except Exception as e:
            print(f"Test Failed: {str(e)}")
            self.fail("Test Failed: Exception occurred during login and navigation.")

    def tearDown(self):
        """Test bitiminde WebDriver'ı kapat."""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()




