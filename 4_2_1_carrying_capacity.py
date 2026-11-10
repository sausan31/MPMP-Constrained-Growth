
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy.interpolate import PchipInterpolator

# Data historis
tahun = np.array([2019, 2020, 2021, 2022, 2023, 2024, 2025])
kapasitas = np.array([698, 809, 929, 1087, 1223, 1341, 1357])

# Carrying Capacity (NLS)
M = 1690.81

# Interpolasi agar garis lebih halus
tahun_smooth = np.linspace(2019, 2025, 500)
interpolasi = PchipInterpolator(tahun, kapasitas)
kapasitas_smooth = interpolasi(tahun_smooth)

# Membuat grafik
fig, ax = plt.subplots(figsize=(12, 7), dpi=150)

# Garis kapasitas aktual smooth
ax.plot(
    tahun_smooth,
    kapasitas_smooth,
    color="#00558A",
    linewidth=2.5,
    label="Data aktual (MW)"
)

# Titik data aktual tetap ditampilkan
ax.scatter(
    tahun,
    kapasitas,
    color="#00558A",
    s=85,
    zorder=3
)

# Garis batas M
ax.axhline(
    y=M,
    color="#D32F2F",
    linestyle=(0, (6, 5)),
    linewidth=2.5,
    label="M (NLS) = 1.690,81 MW"
)

# Judul
ax.set_title(
    "Kapasitas aktual vs batas M",
    fontsize=20,
    fontweight="bold",
    color="black",
    pad=24
)

# Label sumbu
ax.set_ylabel("MW", fontsize=16, color="black")

# Pengaturan sumbu
ax.set_xticks(tahun)
ax.set_ylim(0, 2000)
ax.set_yticks(range(0, 2001, 250))

# Format angka Indonesia
ax.yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"{x:,.0f}".replace(",", "."))
)

# Warna label hitam
ax.tick_params(
    axis="both",
    labelsize=14,
    labelcolor="black"
)

# Grid horizontal
ax.grid(
    axis="y",
    color="#BBBBBB",
    linewidth=0.8
)

# Bingkai grafik
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# Legenda
ax.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, -0.08),
    ncol=2,
    fontsize=14,
    frameon=False,
    labelcolor="black"
)

plt.tight_layout()

# Simpan gambar HD
nama_file = "4.2.1_Carrying_Capacity_IT_Data_Center.png"

plt.savefig(
    nama_file,
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()
