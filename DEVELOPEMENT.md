
## 📄 `DEVELOPMENT.md` for Task Manager CLI

```markdown
# 🛠️ Task Manager CLI - Development Log

This file documents the development process, design choices, and future enhancements of the Task Manager CLI application.

---

## 📅 Project Timeline

### ✅ Phase 1: Basic Functionality
- Setup folder structure and `main.py`
- Added task loading/saving via `tasks.json`
- Implemented:
  - View tasks
  - Add new tasks
  - Mark tasks as completed

### ✅ Phase 2: Bug Fixes and Improvements
- Fixed `KeyError` by ensuring `"completed"` field is always included
- Used `.get()` method for safer dictionary access
- Removed the `.get()` method as it was causing some errors

### ✅ Phase 3: Enhanced User Experience
- Added delete task feature
- Implemented colored CLI output using `colorama`
- Sorted tasks (pending first, done last)
- Task summary added (total, done, pending)

---

## 🧠 Design Decisions

- **CLI over GUI**: Focused on clean, keyboard-friendly interaction for simplicity
- **JSON for storage**: Easy to read/write and portable
- **colorama**: Added to make status visibility intuitive (✅ Done vs ❌ Not Done)
- **Sorted view**: Tasks are sorted to show pending tasks first, improving focus

---

## 🔍 Code Structure

```

task\_manager/
├── main.py         # Core logic and CLI menu
├── tasks.json      # Stores all tasks (auto-created)
├── README.md       # Project overview and usage guide
└── DEVELOPMENT.md  # This file - development insights

```

---

## 📌 Future Plans

- Add due dates and priority levels
- Add search or filter functionality (e.g., show only completed)
- Save tasks in a database (SQLite) instead of JSON
- Build a GUI version with `tkinter` or `PyQt`
- Export tasks to `.csv`

---

## 🤝 Contributions

This is a solo project by **Vedant Vidhate**, but contributions or feedback are always welcome. Fork, improve, and share!

---

> This log reflects the incremental, test-driven, and educational approach used during development.
