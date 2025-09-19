# Auto Insights Generator

A minimal Python package that streamlines the **EDA (Exploratory Data Analysis)** step in a data science workflow.  
Given a pandas DataFrame, it can generate quick descriptive stats, simple plots, and structured outputs to speed up analysis.

---

## Features
- Lightweight API: pass in a DataFrame, get back an insights dictionary.
- Configurable sampling (analyze a subset for speed).
- Exports a summary CSV and basic plots (histograms for numeric columns).
- Easy to extend with new analyzers (correlations, statistical tests, etc.).
- Optional Quarto `.qmd` demo for rendering a report.

---

## Installation

Clone the repo and install in editable/development mode:

```bash
git clone https://github.com/<your-username>/auto-insights.git
cd auto-insights
python -m venv .venv && source .venv/bin/activate   # (Mac/Linux)
pip install -U pip pytest pandas
pip install -e .
