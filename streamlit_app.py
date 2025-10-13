#!/usr/bin/env python3
import streamlit as st

LB_TO_KG = 0.45359237

st.set_page_config(page_title="WestPak Avocado Box Weight Calculator", layout="centered")
st.image("WPA.png", width =250)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e6ffe6; /* light gray */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("WestPak Avocado Box Weight Calculator")

st.markdown("Enter your inputs below. Calculated fields update when all required inputs are provided.")

# --- Line 1: Bags & pieces ---
col1, col2 = st.columns(2)
num_bags = col1.number_input("Number of Bags", min_value=0, step=1, format="%d")
pieces_per_bag = col2.number_input("Pieces per bag", min_value=0, step=1, format="%d")

total_pieces = num_bags * pieces_per_bag
st.text_input("Total pieces (calculated)", value=str(total_pieces), disabled=True)

# --- Line 2: Lug & size ---
col3, col4 = st.columns(2)
equiv_lug_lb = col3.number_input("Equivalent Lug Weight in Pounds. Use 22 for 84's otherwise 25 for sizes 28-70", min_value=0.0, value=25.0, step=0.5)
size = col4.number_input("Size (count per 25-lb lug, e.g., 48)", min_value=48, step=1, format="%d")

# Equivalent lug ratio = equiv_lug_lb / size
equiv_lug_ratio = (equiv_lug_lb / size) if size else 0.0
st.text_input("Equivalent lug ratio", value=f"{equiv_lug_ratio:.6f}", disabled=True)

# --- Line 3: Totals ---
total_box_lb = total_pieces * equiv_lug_ratio
total_box_kg = total_box_lb * LB_TO_KG

st.number_input("Total Box Weight - Pounds (calculated)", value=float(round(total_box_lb, 3)), disabled=True)
st.number_input("Total Box Weight - Kilos (calculated)", value=float(round(total_box_kg, 3)), disabled=True)

# --- Line 4 : Bulk Fill ----
st.title("Bulk Fill")
col5, col6 = st.columns(2)
sizebulk = col5.number_input("Size", min_value=36, step=1, format="%d")
piecesbulk = col6.number_input("Pieces", min_value=36, step=1, format="%d")

equiv_lug_ratio_bulk = (piecesbulk / sizebulk) if size else 0.0
st.text_input("Equivalent lug ratio(bulk)", value=f"{equiv_lug_ratio_bulk:.6f}", disabled=True)

total_box_lb_bulk = equiv_lug_lb * equiv_lug_ratio_bulk
total_box_kg_bulk = total_box_lb_bulk * LB_TO_KG

st.number_input("Total Box Weight (bulk fill) - Pounds (calculated)", value=float(round(total_box_lb_bulk, 3)), disabled=True)
st.number_input("Total Box Weight (bulk fill) - Kilos (calculated)", value=float(round(total_box_kg_bulk, 3)), disabled=True)


# --- Line 5 : Equivalent Lug Calculations
st.title("Equivalent Lug Calculations. (Assuming sizes 28 - 70)")
col7, col8 = st.columns(2)

kilo_box = col7.number_input("Kilo Box", min_value=0, step=1, format="%d")
box_qnt = col8.number_input("Box Quantity", min_value=0, step=1, format="%d")

kilos_calc = kilo_box * box_qnt
pounds_cal = kilos_calc * 2.20462
equiv_lug_calc = (pounds_cal / 25)

st.number_input("Kilos (calculated)", value=float(round(kilos_calc, 3)), disabled=True)
st.number_input("Pounds (calculated)", value=float(round(pounds_cal, 3)), disabled=True)
st.number_input("Equiv Lug Calculate (25lb equivalent)", value=float(round(equiv_lug_calc, 3)), disabled=True)

