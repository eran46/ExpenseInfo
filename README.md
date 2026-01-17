# ExpenseInfo 💰

A Streamlit-based Python application to visualize and analyze Splitwise expense data in an interactive and informative way.

## Features

- **Multi-format Support**: Upload CSV or Excel files
- **Hebrew Character Support**: Handles Hebrew names correctly (use Excel export from Google Sheets for best results)
- **Smart Payment Filtering**: Automatically excludes "Payment" and "Settlement" categories from spending calculations
- **Interactive Dashboard**:
  - Total spending metrics with historic monthly average comparison
  - Date range and monthly filters
  - Spending by category (pie chart)
  - Spending trends over time with benchmark lines
  - Member net contributions comparison
  - Searchable transaction table

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd ExpenseInfo
```

2. Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser to the URL shown (typically http://localhost:8501)

3. Upload your Splitwise export file:
   - **For Hebrew names**: Export CSV from Splitwise → Open in Google Sheets → Download as Excel (.xlsx) → Upload here
   - **For regular CSV**: Just upload directly

## Expected File Format

Your file should contain these columns:
- `Date`: Transaction date
- `Description`: Expense description
- `Category`: Expense category (Food, Transport, etc.)
- `Cost`: Amount spent (numeric)
- `Currency`: Currency code
- Additional columns with member names (in any language including Hebrew)

## Tips

- The app automatically detects member columns (any column not in the standard set)
- Use the sidebar filters to focus on specific time periods
- Search the transaction table to find specific expenses
- Download filtered data as CSV for further analysis
- Negative net contributions = member owes money
- Positive net contributions = member is owed money

## Requirements

- Python 3.8+
- streamlit
- pandas
- plotly
- openpyxl (for Excel support)
- numpy
