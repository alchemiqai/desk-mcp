"""Build the GitHub repository Open Graph image for alchemiqai/desk-mcp.

Outputs: .context/desk-mcp-public/og-image.png  (1280x640 PNG)
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO_DIR = Path(__file__).resolve().parents[1]
ATTACH_DIR = REPO_DIR.parent / "attachments"
LIGHT_LOGO = ATTACH_DIR / "YYivJi" / "chatgpt_app_icon_light_512.png"
OUTPUT = REPO_DIR / "og-image.png"

CANVAS = (1280, 640)
SAFE = 40
BG = (11, 30, 63)          # #0B1E3F  Alchemiq dark navy
INK = (255, 255, 255)
MUTED = (180, 192, 214)
ORANGE = (255, 107, 53)    # #FF6B35

SFNS = "/System/Library/Fonts/SFNS.ttf"
SF_ROUNDED = "/System/Library/Fonts/SFNSRounded.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def main() -> None:
    img = Image.new("RGB", CANVAS, BG)
    draw = ImageDraw.Draw(img, "RGBA")

    # Soft radial-ish highlight via two stacked translucent ellipses (top-right).
    for radius, alpha in [(560, 28), (360, 42)]:
        cx, cy = 1080, 120
        bbox = (cx - radius, cy - radius, cx + radius, cy + radius)
        draw.ellipse(bbox, fill=(255, 107, 53, alpha))

    # Thin orange accent stripe along left safe margin.
    draw.rectangle((SAFE + 0, SAFE, SAFE + 6, CANVAS[1] - SAFE), fill=ORANGE)

    # ---- Logo (light variant) on left, inside safe area ----
    logo = Image.open(LIGHT_LOGO).convert("RGBA")
    logo_size = 280
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
    logo_x = SAFE + 60
    logo_y = (CANVAS[1] - logo_size) // 2
    img.paste(logo, (logo_x, logo_y), logo)

    # ---- Text block on right ----
    text_x = logo_x + logo_size + 60
    text_max_w = CANVAS[0] - SAFE - text_x

    title_font = font(SFNS, 70)
    subtitle_font = font(SFNS, 38)
    tag_font = font(SFNS, 28)
    plat_font = font(SF_ROUNDED, 32)

    title = "Alchemiq News\nIntelligence"
    subtitle = "Global news intelligence via MCP"
    platforms = "ChatGPT  ·  Claude  ·  Gemini"
    tagline = "Search · Brief · Localize"

    # Vertically center the stack.
    title_lines = title.split("\n")
    line_h = title_font.getbbox("Ag")[3] + 6
    title_h = line_h * len(title_lines)
    gap_after_title = 18
    sub_h = subtitle_font.getbbox("Ag")[3]
    gap_after_sub = 30
    plat_h = plat_font.getbbox("Ag")[3]
    gap_after_plat = 22
    tag_h = tag_font.getbbox("Ag")[3]

    total_h = title_h + gap_after_title + sub_h + gap_after_sub + plat_h + gap_after_plat + tag_h
    y = (CANVAS[1] - total_h) // 2

    for line in title_lines:
        draw.text((text_x, y), line, font=title_font, fill=INK)
        y += line_h
    y += gap_after_title - 6

    draw.text((text_x, y), subtitle, font=subtitle_font, fill=MUTED)
    y += sub_h + gap_after_sub

    # Platform pills look — draw simple text in orange.
    draw.text((text_x, y), platforms, font=plat_font, fill=ORANGE)
    y += plat_h + gap_after_plat

    draw.text((text_x, y), tagline, font=tag_font, fill=MUTED)

    img.save(OUTPUT, format="PNG", optimize=True)
    print(f"Wrote {OUTPUT}  ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
