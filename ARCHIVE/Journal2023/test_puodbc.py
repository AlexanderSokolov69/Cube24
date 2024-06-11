import pyodbc

cnxn = pyodbc.connect('driver={SQLite3 ODBC driver};'
                      'database=db/database_J2023.db;'
                      'trusted_consnection=yes')
