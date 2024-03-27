# performance_test.py
import requests
import time
import json
from statistics import mean

URL = "https://parabank.parasoft.com/parabank/index.htm"

def measure_response_time(url):
    start_time = time.perf_counter()
    response = requests.get(url)
    elapsed_time = time.perf_counter() - start_time
    if response.status_code == 200:
        return elapsed_time
    else:
        return None

def run_performance_test():
    num_requests = 5
    response_times = []

    for _ in range(num_requests):
        elapsed_time = measure_response_time(URL)
        if elapsed_time is not None:
            response_times.append(elapsed_time)

    if response_times:
        test_output = {
            'Average Response Time': f'{mean(response_times):.4f} seconds',
            'Min Response Time': f'{min(response_times):.4f} seconds',
            'Max Response Time': f'{max(response_times):.4f} seconds'
        }
    else:
        test_output = {
            'Error': 'No successful responses were recorded.'
        }
    print(json.dumps(test_output))

if __name__ == "__main__":
    run_performance_test()




