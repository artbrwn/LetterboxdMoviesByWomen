# 🎬 Letterboxd Movies by Women

## 🚧 Work in progress

This project is under development, but currently working.

Feel free to follow along in the commit history or check the Issues tab to see planned features.

## 📌 Project Description

**Letterboxd Movies by Women** is a Python project that analyzes the movie-watching history of a Letterboxd user to calculate the percentage of films directed by women. The goal is to raise awareness about gender representation in cinema while practicing data analysis and Python development skills.

## 🎯 Motivation
A few years ago, someone asked me to name ten women film directors. Although many of my favorite films are directed by women—and many of my creative role models are women—I struggled to come up with ten names on the spot. That moment made me realize how invisible women’s work can be, even to someone who actively seeks it out.

This project is a personal effort to make that imbalance visible in my own viewing habits. It’s also part of my journey learning Python and practicing data analysis. Through this small tool, I've explored concepts like web APIs, data structures, visualization with Matplotlib, and how to think critically about the biases present in our data and tools.


## 🔍 Main Features

- Import movie data from a Letterboxd-exported CSV file.
- Detect which movies were directed by women.
- Calculate and display the percentage of watched movies directed by women.
- Generate simple summaries and visualizations.
- Explore trends over time.
- Export the resulting list as a csv that can be imported into Letterboxd, useful while analyzing your watchlist.


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
- For each film, query TMDb using its title and year.
- Retrieve the director(s) from the crew list of the movie's credits.
- Determine gender using TMDb's person metadata.


## 🚧 Future Improvements

Allow to iterate over non detected movies and asign them as either directed by women or not directed by women.

Allow to choose between your already watched films and a watchlist or any other type of list (you can actually already do that) and handle the response.


## ⚠️ Gender Disclaimer
This project relies on gender data provided by The Movie Database (TMDB) API. Gender is assigned based on TMDB's internal categorization. While TMDB appears to recognize and correctly identify many trans and nonbinary creators, I cannot guarantee that there are no misclassifications or omissions in their database. If you spot an error, feel free to contribute or open an issue.


## 📄 License
This project is licensed under the MIT License.


## 🤝 Credits
Letterboxd movies by women uses the TMDB API but is not endorsed or certified by TMDB.
