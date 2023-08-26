import glob
import streamlit as st
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []
for filepath in filepaths:
	with open(filepath) as file:
		content = file.read()
	scores = analyzer.polarity_scores(content)
	positivity.append(scores['pos'])
	negativity.append(scores['neg'])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]

st.title("Diary Tone")
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity,
					 labels={"x":"dates", "y":"negativity"})

st.plotly_chart(pos_figure)

st.subheader("Positivity")
neg_figure = px.line(x=dates, y=negativity,
					 labels={"x":"dates", "y":"negativity"})
st.plotly_chart(neg_figure)


