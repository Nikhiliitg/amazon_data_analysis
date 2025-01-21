# **Amazon Sales Analysis and Visualization**

## **Project Overview**
This project demonstrates a **comprehensive data pipeline workflow** for analyzing Amazon sales data and generating actionable insights. Leveraging **Kaggle**, **AWS S3**, **Snowflake**, and **Tableau**, this project highlights my expertise in **data engineering**, **data warehousing**, and **business intelligence**.

---

## **Workflow and Technologies Used**

### **1. Data Ingestion**
- **Source**: Dataset obtained from **Kaggle**.
- **Storage**: Loaded into an **AWS S3 bucket** using Python.
- **Tools & Libraries**: `boto3`, `pandas`, `os`.

### **2. Data Transformation (ETL Pipeline)**
- Implemented an **ETL pipeline** to clean, transform, and preprocess raw data:
  1. **Extract**: Retrieved data from Kaggle using the Kaggle API.
  2. **Transform**: Cleaned data, standardized columns, and split hierarchical categories into subcategories.
  3. **Load**: Stored the transformed data back into an **AWS S3 bucket**.

### **3. Data Warehousing (Snowflake)**
- Loaded the transformed data into **Snowflake** for analysis using **SQL scripts**:
  - Created Snowflake databases, schemas, and tables.
  - Defined **stages** to load data directly from S3.
  - Performed transformations such as:
    - Extracting subcategories from product categories.
    - Generating additional insight columns like revenue and profit margins.
  - Executed advanced queries to analyze trends and relationships in the data.

### **4. Data Visualization (Tableau)**
- Connected **Snowflake** data to **Tableau** to build **interactive dashboards**:
  - Visualized revenue distribution across categories and subcategories.
  - Analyzed discount trends and their impact on sales.
  - Explored correlations between ratings and sales.

---

## **Pipeline Diagram**
Below is a visual representation of the workflow:
![Pipeline Diagram](diagram-export-1-20-2025-11_33_54-PM.png)

---

## **Key Insights**
1. **Category-Level Revenue**:
   - The "Computers & Accessories" category generated the highest revenue, with "Cables" being a major contributor.
2. **Impact of Discounts**:
   - Products with discounts between 50-70% had the highest sales volumes but reduced revenue per unit.
3. **Ratings and Sales**:
   - Products with a rating above 4.5 experienced significantly higher sales and reviews.
4. **Profit Margins**:
   - Subcategories with smaller discounts but higher ratings maintained better profit margins.

---

## **How to Run the Project**

### **1. Prerequisites**
- **AWS Account**: To create an S3 bucket and store data.
- **Snowflake Account**: For data warehousing.
- **Tableau**: For visualization.
- **Python Installed**: To execute ETL scripts.

### **2. Steps to Execute**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Nikhiliitg/amazon_data_analysis
   cd amazon_data_analysis
   ```

2. **Set Up S3 Bucket**:
   - Create an S3 bucket and configure access permissions.
   - Use the provided Python script to load Kaggle data into the bucket.

3. **Run the ETL Pipeline**:
   - Execute the Python ETL script to transform the data.
   ```bash
   python3 amazon_analysis/src/etl_pipeline.py
   ```

4. **Load Data into Snowflake**:
   - Use the provided SQL scripts to create stages and load data into Snowflake.
   ```sql
   CREATE OR REPLACE STAGE amazon_stage
   URL = 's3://your-bucket-name';
   COPY INTO amazon_sales FROM @amazon_stage;
   ```

5. **Connect Snowflake to Tableau**:
   - Use Tableau’s Snowflake connector to load the transformed data.

6. **Generate Dashboards**:
   - Use the Tableau dashboard template to create interactive visualizations.

---

## **Acknowledgments**
- **Kaggle**: For providing the dataset.
- **AWS S3**: For data storage.
- **Snowflake**: For data warehousing.
- **Tableau**: For data visualization.

---

## **Contact**
For questions or suggestions, feel free to contact me:

**Email**: nikhiliitg07@gmail.com  
**GitHub**: [https://github.com/Nikhiliitg](https://github.com/Nikhiliitg)
