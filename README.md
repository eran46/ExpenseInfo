# streamlit-splitwise-dashboard 💰

A powerful Streamlit-based Python application for visualizing and analyzing Splitwise expense data. Transform your Splitwise exports into beautiful, interactive dashboards with comprehensive analytics, multi-group support, and smart expense tracking.

## 🎯 Who Is This For?

This app is perfect for **Splitwise power users** who:
- **Consistently track expenses** through Splitwise (households, roommates, travel groups, etc.)
- Want **deeper insights** beyond what Splitwise provides
- Need to **analyze spending patterns** across multiple groups
- Track both **personal expenses** and **household/group costs**
- Want to **monitor income vs expenses** and savings rates
- Need **historical analysis** and trend visualization
- Value **privacy** with local data storage

## 📋 Requirements

### What You Need:
1. **Active Splitwise Usage**: Regular expense tracking in Splitwise
2. **Python 3.8+** installed on your computer
3. **Splitwise Export Files**: CSV exports from your Splitwise groups
4. **Basic Terminal Knowledge**: To run Python commands

### How to Export from Splitwise:

#### Option 1: Splitwise Website (Recommended)
1. Go to [Splitwise.com](https://www.splitwise.com) and log in
2. Navigate to your group (or "All expenses" for everything)
3. Click on the **⚙️ Settings** icon (top right)
4. Select **"Export as spreadsheet"**
5. Choose **CSV** format and click **Download**
6. Save the file to your computer

#### Option 2: Via Google Sheets (Best for Hebrew/Non-English Names)
1. Export CSV from Splitwise (as above)
2. Open the CSV file in **Google Sheets**
3. Go to **File → Download → Microsoft Excel (.xlsx)**
4. This preserves character encoding for Hebrew and other languages

**Note**: For multiple groups, export each group separately and import them individually into the app.

## ✨ Features

### 📊 Overview Dashboard
- **Total Spending Metrics**: See aggregate personal expenses across all members
- **Historic Monthly Average**: Compare current month spending to historical patterns
- **Current Month Tracking**: Real-time spending for the ongoing month
- **Expense Ratio**: Compare spending against monthly income (if configured)
- **Category Breakdown**: Visual pie chart of spending by category (excluding internal transfers)
- **Timeline Visualization**: Track spending trends over time with interactive charts
- **Smart Filtering**: Automatically excludes Payment/Settlement categories and reimbursement transactions

### 📈 Advanced Analytics
- **Monthly Spending Analysis**: Detailed breakdown by category with stacked visualizations
- **Yearly Spending Overview**: Interactive pie chart showing category distribution by year
- **Year-over-Year Comparison**: Track spending patterns with customizable date ranges
- **Cost-Based Calculations**: All plots show actual transaction costs (not just individual shares)

### 💰 Income & Savings Tracking
- **Income Sources Management**: Track multiple income streams with custom labels
- **Savings Rate Calculator**: Automatic calculation of monthly savings percentage
- **Income vs Expenses**: Visual comparison of monthly income and spending
- **Historical Income Tracking**: View income history and trends over time

### 👥 Multi-Group Support
- **Multiple Groups**: Manage data from different Splitwise groups separately
- **Group Switching**: Easily switch between groups with visual selectors (emojis + names)
- **Active Group Tracking**: Set which group you're currently viewing
- **Combined Analytics**: Analyze spending across multiple groups simultaneously
- **Individual Member Views**: Deep dive into any member's spending patterns

### 🔄 Combined Analytics (Multi-Group Analysis)
- **All Group Expenses View**:
  - Total spending across all selected groups
  - Spending distribution by group (pie + bar charts)
  - Category breakdown across groups with color-coded visualization
  - Timeline tracking across multiple groups
  - Month-based filtering for all visualizations
  
- **Individual Member View**:
  - Track any member's expenses across all groups
  - Personal expense breakdown by category
  - Spending by group comparison
  - Transaction history with search and filtering
  - Net balance tracking (owed vs owes)

### 💾 Data Management
- **Group-Specific Data Management**: Select which group to import/export data for
- **Persistent Storage**: Data saved locally - no need to re-upload each session
- **Automatic Backups**: Every save creates a backup (keeps 5 most recent)
- **Duplicate Detection**: Smart detection prevents duplicate transactions
- **Multiple Import Formats**: Support for CSV and Excel files
- **Multiple Export Formats**: Export to CSV, Excel, or JSON
- **Data Integrity**: Validates all transactions before saving
- **Concurrent Access Protection**: File locking prevents data corruption
- **Member Auto-Discovery**: Automatically detects and updates group members from imported data

### 🏢 Group Management
- **Create Multiple Groups**: Set up separate groups with custom names and emojis
- **Edit Group Details**: Change names, emojis, and descriptions anytime
- **Delete Groups**: Remove groups with confirmation (includes data cleanup)
- **Set Active Group**: Choose which group to view in Overview/Analytics
- **Visual Organization**: Emoji-based identification for quick group recognition

### 🎨 Smart Features
- **Payment Filtering**: Automatically excludes "Payment" and "Settlement" transactions from spending analysis
- **Reimbursement Detection**: Identifies and filters out "owed full amount" transactions (where member debt equals transaction cost)
- **Multi-Language Support**: Full support for Hebrew and other non-English characters
- **Responsive Design**: Clean, intuitive interface with Streamlit
- **Interactive Visualizations**: Plotly-powered charts with hover details and zoom
- **Real-time Filtering**: Date range selectors with automatic recalculation

## 🚀 Installation

1. **Clone this repository**:
```bash
git clone <repository-url>
cd ExpenseInfo
```

2. **Install dependencies**:
```bash
python3 -m pip install -r requirements.txt
```

## 📖 Usage

### First Time Setup

1. **Run the Streamlit app**:
```bash
streamlit run app.py
```

2. **Open your browser** to the URL shown (typically http://localhost:8501)

3. **Create Your First Group**:
   - Go to **"Manage Groups"** in the sidebar
   - Click **"Create New Group"**
   - Enter a name (e.g., "Home 🏡" or "Travel ✈️")
   - Choose an emoji for visual identification
   - Click **Create**

4. **Import Your Splitwise Data**:
   - Navigate to **"Data Management"** page
   - Select the group you want to import data for
   - Click **"Choose files"** and upload your Splitwise CSV/Excel export
   - The app will automatically:
     - Detect and add group members
     - Skip duplicate transactions
     - Save your data locally
     - Create an automatic backup

5. **Start Exploring**:
   - Switch to **"Overview"** to see your spending dashboard
   - Use **"Analytics"** for detailed breakdowns
   - Track income in **"Income & Savings"**
   - Compare groups in **"Combined Analytics"**

### Subsequent Usage

Once set up, simply run `streamlit run app.py` and:
- ✅ Your data loads automatically
- ✅ All groups are preserved
- ✅ No need to re-upload files
- ✅ Continue where you left off

### Adding More Data

1. Export new data from Splitwise (follow export instructions above)
2. Go to **"Data Management"**
3. Select the appropriate group
4. Upload the new file
5. Duplicates are automatically skipped - safe to import overlapping data!

## 📁 Data Storage

All data is stored locally in the `user_data/` directory:

```
user_data/
├── groups.json              # Group configuration
├── income_data.json         # Income tracking data
└── groups/
    ├── group_id_1/
    │   ├── transactions.json
    │   └── backups/
    │       ├── transactions_backup_*.json
    │       └── ...
    ├── group_id_2/
    │   ├── transactions.json
    │   └── backups/
    └── ...
```

**Privacy Note**: This directory is git-ignored. Your financial data stays private and local.

## 📊 Expected File Format

Your Splitwise export should contain these columns:

| Column | Description | Example |
|--------|-------------|---------|
| `Date` | Transaction date | 2024-01-15 |
| `Description` | Expense description | Groceries |
| `Category` | Expense category | Food |
| `Cost` | Total transaction amount | 8500.00 |
| `Currency` | Currency code | ILS, USD, EUR |
| `Member Names` | One column per member | Positive = paid, Negative = owes |

**Important Notes**:
- Member columns are **auto-detected** (any column not in the standard set)
- Positive values = Member paid this amount
- Negative values = Member owes this amount
- Hebrew and special characters are fully supported
- Payment/Settlement transactions are automatically filtered from analysis

## 💡 Tips & Tricks

### Understanding the Numbers
- **Total Spending (₪222k)**: Sum of all positive member values = what everyone paid out of pocket
- **Plot Amounts**: Show actual transaction costs (excluding internal transfers)
- **Net Balance**: Positive = owed money, Negative = owes money

### Best Practices
1. **Export regularly** from Splitwise to keep data current
2. **Use meaningful group names** with emojis for quick identification
3. **Set up income sources** for accurate savings rate tracking
4. **Use Combined Analytics** to see the big picture across all groups
5. **Check backups** before clearing data - they're there for a reason!

### Working with Multiple Groups
- Each group maintains **separate transaction data**
- **Switch active group** in sidebar to change Overview/Analytics view
- Use **Combined Analytics** to analyze spending across all groups
- Import data to the **correct group** via Data Management page

### Data Safety
- ✅ **5 automatic backups** kept at all times
- ✅ **Create manual backups** before major imports
- ✅ **Restore from backup** if something goes wrong
- ✅ **Export data regularly** as an extra precaution

## 🔧 Requirements

**Python Packages** (auto-installed with requirements.txt):
- `streamlit` - Web interface framework
- `pandas` - Data processing and analysis
- `plotly` - Interactive visualizations
- `openpyxl` - Excel file support
- `numpy` - Numerical computations

**System Requirements**:
- Python 3.8 or higher
- ~50MB disk space for installation
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🤝 Contributing

Found a bug or have a feature request? Feel free to open an issue or submit a pull request!

## 📝 License

This project is open source and available under the MIT License.

---

**Made with ❤️ for Splitwise users who want deeper insights into their spending patterns.**
