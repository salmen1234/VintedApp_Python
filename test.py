from pythed.app import Vinted

app = Vinted.Vinted()

brands = app.get_brands(brand_names=["Jordan", "Nike"])
brand1 = brands[0]["id"]
brand2 = brands[1]["id"]

items = app.search_items(search_text="sneakers", perPage=1, brand_ids=[brand1, brand2], price_to=15, order="newest_first")

print(items)