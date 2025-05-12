import requests
import os
from tqdm import tqdm

def download_mars_photos(sol, camera, api_key = 'DEMO_KEY', limit=None, folder='mars_photos'):
    """
    Завантажує фото з Mars Rover API (Curiosity) та зберігає локально з прогрес-баром.
    """

    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol' : sol, 'camera' : camera, 'api_key' : api_key}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Помилка запиту: {response.status_code}")
        return
    data = response.json()
    photos = data['photos']

    if not photos:
        print("Фото не знайдено.")
        return
    
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Папка '{folder}' була створена.")

    if limit:
        photos = photos[:limit]

    print(f"\nЗавантаження {len(photos)} фото з Марсу")

    for i, photo in enumerate(tqdm(photos, desc="Завантаження", unit="фото")):
        img_url = photo['img_src']
        img_data = requests.get(img_url).content
        filename = os.path.join(folder, f"mars_photo{i+1}.jpg")
        with open(filename, 'wb') as f:
            f.write(img_data)

        print("\n Завершено!")

if __name__ == "__main__":
    print("Завантаження фото з марсохода Curiosity\n")


    try:
        sol = int(input("Введи марсіанський день (sol): "))
    except ValueError:
        print("Невірний формат sol. Використовується значення за замовчуванням: 1000")
        sol = 1000

    camera = input("Введи камеру (fhaz, rhaz, mast, navcam...): ").strip().lower()
    if not camera:
        camera = 'fhaz'

    try:
        limit_input = input("Максимальна кількість фото (залиш порожнім для всіх): ")
        limit = int(limit_input) if limit_input else None
    except ValueError:
        print("Невірний формат. Завантажимо всі доступні фото.")
        limit = None


    download_mars_photos(sol=sol, camera=camera, limit=limit)
