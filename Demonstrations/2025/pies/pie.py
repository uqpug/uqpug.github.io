import os
import matplotlib.pyplot as plt

exts = [
    fext
    for _, _, fs in os.walk("C:/")
    for f in fs
    if (fext := os.path.splitext(f)[1]) != ""
]

ext_counts = {ext: exts.count(ext) for ext in set(exts)}

vals = tuple(ext_counts.values())
labs = tuple(ext_counts.keys())

plt.pie(
    vals,
    [(1 - val / (max(vals) + 1)) for val in vals],
    labs,
    rotatelabels=True,
    autopct=lambda x: str(x),
    shadow=True,
    hatch=["XX", "||", "--"],
)
plt.legend(loc="upper left")

plt.savefig("Demonstrations/pies/pie.png")
