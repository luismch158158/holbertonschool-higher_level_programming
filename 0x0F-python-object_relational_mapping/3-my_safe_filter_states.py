#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument safe from MySQL Injections"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    import re

    if (len(argv) != 5):

        print("You must be use mysql username, mysql password,\
               database name and state name searched")
        exit(1)

    argument = ''.join(argv[4].split())

    if (re.search('^[a-zA-Z]+$', argument) is None):
        print('Please enter a valid name State')
        exit(1)

    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])
    except Exception:
        print("Can't connect to database")
        exit(0)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states\
                    WHERE name = '{:s}' ORDER BY id ASC;".format(argument))

    m = cursor.fetchall()

    for row in m:
        print(row)

    cursor.close()
    db.close()
