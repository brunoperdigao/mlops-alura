from textblob import TextBlob

frase = "O Fortaleza e o melhor time do nordeste"
tb = TextBlob(frase)
tb_en = tb.translate(from_lang='pt_br', to='en')

tb_en.sentiment.polarity
