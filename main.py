# from fastapi import FastAPI , status,HTTPException
# from pydantic import BaseModel

# class Item(BaseModel):
#     title: str
#     content: str
#     id: int

# app = FastAPI()

# data = [
#     {"id":1,"title": "sports", "content": "i like cricket "},
#     {"id":2,"title": "fruits", "content": "it,s good for health "},
# ]

# def find_single_data(id):
#     for item in data:
#         if item["id"] == id:
#             return {"data": item}
    
# @app.post("/posts" , status_code=status.HTTP_201_CREATED)

# async def create_post(item: Item  ):
#     global next_id 
#     data.append(item.dict())  #  dictionary conversion
#     return {"data": data}

# @app.get("/get")  
# async def get_data():
#     return {"data": data}

# @app.get("/get/{item_id}")
# async def get_single_data(item_id : int  ):

#     single_data = find_single_data(item_id)

#     if not single_data:
       
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , detail = f"data with id {item_id} not found " )

#     return{"single_data":single_data}


from fastapi import FastAPI , status , HTTPException
from pydantic import BaseModel
app=FastAPI()


data_list = [
  
  {"title":"sports","content":"i like to play cricket ","id":1},
  {"title":"fruits","content":"it,s good for health ","id":2}

            ]

# post method 

class Item(BaseModel):
  title:str
  content:str
  id:int


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(item:Item):
  data_list.append(item.model_dump())
  
  return {"post":item}


#get method 

@app.get("/get") 

async def get_posts():
  return{"data":data_list}

#get data with specific id 

def find_single_data(id):
    for item in data_list:
        if item["id"] == id:
            return {"data": item}



@app.get("/get/{id}")
async def get_single_data(id : int  ):

    single_data = find_single_data(id)
    #HTTP Error handle 
    if not single_data:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"data with id {id} are not found ")

   

    return{"single_data":single_data}




