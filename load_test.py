# load_test.py
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import json

URL = "https://parabank.parasoft.com/parabank/index.htm"
REQUESTS_PER_THREAD = 10
MAX_WORKERS = 5

def make_request(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return str(e)

def run_load_test():
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(make_request, URL) for _ in range(MAX_WORKERS * REQUESTS_PER_THREAD)]
        start_time = time.time()
        results = [future.result() for future in as_completed(futures)]
        end_time = time.time()

    success = sum(1 for result in results if result == 200)
    failures = len(results) - success
    total_time = end_time - start_time

    test_output = {
        'Total Requests': len(results),
        'Successful Requests': success,
        'Failed Requests': failures,
        'Total Test Time': f'{total_time:.2f} seconds',
        'Requests per second': f'{len(results) / total_time:.2f} RPS'
    }
    print(json.dumps(test_output))

if __name__ == "__main__":
    run_load_test()
