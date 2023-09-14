from fastapi import FastAPI

from db.db_setup import engine
import person
import person_model

person_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(person.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}