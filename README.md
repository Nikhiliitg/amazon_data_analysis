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

![Projects Structure](diagram-export-1-20-2025-11_33_54-PM.png)


---

## **Key Insights**
1. **Category-Level Revenue**:
   - The "Computers & Accessories" category generated the highest revenue, with the "Cables" subcategory contributing significantly.

2. **Impact of Discounts**:
   - Products with discounts between 50-70% drove the highest sales volumes but reduced revenue per unit.

3. **Ratings and Sales**:
   - Products with a rating above 4.5 experienced a significantly higher number of reviews and sales.

4. **Profit Margins**:
   - Subcategories with a smaller discount percentage but higher ratings maintained better profit margins.

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

   cd project-directory

2. **Set Up S3 Bucket**:
  Create an S3 bucket and configure access permissions.
  Use the provided Python script to load Kaggle data into the bucket.

3. **Run the ETL Pipeline**:
  Execute the Python ETL script to transform the data.
  ```bash
    python3 amazon_analysis/src/etl_pipeline.py

4. **Load Data into Snowflake**:
  Use the provided SQL scripts to create stages and load the data into Snowflake.
  ```bash 
  CREATE OR REPLACE STAGE amazon_stage
  URL = 's3://bucket';
  COPY INTO amazon_sales FROM @amazon_stage;

5. **Connect Snowflake to Tableau**:
  Use Tableau’s Snowflake connector to load the transformed data for visualization.

6. **Generate Dashboards**:
  Use the Tableau dashboard template to create interactive visualizations.

# Acknowledgments

  **Kaggle: For providing the dataset.**
  **AWS S3: For data storage.**
  **Snowflake: For data warehousing.**
  **Tableau: For data visualization and dashboard creation.**

## Contact

For any questions or suggestions, feel free to contact me at :
  nikhiliitg07@gmail.com

