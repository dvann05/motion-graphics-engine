"""
Motion Craft - Visual Canvas & Styling Engine
Utilities for gradients, glow effects, glassmorphic cards, and background grids.
"""

import math
import numpy as np
from PIL import Image, ImageDraw

def create_gradient_background(width: int, height: int, color_top: tuple, color_bottom: tuple) -> Image.Image:
    """Creates a smooth vertical 2-color linear gradient."""
    r_step = np.linspace(color_top[0], color_bottom[0], height)
    g_step = np.linspace(color_top[1], color_bottom[1], height)
    b_step = np.linspace(color_top[2], color_bottom[2], height)
    a_step = np.linspace(color_top[3] if len(color_top) > 3 else 255,
                         color_bottom[3] if len(color_bottom) > 3 else 255, height)

    gradient = np.stack([r_step, g_step, b_step, a_step], axis=-1).astype(np.uint8)
    gradient = np.repeat(gradient[:, np.newaxis, :], width, axis=1)
    return Image.fromarray(gradient, mode="RGBA")

def draw_neon_glow(draw: ImageDraw.ImageDraw, center_x: int, center_y: int,
                   color_rgb: tuple, radius: float = 200.0,
                   max_alpha: int = 40, layers: int = 5):
    """Draws multi-layered radial soft neon glow circles."""
    r, g, b = color_rgb[:3]
    for i in range(layers, 0, -1):
        layer_r = radius * (i / layers)
        alpha = int((max_alpha / layers) * (layers - i + 1))
        draw.ellipse(
            [center_x - layer_r, center_y - layer_r, center_x + layer_r, center_y + layer_r],
            fill=(r, g, b, alpha)
        )

def draw_cyber_grid(draw: ImageDraw.ImageDraw, width: int, height: int,
                    time_sec: float, spacing: int = 60, speed: float = 40.0,
                    color_rgba: tuple = (255, 255, 255, 14)):
    """Draws animated scrolling perspective/cyber grid."""
    offset_y = (time_sec * speed) % spacing
    r, g, b, a = color_rgba

    # Horizontal lines
    curr_y = offset_y
    while curr_y < height:
        pulsed_alpha = max(4, min(35, int(a + 8 * math.sin(curr_y / 150.0 + time_sec * 2.0))))
        draw.line([(0, curr_y), (width, curr_y)], fill=(r, g, b, pulsed_alpha), width=1)
        curr_y += spacing

    # Vertical lines
    for x in range(0, width, spacing):
        draw.line([(x, 0), (x, height)], fill=(r, g, b, a // 2), width=1)

def draw_rounded_card(img: Image.Image, box: tuple, radius: int,
                      bg_color: tuple = (25, 30, 48, 200),
                      border_color: tuple = (99, 102, 241, 180),
                      border_width: int = 2):
    """Renders a modern glassmorphic rounded card overlay."""
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    x1, y1, x2, y2 = box

    # Card background
    d.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=bg_color)

    # Card highlight border
    if border_width > 0 and border_color:
        d.rounded_rectangle([x1, y1, x2, y2], radius=radius, outline=border_color, width=border_width)

    # Alpha composite back onto canvas
    img.alpha_composite(overlay)
