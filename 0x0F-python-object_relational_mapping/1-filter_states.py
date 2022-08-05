#!/usr/bin/python3
"""script that lists all states with a name starting with
 N (upper N) from the database hbtn_0e_0_usa"""


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

    cursor.execute("SELECT * FROM states\
                    WHERE name LIKE 'N%' ORDER BY id ASC;")

    m = cursor.fetchall()

    for row in m:
        print(row)

    cursor.close()
    db.close()
