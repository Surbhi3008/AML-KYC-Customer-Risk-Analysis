
# Financial-Crime-Risk-Analysis & Automation Pipeline

## Project Overview
This project delivers an enterprise-grade customer risk profiling and automation pipeline using PostgreSQL, Python, and Excel. The system focuses on identifying high-risk customers, evaluating geographic and occupational exposure based on international regulatory standards, and automating data delivery for Enhanced Due Diligence (EDD) workflows. An interactive Excel dashboard complements the automated backend to enable seamless compliance monitoring and data-driven decision-making.

## Business Impact: 
In a real banking environment, manual Enhanced Due Diligence (EDD) costs roughly $500 per customer profile. By segregating the 34.8% high-risk segment and cross-referencing them with PEP status, this analysis allows compliance teams to allocate expensive human investigator resources exclusively to high-yield risk targets, drastically reducing operational overhead.

 ## Dashboard Preview

![AML KYC Dashboard](screenshots/dashboard.png)

## Objectives
* **Isolate High-Risk Segments:** Segment customer databases to prioritize high-risk profiles and optimize compliance resource allocation.
* **Map Regulatory Risk Exposure:** Evaluate country-wise and occupation-wise exposure using frameworks aligned with FATF (Financial Action Task Force) and Wolfsberg Group standards.
* **Assess PEP Vulnerabilities:** Quantify the statistical risk impact of Politically Exposed Persons (PEPs) across different financial buckets.
* **Automate Compliance Reporting:** Eliminate manual data extraction bottlenecks by engineering an automated database-to-Excel Python data pipeline.

## Dataset Description
The dataset models core KYC and behavioral banking metrics across 500 customer accounts:
* `Customer_ID`, `Age`, `Country`, `Occupation`, `Annual_Income`
* `Monthly_Transactions`, `Avg_Transaction_Value`
* `PEP Status`, `High_Risk_Country`, `Risk_Score`, `Risk_Category`

## Tools Used
* **Database Management:** PostgreSQL (pgAdmin)
* **Automation Engineering:** Python (Pandas, SQLAlchemy, Psycopg2, Openpyxl)
* **Data Visualization & Analytics:** Microsoft Excel (Pivot Tables, Charts, Slicers)
* **Version Control:** GitHub

## Architecture & Data Pipeline Workflow
1. **Data Ingestion & Storage:** Raw customer onboarding data is securely housed and queried within a structured PostgreSQL database environment.
2. **Automated Extraction (The Python Layer):** A headless Python script (`AML.py`) uses `SQLAlchemy` to establish an authenticated local bridge to the PostgreSQL engine.
3. **Data Normalization & Delivery:** The pipeline extracts active high-risk and PEP matrices dynamically, handles string-matching variances, and auto-generates a standardized, audit-ready compliance spreadsheet (`High_Risk_Compliance_Alerts.xlsx`) instantly.

## Key Insights & Governance Findings
* **Targeted High-Risk Cohort:** Isolated a concentrated 34.8% segment (174 out of 500 accounts) classified as High Risk.
    ```sql
  -- Prioritized EDD Queue Filter
  SELECT 
      customer_id, 
      country, 
      pep_status,
      CASE 
          WHEN pep_status = 'Yes' AND high_risk_country = 'Yes' THEN 'Immediate EDD Request'
          WHEN pep_status = 'Yes' OR high_risk_country = 'Yes' THEN 'High Priority Review'
          ELSE 'Standard Monitoring'
      END AS edd_risk_flag
  FROM compliance_database;
  ```
  * **Alert Optimization:** While Medium-Risk customers form the largest segment (277), a variance analysis indicates that tweaking the transaction volume threshold by 10% could safely reclassify low-risk activity, potentially reducing compliance alert volume by 15% without increasing risk exposure.
* **Geographic Sanction Alignment:** Data revealed severe risk grouping concentrated in Russia (41 accounts), Syria (40 accounts), and Iran (36 accounts), which directly maps to active FATF high-risk jurisdictions under monitored call-for-action lists.
* **PEP Vulnerability Disparity:** Politically Exposed Persons (PEPs) exhibited a substantially elevated average risk score (113.86) compared to non-PEP customers (95.10), validating the need for automated triggers for continuous account monitoring.
* **Occupational Risk Concentration:** Risk scoring successfully flagged Politicians (103.4) and Business Owners (100.6) as primary risk vectors, aligning with Wolfsberg Group anti-bribery and corruption parameters, while salaried accounts maintained the lowest baseline threat vector (85.0).

## Repository Structure
```text
Financial-Crime-Risk-Analysis/
│
├── README.md
├── dataset/
│   └── customers.csv
├── sql_queries/
│   └── Financial-Crime-Risk-Analysis.sql
├── python_pipeline/
│   └── AML.py                     # Automated Data Extraction Engine
├── outputs/                       # Python-generated automation outputs
│   └── High_Risk_Compliance_Alerts.xls                  
├── dashboard/
│   └── Financial-Crime-Risk-Analysis-Dashboard.xlsx     # Interactive Visual Layer
└── screenshots/
    ├── dashboard.png
    └── execution_success.png
```
## Conclusion
This framework demonstrates how bridging relational databases with automated Python scripting solves critical operational bottlenecks in Financial Crime compliance. By transforming static customer records into an automated, audit-ready data pipeline, the project showcases data analytics' practical, cost-saving application in modern risk management.

## Author
**Surbhi Sharma Panchal**
