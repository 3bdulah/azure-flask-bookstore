# Contributing

Thanks for improving this project.

## Before you open a PR

1. **Do not commit secrets** — no `.env`, no real Cosmos connection strings, and no production Kubernetes secrets. Use placeholders and local-only files.
2. **Run a quick check** (from `bookstore-app/` after `pip install -r requirements.txt`):

   ```bash
   python -m compileall -q app app.py
   ```

3. **Describe the change** — what broke, what you fixed, and how you verified it.

## Issues

Use GitHub Issues for bugs or small feature ideas. Include OS, Python version, and steps to reproduce when reporting bugs.
