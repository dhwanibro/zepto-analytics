import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_dashboard(df):
    """
    Generate comprehensive analytics dashboard for Zepto product data
    
    Parameters:
        df (pd.DataFrame): Input dataframe containing:
            - category: Product category
            - revenue: Sales revenue
            - discountpercent: Discount percentage
            - in_stock: Stock availability
            - weightingms: Product weight in grams
            - mrp: Maximum retail price
    """
    # Input validation
    if df is None or df.empty:
        print("⚠️ No data to visualize")
        return

    # Initialize figure
    plt.figure(figsize=(16, 12))
    plt.suptitle('Zepto Product Performance Dashboard',
                fontsize=16,
                fontweight='bold',
                y=1.02)

    # 1. Revenue Analysis
    if 'revenue' in df.columns:
        ax1 = plt.subplot(2, 2, 1)
        revenue_data = (df.groupby('category')['revenue']
                      .sum()
                      .sort_values(ascending=False)
                      .head(10))
        revenue_data.plot(kind='bar',
                        color='#1f77b4',
                        edgecolor='darkblue',
                        ax=ax1)
        ax1.set_title('Top Revenue Categories', fontweight='bold')
        ax1.set_ylabel('Revenue (₹)')
        plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')  # Corrected rotation
        ax1.grid(axis='y', linestyle=':', alpha=0.4)

    # 2. Discount Analysis
    if 'discountpercent' in df.columns:
        ax2 = plt.subplot(2, 2, 2)
        sns.boxplot(data=df,
                   x='category',
                   y='discountpercent',
                   palette='pastel',
                   showfliers=False,
                   ax=ax2)
        ax2.set_title('Discount Distribution', fontweight='bold')
        ax2.set_ylabel('Discount (%)')
        plt.setp(ax2.get_xticklabels(), rotation=90)  # Corrected rotation
        ax2.grid(axis='y', linestyle=':', alpha=0.4)

    # 3. Stock Analysis
    if 'in_stock' in df.columns:
        ax3 = plt.subplot(2, 2, 3)
        stock_data = (df.groupby('category')['in_stock']
                     .mean()
                     .sort_values())
        stock_data.plot(kind='barh',
                      color='#2ca02c',
                      edgecolor='darkgreen',
                      ax=ax3)
        ax3.set_title('In-Stock Probability', fontweight='bold')
        ax3.set_xlabel('Availability Rate')
        ax3.grid(axis='x', linestyle=':', alpha=0.4)
        ax3.set_xlim(0, 1)

    # 4. Weight vs Price Analysis
    if all(col in df.columns for col in ['weightingms', 'mrp', 'category']):
        ax4 = plt.subplot(2, 2, 4)
        sample_df = df.sample(min(1000, len(df))) if len(df) > 1000 else df
        
        sns.scatterplot(data=sample_df,
                       x='weightingms',
                       y='mrp',
                       hue='category',
                       palette='tab20',
                       alpha=0.7,
                       s=50,  # Fixed size
                       ax=ax4)
        
        ax4.set_title('Weight vs Price by Category', fontweight='bold')
        ax4.set_xlabel('Weight (grams) [Log Scale]')
        ax4.set_ylabel('MRP (₹)')
        ax4.set_xscale('log')
        ax4.grid(True, which='both', linestyle=':', alpha=0.3)
        ax4.legend(bbox_to_anchor=(1.05, 1),
                  loc='upper left',
                  title='Category')

    plt.tight_layout()
    plt.show()
