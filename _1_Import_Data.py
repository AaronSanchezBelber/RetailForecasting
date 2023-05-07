import os
import pandas as pd

PATH_FOLDER = os.path.join(os.getcwd(), r"C:\Users\Lenovo\Desktop\Master Data Science - Nuclio Digital School\Projects\TimeSeries\Data")

merged = os.path.join(PATH_FOLDER, 'df_merged.csv', index_col=0)

df_merged = pd.read_csv(merged)

df_merged