"""Generate QR codes pointing at the published SProtocols site.

Run:  python assets/generate_qr.py

Produces PNG + SVG QR codes in assets/qr/ for:
  - the site home page
  - the emergency quick-access page

Requires: pip install "qrcode[pil]"
"""
from pathlib import Path

import qrcode
import qrcode.image.svg

BASE_URL = "https://amir-daniel.github.io/SProtocols/"

TARGETS = {
    "site-home": BASE_URL,
    "emergency": BASE_URL + "EMERGENCY/",
}

OUT_DIR = Path(__file__).parent / "qr"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def make(name: str, url: str) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=12,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # PNG (for printing / stickers)
    png = qr.make_image(fill_color="black", back_color="white")
    png.save(OUT_DIR / f"{name}.png")

    # SVG (scalable / crisp at any size)
    svg = qrcode.make(
        url, image_factory=qrcode.image.svg.SvgPathImage
    )
    svg.save(OUT_DIR / f"{name}.svg")

    print(f"  {name}: {url}")


if __name__ == "__main__":
    print("Generating QR codes:")
    for n, u in TARGETS.items():
        make(n, u)
    print(f"Saved to: {OUT_DIR.resolve()}")
