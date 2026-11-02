---
name: watch-reel
description: Watch a video reel/short (Instagram, TikTok, YouTube, X) by downloading it, transcribing its audio, and reading frames. Use when the user shares a reel/video link, says "watch this reel", "my last saved reel", or asks what a video says.
---

# Watch a reel

You can't hear audio, but `watch_reel.py` (in this skill's folder) turns it into text. Never step through a video frame by frame in a browser.

**One-time setup:** `py -m pip install --user yt-dlp faster-whisper imageio-ffmpeg` (ffmpeg comes bundled). The first run downloads the speech model (~500 MB).

## Steps

1. **Get the link.**
   - User gave a link → use it.
   - "the reel I have open" → read `location.href` of the open tab in the browser.
   - "my last saved reel" → in a browser where Instagram is logged in, open the profile, then `/<username>/saved/all-posts/`, and take the first `/p/` or `/reel/` link.
2. **Run** (~1 min): `py "<this skill's folder>/watch_reel.py" "<url>"`
   If it says DOWNLOAD FAILED, retry with `--cookies chrome`. Works in any language.
3. **Read** the caption + timed transcript it prints. That is usually enough.
4. **Frames** only if the user asks about something visual (a design, a UI, a list on screen): read 3–5 frames from the printed folder near the matching timestamps (`f_001` = 0s, one every 3s).
5. **Answer** in the user's style, linking what the video says to their project, and end with one recommendation.
