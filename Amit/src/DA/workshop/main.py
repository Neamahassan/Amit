from config import DROP_COLS
from pro import drop_cols  # (أو اسم ملف الـ py اللي فيه الدالة)
import pandas as pd

# قراءة الملف
df = pd.read_csv("Titanic.csv")

# استدعاء الدالة باستخدام المتغير المستورد من config
df = drop_cols(df, DROP_COLS)
print(df.head())