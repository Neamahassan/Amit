from config import DROP_COLS
from pro import drop_cols
import pandas as pd

# read the dataset
df = pd.read_csv("Titanic.csv")

#drop the columns specified in the config file
df = drop_cols(df, DROP_COLS)
print(df.head())