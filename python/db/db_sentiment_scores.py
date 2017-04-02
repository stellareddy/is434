import pymysql as mysql

config = {
'user': 'root',
'password': 'admin',
'host': 'localhost',
'database': 'dhl'
}
    # a = conn.cursor()
    # sql = ''
    # a.execute(sql)

try:
    cnx = mysql.connect(
        user='root',
        password= 'admin',
        host = '127.0.0.1',
        port = 3306,
        database= 'dhl',
        charset='utf8mb4',
        cursorclass=mysql.cursors.DictCursor
    )
    cursor = cnx.cursor()
    #SQL Codes
    #Eg: readContactPerson = "select * from contactmanagerapplication.contactperson"
    cnx.commit()
    query1 = "SELECT * from `corporate_buzz`"
    cursor.execute(query1)
    #e.g. #specify the attributes that you want to display
    for row in cursor:
        result = row
        print(result)
        #print(result['brand'])
        #print(result['source'])
        #print(result['datetime'])
        #print(result['score'])
    cnx.commit()
except mysql.Error as err:
        print(err)
else:
    cursor.close()
    cnx.close()