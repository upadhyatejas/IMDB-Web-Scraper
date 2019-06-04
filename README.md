# IMDB Web Scraper 
A Python-based Scraper that recommends movies based on Emotion

# Basics Used:
- Web Scraping

# Recommendation:
- Based on the emotion entered, each emotion has been quantified as follows:
- Emotion || Recommended Genre

- Sad – Drama
- Disgust – Musical
- Anger – Family
- Anticipation – Thriller
- Fear – Sport
- Enjoyment – Thriller
- Trust – Western
- Surprise – Film-Noir

# Scraping:
- IMDb does not have an API , so data accumulation is performed by using scraping a particular URL of the accompanying emotion.
- Based on the emotion entered, top 'n' movies for that emotion are displayed, where 'n' is entered by the user.

# Files:
- sentiment.py : actual program to scrape / get the movie recommendation
- feels.py : a module in the package 'feeling', which takes in an emotion from sentiment, classifies it into one of 8 predefined emotions and returns said emotion category back to sentiment.py

# Text files:
- Each of the 8 emotions have a file with sample data inside them.
- Sample Data for each file consists of words which lean towards / convey the particular emotion
