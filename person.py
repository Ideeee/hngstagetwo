from typing import Optional, List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_
from datetime import datetime

from person_model import Person
import person_schema as schemas
from db.db_setup import get_db

router = APIRouter(tags=['Person'])


@router.post('/api', status_code=201, response_model=schemas.Person)
def create_person(
    person : schemas.PersonBase,
    db: Session = Depends(get_db)
):
    existing = db.query(Person).filter(Person.name == person.name.lower()).first()

    if existing:
        raise HTTPException(status_code=400, detail='This user already exists')
    
    new_person = Person(
        name=person.name.lower(),
        city=person.city.lower(),
    )

    db.add(new_person)
    db.commit()
    db.refresh(new_person)

    return new_person

@router.get('/api', status_code=200, response_model=List[schemas.Person])
def get_people(
    db: Session = Depends(get_db)
):
    
    query = db.query(Person).all()

    # if user_id:

    #     query = b_query.filter(Person.id == user_id).first()

    #     if query is None:
    #         query = b_query.filter(Person.name == user_id).first()

    #     if query is None:
    #         raise HTTPException(404, "Resource Not Found")
        
    #     return query
    
    # query = b_query

    return query

@router.get('/api/{user_id}', status_code=200, response_model=schemas.Person)
def get_person_by_id(
    user_id : str,
    db: Session = Depends(get_db)
):
    if user_id.isdigit():
        query = db.query(Person).filter(Person.id == user_id).first()
    else:
        query = db.query(Person).filter(Person.name == user_id.lower()).first()

    if query is None:
        raise HTTPException(404, "Resource Not Found")
    
    return query
    
@router.patch('/api/{user_id}', status_code=200, response_model=schemas.Person)
def update_person(
    user_id : str,
    person_update : schemas.PersonBase,
    db: Session = Depends(get_db)
):
    if user_id.isdigit():
        person = db.query(Person).filter(Person.id == user_id).first()
    else:
        person = db.query(Person).filter(Person.name == user_id.lower()).first()

    if person is None:
        raise HTTPException(404, "Resource Not Found")
    
    person.name = person_update.name
    person.city = person_update.city if person_update.city else None

    db.commit()
    db.refresh(person)
    
    return person
    
@router.delete('/api/{user_id}', status_code=200)
def delete_person(
    user_id : str,
    db: Session = Depends(get_db)
):
    if user_id.isdigit():
        query = db.query(Person).filter(Person.id == user_id).first()
    else:
        query = db.query(Person).filter(Person.name == user_id.lower()).first()

    if query is None:
        raise HTTPException(404, "Resource Not Found")
    
    db.delete(query)
    db.commit()
    
    return "Resource has been deleted successfully"
    