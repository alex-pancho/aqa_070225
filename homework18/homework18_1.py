import requests

API_URL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
PARAMS = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

def get_data(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if not data.get('photos'):
            print("No photos available for the given parameters.")
            return None
        return data
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def extract_photo_urls(data):
    photos = data.get('photos', [])
    urls = [photo['img_src'] for photo in photos]
    print(f"Found {len(urls)} photo(s).")
    return urls

def download_photo(url, photo_num):
    try:
        response = requests.get(url)
        response.raise_for_status()
        filename = f"mars_photo{photo_num}.jpg"
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Photo {photo_num} saved as {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download photo {photo_num}: {e}")

def main():
    data = get_data(API_URL, PARAMS)
    if not data:
        print("Failed to retrieve data.")
        return
    urls = extract_photo_urls(data)
    if not urls:
        print("No photo URLs found.")
        return
    for i, url in enumerate(urls, start=1):
        download_photo(url, i)

if __name__ == "__main__":
    main()