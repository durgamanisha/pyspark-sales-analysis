# 🧾 Real-Time Sales Data Analysis using PySpark

## 📘 Project Overview
This project demonstrates how to analyze **real-time sales data** using **PySpark**, **Python**, and **SQL**.  
It performs data cleaning, aggregation, and analysis on large-scale sales transactions to extract meaningful business insights such as:
- Total sales per region  
- Top-selling products  
- Daily revenue trends  
- Average order value by category  

---

## ⚙️ Technologies Used
- 🐍 **Python**
- 🔥 **Apache PySpark**
- 🧠 **SQL (via Spark SQL)**
- 📄 **CSV Dataset**

---

## 📊 Dataset Information
**File:** `sales_data.csv`

| order_id | product     | category     | region | quantity | price | date       |
|-----------|-------------|--------------|---------|-----------|--------|------------|
| 1001      | Laptop      | Electronics  | South   | 2         | 55000  | 2025-01-05 |
| 1002      | Phone       | Electronics  | North   | 5         | 20000  | 2025-01-05 |
| 1003      | TV          | Electronics  | East    | 3         | 30000  | 2025-01-06 |
| 1004      | Chair       | Furniture    | South   | 10        | 1500   | 2025-01-06 |
| 1005      | Sofa        | Furniture    | West    | 2         | 20000  | 2025-01-07 |

---

## 💻 Code Highlights
Key operations performed in the PySpark script:
```python
# Load data
df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)

# Clean data
df = df.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))
df.createOrReplaceTempView("sales")

# SQL queries
spark.sql("""
    SELECT region, SUM(quantity * price) AS total_sales
    FROM sales
    GROUP BY region
    ORDER BY total_sales DESC
""").show()
