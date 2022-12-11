import pydantic_models
import database
import config
import fastapi
from fastapi import Request

api = fastapi.FastAPI()


@api.get('/users')
def user(skip: int = 0, limit: int = 10):
    return fake_database['users'][skip: skip + limit]




fake_database = {'users':[
    {
        "id":1,
        "name":"Anna",
        "nick":"Anny42",
        "balance": 15300
     },

    {
        "id":2,
        "name":"Dima",
        "nick":"dimon2319",
        "balance": 160.23
     },
    {
        "id":3,
        "name":"Vladimir",
        "nick":"Vova777",
        "balance": 200.1
     }
    ], }


@api.get('/get_info_by_user_id/{id:int}')
def user_info():
    for indx, user in enumerate(fake_database['users']):
        if user_id == user['id']:
            return fake_database['users'][indx]


@api.get('/get_user_balance_by_id/{id:int}')
def user_balance():
    for indx, user in enumerate(fake_database['users']):
        if user_id == user['id']:
            return fake_database['users'][indx]['balance']


@api.get('/get_total_balance')
def total_balance():
    tot_bal = sum([pydantic_models.User(**user).balance for user in fake_database['users']])
    return tot_bal


@api.post('/user/create')
def add_user(user: pydantic_models.User):
    fake_database['users'].append(user)
    return {'user_add': user}


@api.put('/user/{user_id}')
def update_user(user_id: int, new_user: pydantic_models.User = fastapi.Body()):
    for indx, user in enumerate(fake_database['users']):
        if user['id'] == user_id:
            fake_database['users'][indx] = new_user
            return 'update_user done'


@api.delete('/user/{user_id}')
def delete_user(user_id: int):
    for indx, user in enumerate(fake_database['users']):
        if user_id == user['id']:
            del fake_database['users'][indx]
            return 'delete complete'