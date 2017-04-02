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
    query1 = "SELECT * from `brand_comentions`"
    cursor.execute(query1)
    result = ""
    #e.g. #specify the attributes that you want to display
    for row in cursor:
        result = row
        print(result)
        #print(result['first_brand'])
        #print(result['second_brand'])
        #print(result['source'])
        #print(result['count'])
    cnx.commit()

    def print_result():
        return result

except mysql.Error as err:
        print(err)
else:
    cursor.close()
    cnx.close()