# Django News Aggregator

A portfolio-ready Django project that aggregates news from external sources, lets users browse/filter by topics, and exposes a simple JSON API.

## ✨ Features
- Topic model with slugs (SEO-friendly topic pages)
- Article ingestion from NewsAPI via a custom management command
- Duplicate-safe ingestion (`get_or_create` on URL), robust date parsing, optional images
- Search in titles/summaries, topic chips, pagination
- Simple JSON API: list articles with filters
- Admin-ready (manage topics, inspect articles)
- Production-ready knobs (Gunicorn, WhiteNoise, `DATABASE_URL` support)
- Test suite using `pytest` + `pytest-django`

## 🧱 Tech Stack
- Python 3.12, Django 5
- SQLite (dev) / PostgreSQL (prod-ready via `DATABASE_URL`)
- Requests, django-environ
- (Optional) djangorestframework for API class-based views
- pytest / pytest-django for testing

## 🚀 Getting Started (Local)

```bash
git clone https://github.com/yourname/django-news-aggregator.git
cd django-news-aggregator
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env  # fill in your keys
python manage.py migrate
python manage.py runserver
```

Open: http://127.0.0.1:8000

## ⚙️ Environment Variables

Create a `.env` file (see `.env.example`):

```
SECRET_KEY=your-django-secret
DEBUG=True
NEWSAPI_KEY=your-newsapi-key
ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=
DATABASE_URL=sqlite:///db.sqlite3
```

## 📥 Ingesting Articles

Run the custom management command to fetch articles for all topics:

```bash
python manage.py fetch_articles
```

Optional: add a single-topic mode (see code comments) and scheduled cron in production.

## 🔎 API Endpoints (basic)

```
GET /api/health/             -> {"status":"ok"}
GET /api/topics/             -> list topics
GET /api/articles/?q=...&topic=ID&page=N  -> paginated list
```

## 🧪 Tests

```bash
pip install pytest pytest-django factory_boy coverage
pytest
# Coverage:
coverage run -m pytest && coverage html
```

## 🧽 Lint & Format

- **Ruff** (linter): `ruff check .`  (auto-fix: `ruff check . --fix`)
- **Black** (formatter): `black .`

Example `ruff.toml`:

```toml
line-length = 100
target-version = "py312"
extend-select = ["E", "F", "I"]  # pycodestyle, pyflakes, isort

[format]
quote-style = "double"
```

## 🏭 Production (later)

- Set env vars: `SECRET_KEY`, `DEBUG=False`, `NEWSAPI_KEY`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, `DATABASE_URL`
- Serve via Gunicorn + WhiteNoise, run `collectstatic`, run `migrate`
- Add a cron to run `python manage.py fetch_articles` hourly

## 📝 License

MIT (adjust as you wish).
