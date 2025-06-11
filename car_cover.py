import requests 
from bs4 import BeautifulSoup
import pandas as pd
import time

def fetch_car_cover_data(url):
    base_url = "https://www.olx.in/items/q-car-cover"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("Request timed out.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extracting car cover data
    car_covers = []
    for item in soup.select("li.EIR5N"):
        title = item.select_one("span._2tW1I")
        price = item.select_one("span._89yzn")
        location = item.select_one("span._2tW1I._2_iZc")

        car_covers.append({
            "title": title.text.strip() if title else "N/A",
            "price": price.text.strip() if price else "N/A",
            "location": location.text.strip() if location else "N/A"
        })

    return car_covers

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    url = "https://www.olx.in/items/q-car-cover"
    data = fetch_car_cover_data(url)

    if data:
        save_to_csv(data, "car_covers.csv")
    else:
        print("No data fetched.")
