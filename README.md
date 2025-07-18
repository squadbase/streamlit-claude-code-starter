# Streamlit BI Dashboard Starter

A beginner-friendly starter template for building Business Intelligence (BI) dashboards using Streamlit and Python. Perfect for hands-on learning and rapid prototyping of data visualization applications.

## One-click deployment

[![Deploy to Squadbase](https://app.squadbase.dev/button.svg)](https://app.squadbase.dev/new/clone?repository-url=https://github.com/squadbase/streamlit-claude-code-starter)

## What You'll Learn

- How to build interactive web dashboards with Streamlit
- Data visualization and analysis with Python
- Working with CSV data and Pandas
- Creating multi-page applications
- Using Claude Code for AI-assisted development

## Quick Start

### Prerequisites

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) package manager (recommended) or pip

### Installation

1. **Fork this repository** to your GitHub account
2. **Clone your fork** to your local machine:

   ```bash
   git clone https://github.com/YOUR_USERNAME/streamlit-claude-code-starter.git
   cd streamlit-claude-code-starter
   ```

3. **Install dependencies**:

   ```bash
   # Using uv (recommended)
   uv sync

   # Or using pip
   pip install streamlit pandas plotly
   ```

4. **Run the application**:

   ```bash
   # Using uv
   uv run streamlit run app.py

   # Or using python directly
   streamlit run app.py
   ```

5. **Open your browser** to `http://localhost:8501` to see your dashboard!

## Project Structure

```
streamlit-claude-code-starter/
├── app.py              # Main dashboard application
├── pages/              # Additional pages for multi-page app
│   └── About_Us.py     # About page
├── sample_data/        # Sample CSV datasets
│   ├── orders.csv      # E-commerce orders data
│   └── users.csv       # User profiles data
├── pyproject.toml      # Python dependencies
└── README.md           # This file
```

## Sample Data

The `sample_data/` directory contains realistic e-commerce datasets for building your dashboard:

### Core Datasets

- **`orders.csv`** (37,957 records): E-commerce order transactions from 2025

  - Fields: `order_id`, `user_id`, `status`, `gender`, `created_at`, `returned_at`, `shipped_at`, `delivered_at`, `num_of_item`
  - Filtered to contain only 2025+ data for current analysis

- **`users.csv`** (29,357 records): Customer profiles linked to the filtered orders
  - Fields: `id`, `first_name`, `last_name`, `email`, `age`, `gender`, `state`, `street_address`, `postal_code`, `city`, `country`, `latitude`, `longitude`, `traffic_source`, `created_at`, `user_geom`
  - Contains only users who have placed orders in the filtered dataset

### Supporting Data Files (in `local/` directory)

- **`order_items.csv`** (55,150 records): Individual items within each order
  - Fields: `id`, `order_id`, `user_id`, `product_id`, `inventory_item_id`, `status`, `created_at`, `shipped_at`, `delivered_at`, `returned_at`, `sale_price`
- **`products.csv`** (24,640 records): Product catalog for items in the orders
  - Fields: `id`, `cost`, `category`, `name`, `brand`, `retail_price`, `department`, `sku`, `distribution_center_id`

All supporting datasets are filtered to only include data related to the current orders in `sample_data/`.

### Date Format Standardization

All date columns in the CSV files follow a consistent format:

- **Format**: `YYYY-MM-DD HH:MM:SS` (ISO 8601 standard)
- **Example**: `2025-07-04 15:33:00`
- **Timezone**: All dates are normalized to remove timezone information for consistency

Date columns include:

- `created_at`: When the record was created
- `shipped_at`: When the order was shipped
- `delivered_at`: When the order was delivered
- `returned_at`: When the order was returned

A standardization script (`local/standardize_dates.py`) is available to ensure date format consistency across all CSV files.

## Development with Claude Code

This project is optimized for use with [Claude Code](https://claude.ai/code), an AI coding assistant:

1. **Ask Claude to add features**: "Add a sales chart to the dashboard"
2. **Request improvements**: "Make the data tables more interactive"
3. **Get explanations**: "Explain how Streamlit caching works"
4. **Debug issues**: "Why isn't my chart displaying?"

### Example Prompts for Claude Code

- "Add a sidebar filter for order status"
- "Create a line chart showing orders over time"
- "Add user authentication to the dashboard"
- "Implement data export functionality"
- "Add responsive design for mobile devices"

## Customization Ideas

Start with these beginner-friendly modifications:

1. **Add Charts**: Create bar charts, line graphs, or pie charts
2. **Implement Filters**: Add dropdown menus or sliders for data filtering
3. **New Pages**: Create additional pages for different views
4. **Styling**: Customize colors, fonts, and layout
5. **Real Data**: Replace sample data with your own CSV files

## Learning Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas Tutorial](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Plotly Documentation](https://plotly.com/python/)
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)

## Contributing

This is a learning project! Feel free to:

- Fork and experiment
- Share your improvements
- Ask questions in the issues
- Submit pull requests with enhancements

## Next Steps

1. **Explore the code**: Start by understanding `app.py`
2. **Make small changes**: Try modifying the title or adding a new metric
3. **Add features**: Use Claude Code to help implement new functionality
4. **Share your work**: Deploy your dashboard to Streamlit Cloud

## License

MIT License - feel free to use this for learning and commercial projects.

---

**Happy Dashboard Building!**

Start building your first BI dashboard today and see how AI-assisted development with Claude Code can accelerate your learning journey.

**Deploy here!**

[![Deploy to Squadbase](https://app.squadbase.dev/button.svg)](https://app.squadbase.dev/new/clone?repository-url=https://github.com/squadbase/streamlit-claude-code-starter)
