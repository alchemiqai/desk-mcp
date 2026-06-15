"""Build the GitHub repository Open Graph image for alchemiqai/desk-mcp.

A clean, centered Alchemiq logo on the brand navy background.
Outputs: .context/desk-mcp-public/og-image.png  (1280x640 PNG)
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

REPO_DIR = Path(__file__).resolve().parents[1]
ATTACH_DIR = REPO_DIR.parent / "attachments"
LIGHT_LOGO = ATTACH_DIR / "YYivJi" / "chatgpt_app_icon_light_512.png"
OUTPUT = REPO_DIR / "og-image.png"

CANVAS = (1280, 640)
SAFE = 40
BG = (11, 30, 63)          # #0B1E3F  Alchemiq dark navy
INK = (255, 255, 255)
ORANGE = (255, 107, 53)    # #FF6B35

SFNS = "/System/Library/Fonts/SFNS.ttf"


def main() -> None:
    img = Image.new("RGB", CANVAS, BG)

    # Soft orange glow behind the logo, blurred to avoid banding.
    glow = Image.new("RGBA", CANVAS, (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    cx, cy = CANVAS[0] // 2, 250
    radius = 230
    gdraw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius),
                  fill=(255, 107, 53, 60))
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")

    draw = ImageDraw.Draw(img, "RGBA")

    # ---- Logo centered ----
    logo = Image.open(LIGHT_LOGO).convert("RGBA")
    logo_size = 300
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
    logo_x = (CANVAS[0] - logo_size) // 2
    logo_y = 90
    img.paste(logo, (logo_x, logo_y), logo)

    # ---- Wordmark under the logo ----
    wordmark_font = ImageFont.truetype(SFNS, 72)
    wordmark = "Alchemiq"
    w = draw.textlength(wordmark, font=wordmark_font)
    draw.text(((CANVAS[0] - w) // 2, logo_y + logo_size + 24),
              wordmark, font=wordmark_font, fill=INK)

    img.save(OUTPUT, format="PNG", optimize=True)
    print(f"Wrote {OUTPUT}  ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
