"""
Motion Craft - Typography & Kinetic Text Engine
Font resolver, text layout, staggered character animation, and badge rendering.
"""

import os
from PIL import ImageDraw, ImageFont
from .easing import clamp, ease_out_back, ease_out_cubic

SYSTEM_FONT_CANDIDATES = [
    # Termux / Android common fonts
    "/system/fonts/SourceSansPro-Bold.ttf",
    "/system/fonts/Roboto-Bold.ttf",
    "/system/fonts/Roboto-Medium.ttf",
    "/system/fonts/Roboto-Regular.ttf",
    "/system/fonts/DroidSans-Bold.ttf",
    "/system/fonts/DroidSans.ttf",
    # Linux desktop fallbacks
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/TTF/DejaVuSans.ttf"
]

def load_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    """Tries to find a clean TTF font on the host system or returns default."""
    for path in SYSTEM_FONT_CANDIDATES:
        if bold and "regular" in path.lower():
            continue
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    # Fallback to any found font
    for path in SYSTEM_FONT_CANDIDATES:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def get_text_dimensions(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple:
    """Returns (width, height) of text bounding box."""
    bbox = draw.textbbox((0, 0), text, font=font)
    return (bbox[2] - bbox[0], bbox[3] - bbox[1])

def draw_centered_text(draw: ImageDraw.ImageDraw, center_x: int, center_y: int,
                       text: str, font: ImageFont.ImageFont, fill: tuple = (255, 255, 255, 255)):
    """Draws text centered exactly at (center_x, center_y)."""
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((center_x - tw // 2, center_y - th // 2), text, font=font, fill=fill)

def draw_staggered_text(draw: ImageDraw.ImageDraw, start_x: int, start_y: int,
                        text: str, font: ImageFont.ImageFont, progress: float,
                        color_rgb: tuple = (255, 255, 255), stagger_delay: float = 0.04):
    """
    Renders text where each letter pops in sequentially with an overshoot spring.
    progress: 0.0 to 1.0 (scene entrance progress)
    """
    curr_x = start_x
    n_chars = max(1, len(text))

    for idx, char in enumerate(text):
        char_bbox = draw.textbbox((0, 0), char, font=font)
        char_w = char_bbox[2] - char_bbox[0]

        char_start_prog = (idx / n_chars) * (1.0 - stagger_delay * n_chars)
        char_end_prog = char_start_prog + stagger_delay * 2.0
        
        char_t = clamp((progress - char_start_prog) / max(0.001, (char_end_prog - char_start_prog)))
        if char_t <= 0.0:
            curr_x += char_w + 2
            continue

        eased_pop = ease_out_back(char_t, s=2.0)
        alpha = int(clamp(char_t * 1.5) * 255)
        offset_y = int((1.0 - eased_pop) * 25.0)

        draw.text((curr_x, start_y + offset_y), char, font=font, fill=color_rgb + (alpha,))
        curr_x += char_w + 2

def draw_badge(draw: ImageDraw.ImageDraw, center_x: int, center_y: int, text: str,
               font: ImageFont.ImageFont, bg_color: tuple = (59, 130, 246, 200),
               text_color: tuple = (255, 255, 255, 255), padding_x: int = 24, padding_y: int = 10,
               border_color: tuple = (96, 165, 250, 240)):
    """Draws modern rounded tag/badge with centered label."""
    tw, th = get_text_dimensions(draw, text, font)
    box = [
        center_x - tw // 2 - padding_x,
        center_y - th // 2 - padding_y,
        center_x + tw // 2 + padding_x,
        center_y + th // 2 + padding_y,
    ]
    radius = (box[3] - box[1]) // 2
    draw.rounded_rectangle(box, radius=radius, fill=bg_color, outline=border_color, width=2)
    draw.text((center_x - tw // 2, center_y - th // 2 - 2), text, font=font, fill=text_color)
