import cv2
import numpy as np


def analyze_terrain_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(
            f"Could not read image: {image_path}"
        )

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    edges = cv2.Canny(
        gray,
        80,
        160
    )

    edge_density = float(
        np.mean(edges > 0)
    )

    texture = float(
        np.std(gray) / 64.0
    )

    texture = min(
        texture,
        1.0
    )

    visual_score = min(
        1.0,
        0.65 * edge_density +
        0.35 * texture
    )

    if visual_score < 0.20:

        indication = "Low visual indication"

    elif visual_score < 0.40:

        indication = "Medium visual indication"

    else:

        indication = "High visual indication"

    return {

        "visual_score":
            visual_score,

        "indication":
            indication,

        "message":
            "Prototype camera-based visual analysis."
    }
