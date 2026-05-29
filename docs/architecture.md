# Data Engineering Architecture

sales_data.csv
      |
      v
PySpark ETL Job
      |
      +--> Data Validation
      |
      +--> Data Transformation
      |
      +--> Business Calculations
      |
      v
Processed Dataset
      |
      v
Analytics / Reporting Layer

Future Cloud Architecture

Source Data
      |
      v
AWS S3
      |
      v
AWS Glue (PySpark)
      |
      v
Amazon Redshift
      |
      v
Power BI / Tableau
