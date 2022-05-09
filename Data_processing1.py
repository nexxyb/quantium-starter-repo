import pandas as pd

#read files from folder
df0 = pd.read_csv("daily_sales_data_0.csv", index_col = "product", parse_dates= ["date"])
df1 = pd.read_csv("daily_sales_data_1.csv", index_col = "product", parse_dates= ["date"])
df2 = pd.read_csv("daily_sales_data_2.csv", index_col = "product", parse_dates= ["date"])

#combine the 3files together
df0.to_csv("Total_sales.csv", mode= 'w')
df1.to_csv("Total_sales.csv", mode= 'a')
df2.to_csv("Total_sales.csv", mode= 'a')

#read the combined file to dataframe
df= pd.read_csv("Total_sales.csv", parse_dates= ['date'])

#drop rows not relevanrt to 'pink morsel'
p_names=df[ (df['product'] != 'pink morsel')].index
df.drop(p_names, inplace=True)

#remove $ from price column
def cleanup(x):
    if isinstance(x, str):
        return(x.replace('$',''))

df['price']= df['price'].apply(cleanup).astype('float')
df['price_type']= df["price"].apply(lambda x: type(x).__name__)

#convert quantity to float
df['quantity']= df['quantity'].astype('float')
df['quantity_type']= df["quantity"].apply(lambda x: type(x).__name__)

#create new 'sales' column
df['sales']= df['price'] * df['quantity']

#drop all columns except sale, region and date
df.drop(['product', 'price', 'quantity', 'price_type', 'quantity_type'], axis = 1, inplace=True)

#write the dataframe to csv
df.to_csv('Final_sales.csv')