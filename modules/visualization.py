import matplotlib.pyplot as plt

# 📊 Plot expenses by category
def plot_category_expenses(cat_summary, save_path=None):
    plt.figure(figsize=(8, 6))
    cat_summary.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Expenses by Category", fontsize=14, weight="bold")
    plt.xlabel("Category", fontsize=12)
    plt.ylabel("Total Amount ($)", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"✅ Category expenses chart saved at: {save_path}")
        plt.close()
    else:
        plt.show()

# 📈 Plot monthly expense trend
def plot_monthly_trend(month_summary, save_path=None):
    plt.figure(figsize=(8, 6))
    month_summary.plot(kind='line', marker='o', linestyle='-', color='green')
    plt.title("Monthly Expense Trend", fontsize=14, weight="bold")
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Total Amount ($)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"✅ Monthly trend chart saved at: {save_path}")
        plt.close()
    else:
        plt.show()
