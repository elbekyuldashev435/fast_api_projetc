from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    is_staff: bool = False
    is_active: bool = True


class PasswordSchema(UserSchema):
    password: str

    class Config:
        from_attributes = True


class Setting(BaseModel):
    jwt_secret_key = str = "7515d6035a89a17c6dd889d6be6cd3ea6edf75723a08215e3b226b23cd5c8fbb"