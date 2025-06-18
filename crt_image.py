from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import random

# Create output folder for images
output_folder = "data/csv_generated_frame_placeholders"
os.makedirs(output_folder, exist_ok=True)

# Define artificial frame attributes
materials = ["Wood", "Metal", "Composite"]
colors = ["Black", "White", "Walnut", "Gold", "Silver", "Natural", "Espresso", "Charcoal", "Oak", "Champagne"]
styles = ["Modern", "Classic", "Vintage", "Rustic", "Minimalist", "Baroque"]
finishes = ["Matte", "Glossy", "Satin", "Brushed"]
categories = ["Gallery", "Home Decor", "Museum", "Photography", "Poster"]
availability = ["In Stock", "Low Stock", "Discontinued"]
width_range = [0.5, 0.75, 1, 1.25, 1.5, 2, 2.25, 2.5, 3]

# Color map for placeholder visuals
color_map = {
    "Black": (30, 30, 30),
    "White": (240, 240, 240),
    "Walnut": (115, 74, 18),
    "Gold": (212, 175, 55),
    "Silver": (192, 192, 192),
    "Natural": (194, 154, 107),
    "Charcoal": (54, 69, 79),
    "Champagne": (247, 231, 206),
    "Oak": (160, 82, 45),
    "Espresso": (92, 64, 51)
}

# Step 1: Create Data
data = []
for i in range(1, 201):
    frame_id = f"F{i:04d}"
    color = random.choice(colors)
    material = random.choice(materials)
    width = random.choice(width_range)
    style = random.choice(styles)
    finish = random.choice(finishes)
    category = random.choice(categories)
    status = random.choice(availability)

    data.append({
        "Frame ID": frame_id,
        "Material": material,
        "Color": color,
        "Width (inches)": width,
        "Style": style,
        "Finish": finish,
        "Category": category,
        "Availability": status,
        "Image Filename": f"{frame_id}.png"
    })

df = pd.DataFrame(data)

# Step 2: Generate Images
for _, row in df.iterrows():
    frame_id = row["Frame ID"]
    color = row["Color"]
    width_in = row["Width (inches)"]
    style = row["Style"]

    img_size = (300, 300)
    frame_color = color_map.get(color, (150, 150, 150))
    border_thickness = int(width_in * 10)

    img = Image.new("RGB", img_size, "white")
    draw = ImageDraw.Draw(img)

    # Draw border
    for i in range(border_thickness):
        draw.rectangle([i, i, img_size[0]-i-1, img_size[1]-i-1], outline=frame_color)

    # Text label
    label = f"{frame_id}\n{color}\n{style}"
    try:
        font = ImageFont.truetype("arial.ttf", 14)
    except:
        font = ImageFont.load_default()
    draw.multiline_text((10, img_size[1] - 50), label, fill=(0, 0, 0), font=font)

    img.save(os.path.join(output_folder, f"{frame_id}.png"))

# Step 3: Save CSV
csv_path = os.path.join(output_folder, "frame_inventory_with_images.csv")
df.to_csv(csv_path, index=False)

print(f"✅ All images and CSV saved to: {output_folder}")
