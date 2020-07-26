import pyodbc

class Database(object):
    def _init_(self):
        server = 'TRIBUT3\MSSQLSERVER01'
        database = 'Lego_Store'
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' 
                          + server + '; DATABASE=' + database +
                          '; Trusted_connection=yes;')
        self.cursor = cnxn.cursor()

