from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("Sales ETL Pipeline") \
    .getOrCreate()

df = spark.read.csv(
    "data/sales_data.csv",
    header=True,
    inferSchema=True
)

df = df.withColumn(
    "total_amount",
    col("quantity") * col("price")
)

df.show()

df.write.mode("overwrite") \
    .csv("output/transformed_data.csv", header=True)

spark.stop()
