from pythed.app.utils import config_functions
from pythed.app.api import *

try:
    brands_data: dict = config_functions.read_json("../config/brands.json")
except Exception as e:
    raise Exception(e)

def filter_brand(brand_id:int = None, name:str = None, is_luxury:bool = None, authenticity_check_required:bool = None):
    filtered = []
    
    args = check_params(brand_id=brand_id, name=name, is_luxury=is_luxury, authenticity_check_required=authenticity_check_required)
    
    if len(args) == 0:
        raise Exception("Error: no params were given. ❌")
    
    for brand in brands_data:
        if brand_id and brand["id"] == brand_id:
            filtered.append(brand)
        if name and name.lower() in brand["slug"]:
            filtered.append(brand)
        if is_luxury and brand["is_luxury"] == is_luxury:
            filtered.append(brand)
        if authenticity_check_required and brand["requires_authenticity_check"] == authenticity_check_required:
            filtered.append(brand)
        
    return filtered[0]

def get_brands():
    try:
        return brands_data
    except Exception as e:
        raise Exception(e)
    
def get_multiple_brands(names: list = []):
    brands = []
    
    for brand in names:
        brands.append(filter_brand(name=brand))
        
    return brands