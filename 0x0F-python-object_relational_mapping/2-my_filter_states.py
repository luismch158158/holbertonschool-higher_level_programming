#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])
    except Exception:
        print("Can't connect to database")
        exit(0)

    cursor = db.cursor()

    argument = argv[4]

    cursor.execute("SELECT * FROM states\
                    WHERE name = BINARY '{:s}'\
                    ORDER BY id ASC;".format(argument))

    m = cursor.fetchall()

    for row in m:
        print(row)

    cursor.close()
    db.close()
