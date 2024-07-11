from fastapi import FastAPI
from routers.auth_routers import auth_router
from fastapi_jwt_auth import AuthJWT
from conf.schemas import Setting


app = FastAPI()


@AuthJWT.load_config
def get_config():
    return Setting()


app.include_router(auth_router)