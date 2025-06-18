# AI Frame Recommender + Visualizer App

This project is an AI-powered frame recommendation and visualization tool built with Python and Streamlit. Users can upload an image of an artwork and receive smart frame style recommendations from an inventory. The selected frame is automatically applied around the painting in a realistic preview.

---

## Features

- Upload artwork image and input dimensions (in inches)
- Recommend a frame style based on AI embeddings
- Realistically preview the artwork inside the selected frame
- Visualized with PIL (Python Imaging Library) and Streamlit
- Modular pipeline: frame generation, metadata embedding, UI preview

---

## Project Structure

├── app.py # Streamlit app
├── recommend_frame.py # Recommend frames using embeddings
├── create_frame_preview # Create a simulated uploaded painting with frame
├── crt_images.py # Generate placeholder frame images with metadata
├── convert_metadata_description.py # Add natural language descriptions to frames
├── embed_frame_description.py # Generate embeddings using CLIP model
├── data/
│ ├── frame_inventory_with_images.csv
│ ├── frame_inventory_with_description.csv
│ ├── frame_embeddings_local.csv
│ └── images/ # Folder of generated frame PNGs
└── README.md