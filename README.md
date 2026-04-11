## Market Basket Analysis
Problem

Retail businesses generate massive amounts of transactional data, but often fail to extract meaningful insights from it.

One key challenge is:

Understanding which products are frequently purchased together
Identifying cross-selling opportunities
Improving customer purchase experience

Without this knowledge, businesses miss chances to:

Increase revenue
Optimize product placement
Create effective promotions
Approach

We applied Market Basket Analysis using the Apriori Algorithm to uncover relationships between products.

Step 1: Data Preprocessing
Cleaned product_size column
Handled missing values
Converted ID columns (basket, upc, store, household) into categorical types
Step 2: Basket Matrix Creation
Transformed transactional data into a basket format
Rows → Transactions (baskets)
Columns → Products (UPC)
Values → 1 (purchased) or 0 (not purchased)
Step 3: Frequent Itemsets
Applied Apriori algorithm
Extracted item combinations based on minimum support
Step 4: Association Rule Mining

Generated rules using:

Support → Frequency of itemset
Confidence → Likelihood of co-purchase
Lift → Strength of association
Step 5: Focused Analysis
Analyzed complementary categories
Example: Pasta & Pasta Sauce
Results
Discovered strong product associations
Identified high-lift rules indicating meaningful relationships
Key Insights:
Customers buying Pasta often also buy Pasta Sauce
Certain products act as drivers for additional purchases
Some high-frequency products are not strongly associated (important distinction)
Visualizations:
Distribution of product popularity
Commodity-wise sales
Customer spending patterns
Business Value

This analysis provides direct business impact:

Cross-Selling

Recommend related products to customers

Store Layout Optimization

Place frequently bought items together

Targeted Promotions

Create combo offers and bundles

Inventory Management

Ensure availability of complementary products
Conclusion

Market Basket Analysis helps businesses move from data → insights → action.

By leveraging association rules, companies can:

Improve customer experience
Increase average basket size
Drive higher revenue
