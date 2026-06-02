# Databricks notebook source
# ============================================
# SILVER → GOLD PIPELINE
# ============================================

from pyspark.sql.functions import *

# --------------------------------------------
# 1. READ SILVER DATA (DELTA)
# --------------------------------------------
df = spark.read.format("delta") \
    .load("/Volumes/ecom-medallion-pipeline/silver/mobile_orders")

print("Silver Data Loaded:", df.count())

# --------------------------------------------
# 2. BRAND SUMMARY TABLE
# --------------------------------------------
brand_summary = df.groupBy("brand").agg(
    avg("selling_price").alias("avg_price"),
    avg("ratings").alias("avg_rating"),
    count("*").alias("total_products")
)

# Save
brand_summary.write.format("delta") \
    .mode("overwrite") \
    .save("/Volumes/ecom-medallion-pipeline/gold/brand_summary")

# --------------------------------------------
# 3. TOP RATED PHONES
# --------------------------------------------
top_rated = df.filter(col("ratings") >= 4.0) \
              .orderBy(col("ratings").desc(), col("selling_price").asc())

# Save
top_rated.write.format("delta") \
    .mode("overwrite") \
    .save("/Volumes/ecom-medallion-pipeline/gold/top_rated_phones")

# --------------------------------------------
# 4. PRICE SEGMENT ANALYSIS
# --------------------------------------------
df = df.withColumn(
    "price_category",
    when(col("selling_price") < 10000, "Budget")
    .when((col("selling_price") >= 10000) & (col("selling_price") < 20000), "Mid-Range")
    .otherwise("Premium")
)

price_segment = df.groupBy("price_category").agg(
    avg("selling_price").alias("avg_price"),
    avg("ratings").alias("avg_rating"),
    count("*").alias("total_products")
)

# Save
price_segment.write.format("delta") \
    .mode("overwrite") \
    .save("/Volumes/ecom-medallion-pipeline/gold/price_segments")

# --------------------------------------------
# 5. FINAL MESSAGE
# --------------------------------------------
print("✅ Gold Layer Created Successfully")

# COMMAND ----------


# SAVING AS TABLES ALSO SO THAT WE CAN DO QUERY USING SQL 
from pyspark.sql.functions import *

brand_df = spark.read.format("delta").load("/Volumes/ecom-medallion-pipeline/gold/brand_summary")
top_df = spark.read.format("delta").load("/Volumes/ecom-medallion-pipeline/gold/top_rated_phones")
segment_df = spark.read.format("delta").load("/Volumes/ecom-medallion-pipeline/gold/price_segments")

# SAVING AS TABLES ALSO SO THAT WE CAN DO QUERY USING SQL 
brand_df.write.mode("overwrite").saveAsTable("`ecom-medallion-pipeline`.gold.brand_summary")
top_df.write.mode("overwrite").saveAsTable("`ecom-medallion-pipeline`.gold.top_rated_phones")
segment_df.write.mode("overwrite").saveAsTable("`ecom-medallion-pipeline`.gold.price_segments")
