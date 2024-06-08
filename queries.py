from HAEstates import db_cursor, conn
from HAEstates.models import Produce, Property


# SELECT QUERIES

def get_produce_by_filters(category=None, item=None, variety=None,
                           farmer_pk=None, farmer_name=None, price=None):
    sql = """
    SELECT * FROM vw_produce
    WHERE
    """
    conditionals = []
    if category:
        conditionals.append(f"category='{category}'")
    if item:
        conditionals.append(f"item='{item}'")
    if variety:
        conditionals.append(f"variety = '{variety}'")
    if farmer_pk:
        conditionals.append(f"farmer_pk = '{farmer_pk}'")
    if farmer_name:
        conditionals.append(f"farmer_name LIKE '%{farmer_name}%'")
    if price:
        conditionals.append(f"price <= {price}")

    args_str = ' AND '.join(conditionals)
    order = " ORDER BY price "
    db_cursor.execute(sql + args_str + order)
    produce = [Produce(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
    return produce

