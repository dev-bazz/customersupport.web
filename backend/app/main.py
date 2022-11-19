from fastapi import FastAPI
import schema as _schema
import utils as _utils

app = FastAPI()


@app.put("/update_user/{user_id}", response_model=_schema.user_update)
def update_user(user: _schema.user_update, user_id: int):
    return _utils.update_user(user=user, user_id=user_id)
