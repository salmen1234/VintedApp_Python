import sys
from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent.parent.parent.parent.__str__()
sys.path.append(ROOT_DIR)
from src.app.utils import cookies
from src.app.api.items import search, similar_items
from src.app.api.shipping_details import get_shipping_details
import unittest

auth = cookies.load_auth_cookie()

c = {
   auth[0]: auth[1]
}    

class TestSearch(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.response = search(cookies=c, page=1, query='Jordan')

    def test_failure(self):   
        with self.assertRaises(Exception):
            search()
            
    def test_success(self):
        self.assertIsInstance(self.response, dict)                  
    
class TestSimilarItems(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.response = similar_items(cookies=c, item_id="4596703874")  

    def test_failure(self):
        with self.assertRaises(Exception):
            similar_items()
            
    def test_success(self):
        self.assertIsInstance(self.response, dict)                  
       
class TestGetShippingDetails(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.response = get_shipping_details(cookies=c, item_id="4596703874")  

    def test_failure(self):
        with self.assertRaises(Exception):
            get_shipping_details()
            
    def test_success(self):
        self.assertIsInstance(self.response, dict)        
 
if __name__ == "__main__":
    unittest.main()