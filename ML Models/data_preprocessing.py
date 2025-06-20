# -*- coding: utf-8 -*-
"""order_data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oRQCbLGtf75jCj83KqKMlvrwPlbJIVmt
"""

import pandas as pd

# Merge multiple galaxy datasets
def merge_galaxy_datasets(galaxy_files):
    galaxy_dataframes = []
    for file in galaxy_files:
        df = pd.read_csv(file, delimiter=",", header=0)  # Adjust delimiter if needed
        galaxy_dataframes.append(df)
    merged_galaxy_data = pd.concat(galaxy_dataframes, ignore_index=True)
    # Drop duplicates based on 'objid' if needed
    merged_galaxy_data = merged_galaxy_data.drop_duplicates(subset=['objid'])
    return merged_galaxy_data

# List of galaxy data files
galaxy_files = [
    "quasar_00_10.csv",  # 0-01
    "quasar_10_20.csv",  # 0-01
    "quasar_20_100.csv",  # 0-01
]

# Load and merge galaxy datasets
merged_galaxy_data = merge_galaxy_datasets(galaxy_files)

# Load supernova data
supernova_data = pd.read_csv('supernova_data.dat', delimiter=" ", header=0)

# Filter supernova data for zCMB values between 0 and 0.1
filtered_supernova_data = supernova_data[(supernova_data['zCMB'] >= 0) & (supernova_data['zCMB'] <= 3)]

# Initialize results list
results = []

# Process supernova data
for _, sn_row in filtered_supernova_data.iterrows():
    sn_zCMB = sn_row['zCMB']
    sn_CID = sn_row['CID']
    sn_MU_SH0ES = sn_row['MU_SH0ES']
    sn_m_b_corr = sn_row['m_b_corr']

    # Add z_diff column to the merged galaxy data
    merged_galaxy_data['z_diff'] = merged_galaxy_data['redshift'] - sn_zCMB

    # Filter galaxies based on z_diff range
    filtered_galaxies = merged_galaxy_data[
        (merged_galaxy_data['z_diff'] >= -0.0004) &
        (merged_galaxy_data['z_diff'] <= 0.0004)
    ]

    # Sort galaxies by absolute z_diff and select the 20 closest
    closest_galaxies = filtered_galaxies.nsmallest(100, 'z_diff')

    # Add data for each closest galaxy to the results
    for _, galaxy_row in closest_galaxies.iterrows():
        result_row = [
            sn_CID,             # Supernova CID
            sn_zCMB,            # Supernova zCMB
            sn_MU_SH0ES,        # Supernova MU_SH0ES
            sn_m_b_corr,        # Supernova m_b_corr
            galaxy_row['u'],    # u-band magnitude
            galaxy_row['g'],    # g-band magnitude
            galaxy_row['r'],    # r-band magnitude
            galaxy_row['i'],    # i-band magnitude
            galaxy_row['z'],    # z-band magnitude
            galaxy_row['redshift'],  # Galaxy redshift
            galaxy_row['objid'],    # Galaxy objid
            galaxy_row['z_diff']    # zCMB - redshift difference
        ]
        results.append(result_row)


# Define output columns
columns = ['cid', 'zcmb', 'MU_SH0ES', 'm_b_corr', 'u', 'g', 'r', 'i', 'z', 'redshift', 'objid', 'z_diff']

# Create DataFrame for the results
output_df = pd.DataFrame(results, columns=columns)

# Save the output to a file
output_df.to_csv('supernova_quasar_output.csv', index=False)

# Print a few rows of the output
print(output_df.head())

import pandas as pd
from tqdm import tqdm

# Merge multiple galaxy datasets
def merge_galaxy_datasets(galaxy_files):
    galaxy_dataframes = []
    for file in galaxy_files:
        df = pd.read_csv(file, delimiter=",", header=0)
        galaxy_dataframes.append(df)
    merged_galaxy_data = pd.concat(galaxy_dataframes, ignore_index=True)
    merged_galaxy_data = merged_galaxy_data.drop_duplicates(subset=['objid'])
    return merged_galaxy_data

# List of galaxy data files
galaxy_files = [
    "quasar_00_10.csv",
    "quasar_10_20.csv",
    "quasar_20_100.csv",
]

# Load and merge galaxy datasets
merged_galaxy_data = merge_galaxy_datasets(galaxy_files)

# Load supernova data (using whitespace delimiter)
supernova_data = pd.read_csv('Pantheon+SH0ES.dat', delim_whitespace=True, header=0)

# Filter supernova data for zCMB values between 0 and 3
filtered_supernova_data = supernova_data[(supernova_data['zCMB'] >= 0) & (supernova_data['zCMB'] <= 3)]

# Initialize results list
results = []

# Use tqdm to visualize progress
for _, sn_row in tqdm(filtered_supernova_data.iterrows(), total=filtered_supernova_data.shape[0]):
    sn_zCMB = sn_row['zCMB']
    sn_CID = sn_row['CID']
    sn_MU_SH0ES = sn_row['MU_SH0ES']
    sn_MU_SH0ES_err = sn_row['MU_SH0ES_ERR_DIAG']
    sn_m_b_corr = sn_row['m_b_corr']
    sn_m_b_corr_err = sn_row['m_b_corr_err_DIAG']
    sn_zCMB_err = sn_row['zCMBERR']

    # Calculate z_diff once per SN
    merged_galaxy_data['z_diff'] = merged_galaxy_data['redshift'] - sn_zCMB

    # Filter galaxies based on z_diff range
    filtered_galaxies = merged_galaxy_data[
        (merged_galaxy_data['z_diff'] >= -0.0004) &
        (merged_galaxy_data['z_diff'] <= 0.0004)
    ]

    # Sort galaxies by absolute z_diff and select 100 closest
    closest_galaxies = filtered_galaxies.iloc[
        (filtered_galaxies['z_diff'].abs()).argsort()[:100]
    ]

    # Add data for each closest galaxy to the results
    for _, galaxy_row in closest_galaxies.iterrows():
        result_row = [
            sn_CID,
            sn_zCMB,
            sn_zCMB_err,
            sn_MU_SH0ES,
            sn_MU_SH0ES_err,
            sn_m_b_corr,
            sn_m_b_corr_err,
            galaxy_row['u'],
            galaxy_row['g'],
            galaxy_row['r'],
            galaxy_row['i'],
            galaxy_row['z'],
            galaxy_row['redshift'],
            galaxy_row['objid'],
            galaxy_row['z_diff']
        ]
        results.append(result_row)

# Define output columns
columns = ['cid', 'zcmb', 'zcmb_err', 'MU_SH0ES', 'MU_SH0ES_err', 'm_b_corr', 'm_b_corr_err',
           'u', 'g', 'r', 'i', 'z', 'redshift', 'objid', 'z_diff']

# Create DataFrame for the results
output_df = pd.DataFrame(results, columns=columns)

# Save the output to a file
output_df.to_csv('supernova_quasar_output_with_errors.csv', index=False)

# Show preview of the output
import ace_tools as tools; tools.display_dataframe_to_user(name="Supernova-Quasar Matches with Errors", dataframe=output_df)