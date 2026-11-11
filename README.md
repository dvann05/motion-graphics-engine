# 🎬 Motion Craft

> **Code-Driven Programmatic Motion Graphics Engine & Starter Kit**  
> Build high-quality kinetic typography, glassmorphism cards, ambient particle fields, and animated video sequences directly using Python, FFmpeg, and React (Remotion).

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-H.264%20Piped-007808?style=flat-square&logo=ffmpeg&logoColor=white)](https://ffmpeg.org)
[![Remotion](https://img.shields.io/badge/Remotion-React%20Video-0B84F3?style=flat-square&logo=react&logoColor=white)](https://remotion.dev)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)](.github/workflows/render-demo.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

---

## ✨ Features

- ⚡ **Direct FFmpeg Stream Pipeline**: Streams raw RGB/RGBA frames directly into FFmpeg stdin. Zero intermediate PNG/JPEG disk writes for maximum speed and SSD preservation.
- 📐 **Rich Easing Physics Engine**: Built-in cubic, spring, bounce, elastic, and back easing curves for snappy and organic animation motion.
- 🎨 **Visual Canvas & Effects**:
  - Dynamic scrolling perspective/cyber grids
  - Pulsing radial neon glow beacons
  - Floating ambient particle fields with velocity trails
  - Glassmorphic rounded UI cards with highlight borders
  - Kinetic typography with letter-by-letter spring staggering
- 📱 **Multi-Format Aspect Ratio Support**:
  - `9:16` Vertical (1080x1920) for TikTok, Instagram Reels, and YouTube Shorts.
  - `16:9` Widescreen (1920x1080) for YouTube and Presentations.
  - `1:1` Square (1080x1080) for Instagram Feed and Social Media cards.
- ⚛️ **Dual-Engine Architecture**: Includes both lightweight standalone Python/FFmpeg engine (runs on Termux, Android, Linux, Mac, Windows) and a full React/TypeScript Remotion suite.
- 🚀 **GitHub Actions Automated Rendering**: Renders demo videos on push and uploads the MP4 as a build artifact automatically.

---

## 📁 Repository Structure

```text
motion-craft/
├── .github/
│   └── workflows/
│       └── render-demo.yml           # Automated CI video render on push
├── engines/
│   ├── python_ffmpeg/                # Standalone lightweight Python engine
│   │   ├── cli.py                    # Unified command-line interface
│   │   ├── core/
│   │   │   ├── canvas.py             # Gradients, glow beacons, glass cards, grids
│   │   │   ├── easing.py             # Easing curves (spring, elastic, cubic, back)
│   │   │   ├── particles.py          # Ambient particle fields with motion trails
│   │   │   ├── typography.py         # Kinetic staggered text and badges
│   │   │   └── renderer.py           # FFmpeg direct raw pipe streaming
│   │   └── scenes/
│   │       ├── tech_intro.py         # Cyber tech intro scene
│   │       └── promo_card.py         # SaaS product announcement scene
│   └── remotion/                     # React & TypeScript component suite
│       ├── package.json
│       ├── tsconfig.json
│       ├── remotion.config.ts
│       └── src/
│           ├── Root.tsx              # Composition definitions
│           ├── components/           # GlowCard, KineticText, ParticleField
│           └── compositions/         # TechShowcase composition
├── examples/
│   └── render_quick_demo.py          # 1-click sample render script
├── scripts/
│   └── push_to_github.sh             # Helper to initialize & push to GitHub
├── requirements.txt                  # Python dependencies (Pillow, numpy)
├── LICENSE                           # MIT License
└── README.md
```

---

## 🚀 Quick Start (Python & FFmpeg)

### 1. Requirements
Ensure you have `python` (3.9+) and `ffmpeg` installed:
```bash
# Ubuntu / Debian
sudo apt-get install python3 python3-pip ffmpeg

# Termux (Android)
pkg install python ffmpeg
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Render 1-Click Demo
```bash
python examples/render_quick_demo.py
```
Output will be saved to `output/quick_demo_vertical.mp4`.

---

## 🖥️ Command-Line Interface (CLI)

Use `engines.python_ffmpeg.cli` to customize your video renders:

```bash
# Render Cyber Tech Intro in 9:16 Vertical (Shorts/Reels)
python -m engines.python_ffmpeg.cli --scene tech_intro --format 9:16 --fps 30 --duration 6.0 --output output/tech_9x16.mp4

# Render in 16:9 Landscape for YouTube
python -m engines.python_ffmpeg.cli --scene tech_intro --format 16:9 --fps 30 --duration 6.0 --output output/tech_16x9.mp4

# Render Product Promo Card scene with custom CRF quality
python -m engines.python_ffmpeg.cli --scene promo_card --format 9:16 --crf 16 --output output/promo.mp4

# Render with background audio track
python -m engines.python_ffmpeg.cli --scene tech_intro --audio path/to/music.mp3 --output output/with_audio.mp4
```

### CLI Arguments Reference

| Flag | Default | Description |
| :--- | :--- | :--- |
| `--scene` | `tech_intro` | Scene template (`tech_intro`, `promo_card`) |
| `--format` | `9:16` | Aspect ratio (`9:16`, `16:9`, `1:1`) |
| `--fps` | `30` | Frame rate (e.g. `30` or `60`) |
| `--duration` | `5.0` | Video duration in seconds |
| `--output` | `output/rendered_motion.mp4` | Destination MP4 file path |
| `--audio` | `None` | Optional path to audio file (`.mp3` or `.aac`) |
| `--crf` | `18` | H.264 visual quality (18 = visually lossless) |
| `--preset` | `fast` | FFmpeg speed preset (`ultrafast`, `fast`, `medium`) |

---

## ⚛️ Remotion Quick Start (React + TypeScript)

If you prefer editing in React with a browser-based live preview:

```bash
cd engines/remotion
npm install

# Start local interactive player
npm start

# Render production video
npm run build
```

---

## 🐙 Push to GitHub

To publish this repository directly to your GitHub profile:

1. Create a new empty repository at [github.com/new](https://github.com/new) (e.g., named `motion-craft`).
2. Run the interactive helper:
```bash
bash scripts/push_to_github.sh
```
Or run manually:
```bash
git init -b main
git add .
git commit -m "feat: initial commit - programmatic motion graphics engine"
git remote add origin https://github.com/<YOUR_USERNAME>/motion-craft.git
git push -u origin main
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
