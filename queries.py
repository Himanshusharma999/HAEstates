from HAEstates import db_cursor, conn
from HAEstates.models import Produce, Property


# SELECT QUERIES
def get_property_by_filters(type=None, beds=None, baths=None, stories=None, sold_by=None, price=None):
    sql = """
    SELECT * FROM vw_property
    WHERE
    """
    conditionals = []
    if type:
        conditionals.append(f"type='{type}'")
    if beds:
        conditionals.append(f"beds={beds}")
    if baths:
        conditionals.append(f"baths={baths}")
    if stories:
        conditionals.append(f"stories={stories}")
    if sold_by:
        conditionals.append(f"sold_by={sold_by}")
    if price:
        conditionals.append(f"price <= {price}")

    args_str = ' AND '.join(conditionals)
    order = " ORDER BY price "
    db_cursor.execute(sql + args_str + order)
    property = [Property(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
    return property
