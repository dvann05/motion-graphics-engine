#!/usr/bin/env python3
"""
Motion Craft - 1-Click Quick Demo Generator
Generates a quick 4-second motion graphics video sample.
Usage:
    python examples/render_quick_demo.py
"""

import os
import sys

# Add project root to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from engines.python_ffmpeg.scenes.tech_intro import build_tech_intro
from engines.python_ffmpeg.core.renderer import render_to_mp4

def run():
    output_file = os.path.join(BASE_DIR, "output", "quick_demo_vertical.mp4")
    print("\n🚀 Rendering Quick Demo (9:16 Vertical - 4 seconds @ 30fps)...")
    
    frames, total_frames = build_tech_intro(width=1080, height=1920, fps=30, duration_sec=4.0)
    render_to_mp4(
        frame_generator=frames,
        total_frames=total_frames,
        width=1080,
        height=1920,
        fps=30,
        output_path=output_file,
        preset="ultrafast"
    )

if __name__ == "__main__":
    run()
