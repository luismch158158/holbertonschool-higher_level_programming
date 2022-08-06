#!/usr/bin/python3
"""script that takes in the name of a state as an argument and
lists all cities of that state,using the database hbtn_0e_4_usa"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    import re

    if (len(argv) != 5):

        print("You must be use mysql username, mysql password,\
               database name and state name")
        exit(1)

    argument = ' '.join(argv[4].split())

    if (re.search('^[a-zA-Z ]+$', argument) is None):
        print('Please enter a valid name State')
        exit(1)

    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])
    except Exception:
        print("Can't connect to database")
        exit(0)

    cursor = db.cursor()

    result_quantity = cursor.execute("SELECT cities.name FROM cities\
                    INNER JOIN states ON cities.state_id=states.id\
                    WHERE states.name = '{:s}'\
                    ORDER BY cities.id ASC;".format(argument))

    data_of_query = cursor.fetchall()

    final_array = []

    for i in range(result_quantity):
        final_array.append(data_of_query[i][0])

    print(', '.join(final_array))

    cursor.close()
    db.close()
