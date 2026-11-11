"""
Motion Craft - Scene: Product Promo & Stat Counter
Features: Floating glass cards, spring counter increment, tags, and clean SaaS-style layout.
"""

import math
from PIL import Image, ImageDraw
from ..core.easing import ease_out_bounce, ease_out_cubic, interpolate
from ..core.canvas import draw_rounded_card, draw_neon_glow
from ..core.particles import ParticleField
from ..core.typography import load_font, draw_centered_text, draw_badge

def build_promo_card(width: int = 1080, height: int = 1920, fps: int = 30, duration_sec: float = 5.0):
    total_frames = int(fps * duration_sec)
    particles = ParticleField(count=30, width=width, height=height)
    scale_factor = width / 1080.0

    font_huge = load_font(int(88 * scale_factor), bold=True)
    font_title = load_font(int(52 * scale_factor), bold=True)
    font_body = load_font(int(32 * scale_factor), bold=False)
    font_badge = load_font(int(26 * scale_factor), bold=True)

    def frame_generator():
        for frame_idx in range(total_frames):
            t = frame_idx / fps
            img = Image.new("RGBA", (width, height), (15, 23, 42, 255))
            draw = ImageDraw.Draw(img)

            # Ambient Soft Glow
            draw_neon_glow(draw, width // 2, height // 2, (99, 102, 241), radius=350 * scale_factor, max_alpha=30)
            particles.draw(draw, t, speed_mult=0.7)

            # Top Badge
            badge_t = interpolate(t, (0.2, 1.0), (0.0, 1.0), easing=ease_out_cubic)
            if badge_t > 0:
                draw_badge(draw, width // 2, int(height * 0.22), "LAUNCH ANNOUNCEMENT", font_badge,
                           bg_color=(16, 185, 129, 220), border_color=(52, 211, 153, 255))

            # Floating Card
            card_t = interpolate(t, (0.5, 1.8), (0.0, 1.0), easing=ease_out_cubic)
            if card_t > 0:
                card_w = int(width * 0.86)
                card_h = int(height * 0.40)
                float_offset = math.sin(t * 3.0) * 12.0
                cx = width // 2
                cy = int(height * 0.52 + (1.0 - card_t) * 100 + float_offset)

                draw_rounded_card(img, (cx - card_w // 2, cy - card_h // 2, cx + card_w // 2, cy + card_h // 2),
                                  radius=int(32 * scale_factor),
                                  bg_color=(30, 41, 59, 230),
                                  border_color=(147, 197, 253, 160),
                                  border_width=2)

                draw = ImageDraw.Draw(img)

                # Animated Counter: from 0 to 99%
                counter_t = interpolate(t, (1.2, 3.2), (0.0, 1.0), easing=ease_out_cubic)
                counter_val = int(counter_t * 99)

                draw_centered_text(draw, cx, cy - int(60 * scale_factor), f"{counter_val}% Faster",
                                   font_huge, fill=(244, 63, 94, 255))
                draw_centered_text(draw, cx, cy + int(20 * scale_factor), "Automated Video Pipeline",
                                   font_title, fill=(255, 255, 255, 255))
                draw_centered_text(draw, cx, cy + int(80 * scale_factor), "Built with Python & FFmpeg",
                                   font_body, fill=(148, 163, 184, 255))

            # CTA Button (Entrance 2.8s)
            cta_t = interpolate(t, (2.6, 3.6), (0.0, 1.0), easing=ease_out_bounce)
            if cta_t > 0:
                cta_y = int(height * 0.82)
                draw_badge(draw, width // 2, cta_y, "STAR ON GITHUB  ★", font_badge,
                           bg_color=(236, 72, 153, int(cta_t * 240)),
                           border_color=(244, 114, 182, 255),
                           padding_x=36, padding_y=16)

            yield img

    return frame_generator(), total_frames
