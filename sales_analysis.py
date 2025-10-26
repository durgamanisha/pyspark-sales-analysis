from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, avg, count, desc, to_date

# Step 1: Create Spark session
spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()

# Step 2: Load CSV file
df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)

# Step 3: Data Cleaning
df = df.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))

# Step 4: Register temporary view for SQL queries
df.createOrReplaceTempView("sales")

# Step 5: SQL Queries for Insights

# a) Total Sales per Region
region_sales = spark.sql("""
    SELECT region, SUM(quantity * price) AS total_sales
    FROM sales
    GROUP BY region
    ORDER BY total_sales DESC
""")
region_sales.show()

# b) Top 3 Best-Selling Products
top_products = spark.sql("""
    SELECT product, SUM(quantity) AS total_sold
    FROM sales
    GROUP BY product
    ORDER BY total_sold DESC
    LIMIT 3
""")
top_products.show()

# c) Average Order Value per Category
avg_order = spark.sql("""
    SELECT category, AVG(quantity * price) AS avg_order_value
    FROM sales
    GROUP BY category
""")
avg_order.show()

# d) Daily Revenue Trend
daily_revenue = spark.sql("""
    SELECT date, SUM(quantity * price) AS daily_revenue
    FROM sales
    GROUP BY date
    ORDER BY date
""")
daily_revenue.show()
