import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Test edilecek web sitesi URL'si
URL = "https://parabank.parasoft.com/parabank/index.htm"

def make_request(url):
    """Belirtilen URL'ye HTTP GET isteği yapar."""
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return str(e)

def run_stress_test():
    """Sürekli artan işçi sayısı ile stres testi yapar."""
    initial_workers = 10  # Başlangıç işçi sayısı
    max_workers = 50   # Maksimum işçi sayısı
    increment = 10       # Her adımda işçi sayısını artırma miktarı
    test_duration = 0.1   # Her yük seviyesi için test süresi (saniye)
    
    for worker_count in range(initial_workers, max_workers + 1, increment):
        with ThreadPoolExecutor(max_workers=worker_count) as executor:
            print(f"Testing with {worker_count} workers...")
            start_time = time.time()
            futures = [executor.submit(make_request, URL) for _ in range(worker_count)]
            results = [future.result() for future in as_completed(futures)]
            end_time = time.time()

            success = sum(1 for result in results if result == 200)
            failures = len(results) - success
            total_time = end_time - start_time

            print(f"Total Requests: {len(results)}")
            print(f"Successful Requests: {success}")
            print(f"Failed Requests: {failures}")
            print(f"Total Test Time: {total_time:.2f} seconds")
            print(f"Requests per second: {len(results) / total_time:.2f} RPS")

            time.sleep(test_duration)  # Her test arasında belirli bir süre bekle

if __name__ == "__main__":
    run_stress_test()




