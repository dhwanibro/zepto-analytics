def generate_insights(df):
    """Print business insights"""
    if df is None:
        print("⚠️ No data to generate insights")
        return

    print("\n📊 Zepto Strategic Insights")
    print("="*50)

    if 'availablequantity' in df.columns:
        low_stock = (df.groupby('category')['availablequantity']
                    .mean()
                    .nsmallest(3)
                    .index.tolist())
        print(f"\n🚨 Low Stock Alert: Prioritize {', '.join(low_stock)}")

    if all(col in df.columns for col in ['mrp', 'discountpercent', 'quantity']):
        elasticity = df[['mrp', 'quantity']].corr().iloc[0,1]
        print(f"\n💰 Price Elasticity: {elasticity:.2f}")
        print("   - Consider discounts on high-MRP items" if elasticity < -0.3 
              else "   - Maintain current pricing strategy")

    if 'weightingms' in df.columns:
        heavy_items = df[df['weightingms'] > 1000]['category'].unique()
        print(f"\n📦 Heavy Items: {len(heavy_items)} categories exceed 1kg")
        print("   - Optimize delivery logistics for these items")
