## URL_SHORTER
-  just trying to implement `url_shortener` from `first principles` thought
- applying basic knowledge of how should a simple `url shortener` work
- then expand it (Improve it) :(
- Project is on `development` phase. It's just the basic starter kit
## ⚙️ Local Setup

1. **Clone & Navigate**
```bash
git clone git@github.com:PritomKarmokar/url_shorter.git
cd mindInk
```
2. **Copy `.env.example` to `.env`**
```bash
cp .env.example .env
# Update `.env` with DB credentials & secret key
```
3. **Create & Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
4. **Install Dependencies**
```bash
pip install -r requirements.txt 
```
5. **Database & Server**
```bash
python manage.py migrate
python manage.py runserver
```
6. **Create Admin**
```bash
python manage.py createsuperuser
```