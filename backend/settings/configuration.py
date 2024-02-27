from dotenv import dotenv_values
from typing import List
values = dotenv_values()


class Config:
    DB_CONNECTION: str = values['DB_CONNECTION']
    DB_MODELS: List[str] = ['api.models']
