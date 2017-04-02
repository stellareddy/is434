import pymysql as mysql
import json

result = [];

try:
    cnx = mysql.connect(
        user='root',
        password= 'admin',
        host = '127.0.0.1',
        port = 3306,
        database= 'dhl_luxury_fashion',
        charset='utf8mb4',
        cursorclass=mysql.cursors.DictCursor
    )
    cursor = cnx.cursor()
    #SQL Codes
    cnx.commit()
    query1 = "SELECT first_brand, second_brand, SUM(count) as counter FROM brand_comentions GROUP BY first_brand, " \
             "second_brand;"
    cursor.execute(query1)
    for row in cursor:
        brandLine = row['first_brand']
        lineBrands = row['second_brand']
        count = int(row['counter'])

        for i in range(len(result)):
            if (result[i][0] == brandLine):
                result[i][1].append(lineBrands)
                result[i][2].append(str(count))
                if count < 10: # For sizing of bubbles
                    result[i][3].append(str(10))
                else:
                    result[i][3].append(str(count*3))
                #add another side in..
                for x in range(len(result)):
                    if (result[x][0] == lineBrands):
                        result[x][1].append(brandLine)
                        result[x][2].append(str(count))
                        if count < 10: # For sizing of bubbles
                            result[x][3].append(str(10))
                        else:
                            result[x][3].append(str(count*3))
                        break
                else:
                    addToResult = [lineBrands, [], [], []]
                    addToResult[1].append(brandLine)
                    addToResult[2].append(str(count))
                    if count < 10:
                        addToResult[3].append(str(10))
                    else:
                        addToResult[3].append(str(count * 3))
                    result.append(addToResult)
                break
        else:
            # 1st brand, [2nd brand], count, size
            addToResult = [brandLine, [], [],[]]
            addToResult[1].append(lineBrands)
            addToResult[2].append(str(count))

            addToResult2 = [lineBrands, [], [],[]]
            addToResult2[1].append(brandLine)
            addToResult2[2].append(str(count))
            if count < 10:
                addToResult[3].append(str(10))
                addToResult2[3].append(str(10))
            else:
                addToResult[3].append(str(count * 3))
                addToResult2[3].append(str(count * 3))

            result.append(addToResult)
            result.append(addToResult2)

    cnx.commit()
    print(result)

    with open('../static/json/branddata.json', 'w') as f:
        json.dump(result, f)

except mysql.Error as err:
        print(err)
else:
    cursor.close()
    cnx.close()

# Brand names