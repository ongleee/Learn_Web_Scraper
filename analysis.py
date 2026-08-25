import pandas as pd
import matplotlib.pyplot as plt


def analyze(file):
  df = pd.read_csv(file)

  print("Question 1")
  print("Author คนไหนมี Quote มากที่สุด?")
  author_counts = df["author"].value_counts()
  print(author_counts.index[0])

  print()
  print("Question 2")
  print("Tag ไหนถูกใช้บ่อยที่สุด?")
  tag_counts = (df["tags"].dropna().str.split(",").explode().str.strip().value_counts())

  print(tag_counts.index[0])

  print()
  print("Question 3")
  print("Albert Einstein มี Quote กี่อัน?")
  count_Einstein = (df["author"] == "Albert Einstein").sum()
  print(count_Einstein)


  print()
  print("Question 4")
  print("Quote ที่มี Tag inspirational มีทั้งหมดกี่อัน?")
  count_inspirational = (df["tags"].dropna().str.split(",").explode().str.strip() == "inspirational").sum()
  print(count_inspirational)

  print()
  print("Question 5")
  print("Author แต่ละคนมี Tag อะไรบ่อยที่สุด?")
  for author in df["author"].dropna().unique():
    author_df = df[df["author"] == author]
    count_tag_author = (
      author_df["tags"]
      .dropna()
      .str.split(",")
      .explode()
      .str.strip().value_counts()
    )
    if not count_tag_author.empty:
      top_tag = count_tag_author.index[0]
      print(f"{author} = {top_tag}")
    else:
      print(f"{author} = ไม่มี tags")


  print()
  author_counts.head(10).plot(kind="bar")
  plt.title("Top 10 Authors ตามจำนวน Quote")
  plt.xlabel("Author")
  plt.ylabel("Quotes")
  plt.show()

  print()
  tag_counts.head(10).plot(kind="bar")
  plt.title("Top 10 Tags")
  plt.xlabel("Tag")
  plt.ylabel("count")
  plt.show()



analyze("quotes.csv")