import streamlit as st
import pandas as pd

# Load CSV from same folder
data = pd.read_csv("stock.csv")

st.title("Stock Checker")

item_code = st.text_input("Enter Item Details")

if item_code:
    result = data[data['Item Details'].astype(str).str.contains(item_code, case=False, na=False)]

    if not result.empty:
        qty = result.iloc[0]['Qty.']
        unit = result.iloc[0]['Unit']
        st.success(f"Stock: {qty} {unit}")
    else:
        st.error("Item not found")
