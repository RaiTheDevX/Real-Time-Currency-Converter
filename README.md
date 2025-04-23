# 💱 Real Time Currency Converter

## 📜 Project Overview
This project is an **interactive currency converter tool** developed in Python that fetches real-time exchange rates and converts between different currencies.  
Users can input a base currency, target currency, and an amount to get the converted result instantly using a simple CLI. It demonstrates working with APIs and Python fundamentals.

---

## ⚙️ Features
- **Real-Time Exchange Rates:** Fetches live exchange rates via API.
- **Currency Conversion:** Converts entered amount from base to target currency.
- **Error Handling:** Handles invalid inputs and connection errors gracefully.
- **Multi-Currency Support:** Works with various global currencies like USD, EUR, INR, GBP, etc.
- **Command-Line Interface:** Lightweight and easy to use through the terminal.

---

## 🛠️ How It Works
1. **API Integration:**  
   Connects to an exchange rate API (like ExchangeRate-API or exchangerate.host) to fetch live data.

2. **User Input:**  
   Prompts user to enter:
   - Base currency (e.g., USD)
   - Target currency (e.g., EUR)
   - Amount to convert

3. **Conversion Logic:**  
   Multiplies amount with exchange rate and displays result.

4. **Error Handling:**  
   Checks for valid currency codes, connection issues, and numeric input for amount.

---

## 🖥️ Requirements
- Python 3.x
- Libraries:
  - `requests`

Install the required library using:
```bash
pip install requests
```

---

## 🚀 Usage

- **Clone the repository:**
  ```bash
  gh repo clone RaiTheDevX/Real-Time-Currency-Converter
  ```

- **Run the script:**
  ```bash
  python currency_converter.py
  ```

- **Follow the prompts to:**
  - Enter the base currency
  - Enter the target currency
  - Enter the amount
  - View the conversion result

---

## 📊 Example Output
```text
Enter base currency (e.g., USD, EUR): USD
Enter target currency (e.g., EUR, INR): EUR
Enter the amount to convert: 100

100 USD is equal to 92.34 EUR
```

---

## 🤔 Why This Project?
This project demonstrates:
- 🌐 Integration with real-time public APIs.
- 🧮 Dynamic conversion logic based on live data.
- 👨‍💻 Simple terminal-based interaction using core Python.
- 🛠️ Practical usage of error handling and input validation.

---

## 🙌 Contributing
Contributions are welcome!  
Feel free to **open an issue** or **submit a pull request** to enhance functionality or improve the interface.

---

## 📜 License
This project is licensed under the MIT License.
