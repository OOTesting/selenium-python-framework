import pandas as pd
from typing import List, Dict
from models import User

"""
Read data from test data sheet
"""
def import_user(file_name: str = None, sheet_name: str = None) -> List[User]:
    if sheet_name is None:
        df = pd.read_excel(file_name)
    else:
        df = pd.read_excel(file_name, sheet_name=sheet_name)
    users_dict: List[Dict[str, str]] = df.astype(str).to_dict(orient='records')
    return [User(**user_data) for user_data in users_dict]