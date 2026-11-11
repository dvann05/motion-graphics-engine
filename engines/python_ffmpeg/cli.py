"""
Motion Craft - Command Line Interface
Unified CLI for selecting scenes, aspect ratios, durations, and rendering directly to MP4.
"""

import argparse
import sys
from .scenes import AVAILABLE_SCENES
from .core.renderer import render_to_mp4

ASPECT_RATIOS = {
    "9:16": (1080, 1920),  # TikTok, Reels, Shorts
    "16:9": (1920, 1080),  # YouTube, Landscape
    "1:1": (1080, 1080),   # Instagram Post / Square
}

def parse_args():
    parser = argparse.ArgumentParser(description="Motion Craft - Code-Driven Motion Graphics Engine")
    parser.add_argument("--scene", choices=list(AVAILABLE_SCENES.keys()), default="tech_intro",
                        help=f"Scene template to render (choices: {', '.join(AVAILABLE_SCENES.keys())})")
    parser.add_argument("--format", choices=list(ASPECT_RATIOS.keys()), default="9:16",
                        help="Video aspect ratio format (9:16 vertical, 16:9 landscape, 1:1 square)")
    parser.add_argument("--fps", type=int, default=30, help="Frames per second (default: 30)")
    parser.add_argument("--duration", type=float, default=5.0, help="Duration in seconds (default: 5.0)")
    parser.add_argument("--output", type=str, default="output/rendered_motion.mp4",
                        help="Output mp4 destination file path")
    parser.add_argument("--audio", type=str, default=None, help="Optional background audio / VO track path")
    parser.add_argument("--crf", type=int, default=18, help="H.264 visual quality CRF (lower is higher quality, default: 18)")
    parser.add_argument("--preset", type=str, default="fast", help="FFmpeg encoding preset (ultrafast, fast, medium, slow)")
    return parser.parse_args()

def main():
    args = parse_args()
    width, height = ASPECT_RATIOS[args.format]
    builder_fn = AVAILABLE_SCENES[args.scene]

    print(f"==================================================")
    print(f"🎬 Motion Craft Engine")
    print(f"• Scene    : {args.scene}")
    print(f"• Format   : {args.format} ({width}x{height})")
    print(f"• Duration : {args.duration}s @ {args.fps} FPS")
    print(f"• Target   : {args.output}")
    print(f"==================================================")

    frames, total_frames = builder_fn(width=width, height=height, fps=args.fps, duration_sec=args.duration)
    render_to_mp4(
        frame_generator=frames,
        total_frames=total_frames,
        width=width,
        height=height,
        fps=args.fps,
        output_path=args.output,
        audio_path=args.audio,
        crf=args.crf,
        preset=args.preset
    )

if __name__ == "__main__":
    main()
