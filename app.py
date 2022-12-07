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
