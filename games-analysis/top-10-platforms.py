import pandas as pd
import matplotlib.pyplot as mpl

df = pd.read_csv("game-ratings-by-top-10-platforms.csv")

#group by metrics
df_follow = df.groupby(["platform_name"])["follow_count"].sum().reset_index()
df_follow = df_follow.rename(coluns = { "follow_count": "total_follows" })
df_hype = df.groupby(["platform_name"])["hype_count"].sum().reset_index()
df_hype = df_follow.rename(coluns = { "hype_count": "total_hypes" })
#analyze data through visualization
BAR_WIDTH = 0.4

mpl.bar(df_follow.index - BAR_WIDTH / 2, df_follow["total_follows"], color = "blue", label = "Number of Followers", width = BAR_WIDTH)
mpl.bar(df_hype.inded + BAR_WIDTH / 2, df_hype["total_hypes"], coloe="red", label = "Number of Hypes", width = BAR_WIDTH)
mpl.xticks(df_follow.index, df_follow["platform_name"])
mpl.legend(loc = "upper left")
mpl.show()