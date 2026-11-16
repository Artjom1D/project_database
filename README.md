# project_database

<img width="1247" height="741" alt="image" src="https://github.com/user-attachments/assets/429fa0e8-ee6d-4671-95a1-b1c70910ed72" />

## Apraksts

**Zoodārza katalogs** — darbvirsmas lietotne (Python + Tkinter + SQLite), kas paredzēta zoodārza darbiniekiem. Tajā var uzturēt katalogu par zoodārzu, tā dzīvniekiem, barību, biļetēm, pasākumiem, darbiniekiem un viņu atvaļinājumiem, kā arī veterinārajiem ierakstiem.

- **Mērķis:** zoodārza kataloga veidošana strādniekiem
- **Lietotāji:** zoodārza dārbnieki

## Funkcionalitāte

- Informācijas **pievienošana**, **labošana** un **dzēšana** visās tabulās
- **Meklēšana** katrā tabulā (pēc nosaukuma, krāsas, datuma u.c. laukiem)
- Katras tabulas automātiska atjaunināšana pēc izmaiņām

## Datubāzes tabulas

`zoo`, `location`, `pet_group`, `pet`, `food`, `veterinary_records`, `tickets`, `events`, `employees`, `vacation`

## Palaist projektu

Nepieciešama tikai Python 3 (standarta bibliotēkas `tkinter` un `sqlite3`):

```
python app.py
```

Datubāzes fails `data.db` tiek izveidots automātiski pirmajā palaišanas reizē.

## Projekta struktūra

| Fails | Saturs |
|---|---|
| `app.py` | Tkinter grafiskais interfeiss (logi, formas, tabulas) |
| `logic.py` | Darbības ar datubāzi (pievienošana, meklēšana, atjaunināšana, dzēšana) |
| `database.py` | Datubāzes shēmas izveide |

## Pēdējās izmaiņas

- `has_free BLOB` → `has_vacation BOOLEAN`
- `free_id` → `vacation_id`
- Tabula `free` pārsaukta par `vacation`
- Tabulā `vacation` vairs nav rindas `name`

## Plānotais

- Uzlabot noformējumu
