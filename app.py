# === app.py ===

import streamlit as st
from PIL import Image
import pandas as pd
import io
from create_frame_preview import create_framed_artwork_preview
from recommend_frame import recommend_frame

# Load frame styles from CSV
@st.cache_data
def load_frame_data(csv_path="data/frame_embeddings_local.csv"):
    df = pd.read_csv(csv_path)
    return df

# Streamlit UI
st.title("🎨 AI Frame Preview from Inventory")
st.write("Upload an artwork, enter its dimensions, and preview it with frame styles from your store.")

# Upload image
uploaded = st.file_uploader("Upload Artwork (JPG/PNG)", type=["jpg", "jpeg", "png"])

# Artwork dimensions
width_in = st.number_input("Artwork Width (inches)", min_value=1.0, value=18.0)
height_in = st.number_input("Artwork Height (inches)", min_value=1.0, value=24.0)

# Load frame CSV and select style
frame_df = load_frame_data()
# frame_options = frame_df['Frame ID'].tolist()
# selected_id = st.selectbox("Select Frame Style", frame_options)

# Get frame style dictionary
# selected_row = frame_df[frame_df['Frame ID'] == selected_id].iloc[0]

# Add color mapping for non-standard names
color_map = {
    "oak": "#c3a27e",           # light-medium warm brown
    "champagne": "#f7e7ce",     # pale beige with soft gold hue
    "walnut": "#5c3a21",        # deep warm brown
    "espresso": "#3b2f2f",      # very dark brown, near black
    "gold": "#d4af37",          # bright metallic gold
    "silver": "#c0c0c0",        # standard silver tone
    "black": "#000000",
    "white": "#ffffff",
    "bronze": "#cd7f32",        # metallic brown-orange
    "mahogany": "#4a0100",      # reddish deep brown
    "maple": "#d4bb93",         # warm light yellowish-brown
    "cherry": "#8b4a32",        # red-toned brown
    "rustic": "#b37f4d",        # earthy golden brown
    "grey": "#808080",          # neutral mid-grey
    "graphite": "#383838",      # dark steel grey
    "antique gold": "#cba135",  # muted vintage gold
    "pewter": "#99aabb",        # bluish silver grey
    "rose gold": "#b76e79",     # muted pinkish gold
    "brushed nickel": "#9ea7aa" # soft industrial silver
}

# color_raw = selected_row["Color"].strip().lower()
# frame_style = {
#     "frame_width_in": float(selected_row["Width (inches)"]),
#     "color": color_map.get(color_raw, "#cccccc"),  # fallback to light grey
#     "style_name": selected_row["Style"]
# }

# Generate preview
if uploaded:
    image = Image.open(uploaded)
    recommended_row = recommend_frame(image)
    
    st.success(f"🎯 Recommended Frame: {recommended_row['Frame ID']} ({recommended_row['Style']}, {recommended_row['Color']})")

    color_raw = recommended_row["Color"].strip().lower()
    frame_style = {
        "frame_width_in": float(recommended_row["Width (inches)"]),
        "color": color_map.get(color_raw, "#cccccc"),  # fallback to light grey
        "style_name": recommended_row["Style"]
    }

    preview = create_framed_artwork_preview(image, width_in, height_in, frame_style)
    st.image(preview, caption="Framed Preview", use_container_width=True)

    # Download
    buf = io.BytesIO()
    preview.save(buf, format="PNG")
    st.download_button("Download Preview", buf.getvalue(), file_name="framed_preview.png", mime="image/png")
