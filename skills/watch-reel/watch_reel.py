"""Download a reel/short, transcribe its audio, and save frames for Claude to read.

Usage: py watch_reel.py <url> [--out DIR] [--every SECONDS] [--model small] [--cookies chrome]
Prints the caption, the timed transcript, and where the frames are.
"""
import argparse
import hashlib
import os
import subprocess
import sys
import tempfile

import imageio_ffmpeg
import numpy as np
import yt_dlp
from faster_whisper import WhisperModel


def download(url, out_dir, cookies_browser=None):
    opts = {
        "outtmpl": os.path.join(out_dir, "video.%(ext)s"),
        "format": "best[height<=720]/best",
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
    }
    if cookies_browser:
        opts["cookiesfrombrowser"] = (cookies_browser,)
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info), info


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser()
    p.add_argument("url")
    p.add_argument("--out")
    p.add_argument("--every", type=float, default=3.0, help="seconds between frames")
    p.add_argument("--model", default="small", help="whisper model: base, small, medium")
    p.add_argument("--cookies", help="browser to borrow login cookies from, e.g. chrome")
    a = p.parse_args()

    key = hashlib.md5(a.url.encode()).hexdigest()[:10]
    out = a.out or os.path.join(tempfile.gettempdir(), "watch-reel", key)
    os.makedirs(out, exist_ok=True)

    try:
        video, info = download(a.url, out, a.cookies)
    except Exception as e:
        sys.exit(f"DOWNLOAD FAILED: {e}\nTry again with --cookies chrome (or edge/firefox).")

    caption = (info.get("description") or "").strip()
    print(f"# {info.get('uploader', '')} - {info.get('duration', '?')}s\n")
    if caption:
        print("## Caption\n" + caption + "\n")

    # Frames: one every N seconds, small enough to read cheaply.
    frames_dir = os.path.join(out, "frames")
    os.makedirs(frames_dir, exist_ok=True)
    subprocess.run(
        [imageio_ffmpeg.get_ffmpeg_exe(), "-loglevel", "error", "-y", "-i", video,
         "-vf", f"fps=1/{a.every},scale=540:-2",
         os.path.join(frames_dir, "f_%03d.jpg")],
        check=True,
    )

    # Transcript with timestamps. Runs locally on CPU; first run downloads the model.
    # Decode audio with ffmpeg ourselves (avoids PyAV version clashes).
    raw = subprocess.run(
        [imageio_ffmpeg.get_ffmpeg_exe(), "-loglevel", "error", "-i", video,
         "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
        check=True, capture_output=True,
    ).stdout
    audio = np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0
    model = WhisperModel(a.model, device="cpu", compute_type="int8")
    segments, lang = model.transcribe(audio, vad_filter=True)
    transcript = "\n".join(f"[{s.start:5.1f}s] {s.text.strip()}" for s in segments)
    with open(os.path.join(out, "transcript.txt"), "w", encoding="utf-8") as f:
        f.write(transcript)

    print(f"## Transcript (language: {lang.language})\n{transcript}\n")
    print(f"## Frames (one every {a.every:g}s; f_001 = 0s)\n{frames_dir}")
    print(", ".join(sorted(os.listdir(frames_dir))))


if __name__ == "__main__":
    main()
