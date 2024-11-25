# Data Visualization Dashboard

A Flask-based web application for dynamically visualizing datasets. This project uses the Titanic dataset to generate bar plots for categorical data and histograms for numerical data. Users can select features from the dataset to create custom visualizations.

## Features

- Dynamic data visualization.
- Supports bar plots for categorical data and histograms for numerical data.
- Uses Flask for an interactive web interface.
- Automatically handles missing data in the dataset.

## Tech Stack

- Python
- Flask
- Pandas
- Matplotlib

## Requirements

- Python 3.8 or later

Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Installation

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:

   ```
   http://127.0.0.1:5000
   ```

3. Select a feature from the dropdown menu to generate a plot.

## Folder Structure

```
project-folder/
├── app.py              # Main application script
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── index.html      # Homepage for selecting features
│   ├── visualize.html  # Visualization page
├── static/             # Directory for generated plots
```

## Screenshots

### Homepage
A user-friendly interface to select features for visualization.

### Visualization Page
Dynamically generated plots based on the selected feature.

## Future Enhancements

- Add support for uploading custom datasets.
- Include additional plot types such as scatter plots and box plots.
- Enhance the frontend with CSS for improved design.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

For questions or feedback, feel free to open an issue or reach out.

