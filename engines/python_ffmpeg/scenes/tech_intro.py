"""
Motion Craft - Scene: Cyber Tech Intro
Features: Glowing beacons, animated grid, floating particle field, spring badge, and kinetic card.
"""

import math
from PIL import Image, ImageDraw
from ..core.easing import ease_out_back, ease_out_elastic, ease_out_cubic, spring, interpolate
from ..core.canvas import draw_cyber_grid, draw_neon_glow, draw_rounded_card
from ..core.particles import ParticleField
from ..core.typography import load_font, draw_centered_text, draw_staggered_text, draw_badge, get_text_dimensions

def build_tech_intro(width: int = 1080, height: int = 1920, fps: int = 30, duration_sec: float = 6.0):
    total_frames = int(fps * duration_sec)
    particles = ParticleField(count=45, width=width, height=height)

    # Pre-load responsive fonts
    is_vertical = height > width
    scale_factor = width / 1080.0
    font_hero = load_font(int(72 * scale_factor), bold=True)
    font_title = load_font(int(46 * scale_factor), bold=True)
    font_body = load_font(int(32 * scale_factor), bold=False)
    font_badge = load_font(int(24 * scale_factor), bold=True)

    def frame_generator():
        for frame_idx in range(total_frames):
            t = frame_idx / fps
            img = Image.new("RGBA", (width, height), (10, 14, 28, 255))
            draw = ImageDraw.Draw(img)

            # 1. Background Grid & Ambient Glows
            draw_cyber_grid(draw, width, height, t, spacing=int(60 * scale_factor), speed=30.0)

            # Pulsing color beacons
            p1 = math.sin(t * 3.0) * (40 * scale_factor)
            p2 = math.cos(t * 2.5) * (50 * scale_factor)
            draw_neon_glow(draw, width // 2, int(height * 0.28), (14, 165, 233), radius=280 * scale_factor + p1, max_alpha=28)
            draw_neon_glow(draw, width // 2, int(height * 0.65), (236, 72, 153), radius=320 * scale_factor + p2, max_alpha=22)

            # 2. Ambient Floating Particles
            particles.draw(draw, t)

            # 3. Entrance: Top Pill Badge (0.0s - 1.2s)
            badge_t = interpolate(t, (0.2, 1.2), (0.0, 1.0), easing=ease_out_back)
            if badge_t > 0:
                badge_y = int(interpolate(badge_t, (0.0, 1.0), (height * 0.18 - 40, height * 0.18)))
                draw_badge(draw, width // 2, badge_y, "MOTION CRAFT ENGINE v1.0", font_badge,
                           bg_color=(30, 58, 138, 220), border_color=(96, 165, 250, 255))

            # 4. Hero Kinetic Headline (0.5s - 2.5s)
            hero_t = interpolate(t, (0.6, 2.0), (0.0, 1.0), easing=ease_out_cubic)
            if hero_t > 0:
                headline_text = "NEXT-GEN MOTION"
                hw, hh = get_text_dimensions(draw, headline_text, font_hero)
                start_x = width // 2 - hw // 2
                start_y = int(height * 0.26)
                draw_staggered_text(draw, start_x, start_y, headline_text, font_hero, hero_t, color_rgb=(255, 255, 255))

            # Sub-headline
            sub_t = interpolate(t, (1.2, 2.4), (0.0, 1.0), easing=ease_out_cubic)
            if sub_t > 0:
                sub_alpha = int(sub_t * 220)
                sub_y = int(height * 0.33 + (1.0 - sub_t) * 15)
                draw_centered_text(draw, width // 2, sub_y, "Code-driven video animations at 60 FPS",
                                   font_body, fill=(148, 163, 184, sub_alpha))

            # 5. Central Feature Glassmorphism Card (1.8s - 4.5s)
            card_t = interpolate(t, (1.8, 3.0), (0.0, 1.0), easing=ease_out_elastic)
            if card_t > 0:
                card_w = int(width * 0.84)
                card_h = int(height * (0.26 if is_vertical else 0.38))
                scale = card_t
                cw = int(card_w * scale)
                ch = int(card_h * scale)
                cx = width // 2
                cy = int(height * (0.52 if is_vertical else 0.62))

                draw_rounded_card(img, (cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2),
                                  radius=int(28 * scale_factor),
                                  bg_color=(15, 23, 42, 225),
                                  border_color=(129, 140, 248, 230),
                                  border_width=2)

                # Re-acquire draw after alpha composite
                draw = ImageDraw.Draw(img)

                if card_t >= 0.8:
                    content_alpha = int(interpolate(card_t, (0.8, 1.0), (0, 255)))
                    draw_centered_text(draw, cx, cy - int(45 * scale_factor), "Ultra-Smooth Physics",
                                       font_title, fill=(248, 250, 252, content_alpha))
                    draw_centered_text(draw, cx, cy + int(10 * scale_factor), "Spring Interpolation  •  Zero Dependencies",
                                       font_body, fill=(192, 132, 252, content_alpha))
                    draw_centered_text(draw, cx, cy + int(60 * scale_factor), "Piped directly to H.264 MP4",
                                       font_body, fill=(56, 189, 248, content_alpha))

            # 6. Bottom Dynamic Progress Bar
            prog_t = t / duration_sec
            bar_w = int(width * 0.8)
            bar_h = int(6 * scale_factor)
            bar_x = (width - bar_w) // 2
            bar_y = int(height * 0.92)
            draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=3, fill=(30, 41, 59, 180))
            active_w = int(bar_w * prog_t)
            if active_w > 0:
                draw.rounded_rectangle([bar_x, bar_y, bar_x + active_w, bar_y + bar_h], radius=3, fill=(56, 189, 248, 240))

            yield img

    return frame_generator(), total_frames
