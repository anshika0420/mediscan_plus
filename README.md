# MediScan+ — Advanced AI Agent for Cancer Screening and Healthcare Management

**Prototype repository package (local)** — This archive contains a complete, runnable prototype for MediScan+:
- Flask backend with endpoints for symptom triage, appointment scheduling, and (stub) image pre-screening.
- Simple single-page frontend (HTML + JS) to interact with the backend.
- Dockerfile and instructions to run locally and how to push to GitHub.

> Note: This prototype uses a stubbed image classifier and simple triage logic to remain lightweight.
> Instructions in this README show how to connect a real pretrained model (PyTorch / TensorFlow).

## What's included
- `backend/` — Flask API service
- `frontend/` — Single-page UI (index.html + JS)
- `docker/` — Dockerfile for backend
- `sample_data/` — sample appointment CSV and sample images placeholder
- `LICENSE` — MIT license
- `run_locally.sh` — helper script to install & run (Linux / WSL / macOS)

## Quick start (local, using Python 3.9+)
1. Extract the archive and open a terminal in `mediscan_plus/backend`.
2. Create a virtualenv and install:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the backend:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   flask run --host=0.0.0.0 --port=5000
   ```
4. Open `frontend/index.html` in your browser (or serve it with a static server).
   The frontend calls backend endpoints on `http://localhost:5000`.

## How to replace the stub image classifier with a real model
1. In `backend/image_model.py` you'll find `predict_image_preset(file_path)` — currently returns a dummy result.
2. To use PyTorch:
   - `pip install torch torchvision pillow`
   - Load a pretrained ResNet or your fine-tuned checkpoint and replace the stub with real inference code.
   - See commented example in `image_model.py`.
3. To use TensorFlow/Keras:
   - `pip install tensorflow pillow`
   - Load a saved model and adapt the preprocessing pipeline.

## How to make this a GitHub repo (so you can clone & edit)
1. Create a new repo on GitHub (e.g., `MediScan-Plus`).
2. In the project root:
   ```bash
   git init
   git add .
   git commit -m "Initial MediScan+ prototype"
   git branch -M main
   git remote add origin https://github.com/<your-username>/MediScan-Plus.git
   git push -u origin main
   ```
3. Now you — and teammates — can `git clone` the created GitHub repo.

## Suggested next steps to improve prototype (for submission)
- Plug a validated medical imaging model (with appropriate data governance).
- Add authentication, logging, and HIPAA/GDPR-like compliance features.
- Integrate a real scheduling backend (Google Calendar / hospital API).
- Add unit tests and CI workflow (GitHub Actions).
- Add proper DB (Postgres) and migrate sample CSV to DB.

## Contacts / Authors
- Anshika Srivastava — provided project spec and content.

---

