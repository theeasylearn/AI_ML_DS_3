import matplotlib.pyplot as plt
# Employee Monthly Salaries (in thousands) by Department
sales = [45, 48, 50, 52, 47, 49, 51, 46, 53, 48, 120, 35] # Note: 120 (manager), 35 (intern) are outliers
engineering = [65, 70, 68, 72, 67, 71, 69, 73, 66, 70, 150, 40] # Note: 150 (senior architect), 40 (junior) are outliers
hr = [38, 42, 40, 44, 39, 43, 41, 45, 38, 42, 28, 55] # Note: 28 (part-time), 55 (director) are outliers
marketing = [50, 55, 52, 58, 53, 56, 54, 57, 51, 55, 95, 32] # Note: 95 (CMO), 32 (intern) are outliers
# Create box plot
plt.figure(figsize=(10, 6))
plt.boxplot([sales, engineering, hr, marketing],labels=['Sales', 'Engineering', 'HR', 'Marketing'])
plt.xlabel('Department', fontsize=12, fontweight='bold')
plt.ylabel('Monthly Salary (in $1000s)', fontsize=12, fontweight='bold')
plt.title('Employee Salary Distribution by Department', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
company_avg = 55 # $55,000 average
plt.axhline(y=company_avg, color='red', linestyle='--', linewidth=1, alpha=0.5, label=f'Company Avg: ${company_avg}k')
plt.legend()
plt.show()
