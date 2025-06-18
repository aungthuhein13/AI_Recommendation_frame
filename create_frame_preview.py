# === create_framed_preview.py ===

from PIL import Image, ImageDraw

def create_framed_artwork_preview(artwork, width_in, height_in, frame_style, dpi=30):
    """
    Creates a simulated framed artwork using a coded frame style.

    Parameters:
    - artwork: PIL image
    - width_in: width in inches
    - height_in: height in inches
    - frame_style: dict with keys ['frame_width_in', 'color', 'style_name']
    - dpi: virtual pixels per inch (default 30)

    Returns:
    - PIL image of framed artwork
    """
    frame_width_in = frame_style.get("frame_width_in", 2)
    frame_color = frame_style.get("color", "#442B1B")

    # Convert to pixels
    art_w_px = int(width_in * dpi)
    art_h_px = int(height_in * dpi)
    frame_w_px = int(frame_width_in * dpi)

    # Resize artwork
    artwork = artwork.convert("RGBA")
    artwork = artwork.resize((art_w_px, art_h_px))

    # Canvas size
    canvas_w = art_w_px + 2 * frame_w_px
    canvas_h = art_h_px + 2 * frame_w_px

    # Create canvas and draw borders
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (245, 245, 245, 255))  # background wall
    draw = ImageDraw.Draw(canvas)

    # Draw frame
    draw.rectangle([0, 0, canvas_w, frame_w_px], fill=frame_color)  # top
    draw.rectangle([0, canvas_h - frame_w_px, canvas_w, canvas_h], fill=frame_color)  # bottom
    draw.rectangle([0, 0, frame_w_px, canvas_h], fill=frame_color)  # left
    draw.rectangle([canvas_w - frame_w_px, 0, canvas_w, canvas_h], fill=frame_color)  # right

    # Paste artwork in center
    canvas.paste(artwork, (frame_w_px, frame_w_px), artwork)

    return canvas
