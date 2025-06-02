Conversion KPI Analysis: ABC_Conversion_Analysis_2025_05_27.csv


This script performs statistical analysis and visualization of conversion KPIs across different cohorts, based on the dataset ABC_Conversion_Analysis_2025_05_27.csv.

📊 Overview
The analysis covers the following key performance indicators (KPIs):

FIDO_SCORE_TO_KYB_SUBMISSION_DURATION

KYB_TO_DOC_DURATION

DOC_TO_BIZ_APPROVED_DURATION

For each KPI, the script:

Computes summary statistics (mean, median, count) for each cohort.

Performs:

ANOVA (Analysis of Variance) to test for differences in means.

Kruskal-Wallis test for differences in medians.

Plots:

Histograms of KPI distributions per cohort.

Bar plots comparing means and medians across cohorts.

🧪 Statistical Tests
ANOVA
Compares the mean of each KPI across cohorts to check for significant differences.

Kruskal-Wallis
A non-parametric alternative to ANOVA, testing for differences in medians.

Both tests help identify statistically significant differences in cohort performance.

📈 Visualizations
Histograms
Distribution of each KPI per cohort.

Bar plots
Comparison of mean and median KPI durations:

Mean and median comparisons across cohorts.

Mean and median comparisons within each cohort for all KPIs.

These plots offer both high-level and detailed views of performance patterns.

🏃‍♂️ How to Run
1. Install requirements (if you haven’t already):

pip install pandas scipy matplotlib seaborn

2. Run the script:

python ABCSpeedanalysis.py

3. View output:

The script prints summary statistics and p-values for each KPI.

Interactive plots will pop up one by one for you to review.

📂 Input Data
The script expects a CSV file named ABC_Conversion_Analysis_2025_05_27.csv containing at least:

GROUP_NAME: Cohort/group identifier.

The KPIs (FIDO_SCORE_TO_KYB_SUBMISSION_DURATION, KYB_TO_DOC_DURATION, DOC_TO_BIZ_APPROVED_DURATION).

📦 Output
Printed summary tables for each KPI.

p-values for ANOVA and Kruskal-Wallis tests.

Histograms and bar plots visualizing differences and distributions.




