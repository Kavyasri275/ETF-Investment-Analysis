import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1. LOAD CORRELATION MATRIX
# ============================================================

correlation_file = (
    r"C:\Users\Sathya\ETF_dataset\ETF_correlation_matrix.csv"
)

correlation = pd.read_csv(
    correlation_file,
    index_col=0
)

# ============================================================
# 2. CREATE HEATMAP
# ============================================================

fig, ax = plt.subplots(figsize=(12, 9))

image = ax.imshow(
    correlation.values,
    aspect="auto"
)

# ============================================================
# 3. AXIS LABELS
# ============================================================

ax.set_xticks(range(len(correlation.columns)))
ax.set_yticks(range(len(correlation.index)))

ax.set_xticklabels(
    correlation.columns,
    rotation=45,
    ha="right"
)

ax.set_yticklabels(
    correlation.index
)

# ============================================================
# 4. DISPLAY CORRELATION VALUES
# ============================================================

for i in range(len(correlation.index)):

    for j in range(len(correlation.columns)):

        ax.text(
            j,
            i,
            f"{correlation.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

# ============================================================
# 5. TITLE
# ============================================================

ax.set_title(
    "ETF Monthly Return Correlation Heatmap"
)

fig.colorbar(
    image,
    ax=ax,
    label="Correlation"
)

plt.tight_layout()

# ============================================================
# 6. SAVE FIGURE
# ============================================================

output_file = (
    r"C:\Users\Sathya\ETF_dataset\ETF_correlation_heatmap.png"
)

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nCorrelation heatmap saved to:")
print(output_file)