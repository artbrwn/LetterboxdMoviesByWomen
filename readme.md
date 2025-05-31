# 🎬 Letterboxd Movies by Women

## 🚧 Work in progress

This project is under development. I'm currently working on CSV parsing and integrating TMDb API.

Feel free to follow along in the commit history or check the Issues tab to see planned features.

## 📌 Project Description

**Letterboxd Movies by Women** is a Python project that analyzes the movie-watching history of a Letterboxd user to calculate the percentage of films directed by women. The goal is to raise awareness about gender representation in cinema while practicing data analysis and Python development skills.


## 🔍 Main Features

- Import movie data from a Letterboxd-exported CSV file.
- Detect which movies were directed by women.
- Calculate and display the percentage of watched movies directed by women.
- Generate simple summaries and visualizations.
- Explore trends over time (optional/advanced).


## 🚀 How to Use

1. Export your movie history from your [Letterboxd account](https://letterboxd.com/settings/data/) as a `.csv` file.
2. Save the file inside the `data/` folder.
3. Run the script with:

```bash
python main.py --csv data/your-movies.csv
```

## 🔐 TMDb API Configuration

To use this project, you need an API key from [The Movie Database (TMDb)](https://www.themoviedb.org/documentation/api).

1. Create a free TMDb account.
2. Request an API key at: https://www.themoviedb.org/settings/api
3. Once you have your API key, save it in a `.env` file in the project root:

TMDB_API_KEY=your_api_key_here

The project will load it using the `python-dotenv` package. Never commit your `.env` file to version control.


##  🧠 How It Works

The program reads your Letterboxd CSV file and identifies the director(s) of each film by querying the [TMDb API](https://www.themoviedb.org/documentation/api). It then detects their gender and calculates what percentage of the watched movies were directed by women.

Key steps:
- For each film, query TMDb using its title and (optionally) year.
- Retrieve the director(s) from the crew list of the movie's credits.
- Determine gender using TMDb's person metadata.
- Handle cases with missing or ambiguous data gracefully.


## 🚧 Future Improvements
Improve director gender detection using more reliable sources.

Add more advanced visualizations and filtering options.

Support for multiple users and comparison mode.

Develop a minimal web interface or CLI enhancements.


## 📄 License
This project is licensed under the MIT License.


## 🤝 Credits
Letterboxd movies by women uses the TMDB API but is not endorsed or certified by TMDB.