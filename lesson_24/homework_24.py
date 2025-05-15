import logging
import pytest
import requests
from pathlib import Path

# логер для запису в файл
logger = logging.getLogger("file_logger")
file_handler = logging.FileHandler(Path(__file__).parent / 'test_search.log', encoding="utf8")
file_handler.setFormatter(logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

PORT = 8080
BASE_URL = f"http://127.0.0.1:{PORT}"



class TestClass():
    def test_get_car(self, get_token, test_data):
        
        headers = {
            "Authorization": f"Bearer {get_token}"  
        }    
        sort_by, limit = test_data
        params = {"sort_by": sort_by, "limit": limit}
        r = requests.get(f'{BASE_URL}/cars',  headers=headers, params=params)
        
        try:
            assert r.status_code == 200
        except AssertionError:
            logger.error(f"Test fail. Status code { r.status_code}, limit= {limit} | sort_by={sort_by}")   
            pytest.fail(f"Test fail. Status code { r.status_code}") 
            
        try:
            count = len(r.json())
        except ValueError:
            logger.error("Can't read json")
            pytest.fail("Can't read json")    
        
        if not limit:
            limit= count
        
        if count > limit:
            logger.error(f"Test fail. Got {count}, expected <= {test_data[1]} | sort_by={test_data[0]}")
        else:
            logger.info(f'Test passed. Limit: {test_data[1]} |  sort_by: {test_data[0]}') 
            
        assert count <= limit
