"""
Motion Craft - FFmpeg Direct Streaming Renderer
Streams raw RGBA/RGB frames directly into ffmpeg subprocess pipe for high performance and low disk IO.
"""

import os
import sys
import time
import subprocess
from PIL import Image

def render_to_mp4(frame_generator, total_frames: int, width: int, height: int,
                  fps: int, output_path: str, audio_path: str = None,
                  crf: int = 18, preset: str = "fast"):
    """
    Renders video by piping raw image bytes to ffmpeg stdin.
    frame_generator: generator yielding PIL.Image objects
    """
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{width}x{height}",
        "-pix_fmt", "rgba",
        "-r", str(fps),
        "-i", "-",  # Read from stdin
    ]

    if audio_path and os.path.exists(audio_path):
        cmd += ["-i", audio_path, "-c:a", "aac", "-b:a", "192k", "-shortest"]

    cmd += [
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", preset,
        "-crf", str(crf),
        output_path
    ]

    print(f"\n[MotionCraft] Launching FFmpeg Pipe: {width}x{height} @ {fps}fps ({total_frames} frames)")
    print(f"[MotionCraft] Target: {output_path}")

    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

    start_time = time.time()
    try:
        for idx, img in enumerate(frame_generator):
            if img.size != (width, height):
                img = img.resize((width, height))
            if img.mode != "RGBA":
                img = img.convert("RGBA")
            
            process.stdin.write(img.tobytes())

            # Progress indicator
            if (idx + 1) % max(1, fps // 2) == 0 or (idx + 1) == total_frames:
                elapsed = time.time() - start_time
                fps_render = (idx + 1) / max(0.001, elapsed)
                percent = ((idx + 1) / total_frames) * 100
                sys.stdout.write(f"\r rendering: {idx + 1}/{total_frames} frames [{percent:5.1f}%] - {fps_render:4.1f} fps")
                sys.stdout.flush()

        process.stdin.close()
        process.wait()
        total_time = time.time() - start_time
        print(f"\n[MotionCraft] Video rendered successfully in {total_time:.2f}s!")
        print(f"[MotionCraft] Saved to: {output_path}\n")
    except Exception as e:
        process.kill()
        stderr_output = process.stderr.read().decode("utf-8", errors="ignore")
        print(f"\n[MotionCraft] Render failed: {e}\nFFmpeg log:\n{stderr_output}", file=sys.stderr)
        raise
