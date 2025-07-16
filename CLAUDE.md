# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Streamlit-based BI dashboard starter application that displays sample e-commerce data (orders and users). The project uses Python with Streamlit for the web interface and Pandas for data manipulation.

## Architecture

- **Main Application**: `app.py` - Single-file Streamlit application that loads and displays CSV data
- **Data**: `sample_data/` directory contains CSV files with orders and users data
- **Dependencies**: Managed via `pyproject.toml` using uv as the package manager

## Key Components

- **Data Loading**: Uses `@st.cache_data` decorator for efficient CSV loading
- **UI Structure**: Wide layout with data tables displaying the first 10 rows of each dataset
- **Sample Data**: 
  - `orders.csv`: E-commerce order data with status, timestamps, and item counts
  - `users.csv`: User profile data with demographics and geographic information

## Development Commands

### Setup and Installation
```bash
# Install dependencies (assumes uv is installed)
uv sync
```

### Running the Application
```bash
# Start Streamlit development server
uv run streamlit run app.py
```

### Package Management
```bash
# Add new dependency
uv add package-name

# Update dependencies
uv sync
```

## Development Notes

- The application uses Python >=3.11 as specified in pyproject.toml
- Streamlit configuration is set to wide layout mode
- Data caching is implemented for performance with `@st.cache_data`
- No testing framework is currently configured
- No linting or formatting tools are configured in the project