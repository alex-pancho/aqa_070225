import requests
import json

def get_json_with_data(url: str, params: dict) -> str:
    """
    Sends a GET request to the given URL with parameters,
    saves the JSON response to 'data.json', and returns the file name.
    """
    response = requests.get(url, params=params)
    result = response.json()
    with open('data.json', 'w') as file:
        json.dump(result, file, indent=4)
    return file.name

def get_image_urls(file_name: str) -> list:
    """
    Reads the JSON file and extracts all image URLs from 'photos'.
    """
    with open(file_name, 'r') as file:
        data = json.load(file)
    image_urls = [photo['img_src'] for photo in data.get('photos', [])]
    return image_urls

def download_images(image_urls: list):
    """
    Downloads the first 5 images from the list and saves them locally.
    """
    for i, url in enumerate(image_urls[:5], start=1):
        response = requests.get(url)
        if response.status_code == 200:
            file_name = f"mars_photo{i}.jpg"
            with open(file_name, 'wb') as f:
                f.write(response.content)
            print(f"Saved: {file_name}")
        else:
            print(f"Failed to download: {url}")

if __name__ == "__main__":
    cameras = ['fhaz', 'rhaz', 'mast', 'chemcam', 'mahli', 'mardi', 'navcam']
    print("Available cameras:", ", ".join(cameras))

    camera = input("Enter camera name (like fhaz): ").lower()

    if camera not in cameras:
        print("Invalid camera.")
    else:
        sol = input("Enter Martian sol (for example 1000): ")

        if not sol.isdigit():
            print("Sol must be a number.")
        else:
            sol = int(sol)

            url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
            params = {
                "sol": sol,
                "camera": camera,
                "api_key": "dJjtYo3QReYLtbI2lgfi4u9VSqQ4p7Lsh4eRnM3m"
            }

            file_name = get_json_with_data(url, params)
            urls = get_image_urls(file_name)

            if len(urls) == 0:
                print("No images found.")
            else:
                download_images(urls)
