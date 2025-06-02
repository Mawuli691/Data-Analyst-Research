# 📈 Conversion KPI Analysis

This project analyzes key conversion performance indicators across different cohorts using the dataset:  
**`ABC_Conversion_Analysis_2025_05_27.csv`**

---

## 🗂️ Overview

For each KPI, the script:
✅ Computes summary statistics (mean, median, count) per cohort  
✅ Runs statistical tests:
- **ANOVA** (for differences in means)
- **Kruskal-Wallis** (for differences in medians)  
✅ Plots visualizations:
- Histograms for KPI distributions per cohort  
- Bar plots comparing means and medians across cohorts  

---

## 🔍 KPIs Analyzed
- **FIDO_SCORE_TO_KYB_SUBMISSION_DURATION**  
- **KYB_TO_DOC_DURATION**  
- **DOC_TO_BIZ_APPROVED_DURATION**

---

## 🧪 Statistical Tests
- **ANOVA** – Tests for differences in mean KPI durations across cohorts  
- **Kruskal-Wallis** – Non-parametric test for differences in medians across cohorts  

Both tests help identify statistically significant differences in performance.

---

## 📊 Visualizations
- **Histograms** – Show KPI distribution for each cohort  
- **Bar Plots** – Compare mean and median durations:
  - Across cohorts  
  - Within each cohort for all KPIs  

---

## 🚀 How to Run
1️⃣ Install dependencies:
```bash
pip install pandas scipy matplotlib seaborn

---

2️⃣ Run the script:

``` bash
python ABCSpeedanalysis.py

---
3️⃣ View the results:

Summary statistics and p-values printed in the terminal

Interactive plots appear one by one for review




📂 Input Data
The script expects a CSV file named ABC_Conversion_Analysis_2025_05_27.csv containing at least:

GROUP_NAME: Cohort/group identifier.

The KPIs (FIDO_SCORE_TO_KYB_SUBMISSION_DURATION, KYB_TO_DOC_DURATION, DOC_TO_BIZ_APPROVED_DURATION).

📦 Output
Printed summary tables for each KPI.

p-values for ANOVA and Kruskal-Wallis tests.

Histograms and bar plots visualizing differences and distributions.




