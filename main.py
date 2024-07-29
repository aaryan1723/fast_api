from fastapi import FastAPI, Path, Query, Form, File, UploadFile, HTTPException
from typing import Optional
from enum import Enum
from typing import Union
from pydantic import BaseModel

class schema1(BaseModel):
    name:str
    Class:Optional[str]=None
    roll_no:int


app = FastAPI()

@app.get("/fast")
async def hello_world():
    return {"Hello": "from aaryan"}

@app.get("/hello")
async def world():
    return {"Hello": "how are you"}

@app.get("/item/{Item}")
def path_func(Item):
    var_name = {"path variable": Item}
    return {"var_name": Item}

@app.get("/query")
def path_func(name: str, roll_no: Union[str, None]= Query(default=None, min_length=3, max_length=3)):
    query_name = {"name": name, "roll_no": roll_no}
    return (query_name)

class choice_names (str, Enum):
    aaryan= "aaryan"
    one= "one"
    two= "two"
    

@app.get("/models/{model_name}")
async def get_model(model_name: choice_names):
    if model_name.value =="aaryan":
        return{"model_name": model_name, "message": "hii how are you"}
    if model_name.value =="one":
        return{"model_name": model_name, "message": "you chooses one"}
    else:
        return{"model_name": model_name, "message":"you chooses three" }
    


    
@app.post("/items/")
async def create_item(item: schema1):
    return item


@app.post("/form/data")
async def form_data (username : str = Form(...)):
    return {"username": username}

@app.post("/form/upload")
async def file_len_data (file : bytes = File()):
    return ({"file": len(file)})

@app.post("/upload/form")
async def file_upload (file : UploadFile):
    return ({"file": file})

items = [1,2,3,4,5,6]
@app.get("/error/handling")
async def error_handling (item : int):
    if item not in items:
        return HTTPException (status_code= 400 , detail= "iteam is not in the range")
    return {"value" : item}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    