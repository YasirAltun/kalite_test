import unittest
import requests

class OpenRedirectTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://parabank.parasoft.com/parabank/index.htm"

    def test_open_redirect(self):
        redirect_payload = "http://evil.com"
        response = requests.get(f"{self.base_url}?url={redirect_payload}", allow_redirects=False)
        if 'Location' in response.headers and redirect_payload in response.headers['Location']:
            self.fail("Potential Open Redirect vulnerability detected")
        else:
            print("Test Passed: No Open Redirect vulnerability detected")

if __name__ == '__main__':
    unittest.main()
