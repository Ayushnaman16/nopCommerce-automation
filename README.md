# nopCommerce Automation 🚀

Automation testing framework for [nopCommerce](https://www.nopcommerce.com/) using **Python**, **Selenium WebDriver**, and **Pytest**.  
This project follows the **Page Object Model (POM)** design pattern for maintainable and scalable test automation.

---

## 📌 Features
- ✅ Automated UI testing for nopCommerce web application
- ✅ Built with **Python + Selenium + Pytest**
- ✅ Page Object Model (POM) structure for reusability
- ✅ Configurable test execution
- ✅ HTML test reports using `pytest-html`
- ✅ Easy to scale and integrate with CI/CD pipelines

---

## 📂 Project Structure
nopCommerce-automation/
│── tests/ # Test cases
│── pages/ # Page Object Model (POM) classes
│── utils/ # Utility files (driver setup, configs, etc.)
│── requirements.txt # Project dependencies
│── pytest.ini # Pytest configuration
│── README.md # Project documentation
│── .gitignore # Git ignore file
│── LICENSE # License file

1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/nopCommerce-automation.git
cd nopCommerce-automation

2️⃣ Create a virtual environment (recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt

▶️ Running Tests
Run all tests
bash
Copy code
pytest
Run tests with detailed output
bash
Copy code
pytest -v
Generate HTML report
bash
Copy code
pytest --html=report.html --self-contained-html
Run a specific test file
bash
Copy code
pytest tests/test_login.py -v

📊 Reporting
Test execution results are generated in HTML format using pytest-html.
Reports can be found in the project root as report.html.

🔮 Future Enhancements
🔹 Add API testing for nopCommerce REST APIs
🔹 Integrate with Jenkins/GitHub Actions for CI/CD
🔹 Add support for parallel test execution
🔹 Implement cross-browser testing with Selenium Grid

🤝 Contributing
Fork the repository
Create a new branch (feature-xyz)
Commit your changes
Push to your fork and open a Pull Request
