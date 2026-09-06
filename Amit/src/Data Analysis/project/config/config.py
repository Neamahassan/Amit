"""
project configuration  file.
Here, we define constants or settings that my change
with modifying the preprocessing code.

"""
# path to the raw dataset file
RAW_DATA_PATH = "data/raw/Titanic.csv"
# columns to drop because they are not useful for the analysis/model
# They are defined here so they can be changed without modifying preprocessing.py
COLUMNS_TO_DROP =["PassengerId", "Name", "Ticket"]




