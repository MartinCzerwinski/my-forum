# Changelog

## Compost Club — django-simple-forum Fork

---

## [1.0.0] — 2026-03-18

This release brings `django-simple-forum` up to date with modern Django, and introduces the **Compost Club** frontend — a fully themed community gardening forum with a custom design and Insane Mode.

---

### Bug Fixes & Django Compatibility

The original project was written for an older version of Django. The following breaking changes were resolved to allow the app to run on Django 4.x+:

- **`ugettext_lazy` removed** — replaced with `gettext_lazy` in `models.py` (`django.utils.translation`)
- **`ForeignKey` missing `on_delete`** — added `on_delete=models.CASCADE` to all ForeignKey fields in `models.py`
- **`render_to_response` removed** — replaced with `render` throughout `views.py`
- **`django.core.urlresolvers` removed** — replaced with `django.urls` in `views.py`
- **`django.core.context_processors` removed** — CSRF handling updated to use Django's built-in middleware approach
- **`patterns` and `url` removed** — replaced with `re_path` and direct view function imports in `urls.py`
- **`guest.decorators` removed** — replaced with Django's built-in `login_required` decorator
- **`south` migrations removed** — the original migrations relied on the third-party `south` library which was absorbed into Django core. Old migrations were deleted and regenerated using Django's native migration system
- **`{% load url from future %}` removed** — this template tag was removed in modern Django and was cleaned from all templates
- **`from settings import *` removed** — pagination constants (`TOPICS_PER_PAGE`, `REPLIES_PER_PAGE`) are now defined directly in `views.py`

---

### Frontend — Compost Club Theme

A full custom frontend was built on top of the app, replacing the original unstyled templates:

- **Base template** (`base.html`) — shared layout with header, navigation, and global styles
- **Forum index** (`list.html`) — card-based listing of all forum categories
- **Forum detail** (`forum.html`) — topic listing within a forum with post counts and dates
- **Topic detail** (`topic.html`) — threaded post view with user avatars and timestamps
- **Reply form** (`reply.html`) — styled form for posting replies
- **New topic form** (`new-topic.html`) — styled form for creating new topics

**Design language:**
- Warm earthy palette — greens, creams and browns inspired by the garden
- Clean card-based layout with subtle hover interactions
- Fully responsive single-column layout
- System font stack for fast load times

---

### Insane Mode 🌱🤪

A toggleable "Insane Mode" was added as a fun easter egg for community members:

- Rainbow animated logo and headings
- Floating and spinning forum cards
- Flying bees, butterflies and worms across the screen
- Falling petals, flowers and garden critters
- Animated gradient buttons
- Shaking header
- Dark garden colour scheme
- Preference is saved to `localStorage` so it persists across page loads

Toggle is available in the site header on every page.

---

### Project Setup Notes

- Virtual environment (`venv`) excluded from version control via `.gitignore`
- `db.sqlite3` excluded from version control
- `django_simple_forum` installed as a local app inside the `mysite` project directory
- Python path configured in `settings.py` to resolve the nested app location
- Pagination defaults set to 10 topics and 10 replies per page