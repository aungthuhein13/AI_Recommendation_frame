import pandas as pd

# Load your CSV
df = pd.read_csv("data/frame_inventory_with_images.csv")

# Create natural language description for each frame
def describe_frame(row):
    return f"A {row['Style']} style frame made of {row['Material']}, finished in {row['Finish']} {row['Color'].lower()}, with a width of {row['Width (inches)']} inches."

df["description"] = df.apply(describe_frame, axis=1)

# Optional: preview the result
print(df[["Frame ID", "description"]].head())

# Save new CSV for embedding
df.to_csv("data/frame_descriptions.csv", index=False)
