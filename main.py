import os
from modules.data_processing import load_data, categorize_expenses, monthly_summary
from modules.ml_model import predict_next_month
from modules.visualization import plot_category_expenses, plot_monthly_trend

# ✅ Get absolute base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ Path to CSV inside "assets" folder
file_path = os.path.join(BASE_DIR, "assets", "sample_expense_data.csv")

# ✅ Debug check to avoid FileNotFoundError
if not os.path.exists(file_path):
    raise FileNotFoundError(f"CSV file not found at: {file_path}\n"
                            f"Make sure 'sample_expense_data.csv' exists in the assets folder.")

# Load data
df = load_data(file_path)

# Category summary
cat_summary = categorize_expenses(df)
print("\n📊 Expense by Category:\n", cat_summary)

# Monthly summary
month_summary = monthly_summary(df)
print("\n📅 Monthly Expenses:\n", month_summary)

# Plot visuals (saved inside assets/)
charts_dir = os.path.join(BASE_DIR, "assets")
os.makedirs(charts_dir, exist_ok=True)

plot_category_expenses(cat_summary, save_path=os.path.join(charts_dir, "category_expenses.png"))
plot_monthly_trend(month_summary, save_path=os.path.join(charts_dir, "monthly_trend.png"))

print(f"\n✅ Charts saved in: {charts_dir}")

# Predict next month's expenses
prediction = predict_next_month(month_summary)
print(f"\n🤖 Predicted next month's total expenses: ${prediction:.2f}")
