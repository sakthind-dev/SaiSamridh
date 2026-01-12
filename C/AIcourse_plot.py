# Creating decision matrix plot for MSc AI universities in Europe

import matplotlib.pyplot as plt

# University data
universities = [
    "Erasmus Mundus EMAI",
    "TUM (Germany)",
    "ETH Zurich",
    "KU Leuven",
    "Univ. of Amsterdam",
    "Univ. of Edinburgh",
    "Univ. of Helsinki",
    "Univ. of Warsaw",
    "Politecnico di Milano",
    "Sapienza Univ. of Rome"
]

# Cost in Euros (converted where needed)
costs = [
    0,      # Erasmus Mundus EMAI
    300,    # TUM
    1200,   # ETH Zurich
    7500,   # KU Leuven (average)
    13000,  # Amsterdam
    32500,  # Edinburgh (avg of £25k–£30k, converted to EUR ~1.15)
    13500,  # Helsinki (avg)
    4000,   # Warsaw
    3950,   # Politecnico di Milano
    3150    # Sapienza
]

# Prestige levels mapped to numeric scale
prestige_levels = {
    "Medium": 1,
    "Medium-High": 2,
    "High": 3,
    "Very High": 4
}
prestige = [
    prestige_levels["High"],         # EMAI
    prestige_levels["High"],         # TUM
    prestige_levels["Very High"],    # ETH
    prestige_levels["High"],         # KU Leuven
    prestige_levels["High"],         # Amsterdam
    prestige_levels["Very High"],    # Edinburgh
    prestige_levels["Medium-High"],  # Helsinki
    prestige_levels["Medium"],       # Warsaw
    prestige_levels["Medium-High"],  # Politecnico
    prestige_levels["Medium"]        # Sapienza
]

# Scholarship availability (bubble size)
scholarship_scores = [
    100,  # EMAI (full)
    80,   # TUM (DAAD + merit)
    70,   # ETH (Excellence)
    60,   # KU Leuven
    50,   # Amsterdam
    50,   # Edinburgh
    40,   # Helsinki
    40,   # Warsaw
    40,   # Politecnico
    30    # Sapienza
]

# Plotting
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(12, 8))
scatter = ax.scatter(costs, prestige, s=scholarship_scores, alpha=0.7, c=prestige, cmap='viridis', edgecolors='k')

# Annotate each point
for i, university in enumerate(universities):
    ax.text(costs[i]+200, prestige[i]+0.05, university, fontsize=9)

# Axis labels and title
ax.set_xlabel("Cost (Euros per Year)", fontsize=12)
ax.set_ylabel("Prestige (1=Low, 4=Very High)", fontsize=12)
ax.set_title("Decision Matrix: MSc AI Programs in Europe", fontsize=14)
ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(["Medium", "Medium-High", "High", "Very High"])
ax.grid(True)

# Save plot
output_path = "/mnt/data/msc_ai_decision_matrix.png"
plt.tight_layout()
plt.savefig(output_path)
print("Saved decision matrix plot as msc_ai_decision_matrix.png")
