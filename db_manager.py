from databases import PostgresDB, MongoDB


class DBManager:

    def __init__(self, db):
        self.db = db

    def run(self):
        self.db_checker()
        self.logger()

    def db_checker(self):

        if self.db.name == "postgres":
            self.logger()

        else:
            self.logger()

    def logger(self):
        print(f"{self.db.name}: çalıştırıldı")


postgres = PostgresDB("postgres", "sql")
mongo = MongoDB("mongo", "nosql")
db_manager = DBManager(mongo)
db_manager.run()