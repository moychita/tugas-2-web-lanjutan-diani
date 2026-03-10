# TUGAS INDIVIDU 2 PEMROGRAMAN WEB LANJUTAN

API sederhana menggunakan **FastAPI** dan **SQLAlchemy** dengan database **SQLite**.  
Dibuat untuk memenuhi tugas Pemrograman Web Lanjutan.

---

## Teknologi

- Python 3.10+
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn

---

## Instalasi

### 1. Clone repository

```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

### 3. Jalankan server

```bash
uvicorn main:app --reload
```

Server berjalan di: `http://127.0.0.1:8000`

---

## Struktur Project

```
├── main.py        # Entry point & endpoint API
├── models.py      # Model database (SQLAlchemy)
├── schemas.py     # Validasi data (Pydantic)
├── database.py    # Koneksi database SQLite
└── app.db         # File database (auto-generated)
```

---

## Endpoint

| Method | URL | Deskripsi |
|--------|-----|-----------|
| `GET` | `/items/` | Ambil semua item |
| `GET` | `/items/{id}` | Ambil item berdasarkan ID |
| `POST` | `/items/` | Tambah item baru |

---

## Contoh Request

### Tambah Item (POST)

```json
POST /items/
{
  "nama": "Contoh Item",
  "deskripsi": "Deskripsi item",
  "kategori": "Kategori"
}
```

### Response

```json
{
  "id": 1,
  "nama": "Contoh Item",
  "deskripsi": "Deskripsi item",
  "kategori": "Kategori"
}
```

---

## Swagger UI

Setelah server berjalan, buka dokumentasi interaktif di:

```
http://127.0.0.1:8000/docs
```

---

## Author

**Diani** — Tugas 2 Pemrograman Web Lanjutan
