class BaseDB:
    def __init__(self, name, db_type):
        self.name = name
        self.type = db_type


class PostgresDB(BaseDB):
    pass


class MongoDB(BaseDB):
    pass