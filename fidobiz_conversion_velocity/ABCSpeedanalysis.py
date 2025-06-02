import pandas as pd 
from scipy.stats import f_oneway, kruskal 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv("ABC_Conversion_Analysis_2025_05_27.csv")

kpis = ['FIDO_SCORE_TO_KYB_SUBMISSION_DURATION', 'KYB_TO_DOC_DURATION', 'DOC_TO_BIZ_APPROVED_DURATION']
cohorts = df['GROUP_NAME'].unique()

results = []

for kpi in kpis: 
    print(f"----- {kpi} -----")
    df_kpi = df[['GROUP_NAME',kpi]].dropna()

    stats = df_kpi.groupby('GROUP_NAME')[kpi].agg(['mean','median', 'count']).reset_index()
    print(stats)

    groups = [df_kpi[df_kpi['GROUP_NAME']== cohort][kpi] for cohort in cohorts]

    anova_stat, anova_p = f_oneway(*groups)
 
    kw_stat, kw_p = kruskal(*groups)

    row_result = {
        'kpi':kpi, 
        'anova_pval':anova_p, 
        'kruskal_pval':kw_p} 
    for c in cohorts: 
        row_result[f'mean_{c}'] = stats.loc[stats["GROUP_NAME"] == c, "mean"].values[0]
        row_result[f'median_{c}'] = stats.loc[stats["GROUP_NAME"] == c, "median"].values[0]
        row_result[f'n_{c}'] = stats.loc[stats["GROUP_NAME"] == c, "count"].values[0]
    
        cohort_data = df_kpi[df_kpi['GROUP_NAME'] == c][kpi]
        plt.figure(figsize=(10,6))
        plt.hist(cohort_data, label=f'Distribution of {kpi} in {c}', bins=40, alpha=0.6)
    
        plt.title(f'Histogram of {kpi} in {c}')
        plt.xlabel('Duration (seconds)')
        plt.ticklabel_format(style='plain', axis='x')
        plt.ylabel('Count')
        plt.show()
    results.append(row_result)
       

print("\n===== Summary Table =====")
summary_df = pd.DataFrame(results)
print(summary_df)

sns.set_theme(style = "whitegrid")

for idx,row in summary_df.iterrows(): 
    kpi = row['kpi']

    means = [row[f'mean_{c}'] for c in cohorts]
    medians = [row[f'median_{c}'] for c in cohorts]

    fig, axes = plt.subplots(1,2, figsize =(12,5))

    sns.barplot(x=cohorts, y=means, ax=axes[0], palette = 'pastel')
    axes[0].set_title(f"{kpi} - Mean by Cohort")
    axes[0].set_ylabel("Mean Duration (seconds)")


    sns.barplot(x=cohorts, y= medians, ax = axes[1], palette = 'muted')
    axes[1].set_title(f"{kpi} - Median by Cohort")
    axes[1].set_ylabel("Median Duration (seconds)")

    plt.tight_layout()
    plt.show()

    print(f"---- {kpi} ----")
    print(f"ANOVA p-value: {row['anova_pval']:.4f}")
    print(f"Kruskal-Wallis p-value: {row['kruskal_pval']:.4f}\n")
 


 # 1️⃣ Prepare data in long-form
mean_data = []
median_data = []

for idx, row in summary_df.iterrows():
    for c in cohorts:
        mean_data.append({
            'kpi': row['kpi'],
            'cohort': c,
            'duration': row[f'mean_{c}'],
            'statistic': 'mean'
        })
        median_data.append({
            'kpi': row['kpi'],
            'cohort': c,
            'duration': row[f'median_{c}'],
            'statistic': 'median'
        })

# Combine mean and median
long_df = pd.DataFrame(mean_data + median_data)

# 2️⃣ Plot for each cohort
for c in cohorts:
    cohort_df = long_df[long_df['cohort'] == c]
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 8))
    
    # Mean
    mean_df = cohort_df[cohort_df['statistic'] == 'mean']
    sns.barplot(data=mean_df, x='kpi', y='duration', ax=axes[0], palette='pastel')
    axes[0].set_title(f"{c} Cohort - Mean Duration")
    axes[0].set_ylabel("Mean Duration (seconds)")
    axes[0].set_xlabel("KPI")
    axes[0].tick_params(axis='x', rotation=45)
    
    # Median
    median_df = cohort_df[cohort_df['statistic'] == 'median']
    sns.barplot(data=median_df, x='kpi', y='duration', ax=axes[1], palette='muted')
    axes[1].set_title(f"{c} Cohort - Median Duration")
    axes[1].set_ylabel("Median Duration (seconds)")
    axes[1].set_xlabel("KPI")
    axes[1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()
