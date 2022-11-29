import pandas as pd
import matplotlib.pyplot as mpl

df = pd.read_csv("game-ratings-by-release-dates.csv")

#clean up data
df["first_release_date"] = pd.to_datetime(df["first_release_date"])

#analyze data with visualization
mpl.scatter(df["first_release_date"], df["critic_rating_value"], color = "blue", label = "Critic Ratings")
mpl.scatter(df["first_release_date"], df["user_rating_value"], color = "red", label = "User Ratings")

mpl.legend(loc = "upper left")

mpl.show()