from fastapi import FastAPI, Path


app = FastAPI()


@app.get('/')
async def root() -> str:
    return 'Главная страница'


@app.get('/user/{username}/{age}')
async def name_age(username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
                   age: int = Path(ge=18, le=120, description='Enter age', example='25')) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


@app.get('/user/admin')
async def admin() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def id_(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='13')) -> str:
    return f'Вы вошли как пользователь № {user_id}'


# uvicorn module_16_2:app --reload
