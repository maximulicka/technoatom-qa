from faker import Faker

from orm.model import ProjectTable
from orm.orm_client import MysqlOrmConnection

fake = Faker(locale='ru_RU')


class MysqlOrmBuilder:

    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = connection.connection.engine
        self.table = ProjectTable

    def del_user(self, username):
        return self.connection.session.query(self.table).filter_by(username=username).delete()

    def get_access(self, username):
        return self.connection.session.query(self.table).filter_by(username=username).first()
