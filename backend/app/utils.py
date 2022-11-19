import models as _model
import schema as _schema
import sqlalchemy.orm as _orm

# Getting a user
def get_user(db: None, user_id: int):
    # return a instance of the user
    return db.query(_model.user).filter(_model.user.id == user_id).first()

# Update the user
# db = database.Session since it not present yet
def update_user(db: None, user:_schema.user_update, user_id: int):
    # Getting the current user
    db_user = get_user(
        # db = _orm.session,
        user_id=user_id
        )
    db_user.email = user.email
    db_user.username = user.username
    db_user.companyName = user.companyName
    db.commit()
    db.refresh(db_user)
    return db_user