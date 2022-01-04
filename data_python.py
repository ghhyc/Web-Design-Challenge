import pandas as pandas
#import CVS into pandas

data = pd.read_csv("Resources/cities.csv")

#Save to html source:https://stackeroverflow.com/questions/14897833/save-pandas-to-html-as-a-file
data.to_html("data.html", index=False)