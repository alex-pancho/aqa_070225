import requests


def get_photos(url:str = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos', params:dict = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}):
    response = requests.get(url, params=params)
    return response.json()

def extract_img_url(data):
    img_urls = []
    photos = data['photos']
    
    for photo in photos:
        img_urls.append(photo['img_src'])
    
    return img_urls
        
def dowload_image(img_urls):
    for index, url in enumerate(img_urls):
        img_data = requests.get(url).content
        with open(f"mars_photo{index + 1}.jpg", "wb") as file:
            file.write(img_data)
            
def main():
    data = get_photos()
    img_urls = extract_img_url(data)
    dowload_image(img_urls)  
    
if __name__ == "__main__":
    main()  
            



    