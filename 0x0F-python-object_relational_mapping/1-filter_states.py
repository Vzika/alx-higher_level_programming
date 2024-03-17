#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
Use (source maintest/0-select_states.sql) to load into the MySQL Server
Execute by (./0-select_states.py username password database_name)
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    cursor = conn.cursor()
    query = ('SELECT * FROM states '
            'WHERE states.name LIKE BINARY "N%" '
            'ORDER BY states.id ASC')
    cursor.execute(query)
    results = cursor.fetchall()
    
    for row in results:
    print(row)
    
    cursor.close()
    conn.close()