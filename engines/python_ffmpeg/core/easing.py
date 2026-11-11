"""
Motion Craft - Easing & Interpolation Math Engine
Zero-dependency easing curves for smooth kinetic motion graphics.
"""

import math

def clamp(val: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
    return max(min_val, min(max_val, val))

def linear(t: float) -> float:
    return clamp(t)

def ease_in_quad(t: float) -> float:
    t = clamp(t)
    return t * t

def ease_out_quad(t: float) -> float:
    t = clamp(t)
    return t * (2.0 - t)

def ease_in_out_quad(t: float) -> float:
    t = clamp(t)
    return 2.0 * t * t if t < 0.5 else -1.0 + (4.0 - 2.0 * t) * t

def ease_in_cubic(t: float) -> float:
    t = clamp(t)
    return t * t * t

def ease_out_cubic(t: float) -> float:
    t = clamp(t)
    return 1.0 - (1.0 - t) ** 3

def ease_in_out_cubic(t: float) -> float:
    t = clamp(t)
    return 4.0 * t * t * t if t < 0.5 else 1.0 - ((-2.0 * t + 2.0) ** 3) / 2.0

def ease_out_back(t: float, s: float = 1.70158) -> float:
    t = clamp(t) - 1.0
    return t * t * ((s + 1.0) * t + s) + 1.0

def ease_in_back(t: float, s: float = 1.70158) -> float:
    t = clamp(t)
    return t * t * ((s + 1.0) * t - s)

def ease_out_elastic(t: float, period: float = 0.3) -> float:
    t = clamp(t)
    if t <= 0.0:
        return 0.0
    if t >= 1.0:
        return 1.0
    return math.pow(2.0, -10.0 * t) * math.sin((t - period / 4.0) * (2.0 * math.pi) / period) + 1.0

def ease_out_bounce(t: float) -> float:
    t = clamp(t)
    if t < (1.0 / 2.75):
        return 7.5625 * t * t
    elif t < (2.0 / 2.75):
        t -= 1.5 / 2.75
        return 7.5625 * t * t + 0.75
    elif t < (2.5 / 2.75):
        t -= 2.25 / 2.75
        return 7.5625 * t * t + 0.9375
    else:
        t -= 2.625 / 2.75
        return 7.5625 * t * t + 0.984375

def spring(t: float, damping: float = 12.0, stiffness: float = 100.0, mass: float = 1.0) -> float:
    """Simulated physics spring animation clamped between 0 and 1."""
    t = clamp(t)
    if t <= 0.0:
        return 0.0
    if t >= 1.0:
        return 1.0
    w0 = math.sqrt(stiffness / mass)
    zeta = damping / (2.0 * math.sqrt(stiffness * mass))
    if zeta < 1.0:
        # Underdamped
        wd = w0 * math.sqrt(1.0 - zeta * zeta)
        decay = math.exp(-zeta * w0 * t * 4.0)
        return 1.0 - decay * (math.cos(wd * t * 4.0) + (zeta / math.sqrt(1.0 - zeta * zeta)) * math.sin(wd * t * 4.0))
    else:
        # Critically/overdamped fallback
        return ease_out_cubic(t)

def interpolate(val: float, in_range: tuple, out_range: tuple, easing=linear) -> float:
    """Maps val from in_range (in_min, in_max) to out_range (out_min, out_max) with easing."""
    in_min, in_max = in_range
    out_min, out_max = out_range
    if in_max == in_min:
        return out_min
    normalized = clamp((val - in_min) / (in_max - in_min))
    eased = easing(normalized)
    return out_min + (out_max - out_min) * eased
