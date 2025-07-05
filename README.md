# 🛒 Retail Sales ETL Pipeline

## 📌 Project Description

This project simulates a retail business ETL pipeline. It extracts sales and customer data from CSV files, cleans and transforms it using Python and Pandas, and loads the data into a PostgreSQL database. Finally, SQL queries are used to analyze key business metrics like top-selling products, sales trends, and customer lifetime value.

---

## 🧰 Tech Stack

- **Python**: Scripting & ETL logic
- **Pandas**: Data manipulation and cleaning
- **PostgreSQL**: Data storage and querying
- **psycopg2**: PostgreSQL connection in Python

---
## 🔄 ETL Workflow

1. **Extract**  
   Read raw data from `daily_sales.csv` and `customer.csv` using `pandas`.

2. **Transform**  
   - Remove missing values  
   - Format date fields  
   - Clean currency symbols from sales amounts

3. **Load**  
   Insert cleaned data into the `customers` and `sales` tables in PostgreSQL using `psycopg2`.


4. **Analyze**  
   Execute SQL queries to generate insights like:
   - Top selling products
   - Weekly sales trends
   - Customer Lifetime Value (CLV)



---

# 🚀 How to Run the Project

### 1. Clone the Repository
<pre>
git clone <your-repo-url>
cd projectname
</pre>

### 2. Create and Activate Virtual Environment
<pre>
python -m venv .venv
.\.venv\Scripts\activate
</pre>

### 3. Install Dependencies
<pre>
pip install -r requirements.txt
</pre>

### 4. Set Up the Database
<pre>
Make sure PostgreSQL is running, then:
psql -U postgres -d retail_db -f db/init_db.sql
</pre>
#### Replace postgres with your PostgreSQL username if different.


### 5. Add Sample Data
<pre>
Place your daily_sales.csv and customer.csv files inside the data/ folder.
</pre>

### 6. Run the ETL Pipeline
<pre>
python main.py
</pre>

### 7. Run Analysis Queries
<pre>
psql -U postgres -d retail_db -f queries/analysis_queries.sql
</pre>

## IMPORTANT
" In db_config.py set your actual database credentials."

                                                               
# 🧑‍💻 Author

Kavin Kishore   
B.Tech Student, DTU     
Built as a real-time data engineering mini project.