# Market Basket Analysis

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue)
![MLxtend](https://img.shields.io/badge/MLxtend-Association%20Rules-success)
![License](https://img.shields.io/badge/License-MIT-success)

</p>

---

## Overview

Market Basket Analysis is a data analytics project that identifies relationships between products frequently purchased together. Using association rule mining techniques, the project discovers hidden purchasing patterns that can help retailers improve product placement, cross-selling strategies, promotional campaigns, and inventory management.

The project follows a complete data analytics workflow including data preprocessing, exploratory analysis, association rule mining, visualization, and business insight generation.

---

## Problem Statement

Retail businesses generate thousands of transaction records every day, making it difficult to manually identify purchasing patterns. Understanding which products customers frequently buy together is essential for increasing sales, improving customer experience, and optimizing store layouts.

This project aims to discover meaningful associations between products using transaction data and provide actionable business insights.

---

## Solution

The project applies Market Basket Analysis techniques to transactional retail data by preprocessing purchase records, generating frequent itemsets, and extracting association rules using the Apriori algorithm. The resulting insights can be used to optimize marketing strategies and product recommendations.

---

## Features

- Data preprocessing and cleaning
- Transaction data transformation
- Frequent itemset generation
- Association rule mining
- Product relationship analysis
- Customer purchasing pattern analysis
- Professional data visualization
- Business insight generation
- Modular Python project structure

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib |
| Machine Learning | Scikit-learn |
| Association Rule Mining | MLxtend |
| Development Environment | PyCharm |

---

## Project Structure

```text
Market_Basket_Analysis
│
├── data
│   ├── raw.csv
│   ├── final.csv
│   ├── dh_transactions.csv
│   └── dh_product_lookup.csv
│
├── output
│   ├── category_plot.png
│   ├── pasta_plot.png
│   └── plot/
│       ├── top10_brands_sales.png
│       ├── top_commodities.png
│       ├── coupon_boxplot.png
│       ├── units_vs_sales.png
│       └── customer_total_spend_distribution.png
│
├── src
│   ├── preprocessing.py
│   ├── basket.py
│   ├── model.py
│   ├── evaluation.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Dataset

The project utilizes retail transaction data containing customer purchases and product information.

### Dataset Features

- Basket ID
- Product ID
- Product Category
- Brand
- Commodity
- Quantity Purchased
- Dollar Sales
- Coupon Information
- Transaction Time
- Week
- Day
- Geography

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Market_Basket_Analysis.git
```

Navigate to the project directory

```bash
cd Market_Basket_Analysis
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute the application

```bash
python main.py
```

---

## Project Workflow

```text
Raw Transaction Data
          │
          ▼
Data Cleaning
          │
          ▼
Data Preprocessing
          │
          ▼
Transaction Encoding
          │
          ▼
Frequent Itemset Mining
          │
          ▼
Association Rule Generation
          │
          ▼
Performance Evaluation
          │
          ▼
Visualization
          │
          ▼
Business Insights
```

---

## Data Preprocessing

The preprocessing pipeline includes:

- Missing value handling
- Duplicate removal
- Transaction aggregation
- Product encoding
- Basket creation
- Feature transformation
- Data validation

---

## Association Rule Mining

The project applies the Apriori algorithm to discover product associations using metrics such as:

- Support
- Confidence
- Lift
- Leverage
- Conviction

These metrics help identify strong relationships between products purchased together.

---

## Data Visualization

The project generates several analytical visualizations, including:

- Product category distribution
- Top-selling brands
- Commodity analysis
- Customer spending distribution
- Units sold vs. sales
- Coupon usage analysis
- Product popularity distribution
- Transaction time analysis
- Weekly sales trends

---

## Business Insights

The analysis provides valuable insights such as:

- Frequently purchased product combinations
- High-performing product categories
- Customer purchasing behavior
- Product cross-selling opportunities
- Promotion effectiveness
- Sales trends across different periods
- Brand performance analysis

---

## Business Applications

This solution can be applied in:

- Retail Analytics
- E-commerce Platforms
- Supermarkets
- Inventory Management
- Product Recommendation Systems
- Marketing Campaign Optimization
- Customer Behavior Analysis
- Cross-Selling Strategy Development

---

## Skills Demonstrated

- Python Programming
- Data Cleaning
- Data Wrangling
- Exploratory Data Analysis
- Association Rule Mining
- Apriori Algorithm
- Market Basket Analysis
- Data Visualization
- Business Analytics
- Pandas
- NumPy
- MLxtend

---

## Future Improvements

Future enhancements may include:

- FP-Growth algorithm implementation
- Interactive dashboard using Power BI or Streamlit
- Recommendation engine integration
- Real-time transaction analysis
- Customer segmentation
- Automated reporting
- Cloud deployment
- Large-scale distributed data processing

---

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License.

---

## Author

**Farsan K**

Aspiring Data Scientist | Machine Learning Engineer

**GitHub:** https://github.com/Farsan-k

**LinkedIn:** https://www.linkedin.com/in/your-linkedin-profile/
