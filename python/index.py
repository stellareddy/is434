import pymysql as mysql
import json

#result.append([brand], [count], [size], [color.pop(0)], [text])
result = [];
result2 = [];
color = ['red','blue','green','orange','grey','purple','cyan','lightpink','lime','navy']

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
    query1 = "SELECT ibt.brands_mentioned as brand, count(*) as count, category, revenue_in_million_usd FROM " \
             "individual_buzz_twitter ibt JOIN company_information ci ON " \
             "ibt.brands_mentioned = ci.company_name WHERE brands_mentioned = 'chanel' OR brands_mentioned = 'gucci' " \
             "OR brands_mentioned = 'hermes' OR brands_mentioned = 'coach' OR brands_mentioned = 'louis_vuitton' OR " \
             "brands_mentioned = 'kate_spade' OR brands_mentioned = 'prada' OR brands_mentioned = 'calvin_klein' OR " \
             "brands_mentioned = 'longchamp' OR brands_mentioned = 'michael_kors' GROUP BY ibt.brands_mentioned " \
             "ORDER BY category, revenue_in_million_usd;"
    cursor.execute(query1)
    for row in cursor:
        brand = row['brand']
        count = row['count']
        category = row['category']
        revenue = row['revenue_in_million_usd']
        size = int(revenue/100)
        text = "Category: "+category+"<br>Brand: "+ str(brand)+"<br>Revenue(USD): "+ str(revenue)+" million"
        result.append([brand, count, size, color.pop(0), text, category])

    query2 = "SELECT cb.brand, count(*) as count FROM corporate_buzz cb GROUP BY cb.brand;"
    cursor.execute(query2)
    for row in cursor:
        brand = row['brand']
        count = row['count']
        for i in range(len(result)):
            if (result[i][0] == brand):
                #add count to count...
                result[i][1] += count

    query3 = "SELECT cbf.brand, count(*) as count FROM corporate_buzz_facebook cbf GROUP BY cbf.brand;"
    cursor.execute(query3)
    for row in cursor:
        brand = row['brand']
        count = row['count']
        for i in range(len(result)):
            if (result[i][0] == brand):
                #add count to count...
                result[i][1] += count

    query4 = "SELECT ibf.brand, count(*) as count FROM individual_buzz_facebook ibf GROUP BY ibf.brand;"
    cursor.execute(query4)
    for row in cursor:
        brand = row['brand']
        count = row['count']
        for i in range(len(result)):
            if (result[i][0] == brand):
                #add count to count...
                result[i][1] += count

    query5 = "SELECT brand, date_format(datetime, '%Y-%m') as datetime, round(avg(score),0) as score " \
             "FROM corporate_buzz_facebook WHERE date_format(datetime, '%Y-%m') > '2004-02'" \
             "GROUP BY brand, date_format(datetime, '%Y-%m') ORDER BY brand, datetime;"
    cursor.execute(query5)
    for row in cursor:
        brand = row['brand']
        dt = str(row['datetime'])
        score = int(row['score'])
        for i in range(len(result2)):
            if (result2[i][0] == brand):
                result2[i][1].append(dt)
                result2[i][2].append(score)
                break;
        else:
            result2.append([brand, [dt], [score]])

    cnx.commit()
    result = sorted(result, key=lambda i: i[1])
    print(result)
    print(result2)

    with open('../static/json/brandsourcedata.json', 'w') as f:
        json.dump(result, f)
    with open('../static/json/corpfbsourcedata.json', 'w') as f:
        json.dump(result2, f)

except mysql.Error as err:
        print(err)
else:
    cursor.close()
    cnx.close()

# Social Buzz on the net for each brand from various sources