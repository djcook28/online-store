import pandas as pd

df = pd.read_csv("articles.csv")

class Article:
    def __init__(self, id):
        self.id = id
        self.name = str(df.loc[df["id"] == id, "name"].squeeze())
        self.price = float(df.loc[df["id"] == id, "price"].squeeze())

    def buy(self):
        if df.loc[df["id"] == self.id, "in stock"].squeeze() > 0:
            df.loc[df["id"] == self.id, "in stock"] = df.loc[df["id"] == self.id, "in stock"].squeeze() - 1
            return True
        else:
            return False

print(df)

selected_id = int(input("Enter the id number that you would like to purchase: "))
article = Article(selected_id)

print(article.id)
print(article.name)
print(article.price)

article.buy()
print(df)