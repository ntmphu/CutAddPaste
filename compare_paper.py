
import pandas as pd
import matplotlib.pyplot as plt

# 1. Nhập kết quả từ paper gốc
# Thay None bằng số liệu thực tế của paper
paper = {
    "Affiliation F1": None,
    "RPA F1": 68.22,
    "PA F1": 81.95,
    "PW F1": None,
}

# 2. Nhập kết quả thực nghiệm của bạn
# Thay None bằng số liệu sau khi chạy xong 250 series
my_result = {
    "Affiliation F1": None,
    "RPA F1": 50.98,
    "PA F1": 65.53,
    "PW F1": None,
}

# 3. Tạo bảng so sánh
df = pd.DataFrame({
    "Paper": paper,
    "Reproduction": my_result
}).dropna()

if df.empty:
    print("Hãy nhập kết quả paper và thực nghiệm trước.")
else:
    df["Difference"] = df["Reproduction"] - df["Paper"]

    print("\n=== CutAddPaste: Paper vs Reproduction ===")
    print(df.round(4))

    # 4. Lưu bảng
    df.to_csv("paper_comparison.csv")

    # 5. Vẽ biểu đồ
    df[["Paper", "Reproduction"]].plot(
        kind="bar", figsize=(9, 5)
    )

    plt.title("CutAddPaste: Paper vs Reproduction")
    plt.ylabel("Score")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("paper_comparison.png", dpi=200)
    plt.show()
