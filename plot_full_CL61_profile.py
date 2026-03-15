import glob
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.colors import Normalize
import matplotlib.dates as mdates


# Task: do from 01 - 31 Normal plotting [Total Backscatter/Attenuated Backscatter]
# norm=LogNorm(vmin=1e-7, vmax=1e-5): Normal [Total Backscatter/Attenuated Backscatter]

for date in ['01','02','03','04','05','06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']:
    folderPath = fr"C:\Users\aryan\OneDrive\Desktop\HUBeltsvilleData\HU-IRB-2025-07\{date}\*.nc"
    data_files = sorted(glob.glob(folderPath, recursive=True))
    ds = xr.open_mfdataset(data_files, combine='by_coords')
    # Extract variables
    beta_att = ds['linear_depol_ratio'].values  #beta_att, p_pol, x_pol, linear_depol_ratio
    time = ds['time'].values
    altitude = ds['range'].values / 1000  # Altitude in km

    # Create plot (high-resolution)
    plt.figure(figsize=(15, 7), dpi=300)
    # positive_beta_att = beta_att[beta_att > 0]
    # vmin = np.nanpercentile(positive_beta_att, 1)
    # vmax = np.nanpercentile(positive_beta_att, 99)

    # Plot with Logarithmic scale explicitly between 1e-7 and 1e-5
    plt.pcolormesh(
        time, altitude, beta_att.T,
        shading='auto',
        cmap='jet',
        norm=LogNorm(vmin=1e-2, vmax=1e1)
    # norm=Normalize(vmin=0.0, vmax=0.25) # Use this for plotting the depolarization ratio
    )

    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.HourLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H'))
    # ax.set_ylim(0, 6)  # Limit altitude to 6 km

    # Add colorbar
    cbar = plt.colorbar(label='(m⁻¹ sr⁻¹)')
    cbar.ax.tick_params(labelsize=14)
    cbar.set_label(' (m⁻¹ sr⁻¹)', fontsize=16)
    # plt.ylim(0, 6)

    plt.ylabel('Altitude (km)', fontsize=16)
    plt.title(f'Vaisala CL61 @ HU-IRB: July 2025 (linear_depolarization) - Day {date}', fontsize=12)
    plt.grid(True)
    plt.savefig(f'linearDepolarization_{date}_test1.png', bbox_inches='tight', dpi=300)
    break
'''
# Set plot labels and titles
plt.xlabel('Date and Time (UTC)', fontsize=16)
plt.ylabel('Altitude (km)', fontsize=16)
#plt.title('Vaisala CL61 @ HUBC: 21-26 May 2023 (linear_depol_ratio)', fontsize=18)

# Customize x-axis ticks to start at 00, then 06, 12, etc.
plt.gca().xaxis.set_major_locator(mdates.HourLocator(byhour=[0, 6, 12, 18]))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%H'))

# Adjust tick parameters
plt.xticks(rotation=45, fontsize=14)
plt.yticks(fontsize=14)

# Set altitude limit
plt.ylim(0, 6)

# Final adjustments
plt.grid(True)
plt.tight_layout()

# Display and save figure
plt.savefig('linear_depol_ratio_CL61_05-09June2023_FullProfile.png', bbox_inches='tight', dpi=300)
plt.show()
'''

'''
# Extract variables
beta_att = ds['linear_depol_ratio'].values  #beta_att, p_pol, x_pol, linear_depol_ratio
time = ds['time'].values
altitude = ds['range'].values / 1000  # Altitude in km


# Create plot (high-resolution)
fig, ax = plt.subplots(figsize=(10, 8))

# Plot with Logarithmic scale explicitly between 1e-7 and 1e-5
mesh = ax.pcolormesh(
    time, altitude, beta_att.T,
    shading='auto',
    cmap='jet',
    norm=LogNorm(vmin=1e-7, vmax=1e-5)
    # norm=Normalize(vmin=0.0, vmax=0.25)  # Uncomment for depolarization ratio
)

# Add colorbar
fig.colorbar(mesh, ax=ax, label="Backscatter Coefficient")

plt.xlabel("Time")
plt.ylabel("Altitude")
plt.title("Attenuated Backscatter")
plt.savefig('linear_depol_ratio_CL61_05-09June2023_FullProfile.png', bbox_inches='tight', dpi=300)
plt.show()


# Add colorbar
cbar = plt.colorbar(label='(m⁻¹ sr⁻¹)')
cbar.ax.tick_params(labelsize=14)
cbar.set_label(' (m⁻¹ sr⁻¹)', fontsize=16)

# Set plot labels and titles
plt.xlabel('Date and Time (UTC)', fontsize=16)
plt.ylabel('Altitude (km)', fontsize=16)
#plt.title('Vaisala CL61 @ HUBC: 21-26 May 2023 (linear_depol_ratio)', fontsize=18)

# Customize x-axis ticks to start at 00, then 06, 12, etc.
plt.gca().xaxis.set_major_locator(mdates.HourLocator(byhour=[0, 6, 12, 18]))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%H'))

# Adjust tick parameters
plt.xticks(rotation=45, fontsize=14)
plt.yticks(fontsize=14)

# Set altitude limit
plt.ylim(0, 6)

# Final adjustments
plt.grid(True)
plt.tight_layout()

# Display and save figure
plt.savefig('linear_depol_ratio_CL61_05-09June2023_FullProfile.png', bbox_inches='tight', dpi=1200)
'''
