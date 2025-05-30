# 📊 A/B Test Analysis with Z-Test

This script analyzes the difference in conversion rates between two cohorts (`REF` and `NO_REF`) using a **two-proportion z-test**. It helps to statistically compare key performance indicators (KPIs) between two groups.

---

## 📁 Data File

The script reads data from:

KYB_A_B_Test_Preliminary_2025_05_29.csv


The CSV is expected to contain aggregated counts for each cohort:
- `REF_<KPI>` and `REF_<BASE>`
- `NO_REF_<KPI>` and `NO_REF_<BASE>`

For example:
REF_POP_DISBURSEMENTS, REF_POP_COUNT, NO_REF_POP_DISBURSEMENTS, NO_REF_POP_COUNT


---

## ⚙️ How it Works

1. The script loads the dataset using **pandas**.
2. It defines a function `perform_z_tests(kpi, base)` to:
   - Calculate conversion rates for each cohort.
   - Perform a **two-proportion z-test**.
   - Display the results.

3. It loops over the following KPI-base pairs:
   - `POP_DISBURSEMENTS` / `POP_COUNT`
   - `DEFAULTED` / `DUE_LOANS`

---

## 🏃 Usage

Run the script in your terminal:

```bash
python kybref.py


Make sure the script and the CSV file are in the same directory, or update the file path accordingly.

🔧 Dependencies
pandas

statsmodels

Install them with:

pip install pandas statsmodels

📈 Example Output

--- Z-Test for POP_DISBURSEMENTS (base: POP_COUNT)----
>> Conversion Rates:
 Reference: 12.34% (123/1000)
 No Reference : 10.00% (100/1000)
>> A/B Test (Reference vs No Reference):
 z = 1.234, p = 0.217
--------------------------------------------------

--- Z-Test for DEFAULTED (base: DUE_LOANS)----
>> Conversion Rates:
 Reference: 5.00% (50/1000)
 No Reference : 8.00% (80/1000)
>> A/B Test (Reference vs No Reference):
 z = -2.345, p = 0.019
--------------------------------------------------


📌 Notes
The script uses the first row of the dataset for the counts ([0] indexing).

Make sure your data file follows the expected column structure for accurate results.

🤝 Contributions & Questions
Feel free to open an issue or a pull request if you’d like to improve or extend the script!

