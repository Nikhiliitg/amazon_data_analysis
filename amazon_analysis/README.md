# Amazon Sales Analysis and Visualization

## **Project Overview**
This project demonstrates a complete data pipeline workflow, from data ingestion to visualization, to analyze Amazon sales data and generate actionable insights. The workflow leverages **Kaggle**, **AWS S3**, **Snowflake**, and **Tableau**, showcasing expertise in data engineering, data warehousing, and business intelligence.

---

## **Workflow and Technologies Used**

### **1. Data Ingestion**
- The dataset was sourced from **Kaggle** and loaded into an **AWS S3 bucket** using Python code.
- **Python Libraries Used**: `boto3`, `pandas`, `os`.

### **2. Data Transformation (ETL Pipeline)**
- An **ETL pipeline** was implemented to clean, transform, and preprocess the raw data:
  1. **Extract**: Data was extracted from Kaggle using the Kaggle API.
  2. **Transform**: Data was cleaned, columns were standardized, and hierarchical categories were split into subcategories.
  3. **Load**: Transformed data was stored back into an **AWS S3 bucket**.

### **3. Data Warehousing (Snowflake)**
- The transformed data was loaded into **Snowflake** using **SQL scripts**.
- Key steps performed:
  - Created Snowflake databases, schemas, and tables.
  - Defined **stages** to load data directly from S3.
  - Wrote SQL scripts to:
    - Extract hierarchical subcategories from product categories.
    - Generate additional insight columns, such as revenue and profit margins.
  - Performed advanced queries to analyze trends and relationships in the data.

### **4. Data Visualization (Tableau)**
- Data was connected to **Tableau** from Snowflake to build **interactive dashboards**.
- Key visualizations created:
  - Revenue distribution across categories and subcategories.
  - Discount trends and their impact on sales.
  - Ratings vs. sales correlation.

---

## **Pipeline Diagram**

Below is the project pipeline that visualizes the entire workflow:

![Projects Structure](.project_structure/diagram-export-1-20-2025-11_33_54-PM.png)