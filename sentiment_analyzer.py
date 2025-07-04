import re

def clean_text(text):
    """
    Lowercase, remove punctuation, and split into tokens.
    """
    text = text.lower()
    text = re.sub(r"[^a-z\s]", '', text)
    tokens = text.split()
    return tokens

# 1.Knowledge base

positive_words = {
    'happy', 'joy','joyful','cheer','delighted','smile','jolly','content','gleeful','lucky','fortunate', 'untroubled','blissful','tickled','ecstatic','merry'
}
negative_words = {
    'sad', 'unhappy','heartbroken','depressed','bad','upset','melancholy','upset','worried','stress','saddened','gloomy', 'miserable','low','down','unfortunate'
}

# 2. print positive lexicon & negative lexicon:
print("Positive_lexicon:")
print(positive_words)
print("Negative_lexicon:")
print(negative_words)

# --- Interactive Sentiment Testing ---
print("\nEnter sentences to analyze sentiment (type 'exit' to quit):")
while True:
    text = input('> ').strip()
    if text.lower() in ('exit', 'quit'):
        print("Thanks for using the Sentiment Analyzer!")
        break

    tokens = clean_text(text)
    pos_count = sum(1 for t in tokens if t in positive_words)
    neg_count = sum(1 for t in tokens if t in negative_words)
    total = len(tokens)

# 3. Compute simple sentiment score (hint: positive - negative count)

    # Determine sentiment label
    score = pos_count - neg_count
    if score > 0:
        sentiment = 'Positive'
    elif score < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

# 4. print the output results
    print("~ Sentiment Analyzer Results ~")
    print(f"Tokens: {tokens}")
    print(f"+ matches: {pos_count}, - matches: {neg_count}")
    print(f"Score: {score:.3f} => {sentiment}\n")

# 5. Add a short reflection as comments at the bottom (2–3 sentences)


#This lexicon-based sentiment analysis approach is a good option to implement and understand, making it a good starting point for sentiment analysis.
#Its main strengths is transparency and speed for basic sentiment classification.
#However, a significant limitation is its inability to capture nuances like sarcasm, slang, or context-dependent sentiment, leading to potential misclassifications in more complex language.
#The effectiveness is also heavily reliant on the quality and coverage of the defined lexicons and understanding of the creator of the lexicons.
