import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SQLInjectionTest(unittest.TestCase):
    def setUp(self):
        """Test için WebDriver başlatma ve web sitesini açma."""
        self.driver = webdriver.Chrome()
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm')

    def test_sql_injection(self):
        """Giriş formunda SQL Injection açığını test et."""
        sql_payload = "' OR '1'='1"

        try:
            # Kullanıcı adı ve parola alanına SQL Injection payload'ı gönder
            username_input = self.driver.find_element(By.NAME, 'username')
            password_input = self.driver.find_element(By.NAME, 'password')
            username_input.send_keys(sql_payload)
            password_input.send_keys(sql_payload + Keys.RETURN)

            # SQL Injection saldırısının başarılı olup olmadığını kontrol et
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.url_to_be("https://parabank.parasoft.com/parabank/overview.htm")
                )
                self.fail("Test Failed: SQL Injection attack succeeded, site is vulnerable.")
            except:
                print("Test Passed: SQL Injection attack was prevented.")
            
        except Exception as e:
            print(f"Test Error: {str(e)}")
            self.fail("Test Failed: Exception occurred during SQL Injection test.")

    def tearDown(self):
        """Test bitiminde WebDriver'ı kapat."""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
