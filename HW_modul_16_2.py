from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()

@app.get('/')
async def Get_Main_Page():
    return 'Главная страница'

@app.get('/user/admin')
async def Get_Admin_Page():
    return 'Вы вошли как администратор'

@app.get('/user/{userID}')
async def Get_User_Number(userID:Annotated[int, Path(ge=1, le=100, description='Enter your id', example='75')]):
    return f'Вы вошли как пользователь №{userID}'

@app.get('/user/{username}/{age}')
async def Get_User_Info(username:Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
      age:Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    return f'Информация о пользователе. Имя {username}, возраст {age}'
