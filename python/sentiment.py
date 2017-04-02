#  ID and name from the nodes.csv file using the usecols attribute in the 'object' format

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
    query1 = "SELECT ss.brand, ss.source, date_format(ss.datetime, '%Y-%m') as date, COUNT(CASE WHEN ss.score > 0 " \
             "THEN 1 END) AS poscount, COUNT(CASE WHEN ss.score = 0 THEN 1 END) AS neucount, COUNT(CASE WHEN  " \
             "ss.score< 0 THEN 1 END) AS negcount, count(ss.brand) as buzztotal  " \
             "FROM sentiment_scores ss WHERE ss.datetime > date_sub(NOW(),INTERVAL 1 year) Group by ss.brand, " \
             "ss.source, date_format(ss.datetime, '%Y-%m')" \
             " order by ss.brand, date;"
    cursor.execute(query1)
    for row in cursor:
        brandsource = row['brand'] + " " + row['source']
        brand = row['brand']
        totalcount = row['buzztotal']
        poscount = row['poscount'] / totalcount * 100
        negcount = row['negcount'] / totalcount * 100
        neucount = row['neucount'] / totalcount * 100
        date = row['date']
        for i in range(len(result)):
            if (result[i][0] == brandsource):
                # if brand source exist, append [date], [score], [count]
                result[i][1].append(date)
                result[i][2].append("Positive: " + str("%.2f" % poscount) + "%    " + "Neutral: "
                                    + str("%.2f" % neucount) + "%    "
                                    + "Negative: " + str("%.2f" % negcount) + "%")
                result[i][3].append(totalcount)
                break
        else:
            # {"BrandName + source", [date] --> X axis, [score] --> Label , [count] --> y axis}
            addToResult = [brandsource, [], [],[], brand]
            addToResult[1].append(date)
            addToResult[2].append("Positive: " + str("%.2f" % poscount) + "%     " + "Neutral: "
                                  + str("%.2f" % neucount) + "%     "
                                  + "Negative: " + str("%.2f" % negcount) + "%")
            addToResult[3].append(totalcount)
            result.append(addToResult)

    cnx.commit()
    print(result)

    with open('../static/json/sentimentdata.json', 'w') as f:
        json.dump(result, f)

except mysql.Error as err:
        print(err)
else:
    cursor.close()
    cnx.close()
