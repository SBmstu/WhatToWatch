# 🎬 WhatToWatch – Your Ultimate Movie Decision Engine

> _"Stop scrolling. Start watching."_

WhatToWatch is not just another movie picker – it's a **cinematic oracle** that harnesses the raw power of the **Kinopoisk API Unofficial** to serve you a handpicked masterpiece from the **TOP-250 best films of all time**. Every refresh is a journey into the heart of world cinema, curated by a sophisticated Django-powered backend that delivers instant, data‑rich recommendations.

---

## ✨ What Makes WhatToWatch Legendary?

- **One‑Click Serendipity** – With a single tap, you summon a random gem from the pantheon of cinema. No more endless scrolling through Netflix – let fate decide.
- **Rich Cinematic Data** – Each recommendation comes with a high‑resolution poster, IMDb‑style rating, release year, genre tags, and a plot synopsis. You get everything you need to fall in love with your next watch.
- **Lightning‑Fast Response** – Powered by Django and the blazing‑fast `requests` library, WhatToWatch delivers your movie in milliseconds. No lag, no fuss – just pure movie magic.
- **Elegant, Responsive UI** – A clean, card‑based design that adapts to any screen – from desktop to mobile. Every film feels like a collector's edition.
- **Always Fresh** – The page never repeats itself (unless you're really unlucky 😉). Each reload brings a new cinematic adventure.

---

## 🛠️ Tech Stack – The Engines of Destiny

- **Backend:** Django 4+ – the rock‑solid framework that powers the logic.
- **API:** Kinopoisk API Unofficial (v2.2) – the ultimate source of Russian cinema data.
- **HTTP Client:** `requests` – fast, reliable, and battle‑tested.
- **Environment Management:** `python-dotenv` – keeping secrets safe and sound.
- **Frontend:** Pure HTML5 + CSS3 – no bulky frameworks, just clean, semantic markup.
- **Deployment Ready:** Fully containerizable with Docker (optional) and prepared for production with environment‑based settings.

---

## 🚀 Get It Running in 2 Minutes

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SBmstu/WhatToWatch.git
   cd WhatToWatch
   ```

2. **Set up a virtual environment and install dependencies:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Get your free API key** from [Kinopoisk API Unofficial](https://kinopoiskapiunofficial.tech/) – it takes 30 seconds.

4. **Create a `.env` file** in the project root (copy `.env.example` if provided) and add:

   ```
   API_KEY=your_super_secret_key_here
   SECRET_KEY=your_django_secret_here
   DEBUG=True   # switch to False in production
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` and let the movie magic begin!

---

## 🔮 Why WhatToWatch?

- **Built for the indecisive** – if you've ever spent 45 minutes choosing a movie, this is your salvation.
- **Zero bloat** – no accounts, no tracking, no cookies – just pure recommendation bliss.
- **Perfect portfolio piece** – demonstrates clean Django patterns, API integration, environment management, and a polished frontend.
- **Extensible** – easily add filters (genre, year, rating), implement caching, or even hook up a Telegram bot – the sky's the limit.

---

## 🧩 Future Enhancements (Coming Soon™)

- **Genre & Year Filters** – refine your fate.
- **"Watch Later" List** – save favorites with local storage.
- **Caching Layer** – reduce API calls and improve speed.
- **Docker Compose** – one‑command deployment.

---

## 🤝 Contribute

Found a bug? Have a killer feature idea? Pull requests are warmly welcomed. Let's make movie discovery even more magical.

---

## 📄 License

MIT – free to use, modify, and share.

---

**WhatToWatch** – because every night deserves a perfect film. 🌟

---

_Now go ahead – click the button and let destiny pick your next cinematic adventure._
