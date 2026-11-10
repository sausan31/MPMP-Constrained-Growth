
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy.interpolate import PchipInterpolator

# ==========================================
# DATA DAN PARAMETER
# ==========================================

tahun = np.array([2019, 2020, 2021, 2022, 2023, 2024, 2025])
kapasitas = np.array([698, 809, 929, 1087, 1223, 1341, 1357])

P0 = 698
r = 0.313522
M = 1690.81

t_smooth = np.linspace(0, 6, 500)
tahun_smooth = 2019 + t_smooth

# ==========================================
# MODEL PERTUMBUHAN
# ==========================================

# Model eksponensial (ilustrasi)
eksponensial = P0 * np.exp(r * t_smooth)

# Model logistik NLS
A = (M - P0) / P0
logistik = M / (1 + A * np.exp(-r * t_smooth))

# Interpolasi data aktual
interpolasi = PchipInterpolator(tahun, kapasitas)
aktual_smooth = interpolasi(tahun_smooth)

# ==========================================
# MEMBUAT GRAFIK
# ==========================================

fig, ax = plt.subplots(figsize=(12, 7), dpi=150)

# Data aktual - Biru navy
ax.plot(
    tahun_smooth,
    aktual_smooth,
    color="#2563A6",
    linewidth=2.8,
    label="Data aktual"
)

ax.scatter(
    tahun,
    kapasitas,
    color="#2563A6",
    s=85,
    zorder=5
)

# Eksponensial - Merah koral
ax.plot(
    tahun_smooth,
    eksponensial,
    color="#E76F51",
    linestyle=(0, (6, 4)),
    linewidth=2.8,
    label="Eksponensial (ilustrasi)"
)

# Titik eksponensial setiap tahun
t_tahunan = tahun - 2019
eksponensial_tahunan = P0 * np.exp(r * t_tahunan)

ax.scatter(
    tahun,
    eksponensial_tahunan,
    color="#E76F51",
    s=85,
    zorder=5
)

# Logistik NLS - Hijau teal
ax.plot(
    tahun_smooth,
    logistik,
    color="#159895",
    linewidth=3,
    label="Logistik (NLS)"
)

# Carrying capacity - Ungu
ax.axhline(
    y=M,
    color="#8B5CF6",
    linestyle=(0, (7, 4)),
    linewidth=2.5,
    label="M (NLS) = 1.690,81 MW"
)

# ==========================================
# JUDUL DAN LABEL
# ==========================================

ax.set_title(
    "Perbandingan Pertumbuhan Kapasitas IT Data Center",
    fontsize=20,
    fontweight="bold",
    color="black",
    pad=24
)

ax.set_ylabel("MW", fontsize=16, color="black")

# ==========================================
# PENGATURAN SUMBU
# ==========================================

ax.set_xticks(tahun)
ax.set_xlim(2018.5, 2025.5)

ax.set_ylim(0, 5000)

# Interval 500 MW
ax.set_yticks(range(0, 5001, 500))

# Format angka Indonesia
ax.yaxis.set_major_formatter(
    FuncFormatter(
        lambda x, pos: f"{x:,.0f}".replace(",", ".")
    )
)

# Seluruh label hitam
ax.tick_params(
    axis="both",
    labelsize=12,
    labelcolor="black"
)

# Grid horizontal
ax.grid(
    axis="y",
    color="#D1D5DB",
    linewidth=0.8,
    alpha=0.8
)

# Bingkai grafik
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# ==========================================
# LEGENDA
# ==========================================

ax.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, -0.08),
    ncol=2,
    fontsize=12,
    frameon=False,
    labelcolor="black"
)

plt.tight_layout()

# ==========================================
# SIMPAN GAMBAR HD
# ==========================================

nama_file = "4.2.2_Perbandingan_Eksponensial_Logistik.png"

plt.savefig(
    nama_file,
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()
