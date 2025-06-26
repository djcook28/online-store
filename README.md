# 🧾 Article Purchase and PDF Receipt Generator

This Python script allows users to purchase items from a CSV-based inventory and automatically generates a receipt in PDF format using `fpdf`.

## 📦 Features

- Load articles from a CSV file
- Display inventory to the user
- Allow item selection via ID
- Decrease stock after successful purchase
- Automatically generate and save a PDF receipt

## 🛠 How It Works
- Load Inventory: Reads articles.csv into a DataFrame.
- User Input: Displays items and prompts for an ID to purchase.
- Purchase Logic:
- Checks if item is in stock.
- Decreases the stock count and saves the update.
- Generates a PDF receipt with item details.
- Loop Control: Ends once a successful purchase is mad

## 📂 CSV File Format
Make sure your articles.csv file looks something like this:
id,name,price,in stock
100,laptop sven 10,999.0,87
101,mouse clara,12.99,87

## 📄 Sample Receipt Output
A successful purchase will create a PDF file named like:
Receipt 100.pdf

It will include:
- Receipt number
- Item description
- Item price

## 🚀 Running the Program
To start the script, simply run:
python your_script_name.py
Replace your_script_name.py with the actual name of your file.

## 🌍 Real-World Applications
This project simulates a basic point-of-sale system, making it useful for:
- **Small Business Inventory Management**: Track item availability and automatically update stock after purchases.
- **Digital Receipt Generation**: Issue PDF-based receipts, reducing reliance on paper and enabling easy archiving.
- **Rapid Prototyping for Retail Software**: Test simple commerce workflows in Python without needing a full database or web interface.
- **Learning Tool**: Great for beginners looking to understand data manipulation, user interaction, and file I/O with real-world use cases.


