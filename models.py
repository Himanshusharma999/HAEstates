from typing import Dict

from flask_login import UserMixin
from psycopg2 import sql

from HAEstates import login_manager, db_cursor, conn, app


@login_manager.user_loader
def load_user(user_id):
    user_sql = sql.SQL("""
    SELECT * FROM Users
    WHERE pk = %s
    """).format(sql.Identifier('pk'))

    db_cursor.execute(user_sql, (int(user_id),))
    return User(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None


class ModelUserMixin(dict, UserMixin):
    @property
    def id(self):
        return self.pk


class ModelMixin(dict):
    pass


if __name__ == '__main__':
    user_data = dict(full_name='a', user_name='b', password='c')
    user = Farmer(user_data)
    print(user)


class Produce(ModelMixin):
    def __init__(self, produce_data: Dict):
        super(Produce, self).__init__(produce_data)
        self.pk = produce_data.get('pk')
        self.category = produce_data.get('category')
        self.item = produce_data.get('item')
        self.unit = produce_data.get('unit')
        self.variety = produce_data.get('variety')
        self.price = produce_data.get('price')
        # From JOIN w/ Sell relation
        self.available = produce_data.get('available')
        self.farmer_name = produce_data.get('farmer_name')
        self.farmer_pk = produce_data.get('farmer_pk')


class Property(ModelMixin):
    def __init__(self, property_data: Dict):
        super(Property, self).__init__(property_data)
        self.pk = property_data.get('pk')
        self.text = property_data.get('text')
        self.beds = property_data.get('beds')
        self.baths = property_data.get('baths')
        self.type = property_data.get('type')
        self.garage = property_data.get('garage')
        self.sqrf = property_data.get('sqrf')
        self.listPrice = property_data.get('listPrice')
        self.stories = property_data.get('stories')
        self.year_built = property_data.get('year_built')