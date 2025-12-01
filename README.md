# E-Commerce User Behavior Analysis 📊

## Data Source
[Dataset](https://docs.google.com/spreadsheets/d/1dDczkp5SRp6IMNpKxiak_4q0S5qrOSILIyKzp-2I9ZE/export?format=csv&gid=1307725687)
The dataset used in this analysis is an e-commerce event log containing user interactions such as views, searches, and purchases.

- **Source:** RevoU Study Case
- **Format:** CSV
- **Key Columns:**
  - `event_timestamp`: Date and time of the interaction.
  - `event_type`: Type of action (view, cart, search, etc.).
  - `user_id`: Unique identifier for users.
  - `country`: User location.
  - `device`: Device used (Android, iOS, Desktop).
> **Note:** The data is loaded directly via URL in the python script.

## Project Overview
This project analyzes user behavior data from an E-commerce platform. The analysis focuses on identifying key markets, growth trends, device preferences, and feature effectiveness.

## Key Insights
- **Market Focus:** Indonesia is the dominant market with the highest user activity in Q2 2025.
- **Channel Trend:** A significant surge in traffic occurred in April across all channels.
- **Device Preference:** Users exhibit a strong "Mobile-First" behavior (Android & iOS).
- **Optimization:** Peak activity occurs during commuter hours (7-8 AM & 5-7 PM).
- **Critical Finding:** The "Search-to-Cart" conversion rate is **0.21%**, indicating a need for search algorithm optimization.

> Prefer visuals? Access the step-by-step analysis and key findings in the presentation slides:
**[View Full Presentation Slides](ECommerce_User_Behavior_Report.pdf)**

## Tech Stack

**Data Processing & Analysis**
<br>
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

**Data Visualization**
<br>
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-7db0bc?style=for-the-badge&logo=seaborn&logoColor=white)

## How to Run
1. Clone this repository.
2. Install dependencies: `pip install pandas numpy matplotlib seaborn`
3. Run the script: `python ecommerce_analysis.py`

## 🤝 Let's Connect!
I am always open to discussing data analytics, Python projects, or potential collaborations. Feel free to reach out!

- **LinkedIn:** [Rakha Raihan Raditya](https://www.linkedin.com/in/rakharaihanraditya)
- **Email:** [rakharaihanraditya@gmail.com](mailto:rakharaihanraditya@gmail.com)
- **Portfolio:** [Check out my other projects](https://bit.ly/portfolio-rakharaihanraditya)
