from pyspark.sql import SparkSession

if __name__ == "__main__":
    print("Application Started...")

    spark = SparkSession \
            .builder \
            .appName("Testing Pyspark Run") \
            .master("local[*]") \
            .getOrCreate()

    input_file = "myfile.txt"
    rdd1 = spark.sparkContext.textFile(input_file)

    print(rdd1.collect())
