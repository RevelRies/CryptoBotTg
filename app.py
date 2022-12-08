import pydantic_models
import database
import config
import fastapi

api = fastapi.FastAPI()

@api.get('/')
def start():
    return {'message': 'This is message fo "/" way'}


@api.get('/hello')
def hello():
    return 'hello'


@api.get('/about/us')
def about():
    return {'message': 'I`m a champion'}


@api.get('/user/')
def user(skip: int = 0, limit: int = 10):
    return fake_database['users'][skip: skip + limit]


@api.get('/user/{user_id}')
def user_id(user_id: int, req: str | None=None):



fake_database = {'users':[
    {
        "id":1,             # тут тип данных - число
        "name":"Anna",      # тут строка
        "nick":"Anny42",    # и тут
        "balance": 15300    # а тут float
     },

    {
        "id":2,             # у второго пользователя
        "name":"Dima",      # такие же
        "nick":"dimon2319", # типы
        "balance": 160.23     # данных
     }
    ,{
        "id":3,             # у третьего
        "name":"Vladimir",  # юзера
        "nick":"Vova777",   # мы специально сделаем
        "balance": "25000"     # нестандартный тип данных в его балансе
     }
],}


@api.get('/get_info_by_user_id/{id:int}')
def user_info(id):
    return fake_database['users'][id - 1]


@api.get('/get_user_balance_by_id/{id:int}')
def user_balance(id):
    return fake_database['users'][id - 1]['balance']


@api.get('/get_total_balance')
def total_balance():
    tot_bal = sum([pydantic_models.User(**user).balance for user in fake_database['users']])
    return tot_bal

