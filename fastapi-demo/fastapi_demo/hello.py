from fastapi import FastAPI, HTTPException
from .data.models import ItemPayload

app = FastAPI()

# key is item_id
grocery_list: dict[int, ItemPayload] = {}


@app.get("/")
def root():
    return {'message': '你好'}


@app.get("/items/{item_name}/{quantity}")
def add_item(item_name: str, quantity: int):
    print('调用了')
    if quantity <= 0:
        raise HTTPException(status_code=401, detail=f"Invalid quantity '{quantity}': must be positive")
    
    item_name_id_map: dict[str, int] = {
        item.item_name: (
            item.item_id if item.item_id is not None 
            else 0
        ) 
        for item in grocery_list.values()
    }

    if item_name in item_name_id_map.keys():
        item_id: int = item_name_id_map[item_name]
        grocery_list[item_id].quantity += quantity
    else:
        item_id = max(grocery_list.keys()) + 1 if grocery_list else 0
        item = ItemPayload(item_id = item_id, item_name=item_name, quantity=quantity)
        grocery_list[item_id] = item

    return {'item': grocery_list[item_id]}