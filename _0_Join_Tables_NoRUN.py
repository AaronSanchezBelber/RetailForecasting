import os 
import pandas as pd

PATH_FOLDER = os.path.join(os.getcwd(), r"C:\Users\Lenovo\Desktop\Master Data Science - Nuclio Digital School\Projects\TimeSeries\Data")

daily_calendar_with_events = os.path.join(PATH_FOLDER, 'daily_calendar_with_events.csv')
item_prices = os.path.join(PATH_FOLDER, 'item_prices.csv')
item_sales = os.path.join(PATH_FOLDER, 'item_sales.csv')

df_events = pd.read_csv(daily_calendar_with_events)
df_prices = pd.read_csv(item_prices)
df_sales = pd.read_csv(item_sales)

df_prices = df_prices.sample(1000000)

df_events.drop_duplicates(inplace=True)
df_prices.drop_duplicates(inplace=True)
df_sales.drop_duplicates(inplace=True)

df_sales_melt = pd.melt(df_sales, id_vars=['id','item','category','department','store','store_code','region'], var_name='d', value_name='sales')
df_sales_sorted = df_sales_melt.sort_values(by=['id','item','category','department','store','store_code','region','d'])
df_sales_final = df_sales_sorted.rename(columns={'sales': 'a'})
df_sales_final = df_sales_final[['id','item','category','department','store','store_code','region', 'd']]

df_sales_final.to_csv(r'C:\Users\Lenovo\Desktop\Master Data Science - Nuclio Digital School\Projects\TimeSeries\Data\df_sales_final.csv')
df_sales_final = pd.read_csv(r'C:\Users\Lenovo\Desktop\Master Data Science - Nuclio Digital School\Projects\TimeSeries\Data\df_sales_final.csv', index_col=0)

df_sales_final = df_sales_final.sample(1000000)

df_1 = df_sales_final.merge(df_events, on="d")
df_1.drop(['event'], axis=1, inplace=True)
df_1 = df_1.sample(300000)
df_prices = df_prices.sample(300000)
df_merged = df_1.merge(df_prices, on='item')

df_merged.to_csv(r'C:\Users\Lenovo\Desktop\Master Data Science - Nuclio Digital School\Projects\TimeSeries\Data\df_merged.csv')