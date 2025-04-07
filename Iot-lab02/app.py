import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

username = "root"
password = "root"
port = 3307
database = "baseds"

engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:{port}/{database}")
query = "SELECT * FROM usuarios"


# Create a connection to the database
try:
    connection = engine.connect()
    print("Conexión exitosa a la base de datos")
except Exception as e:
    print("Error al conectar a la base de datos:", e)
finally:
    connection.close()
    

# df = pd.io.sql.read_sql(query, engine).set_index("CODIGO")
# print(df.head())

inputFile = "data_usuario.csv"
usuarios = pd.read_csv(inputFile)
# print(usuarios)

# usuarios.to_sql(name="usuarios", con=engine, if_exists="replace", index=False)
usuarios.to_sql(name="usuarios", con=engine, if_exists="append", index=False)
print("Datos insertados correctamente")

sql = "SELECT * FROM usuarios"
df = pd.read_sql_query(sql, engine).set_index("CODIGO")
print(df)

new_usuario = {
    'CODIGO': ['u35', 'u36'],
    'ALIAS': ['mar', 'juanp'],
    'CLAVE': ['042009', 'peru22'],
    'NOMBRE': ['Elena Guerra', 'Juan Perez'],
    'ACCESO': 1,
}

# Convertir el diccionario a un DataFrame
df1 = pd.DataFrame(new_usuario).set_index("CODIGO")
print(df1)

# Insertar datos en mysql
df1.to_sql(name="usuarios", con=engine, if_exists="append", index=True)

sql = "SELECT * FROM usuarios"
df2 = pd.read_sql_query(sql, engine).set_index("CODIGO")
print(df2)

# Ver los datos en un gráfico
df2.plot(kind = "bar")
plt.xlabel("CODIGO")
plt.ylabel("ACCESO")
plt.show()
