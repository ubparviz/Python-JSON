## JSON bilan ishlash

studentlarini score boyicha ratinglashtirish

---

## 📁 Fayl tuzilmasi

```
student_rating_json/
├── students.json     ← Kiruvchi fayl
├── rating.json       ← Chiquvchi fayl
└── rating_sorter.py  ← Python kodi
```

---

## 📄 `students.json` (kiruvchi JSON fayl)

```json
[
  {"name": "Ali", "score": 87},
  {"name": "Laylo", "score": 93},
  {"name": "Sardor", "score": 78},
  {"name": "Nilufar", "score": 91},
  {"name": "Javohir", "score": 65}
]
```

---

## 📄 `rating.json` (chiqish fayli – natija)

```json
[
  {
    "name": "Laylo",
    "score": 93,
    "rank": 1
  },
  {
    "name": "Nilufar",
    "score": 91,
    "rank": 2
  },
  {
    "name": "Ali",
    "score": 87,
    "rank": 3
  },
  {
    "name": "Sardor",
    "score": 78,
    "rank": 4
  },
  {
    "name": "Javohir",
    "score": 65,
    "rank": 5
  }
]
```

---
