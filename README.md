# cinemme.github.io

Project page for **CineMME: From Dialogue Grounding to Narrative Reasoning in Multimodal Video Understanding** (NeurIPS 2026, Track on Evaluations and Datasets).

The page is one static file, `index.html`, with no build step. GitHub Pages serves the `main` branch root.

## Preview locally

```bash
python -m http.server 8000   # then open http://localhost:8000
```

Opening `index.html` directly also works, because the leaderboard data is inline.

## Update the leaderboard

Edit the JSON inside `<script type="application/json" id="lb-data">` in `index.html`. Each row has these fields:

- Reasoning: `model, org, open, input ("V" or "AV"), params, frames, narrative, perception, scene, social, audio, mcq, oeq, n_mcq, n_oeq`
- Grounding: `model, org, open, params, tiou, viou, wer, n_g, n_v`

Ranks, best/second highlighting and the coverage marks (†, ‡) are computed in the page. Keep the numbers identical to the paper tables (`tables/model_compare.tex`, `tables/tracka_compare.tex`, `tables/app_evaluation_coverage.tex`).

## Figures

```bash
pip install pymupdf pillow
python tools/render_figures.py /path/to/arxiv_paper/figures
```

This renders `teaser.webp` and `pipeline.webp` at 3x, cropped to content. If a size changes, update the `width`/`height` in `index.html`. The dataset statistics are HTML bars in `index.html`, not images. Faces are blurred in the source figures. Do not add video files to this repository.
