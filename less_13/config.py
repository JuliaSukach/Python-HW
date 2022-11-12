from pydantic import BaseModel, validator

from settings import *


class DbConfig(BaseModel):
    driver: str = 'postgresql'
    host: str
    port: int
    user: str
    pwd: str
    database: str

    class Config:
        allow_mutation = False

    @validator('port', pre=True)
    def check_port(cls, p):
        if p < 100:
            raise ValueError(f'Port must be greater than 100. Got {p}')
        return p

    @property
    def dsn(self):
        return f'{self.driver}://{self.user}:{self.pwd}@{self.host}:{self.port}/{self.database}'


db_conf = DbConfig(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    pwd=DB_PWD,
    database=DB_NAME
)