import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from zepto.load import load_data
from zepto.preprocess import preprocess_data
from zepto.dashboard import generate_dashboard
from zepto.insights import generate_insights

import warnings
warnings.filterwarnings('ignore')

# Config
plt.style.use('ggplot')
sns.set_palette("husl")
pd.set_option('display.float_format', '{:.2f}'.format)

# Load and process
df = load_data('data/Zepto.xlsx')
df = preprocess_data(df)

if __name__ == "__main__":
    if df is not None:
        print(f"✅ Successfully loaded {len(df):,} records")
        print("Available columns:", df.columns.tolist())
        generate_dashboard(df)
        generate_insights(df)
    else:
        print("❌ Analysis failed - please check input data")


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='weightInGms', y='mrp', alpha=0.5)
plt.title('Weight vs MRP')
plt.xlabel('Weight (gms)')
plt.ylabel('MRP (₹)')
plt.grid(True)
plt.show()
