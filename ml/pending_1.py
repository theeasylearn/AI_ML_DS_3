


# ========================================================
# FINAL SUMMARY + VISUALIZATION
# ========================================================
print("\nCOMPLETE PIPELINE FINISHED SUCCESSFULLY!")
print("You now have two ready-to-use feature sets:")
print("   • X_standard → Recommended for most ML models")
print("   • X_minmax   → Good for neural networks / distance-based algorithms")
print("   • y          → Target variable")
print(f"Final shape     : {X_standard.shape}")

# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(X_standard.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap After Full Preprocessing')
plt.tight_layout()
plt.show()

print("\nNext step: You can now train any ML model on X_standard and y")