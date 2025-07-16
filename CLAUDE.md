# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Streamlit-based BI dashboard starter application that displays sample e-commerce data (orders and users). The project uses Python with Streamlit for the web interface and Pandas for data manipulation.

## Architecture

- **Main Application**: `Home.py` - Multi-page Streamlit application that loads and displays CSV data
- **Pages**: `pages/` directory contains additional pages (`About_Us.py`)
- **Data**: `sample_data/` directory contains CSV files with e-commerce data
- **Local Processing**: `local/` directory contains data processing scripts
- **Dependencies**: Managed via `pyproject.toml` using uv as the package manager

## Key Components

- **Data Loading**: Uses `@st.cache_data` decorator for efficient CSV loading
- **UI Structure**: Wide layout with data tables displaying the first 10 rows of each dataset
- **Multi-page Support**: Streamlit's native multi-page architecture with pages in `pages/` directory
- **Sample Data**: 
  - `orders.csv`: E-commerce order data with status, timestamps, and item counts
  - `users.csv`: User profile data with demographics and geographic information
  - `order_items.csv`: Individual order items data
  - `products.csv`: Product information data

## Development Commands

### Setup and Installation
```bash
# Install dependencies (assumes uv is installed)
uv sync
```

### Running the Application
```bash
# Start Streamlit development server
uv run streamlit run Home.py
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
- Multi-page architecture allows for easy expansion of functionality
- Dependencies include Plotly for enhanced data visualization capabilities
- No testing framework is currently configured
- No linting or formatting tools are configured in the project