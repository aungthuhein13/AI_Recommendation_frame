from transformers import CLIPModel, CLIPProcessor
from sklearn.metrics.pairwise import cosine_similarity
from PIL import Image
import pandas as pd
import torch

# Load model only once
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def load_frame_embeddings(csv_path="data/frame_embeddings_local.csv"):
    df = pd.read_csv(csv_path)
    embeddings = df[[f"embedding_{i}" for i in range(512)]].values
    return df, embeddings

def get_image_embedding(image: Image.Image):
    inputs = clip_processor(images=image, return_tensors="pt", padding=True)
    with torch.no_grad():
        image_features = clip_model.get_image_features(**inputs)
    return image_features / image_features.norm(p=2, dim=-1, keepdim=True)

def recommend_frame(image: Image.Image):
    df, frame_embeddings = load_frame_embeddings()
    image_embedding = get_image_embedding(image)

    # Compute cosine similarity
    sims = cosine_similarity(image_embedding.cpu().numpy(), frame_embeddings)[0]
    top_idx = sims.argmax()
    top_frame = df.iloc[top_idx]
    return top_frame
