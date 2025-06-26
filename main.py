import pandas as pd
from fpdf import FPDF

df = pd.read_csv("articles.csv")

class Article:
    def __init__(self, id):
        self.id = id
        self.name = str(df.loc[df["id"] == id, "name"].squeeze())
        self.price = float(df.loc[df["id"] == id, "price"].squeeze())

    def buy(self):
        if df.loc[df["id"] == self.id, "in stock"].squeeze() > 0:
            df.loc[df["id"] == self.id, "in stock"] -= 1
            df.to_csv("articles.csv", index=False)
            return True
        else:
            return False

class Receipt:
    def __init__(self):
        self.pdf = FPDF()

    def create_pdf(self, article):
        self.pdf.add_page()
        self.pdf.set_font(family="Times", style='B', size=12)
        self.pdf.set_text_color(0, 0, 0)

        self.pdf.text(10, 20, txt=f"Receipt nr.{article.id}")
        self.pdf.text(10, 25, txt=f"Item Description: {article.name}")
        self.pdf.text(10, 30, txt=f"Price: {article.price}")

        self.pdf.output(f"Receipt {article.id}.pdf")

while True:
    print(df)

    selected_id = int(input("Enter the id number that you would like to purchase: "))
    article = Article(selected_id)

    if (article.buy()):
        receipt = Receipt()
        receipt.create_pdf(article)
        break
    else:
        print("Product not available")