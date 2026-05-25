# 🗂️ How to Reorganize Your GitHub Repository

Follow these steps to restructure your repo to the professional layout.

---

## Step 1 — Create the folders on GitHub

In your repository, click **"Add file"** → **"Create new file"**

Type each of these paths (GitHub auto-creates folders when you add a `/`):
- `notebooks/.gitkeep`
- `app/.gitkeep`
- `models/.gitkeep`
- `assets/.gitkeep`
- `data/README.md` ← paste the content from `data/README.md`

Commit each one.

---

## Step 2 — Upload your files to the right folders

| Your file              | Upload to folder  |
|------------------------|-------------------|
| `IDS_system.ipynb`     | `notebooks/`      |
| `app.py`               | `app/`            |

---

## Step 3 — Replace / create these files in the ROOT of your repo

Upload or create these files directly in the root (not inside any folder):

| File               | Action                          |
|--------------------|---------------------------------|
| `README.md`        | Replace with the new one        |
| `requirements.txt` | Create new                      |
| `.gitignore`       | Create new                      |
| `LICENSE`          | Create new                      |

---

## Step 4 — Add a repository description & topics

1. Go to your repo main page
2. Click the ⚙️ gear icon next to "About" (top right of the file list)
3. Set:
   - **Description:** `AI-powered Network Intrusion Detection System using Random Forest on the UNSW-NB15 dataset · Streamlit Dashboard`
   - **Website:** *(leave blank or add your LinkedIn)*
   - **Topics:** `machine-learning` `cybersecurity` `intrusion-detection` `random-forest` `streamlit` `python` `data-science` `unsw-nb15` `ids` `network-security`

---

## Step 5 — Pin the repository

1. Go to your GitHub **profile page**
2. Click **"Customize your pins"**
3. Select **DecodeLabs-Internship**

This makes it the first thing anyone sees on your profile. ✅

---

## Final Result

Your repo will look like this:

```
DecodeLabs-Internship/
├── notebooks/
│   └── IDS_system.ipynb
├── app/
│   └── app.py
├── models/
│   └── (auto-generated — gitignored)
├── assets/
│   └── (auto-generated — gitignored)
├── data/
│   └── README.md
├── README.md        ← professional, badges, mermaid diagram
├── requirements.txt
├── .gitignore
└── LICENSE
```
