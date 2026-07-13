# Maintaining this site

Notes for whoever maintains the Sailing Protocols repo and website. Viewers
don't need any of this — it's build/deploy/tooling only.

## How it publishes

The site is built with **MkDocs + Material** directly from the Markdown files in
this repo (no reformatting) and deployed to GitHub Pages by a GitHub Actions
workflow (`.github/workflows/deploy.yml`) on every
push to `main`.

Live site: **https://amir-daniel.github.io/sailing-protocols/**

## One-time GitHub setup

1. Push this repo to `https://github.com/amir-daniel/sailing-protocols`.
2. In the repo: **Settings → Pages → Build and deployment → Source = "GitHub Actions"**.
3. Push to `main` — the workflow builds and publishes the site.

## Editing

Just edit any `.md` file and push to `main`. The site rebuilds and republishes
itself automatically. To add a page, create the `.md` file and add it to the
`nav:` section of `mkdocs.yml`.

## Preview locally

```powershell
pip install mkdocs-material mkdocs-same-dir
mkdocs serve
```

Then open http://127.0.0.1:8000/.

## QR codes

Print-ready QR codes that open the site live in the `assets/qr/` folder:

- `site-home.*` → the home page (crew onboarding at the dock)
- `emergency.*` → the 🚨 Emergency quick-access page (mount near the nav station)

Regenerate them any time (e.g. if the URL changes):

```powershell
pip install "qrcode[pil]"
python assets/generate_qr.py
```
