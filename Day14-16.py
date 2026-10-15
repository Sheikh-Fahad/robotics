import sqlite3
import pandas as pd

df = pd.read_excel("Date_Fruit_Datasets.xlsx")

con = sqlite3.connect(":memory:")
df.to_sql("data", con, index=False)

def q(sql):
    return pd.read_sql_query(sql, con)

# print(q("SELECT AREA, PERIMETER, Class FROM data LIMIT 3"))

# print(q("SELECT AREA, Class FROM data WHERE AREA > 500000 LIMIT 5"))


# print(q("SELECT AREA, Class FROM data ORDER BY AREA DESC LIMIT 3"))

# print(q("SELECT AREA, Class FROM data ORDER BY AREA LIMIT 3"))


# print(q("SELECT COUNT(*) AS total FROM data"))

# print(q("SELECT Class, COUNT(*) AS n FROM data GROUP BY Class"))

# print(q("SELECT Class, COUNT(*) AS n, ROUND(AVG(AREA)) AS avg_area FROM data GROUP BY Class"))

# print(q("SELECT Class, COUNT(*) AS n FROM data GROUP BY Class HAVING COUNT(*) > 100 ORDER BY n DESC"))



# price = pd.DataFrame({
#     "Class": ["BERHI", "DEGLET", "DOKOL", "IRAQI", "ROTANA", "SAFAVI", "SOGAY"],
#     "price": [500, 450, 300, 400, 350, 420, 380]
# })
# price.to_sql("price", con, index=False)

# print(q("SELECT * FROM price"))


# print(q("SELECT data.AREA, data.Class, price.price FROM data JOIN price ON data.Class = price.Class LIMIT 3"))




# print(q("""
# WITH big AS (
#     SELECT * FROM data WHERE AREA > 400000
# )
# SELECT Class, COUNT(*) AS n
# FROM big
# GROUP BY Class
# """))



print(q("""
SELECT Class, AREA,
       RANK() OVER (PARTITION BY Class ORDER BY AREA DESC) AS rnk
FROM data
ORDER BY Class, rnk
LIMIT 6
"""))