"""Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON 
про фото зробленi ровером “Curiosity” на Марсi. Серед цих даних є посилання на фото якi 
потрiбно розпарсити i потiм за допомогою додаткових запитiв скачати i зберiгти цi фото 
як локальнi файли mars_photo1.jpg , mars_photo2.jpg . Завдання потрiбно зробити використовуючи модуль requests"""

import requests
import json

def get_json_with_data(url: str, params: dict) -> str:
    """
    Sends a GET request to the specified URL with the given parameters,
    saves the JSON response to 'data.json', and returns the file name.

    Parameters:
        url (str): The API endpoint to send the request to.
        params (dict): A dictionary of query parameters for the request.

    Returns:
        str: The name of the file where the JSON response was saved.
    """
    response = requests.get(url, params=params)
    result = response.json()
    with open('data.json', 'w') as file: # Запис JSON-даних у файл
        json.dump(result, file, indent=4)
    return file.name

def get_image_url(file_name: str) -> list:
    """
    Reads a JSON file and extracts all image URLs from the 'photos' list.

    Parameters:
        file_name (str): The name of the JSON file to read.

    Returns:
        list[]: A list of image URLs (from the 'img_src' fields).
    """
    with open(file_name, 'r') as file:
        data = json.load(file)
    image_urls = [] #get list with images
    for image in data["photos"]:
        image_urls.append(image["img_src"])
    return image_urls

def download_images(image_urls: list) -> None:
    """
    Downloads images from a list of URLs and saves them locally

    Parameters:
        image_urls (list[]): A list of image URLs to download.

    Returns:
        None
    """    
    for i, url in enumerate(image_urls, start=1):
        response_image = requests.get(url)
        if response_image.status_code == 200:
            file_name = f'mars_photo{i}.jpg'
            with open(file_name, 'wb') as file:
                file.write(response_image.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Can not download: {url}")

if __name__ == "__main__":
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
    result = get_json_with_data(url, params)
    image_urls = get_image_url(result)
    download_images(image_urls)