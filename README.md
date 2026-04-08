# ✨ Pagecraft — AI-Powered Document Generator

A lightweight, full-stack Django + SQLite web app that lets users generate professional **resumes, invoices, business cards, and social media posts** from templates — supercharged with AI.

## 🚀 Features

- 🎨 **Template System** — pre-built templates per category with dynamic Django rendering
- ⚡ **Live Preview** — real-time updates as you type
- 🤖 **AI Integration** — OpenAI-powered "Enhance with AI" buttons (Improve / Summarize / Auto-fill)
- 📄 **PDF Export** — via WeasyPrint (with HTML fallback if unavailable)
- 💾 **Save & Edit** — store generated documents in SQLite
- 🌐 **Multi-language** — English + हिन्दी
- 📱 **Responsive UI** — TailwindCSS-powered modern design
- 🔌 **REST API** — DRF endpoints for templates, documents, and AI processing

## 📦 Setup with `uv`

This project uses [**uv**](https://github.com/astral-sh/uv) — the fast Python package manager. **No pip needed.**

### 1. Install uv (if you don't have it)
```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install dependencies
```bash
cd "d:/Claude Tool/Card"
uv sync
```
This creates a `.venv/` and installs everything from `pyproject.toml`.

### 3. Configure environment
```bash
cp .env.example .env
# edit .env and add your OPENAI_API_KEY (optional — works without it via fallback)
```

### 4. Run migrations & seed templates
```bash
uv run python manage.py migrate
uv run python manage.py seed_templates
uv run python manage.py createsuperuser   # optional, for /admin
```

### 5. Start the server
```bash
uv run python manage.py runserver
```

Visit **http://127.0.0.1:8000/** 🎉

## 🛠 Useful commands

| Command | Purpose |
|---|---|
| `uv add <package>` | Add a new dependency |
| `uv run python manage.py <cmd>` | Run any Django management command |
| `uv run python manage.py seed_templates` | Re-seed/refresh starter templates |
| `uv run python manage.py makemigrations` | Create new migrations |

## 🧠 AI Notes

- Set `OPENAI_API_KEY` in `.env` for live AI enhancement
- Without an API key, the app uses a **local heuristic fallback** so the UI stays usable

## 📂 Project Structure

```
Card/
├── pyproject.toml          # uv-managed dependencies
├── manage.py
├── docgen/                 # Django project (settings, urls, wsgi)
├── generator/              # Main app
│   ├── models.py           # Template, GeneratedDocument
│   ├── views.py            # Pages + DRF viewsets
│   ├── ai_service.py       # OpenAI wrapper + fallback
│   ├── serializers.py
│   ├── urls.py
│   └── management/commands/seed_templates.py
└── templates/              # base, home, category, editor, documents
```

## 🌐 API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/templates/?category=resume` | List templates |
| POST | `/api/templates/<id>/render/` | Render HTML with data |
| GET/POST | `/api/documents/` | List/save documents |
| POST | `/api/ai/enhance/` | AI text enhancement |
| POST | `/api/export-pdf/<id>/` | Generate PDF |

## 📝 PDF Note (Windows)

WeasyPrint requires GTK on Windows. If you hit install issues, the app **automatically falls back to downloading styled HTML** instead — still printable from any browser. To get true PDF on Windows, install GTK3: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

---
Built with ❤️ using Django, DRF, OpenAI, and uv.
