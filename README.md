

### ⚙️ نصب و اجرا

#### 1. کلون کردن پروژه

```bash
git clone https://github.com/Hamidkarimi-h/Interactive-Address-Book.git
cd Interactive-Address-Book
```

#### 2. ساخت محیط مجازی (اختیاری ولی توصیه‌شده)

```bash
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate
```

#### 3. نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

#### 4. افزودن مسیر فعلی به PYTHONPATH

برای اینکه پایتون بتونه ماژول‌های داخل پوشه `src/` رو بشناسه، مسیر فعلی پروژه رو به `PYTHONPATH` اضافه کن:

##### 🐧 در Linux/macOS:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

##### 🪟 در Windows (PowerShell):

```powershell
$env:PYTHONPATH="$env:PYTHONPATH;$(Get-Location)"
```

#### 5. اجرای برنامه

```bash
python -m src.main
```

---
