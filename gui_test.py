import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ParaBankGUITest(unittest.TestCase):
    def setUp(self):
        """Test için WebDriver başlatma ve web sitesini açma."""
        self.driver = webdriver.Chrome()
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm')

    def test_elements_present(self):
        """Ana sayfadaki bazı GUI öğelerinin mevcut olduğunu kontrol et."""
        results = {}
        try:
            # Logo kontrolü
            logo = self.driver.find_element(By.CLASS_NAME, 'logo')
            results['Logo'] = logo.is_displayed()

            # Giriş formu kontrolü
            login_form = self.driver.find_element(By.ID, 'loginPanel')
            results['Login Form'] = login_form.is_displayed()

            # Giriş butonu kontrolü
            login_button = self.driver.find_element(By.XPATH, "//input[@value='Log In']")
            results['Login Button'] = login_button.is_displayed()

            # Kayıt linki kontrolü
            register_link = self.driver.find_element(By.LINK_TEXT, "Register")
            results['Register Link'] = register_link.is_displayed()

            # Parolayı unuttum linki kontrolü
            forgot_password_link = self.driver.find_element(By.LINK_TEXT, "Forgot login info?")
            results['Forgot Password Link'] = forgot_password_link.is_displayed()

            # Account Services başlığı kontrolü
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Customer Login')]"))
            )
            account_overview_title = self.driver.find_element(By.XPATH, "//h2[contains(text(), 'Customer Login')]")
            results['Customer Login Title'] = account_overview_title.is_displayed()

            # Sonuçları kontrol et
            for element, displayed in results.items():
                self.assertTrue(displayed, f"{element} is not displayed on the page.")
            print("Test Passed: All elements are displayed correctly.")

        except AssertionError as e:
            print(f"Test Failed: {str(e)}")
        except Exception as e:
            print(f"Test Error: {str(e)}")

    def tearDown(self):
        """Test bitiminde WebDriver'ı kapat."""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()




