import requests 
from bs4 import BeautifulSoup
import pandas as pd
import time

def fetch_car_cover_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extracting car cover data
    car_covers = []
    for item in soup.find_all('div', class_='car-cover-item'):
        title = item.find('h2').text.strip()
        price = item.find('span', class_='price').text.strip()
        description = item.find('p', class_='description').text.strip()
        location = item.find('span', class_='location')
        location = location.text.strip() if location else "N/A"

        car_covers.append({
            'title': title,
            'price': price,
            'description': description,
            "Location": location
        })
        
    return car_covers   

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__": 
    url = 'https://example.com/car-covers'  # Replace with the actual URL
    car_cover_data = fetch_car_cover_data(url)
    
    if car_cover_data:
        save_to_csv(car_cover_data, 'car_covers.csv')
    else:
        print("No data to save.")
    
    time.sleep(2)  # Sleep to avoid overwhelming the server
