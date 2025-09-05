# Movie Recommendation System with K-Nearest Neighbors

[![Codespaces Prebuilds](https://github.com/4GeeksAcademy/gperdrizet-recommender-systems/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/4GeeksAcademy/gperdrizet-recommender-systems/actions/workflows/codespaces/create_codespaces_prebuilds)

A comprehensive machine learning project that builds a movie recommendation system using K-Nearest Neighbors (KNN) algorithm with cosine similarity. This project demonstrates content-based filtering techniques through practical implementation with real movie data from The Movie Database (TMDb).

## Project Overview

This project develops a movie recommendation system using the **TMDb 5000 Movie Dataset**. The system analyzes movie features including genres, keywords, cast, and plot overviews to recommend similar films. The project provides hands-on experience with:

- Data preprocessing and feature engineering
- JSON data extraction and parsing
- Text vectorization using TF-IDF
- K-Nearest Neighbors algorithm implementation
- Content-based recommendation systems
- Model deployment as a command-line application

## Getting Started

### Option 1: GitHub Codespaces (Recommended)

1. **Fork the Repository**
   - Click the "Fork" button on the top right of the GitHub repository page
   - 4Geeks students: set 4GeeksAcademy as the owner - 4Geeks pays for your codespace usage. All others, set yourself as the owner
   - Give the fork a descriptive name. 4Geeks students: I recommend including your GitHub username to help in finding the fork if you lose the link
   - Click "Create fork"
   - 4Geeks students: bookmark or otherwise save the link to your fork

2. **Create a GitHub Codespace**
   - On your forked repository, click the "Code" button
   - Select "Create codespace on main"
   - If the "Create codespace on main" option is grayed out - go to your codespaces list from the three-bar menu at the upper left and delete an old codespace
   - Wait for the environment to load (dependencies are pre-installed)

3. **Start Working**
   - Open `notebooks/mvp.ipynb` in the Jupyter interface for the assignment
   - Follow the step-by-step instructions in the notebook
   - View `notebooks/solution.ipynb` for the complete implementation

### Option 2: Local Development

1. **Prerequisites**
   - Git
   - Python >= 3.10

2. **Fork the repository**
   - Click the "Fork" button on the top right of the GitHub repository page
   - Optional: give the fork a new name and/or description
   - Click "Create fork"

3. **Clone the repository**
   - From your fork of the repository, click the green "Code" button at the upper right
   - From the "Local" tab, select HTTPS and copy the link
   - Run the following commands on your machine, replacing `<LINK>` and `<REPO_NAME>`

   ```bash
   git clone <LINK>
   cd <REPO_NAME>
   ```

4. **Set Up Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Launch Jupyter & start the notebook**
   ```bash
   jupyter notebook notebooks/mvp.ipynb
   ```

## Project Structure

```
├── .devcontainer/       # Development container configuration
├── data/                # Data file directory
│   ├── raw/             # Original datasets
│   └── processed/       # Processed data artifacts
│
├── models/              # Trained model directory
│
├── notebooks/           # Jupyter notebook directory
│   ├── app.py           # Command-line recommendation app
│   ├── mvp.ipynb        # Assignment notebook (MVP)
│   └── solution.ipynb   # Complete solution notebook
│
├── .gitignore           # Files/directories not tracked by git
├── LICENSE              # Project license
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Dataset

The project uses two datasets from **The Movie Database (TMDb)**:

### `tmdb_5000_movies.csv`
Contains movie metadata with the following key features:
- **Title & Overview**: Movie titles and plot descriptions
- **Genres**: Movie categories (Action, Comedy, Drama, etc.)
- **Keywords**: Descriptive tags and themes
- **Production Details**: Budget, revenue, release dates
- **Language & Countries**: Original language and production countries

### `tmdb_5000_credits.csv`
Contains cast and crew information:
- **Cast**: Actor names and character details
- **Crew**: Director, producer, and other crew member information

**Note**: This dataset was collected for academic purposes only. No commercial benefit was obtained from web scraping activities.

## Algorithm Overview

The recommendation system uses a **content-based filtering** approach:

1. **Feature Engineering**: Extracts and combines movie genres, keywords, cast, and overview into a single text feature
2. **Text Vectorization**: Uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert text into numerical vectors
3. **Similarity Calculation**: Employs cosine similarity to measure distance between movie vectors
4. **Recommendation**: Uses K-Nearest Neighbors to find the 5 most similar movies

## Learning Objectives

1. **Data Integration**: Merge multiple datasets using pandas
2. **JSON Data Handling**: Parse and extract information from JSON-formatted columns
3. **Feature Engineering**: Combine multiple text features into unified representations
4. **Text Vectorization**: Apply TF-IDF vectorization for machine learning
5. **Machine Learning**: Implement and train a KNN model for recommendations
6. **Model Deployment**: Create a functional command-line application
7. **Data Persistence**: Save and load trained models and processed data

## Technologies Used

- **Python 3.11**: Core programming language
- **Pandas 2.3.1**: Data manipulation and analysis
- **Scikit-learn 1.7.1**: Machine learning algorithms and text processing
- **NumPy 2.3.2**: Numerical computing
- **PyArrow 21.0.0**: Efficient data serialization
- **Jupyter 1.1.1**: Interactive development environment

## Usage

### Running the Command-Line App

After completing the notebook exercises and training the model:

```bash
cd notebooks
python app.py
```

The application will prompt you to enter a movie title and return 5 similar movie recommendations.

### Example Output

```
Enter a movie title: How to Train Your Dragon
Film recommendations for 'How to Train Your Dragon':
- Film: Shrek
- Film: Madagascar
- Film: Ice Age
- Film: Monsters, Inc.
- Film: The Incredibles
```

## Contributing

This is an educational project. Contributions for improving the analysis, adding new features, or enhancing the recommendation algorithm are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

