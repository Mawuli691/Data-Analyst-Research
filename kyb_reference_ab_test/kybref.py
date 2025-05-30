import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

#load dataset
df = pd.read_csv("KYB_A_B_Test_Preliminary_2025_05_29.csv")

print(df)

def perform_z_tests(kpi,base):
    def get_values(cohort):
        success = int(df[f"{cohort}_{kpi}"][0])
        total = int(df[f"{cohort}_{base}"][0])
        rate = (success/total) * 100 if total > 0 else 0 
        return success, total, rate 
    
    ref_s, ref_t, ref_r = get_values("REF")
    no_ref_s, no_ref_t, no_ref_r = get_values("NO_REF")

    z_ab, p_ab = proportions_ztest([ref_s, no_ref_s], [ref_t, no_ref_t])

    print(f"\n--- Z-Test for {kpi} (base: {base})----")
    print(">> Conversion Rates:")
    print(f" Reference: {ref_r:.2f}% ({ref_s}/{ref_t})")
    print(f" No Reference : {no_ref_r:.2f}% ({no_ref_s}/{no_ref_t})")

    print(">> A/B Test (Reference vs No Reference):")
    print(f" z = {z_ab:.3f}, p = {p_ab:.3f}")
    print("-"*50)


kpi_bases = {
    "POP_DISBURSEMENTS":"POP_COUNT", 
    "DEFAULTED":"DUE_LOANS"}

for kpi, base in kpi_bases.items():
    perform_z_tests(kpi,base)