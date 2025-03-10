import sqlite3
import pandas as pd

# Criar conexão SQLite em memória
conn = sqlite3.connect(":memory:")

# Criando DataFrames
customers_df = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})

orders_df = pd.DataFrame({
    "id": [1, 2, 3],
    "customer_id": [1, 2, 1],
    "product": ["Laptop", "Mouse", "Keyboard"]
})

# Salvando os DataFrames no banco SQLite
customers_df.to_sql("customers", conn, index=False, if_exists="replace")
orders_df.to_sql("orders", conn, index=False, if_exists="replace")

# Executar INNER JOIN
query_inner = """
SELECT customers.id, customers.name, orders.product
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id
"""
inner_join_df = pd.read_sql(query_inner, conn)
print("INNER JOIN:")
print(inner_join_df)

# Executar LEFT JOIN
query_left = """
SELECT customers.id, customers.name, orders.product
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
"""
left_join_df = pd.read_sql(query_left, conn)
print("\nLEFT JOIN:")
print(left_join_df)

# Fechar conexão
conn.close()