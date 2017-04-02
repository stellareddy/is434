import networkx as nx
import matplotlib.pyplot as plt

import pymysql as mysql

config = {
'user': 'root',
'password': 'admin',
'host': 'localhost',
'database': 'dhl'
}

############################################################################
################################### MAIN ###################################
############################################################################

if __name__ == "__main__":
    # write to db
    conn = mysql.connect(
        user='root',
        password= 'admin',
        host = '127.0.0.1',
        port = 3306,
        database= 'dhl_luxury_fashion',
        charset='utf8mb4',
        cursorclass=mysql.cursors.DictCursor
    )

    cursor = conn.cursor()
    sql = 'SELECT * FROM brand_comentions'
    cursor.execute(sql)

    pairing_dictionary = {}

    for row in cursor:
        key = row['first_brand'] + "-" + row['second_brand']
        if key in pairing_dictionary:
            pairing_dictionary[key] += row['count']
        else:
            pairing_dictionary[key] = row['count']

    print(pairing_dictionary)

    co_occurance_graph = nx.Graph()
    for brand_pairing, count in pairing_dictionary.items():
        pairs = brand_pairing.split("-")
        first_brand = pairs[0]
        second_brand = pairs[1]
        co_occurance_graph.add_edge(first_brand, second_brand, weight=count)

    nx.write_gml(co_occurance_graph, 'co_occurance_graphfile.gml')

    nx.draw_networkx(co_occurance_graph)
    plt.savefig('../static/img/cooccurance.png')
    #plt.show()