from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel
import uvicorn
from data_interactor import Interactor


class UserContact(BaseModel):
    first_name:str
    last_name:str
    phone_number:str

interactor = Interactor()
app = FastAPI()

@app.post("/contacts")
def create_contact(data:UserContact):
    try:
         result = interactor.create_contact({"first_name":data.first_name,
                    "last_name":data.last_name,"phone_number":data.phone_number})
         return {"the creation was successfully created. the id number is:":result}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)


@app.get("/contacts")
def get_all_contacts():
    try:
        result = interactor.get_all_contacts()
        return result

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)


@app.put("/contacts/{id}")
def update_contact(id,data:UserContact):
    try:
        result = interactor.update_contact(id,{"first_name":data.first_name,
                        "last_name":data.last_name,"phone_number":data.phone_number})
        return {"the update was successful":result}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)


@app.delete("/contacts/{id}")
def delete_contact(id):
    try:
        result = interactor.delete_contact(id)
        return {"the delete was successful": result}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500)
