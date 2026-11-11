"""
Motion Craft - Dynamic Particle System
Lightweight 2D particle engine for ambient starfields, neon embers, and velocity trails.
"""

import math
import random
from PIL import ImageDraw

class ParticleField:
    def __init__(self, count: int = 50, width: int = 1080, height: int = 1920,
                 palette: list = None, seed: int = 42):
        random.seed(seed)
        self.width = width
        self.height = height
        self.palette = palette or [
            (56, 189, 248, 180),   # Sky Cyan
            (168, 85, 247, 180),  # Purple
            (236, 72, 153, 180),  # Pink
            (250, 204, 21, 180),  # Amber
        ]
        self.particles = []
        for _ in range(count):
            self.particles.append({
                "x": random.uniform(10, width - 10),
                "y": random.uniform(10, height - 10),
                "vx": random.uniform(-0.8, 0.8),
                "vy": random.uniform(-1.5, -0.3),
                "radius": random.uniform(2.5, 6.0),
                "color": random.choice(self.palette),
                "pulse_freq": random.uniform(2.0, 5.0),
                "pulse_phase": random.uniform(0, math.pi * 2)
            })

    def draw(self, draw: ImageDraw.ImageDraw, time_sec: float, speed_mult: float = 1.0):
        for p in self.particles:
            px = (p["x"] + p["vx"] * (time_sec * 40.0 * speed_mult)) % self.width
            py = (p["y"] + p["vy"] * (time_sec * 40.0 * speed_mult)) % self.height

            # Pulsing radius
            pulse = math.sin(time_sec * p["pulse_freq"] + p["pulse_phase"])
            r = max(1.0, p["radius"] + pulse * 1.5)

            # Soft trail behind particle
            trail_len = 10.0 * speed_mult
            tx = px - p["vx"] * trail_len
            ty = py - p["vy"] * trail_len
            trail_color = p["color"][:3] + (max(0, p["color"][3] // 4),)
            draw.line([(px, py), (tx, ty)], fill=trail_color, width=max(1, int(r * 0.7)))

            # Particle center core
            draw.ellipse([px - r, py - r, px + r, py + r], fill=p["color"])
