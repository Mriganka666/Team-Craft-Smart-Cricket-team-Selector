# 🏏 TeamCraft – Smart Cricket Team Generator

TeamCraft is a simple Python GUI application that helps you generate the best possible cricket playing XI by selecting two teams and analyzing player performance stats.

## ✨ Features

- Select two cricket teams from a dataset.
- Automatically picks the best XI from combined players.
- Role-based team formation:
  - 4 Batsmen
  - 4 Bowlers
  - 2 All-rounders
  - 1 Wicket-Keeper
- Smart captain and vice-captain suggestions.
- User-friendly GUI with dropdown menus and display area.

## 🖼️ GUI Preview

![TeamCraft GUI Preview](screenshot.png)
<!-- Replace screenshot.png with your actual image file -->

## 🚀 How to Run

1. Install required libraries:
   ```bash
   pip install pandas tabulate
   ```

2. Ensure the dataset file `your_dataset.csv` is in the same folder as `newselect.py`.

3. Run the app:
   ```bash
   python newselect.py
   ```

## 🗂️ Project Files

- `newselect.py` – The main GUI application
- `your_dataset.csv` – Sample dataset containing player statistics
- `README.md` – Project documentation

## 📄 Dataset Format Example

The dataset must be a `.csv` file with columns like this:

```csv
Player,Role,Team,Match1,Match2,Match3,...
Virat Kohli,BAT,India,45,60,72,...
Ben Stokes,ALL,England,38,50,55,...
```
- **Player**: Name of the cricketer
- **Role**: BAT, BOW, ALL, or WK
- **Team**: Team name (e.g., India, England)
- **Match1...MatchN**: Performance values (e.g., runs or points)

## 🛠️ Built With

- Python 3.x
- Tkinter – for GUI
- Pandas – for data handling
- Tabulate – for neatly formatted output

---

## 🙌 Contributing

Pull requests and suggestions are welcome! If you find a bug or have a feature request, feel free to open an issue.

---

## 📄 License

This project is for educational purposes. You are free to use, modify, and enhance it as needed.

---

## 👤 Author

**Mriganka Ghosh**  
Developer & Project Author  
