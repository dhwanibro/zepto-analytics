import pandas as pd

def load_data(file_path):
    """Load data from Excel with required columns and sheet structure"""
    try:
        all_sheets = pd.read_excel(file_path, sheet_name=None)
        if not all_sheets:
            raise ValueError("Excel file contains no sheets")

        combined = []
        required_cols = {'mrp', 'quantity'}

        for sheet_name, df in all_sheets.items():
            df = df.copy()
            df['category'] = sheet_name

            if not required_cols.issubset(df.columns):
                missing = required_cols - set(df.columns)
                print(f"⚠️ Sheet '{sheet_name[:20]}...' missing: {missing}")
                continue

            df.columns = df.columns.str.lower().str.replace('[^a-z0-9]', '_', regex=True)
            combined.append(df)

        if not combined:
            raise ValueError("No valid sheets found")

        return pd.concat(combined, ignore_index=True)

    except Exception as e:
        print(f"❌ Data loading failed: {str(e)}")
        return None
