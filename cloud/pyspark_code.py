# Primero, necesitamos importar las librerías necesarias
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import redis
from pyspark_redis import *


# Inicializamos una sesión de Spark
spark = SparkSession.builder.appName("Ejemplo de Redis en la nube").getOrCreate()

# Creamos una conexión a Redis en la nube
r = redis.Redis(
    host='redis-16287.c302.asia-northeast1-1.gce.cloud.redislabs.com',
    port=16287,
    password='WpnrnezZHgXgnsM9K1xEbzwLwrVTRym6')

# Creamos un par de entradas en Redis
r.set('key1', 'value1')
r.set('key2', 'value2')

# Leemos los datos de Redis en la nube
df = spark.read.format("redis").option("host", "redis-16287.c302.asia-northeast1-1.gce.cloud.redislabs.com").option("port", 16287).option("password", "WpnrnezZHgXgnsM9K1xEbzwLwrVTRym6").option("keys.pattern", "*").load()

# Mostramos los resultados
df.show()