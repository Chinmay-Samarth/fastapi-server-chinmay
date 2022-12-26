from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import dist.model as model
from datetime import datetime
from dist.database import engine, sessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import sql


app = FastAPI()

origins = ['http://localhost:4200','https://webof100.firebaseapp.com/']

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:4200','https://webof100.firebaseapp.com/','http://localhost:4200','https://webof100.firebaseapp.com/'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model.base.metadata.create_all(bind=engine)



d = sql.sqltypes.DATE

def get_db():
    try :
        db = sessionLocal()
        yield db
    except:
        print('problem')
    finally:
        db.close()


class Person(BaseModel):
    name: str
    phone: int
    amount: int

class transact(BaseModel):
    id:int
    date:str

@app.get('/password')
async def throw():
    return 250100

@app.get('/user/{username}')
def give_all_records(username:str, db:Session = Depends(get_db)):
    userId = db.query(model.web_of_100.id).filter(username == model.web_of_100.name).first()
    if userId is None:
        raise HTTPException(404, {'error':'person not found'})
    userId = list(userId).pop()
    _ = db.query(model.web_of_100.amount).filter(userId == model.web_of_100.id).first()
    _ = list(_).pop()

    
    amounts = db.query(model.web_amount).filter(userId == model.web_amount.id).all()
    i = 1
    for person in amounts:
        person.no = i
        person.am = _ / 100;
        i+=1
    
    return amounts

@app.get('/transact')
def throw_all_transaction(db:Session = Depends(get_db)):
    return db.query(model.web_amount.transaction_id,model.web_of_100.amount,model.web_of_100.name,model.web_of_100.phone,model.web_amount.submit_date).select_from(model.web_amount).join(model.web_of_100, model.web_amount.id == model.web_of_100.id).all()

@app.get('/user')
def throwUsers(db:Session = Depends(get_db)):
    return db.query(model.web_of_100).all()

@app.post('/transact/{username}')
def save_record(username:str, db:Session = Depends(get_db)):
    user_id = db.query(model.web_of_100.id).filter(username == model.web_of_100.name).first()

    if user_id is None:
        raise HTTPException(
            status_code=404,
            detail={'error':'user not found'}
        )
    amount_model = model.web_amount()
    amount_model.id = list(user_id).pop()
    amount_model.submit_date = datetime.date(datetime.now())

    db.add(amount_model)
    db.commit()

@app.post('/user')
def save_person(user:Person, db:Session = Depends(get_db)):
    person_model = db.query(model.web_of_100).filter(model.web_of_100.name == user.name).all()

    person_model = model.web_of_100()
    person_model.name = user.name
    person_model.phone = user.phone
    person_model.amount = user.amount

    db.add(person_model)
    db.commit()


@app.delete('/transact/{transaction_id}')
def deleteTransaction(transaction_id:int, db:Session = Depends(get_db)):
    transact = db.query(model.web_amount).filter(model.web_amount.transaction_id == transaction_id).first()

    if transact is None:
        raise HTTPException(
            status_code=404,
            detail={'error':'transaction not found'}
        )

    db.query(model.web_amount).filter(model.web_amount.transaction_id == transaction_id).delete()

    db.commit()


@app.delete('/delete-user/{user_id}')
def deletePerson(user_id:int, db:Session = Depends(get_db)):
    person_model = db.query(model.web_of_100).filter(model.web_of_100.id == user_id).first()

    if person_model is None:
        raise HTTPException(
            status_code=404,
            detail={'error':'user not found'}
        )
    db.query(model.web_of_100).filter(model.web_of_100.id == user_id).delete()
    db.query(model.web_amount).filter(model.web_amount.id == user_id).delete()

    db.commit()

@app.put('/update-transact')
def updateAmount(record:transact,db:Session = Depends(get_db)):

    amount_model = db.query(model.web_amount).filter(record.id == model.web_amount.transaction_id).first()
    print(amount_model)
    if amount_model is None:
        raise HTTPException(status_code=404, detail={'error':'transaction not found'})

    da = datetime.strptime(record.date,'%d-%m-%Y')
    db.query(model.web_amount).filter(record.id == model.web_amount.transaction_id).update({'submit_date':da})
    db.commit()



@app.delete('/tr')
def delete(db:Session =Depends(get_db)):
    db.query(model.web_amount).delete()
    db.commit()



@app.put('/update-user/{user_id}')
def updateUser(user_id:int, person:Person, db:Session = Depends(get_db)): 

    person_id = db.query(model.web_of_100.id).filter(user_id == model.web_of_100.id).first()

    if person_id is None:
        raise HTTPException(status_code=404, detail={'error':'person not found'})
    
    person_model = db.query(model.web_of_100).filter(user_id == model.web_of_100.id).first()

    person_model.name = person.name
    person_model.phone = person.phone
    person_model.amount = person.amount

    db.query(model.web_of_100).filter(user_id == model.web_of_100.id).update({'name':person.name,'phone':person.phone,'amount':person.amount})
    db.commit()



@app.delete('/de')
def delete_alec(db:Session = Depends(get_db)):
    db.query(model.web_of_100).filter(model.web_of_100.id == 3).delete()
    db.commit()


