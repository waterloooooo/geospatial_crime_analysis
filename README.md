# 🗺️ Geospatial Crime Analysis (San Francisco)

This project visualizes San Francisco crime data on interactive maps using Python. It uses `folium` for map rendering, `MarkerCluster` for performance, and optional `HeatMap` overlays for density analysis.

---

## 📁 Project Structure

```

geospatial_crime_analysis
├── data
│   └── sf_crime_data.csv                # Crime dataset (not included — download externally)
├── notebook
│   └── sf_crime_analysis.ipynb          # Jupyter notebook with full analysis
├── output
│   ├── sf_crime_clustered_map.html      # Interactive map with marker clusters
│   └── sf_crime_heatmap.html            # Optional heatmap version
├── scripts
│   └── map_plotter.py                   # Script version of the map generation
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation

```

---

## 📊 Dataset

We use the official [San Francisco Police Department Incident Reports (2018–Present)](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783).

### ⚠️ Note on Dataset

Due to GitHub's file size restrictions, the dataset file `sf_crime_data.csv` is **not included** in this repository.

To run this project:

1. Download the dataset manually from the [SFGov Open Data Portal](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-2018-to-Present/wg3w-h783)
2. Place it in the `data` folder:

```
geospatial_crime_analysis/data/sf_crime_data.csv

````

> The dataset is large. To ensure maps remain responsive, the code samples only a portion of the data (e.g., 1,000 rows).

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/waterloooooo/geospatial_crime_analysis.git
cd geospatial_crime_analysis
````

### 2. Set Up Your Environment

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt:**

```
pandas>=1.5
folium>=0.14
```

---

## 📌 Features

* Clean and filter raw crime data
* Sample the dataset for map performance
* Generate interactive maps:

  * 📍 `MarkerCluster` (group nearby incidents)
  * 🔥 `HeatMap` (optional density visualization)
* Save as standalone `.html` files for sharing

---

## 🧪 How to Run

### Option 1: Run the Notebook

```bash
jupyter notebook notebook/sf_crime_analysis.ipynb
```

### Option 2: Run the Python Script

```bash
python scripts/map_plotter.py
```

> Maps will be saved inside the `output/` directory.

---

## 📂 Output Files

| File                          | Description                            |
| ----------------------------- | -------------------------------------- |
| `sf_crime_clustered_map.html` | Interactive map with clustered markers |
| `sf_crime_heatmap.html`       | Optional density-based heatmap         |

Open these `.html` files in your browser to explore the visualizations.

---

## 🛠️ Customization Ideas

* Filter by incident category (e.g. Theft, Assault)
* Add time sliders or dynamic filters
* Try different base map tiles
* Support other cities or geospatial datasets

---

## 📄 License

This project is licensed under the MIT License.
Dataset provided by the [City and County of San Francisco Open Data Portal](https://data.sfgov.org/).