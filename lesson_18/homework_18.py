"""
Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi 
у виглядi JSON про фото зробленi ровером “Curiosity” на Марсi. Серед цих 
даних є посилання на фото якi потрiбно розпарсити i потiм за допомогою 
додаткових запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg , 
mars_photo2.jpg . Завдання потрiбно зробити використовуючи модуль requests
"""
import json
import requests
from pathlib import Path
from requests.exceptions import HTTPError, ConnectionError, Timeout


def get_data_in_json(url, params):
    """ Getting data... """
    try:
        response = requests.get(url, params, timeout=30)
        response.raise_for_status()
        try:
            data = response.json()
            return data
        except json.JSONDecodeError as e:
           print('Помилка при серіалізації JSON:', e)
       
    except HTTPError as e:
        print('HTTP Помилка:', e)
    except ConnectionError as e:
        print('Помилка з\'єднання:', e)
    except Timeout as e:
        print('Часова помилка:', e)
    except Exception as e:
        print('Невідома помилка:', e)

"""{'photos': 
    [
        {
         'id': 102693, 
         'sol': 1000,
         'camera': {'id': 20, 'name': 'FHAZ', 'rover_id': 5, 'full_name': 'Front Hazard Avoidance Camera'}, 
         'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG', 
         'earth_date': '2015-05-30', 
         'rover': {'id': 5, 'name': 'Curiosity', 'landing_date': '2012-08-06', 'launch_date': '2011-11-26', 'status': 'active'}
         },
          
         {'id': 102694, 'sol': 1000, 
          'camera': {'id': 20, 'name': 'FHAZ', 'rover_id': 5, 'full_name': 'Front Hazard Avoidance Camera'},
           'img_src': 'http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FRB_486265257EDR_F0481570FHAZ00323M_.JPG', 
           'earth_date': '2015-05-30', 
           'rover': {'id': 5, 'name': 'Curiosity', 'landing_date': '2012-08-06', 'launch_date': '2011-11-26', 'status': 'active'}
           }
    ]
}"""

   
def directory():
    #визначаємо папку куди зберігати фото, якщо не існує то створємо папку
    #!!! Не використувати абсолютні шляхи directory = Path(r'C:\Users\dmytr\OneDrive\Desktop\LYUBA\Hillel\aqa_070225\lesson_18\Mars photos')
    #directory = Path.home()/"Mars photos"  #домашня папка C:\Users\dmytr\Mars photos
    my_directory = Path(__file__).parent/"Mars photos"
    if my_directory.exists():
        pass
    else:
        my_directory.mkdir()
    return my_directory

def check_number_of_pic(url, params):
    #підраховує кількість картинок за заданими параметрами
    data = get_data_in_json(url, params)
    try:
        count = len(data["photos"])
        return count
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0

def verify_if_download_all(pic_count):
    # уточнює в юзера чи завантажувати картинки якщо їх більше 5, якщо картинок менще 5 автоматично їх завантажуємо
    if pic_count<=5:
        print(f"{pic_count} pictures will be downloaded")
        return True
    else:
        user_decision = input(f" Do you want to download {pic_count} pictures? enter Y or N?")
        while True:
            if user_decision.upper() == "Y":
                return True
            elif user_decision.upper() == "N":
                print("Download canceled ")
                return False
            else: 
                user_decision = input(f" Do you want to download {pic_count} pictures? Y/N?")

def get_links(url, params):
    # шукаємо список посилань на картинки
    json_data = get_data_in_json(url, params)
    links = []
    for photo in json_data['photos']:
        links.append(photo['img_src'])
    return links
   
def save_pic(url, params):
    #функція зберігає картинки    
    pic_number = 1
    pic_count = check_number_of_pic(url, params)
    if pic_count<1:
        print("No pictures found")
    else:
        save_user_decision = verify_if_download_all(pic_count)
        if save_user_decision:
            links = get_links(url, params)
            for link in links:
                response = requests.get(link)
                with open(directory() / f"mars_photo{pic_number}.jpg", 'wb') as file:
                    file.write(response.content)
                    print(f"Picture mars_photo{pic_number}.jpg is downloaded")
                    pic_number+=1
                    print(f"Picture link {link}")

   
if __name__ == "__main__":
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol': 1001, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
   # params = {'sol': 1001, 'api_key': 'DEMO_KEY'}
   
    save_pic(url, params)