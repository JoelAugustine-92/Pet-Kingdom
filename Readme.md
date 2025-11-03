# Pet Kingdom – Cinematic Pet Store

A **stunning, cinematic pet store** built with **Flask** — featuring video hero, dark mode, login, and a working shopping cart.

Live Demo (Coming Soon): Say **"Deploy online"** to get your free link!

---

## Features

| Feature | Status |
|--------|--------|
| Video Hero Background | Done |
| Particle Effects | Done |
| Dark Mode (Saved in Session) | Done |
| User Login / Register | Done |
| Add to Cart | Done |
| View Cart + Remove Items | Done |
| Checkout (Clear Cart) | Done |
| Responsive Navbar | Done |
| Flash Messages | Done |
| Test User Included | Done |

---

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JS, Jinja2
- **Database**: SQLite + SQLAlchemy
- **Auth**: Flask-Login
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins + Playfair Display)
- **Video**: Free from Pixabay
- **Images**: Amazon, Shutterstock, Unsplash

---

## Project Structure
pet-kingdom-app/
│
├── app.py                  # Main Flask app (routes, cart, auth)
├── models.py               # User model (SQLAlchemy)
├── README.md               # This file
│
├── instance/
│   └── petkingdom.db       # Auto-created SQLite DB
│
├── templates/
│   ├── index.html          # Home + Shop
│   ├── cart.html           # Cart page
│   ├── login.html          # Login form
│   └── register.html       # Register form
│
├── static/
│   ├── stylesheet.css      # All styles
│   └── script.js           # Navbar toggle + particles
│
└── venv/                   # Virtual environment (not in Git)
text---

## How to Run Locally

### 1. Open Terminal in Project Folder
```bash
cd C:\petkingdom\new\pet-kingdom-app
2. Activate Virtual Environment
bashvenv\Scripts\activate
3. Install Dependencies
bashpip install flask flask-login flask-sqlalchemy
4. Run the App
bashpython app.py
5. Open in Browser
http://127.0.0.1:5000