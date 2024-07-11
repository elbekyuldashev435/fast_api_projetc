from conf.database import engine, Base
from conf.models import User


Base.metadata.create_all(bind=engine)