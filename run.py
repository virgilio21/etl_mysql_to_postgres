from dbcontroller_mysql import Rents as RentsMysql
from dbcontroller_postgre import Rents as RentsPostgre, database_postgre


def _save_home(home_features, txn):
    """Save the obtained home in the DB"""

    rent = RentsPostgre.create(**home_features)


if __name__ == '__main__':

    rents_mysql = RentsMysql.select()

    rents_dict = [rent for rent in rents_mysql.dicts()]

        
    print(rents_dict)
    
    with database_postgre.atomic():
        RentsPostgre.insert_many(rents_dict).execute()




