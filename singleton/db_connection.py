from i_connection import IConnection

class DBConnection(IConnection):

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def get_session(self):
        return "Database session is active"