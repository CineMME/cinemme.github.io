"""Render the page figures from the paper's figure PDFs.

    pip install pymupdf pillow
    python tools/render_figures.py /path/to/arxiv_paper/figures

Writes static/images/{teaser,pipeline}.webp.
"""
import io
import sys
from pathlib import Path

import pymupdf
from PIL import Image, ImageChops

SCALE = 3  # the frames embedded in the PDFs are ~3 px/pt; more adds nothing
OUT = Path(__file__).resolve().parent.parent / "static" / "images"
FIGURES = {"teaser": "cinemme_teaser.pdf", "pipeline": "cinemme_pipeline.pdf"}


def render(page):
    pix = page.get_pixmap(matrix=pymupdf.Matrix(SCALE, SCALE), alpha=False)
    return Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")


def trim(im, pad=6):
    # threshold: the slide background is a near-white image, not pure white
    diff = ImageChops.difference(im, Image.new("RGB", im.size, "white")).convert("L")
    box = diff.point(lambda v: 255 if v > 16 else 0).getbbox()
    box = (max(box[0] - pad, 0), max(box[1] - pad, 0), min(box[2] + pad, im.width), min(box[3] + pad, im.height))
    return im.crop(box)


def main():
    src = Path(sys.argv[1])
    OUT.mkdir(parents=True, exist_ok=True)
    for name, pdf in FIGURES.items():
        im = trim(render(pymupdf.open(src / pdf)[0]))
        path = OUT / f"{name}.webp"
        im.save(path, "WEBP", quality=88, method=6)
        print(f"{path.name}: {im.width}x{im.height}, {path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
