from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import pandas as pd
import torch
import os

# Load CLIP model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Load CSV
df = pd.read_csv("data/frame_descriptions.csv")

# Folder where your frame images are stored
image_folder = "data/images"

embeddings = []

for i, row in df.iterrows():
    image_path = os.path.join(image_folder, row['Image Filename'])
    image = Image.open(image_path).convert("RGB")
    
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        image_features = model.get_image_features(**inputs)
    
    # Normalize
    image_features = image_features / image_features.norm(p=2, dim=-1, keepdim=True)
    emb = image_features[0].cpu().tolist()
    embeddings.append(emb)

# Add embedding columns
embedding_df = pd.DataFrame(embeddings, columns=[f"embedding_{i}" for i in range(512)])
df = pd.concat([df, embedding_df], axis=1)

# Save with embeddings
df.to_csv("data/frame_embeddings_local.csv", index=False)
print("✅ Saved embeddings to frame_embeddings_local.csv")
