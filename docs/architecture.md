# Data Engineering Architecture

## Current Project Flow

```text
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
```

## Future Cloud Architecture

```text
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
```

## Technologies

- Python
- PySpark
- AWS S3
- AWS Glue
- Amazon Redshift
- SQL
- ETL Pipelines
