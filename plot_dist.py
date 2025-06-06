
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# plot settings
plt.rcParams.update({'font.size': 17})
plt.rcParams["font.family"]="Sans-serif"
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.linewidth'] = 2.5
plt.rcParams['xtick.major.size'] = 9.5
plt.rcParams['xtick.major.width'] = 2.5
plt.rcParams['xtick.minor.size'] = 6
plt.rcParams['xtick.minor.width'] = 2.5
plt.rcParams['axes.labelsize'] = 18

# Load data into a Pandas DataFrame
df = pd.read_csv("vloose_dists.dat", delim_whitespace=True, 
                 usecols=[3, 11], header=None, names=['TRP Residue', 'Distance'])

# convert to array
#dists = df.to_numpy()

def plot_res_dists(df, resid, ax, plot="hist"):
    """
    Plot a single TRP residue distance distribution.

    Parameters
    ----------
    dists : pandas.DataFrame
        column 1 = resid | column 2 = distance
    resid : int
        resid of interest
    """
    # Filter DataFrame for 'TRP Residue'
    trp_data = df[df['TRP Residue'] == resid]

    if plot == "hist":
        # plot histogram
        ax.hist(trp_data['Distance'], bins=10, label=f"TRP {resid}",
                edgecolor='black')#, alpha=0.5)#color=""
    elif plot == "kde":
        # plot KDE
        # Fit KDE to the 'Distance' data
        kde = gaussian_kde(trp_data['Distance'])

        # Generate values for the continuous distribution
        x_vals = np.linspace(trp_data['Distance'].min(), trp_data['Distance'].max(), 100)
        y_vals = kde(x_vals)

        # Plot histogram
        # plt.hist(trp_data['Distance'], bins=10, density=True, 
        #          alpha=0.5, edgecolor='black', label=f"TRP {resid}")

        # Plot KDE
        ax.plot(x_vals, y_vals, label=f"TRP {resid}", linewidth=2.5)

fig, ax = plt.subplots()

trps = [37, 74, 108, 121, 152]
for trp in trps:
    plot_res_dists(df, trp, ax, "hist")

# Set labels and title
ax.set_xlabel('Distance ($\AA$)')
#plt.ylabel('Frequency')

# Hide borders
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)

# Hide y-axis ticks and labels
#ax.tick_params(left=False)
ax.set_yticklabels([])
ax.set_yticks([])

ax.set_title("Very Loose MTSL")

plt.legend(bbox_to_anchor=[1,1], fontsize=12, frameon=False)

plt.tight_layout()
#plt.savefig("vloose_hist.pdf")
plt.show()