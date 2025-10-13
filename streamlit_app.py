#!/usr/bin/env python3
import streamlit as st

LB_TO_KG = 0.45359237

st.set_page_config(page_title="WestPak Avocado Box Weight Calculator", layout="centered")
st.title("WestPak Avocado Box Weight Calculator")

st.markdown("Enter your inputs below. Calculated fields update when all required inputs are provided.")

# --- Line 1: Bags & pieces ---
col1, col2 = st.columns(2)
num_bags = col1.number_input("# of Bags", min_value=0, step=1, format="%d")
pieces_per_bag = col2.number_input("Pieces per bag", min_value=0, step=1, format="%d")

total_pieces = num_bags * pieces_per_bag
st.text_input("Total pieces (calculated)", value=str(total_pieces), disabled=True)

# --- Line 2: Lug & size ---
col3, col4 = st.columns(2)
equiv_lug_lb = col3.number_input("Equivalent Lug Weight in Pounds", min_value=0.0, value=25.0, step=0.5)
size = col4.number_input("Size (count per 25-lb lug, e.g., 48)", min_value=1, step=1, format="%d")

# Equivalent lug ratio = equiv_lug_lb / size
equiv_lug_ratio = (equiv_lug_lb / size) if size else 0.0
st.text_input("Equivalent lug ratio (lb per piece)", value=f"{equiv_lug_ratio:.6f}", disabled=True)

# --- Line 3: Totals ---
total_box_lb = total_pieces * equiv_lug_ratio
total_box_kg = total_box_lb * LB_TO_KG

st.number_input("Total Box Weight - Pounds (calculated)", value=float(round(total_box_lb, 3)), disabled=True)
st.number_input("Total Box Weight - Kilos (calculated)", value=float(round(total_box_kg, 3)), disabled=True)

# Friendly hints
##st.caption(
##    "Notes: Size is typically the count per 25-lb lug (e.g., 48s). "
##    "Equivalent lug ratio = Lug Weight ÷ Size. "
##    "1 lb = 0.45359237 kg."
##)
