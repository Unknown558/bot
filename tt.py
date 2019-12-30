import tweepy
import requests
import random
import json
import time

consumer_key = "ErZ65rh6UwAKEy0sZxJMrYnlx"
consumer_secret = "2e7WKcUgJu0wdMi58YeFPvhyAn20VOhJk4KXwCuIyopoPj2qbz"

access_token = "1211691414548930561-giwQkJXhkMnQpF7zkia4L4HCo9LXoH"
access_token_secret = "bxPccKxB68auJwrKLq2fyDxtWeiGlRl9v1X1FVoASltDm"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


while True:
	lista = ["gn", "ex", "lv", "nm", "dt", "js", "jz", "rt", "1sm", "2sm", "1rs", "2rs", "1cr", "2cr", "ed", "ne", "et", "job", "sl", "pv", "ec", "ct", "is", "jr", "lm", "ez", "dn", "os", "jl", "am", "ob", "jn", "mq", "na", "hc", "sf", "ag", "zc", "ml", "mt", "mc", "lc", "jo", "at", "rm", "1co", "2co", "gl", "ef", "fp", "cl", "1ts", "2ts", "1tm", "2tm", "tt", "fm", "hb", "tg", "1pe", "2pe", "1jo", "2jo", "3jo", "jd", "ap"]
	livro = random.choice(lista)
	#print(livro)



	r = requests.get("https://bibleapi.co/api/books/" + livro)
	text = json.loads(r.text)
	capitulos = text["chapters"]
	#print("quantidade de cap: " + str(capitulos))
	cap = random.randrange(int(capitulos))

	#print("cap: " + str(cap+1))

	if int(cap) == int(capitulos):
		cap = cap-1

	req = requests.get("https://bibleapi.co/api/verses/nvi/" + livro + "/" + str(cap+1))
	texto = json.loads(req.text)
	versiculos = texto["chapter"]["verses"]
	#print("versiculos: " + str(versiculos))
	postagem = random.randrange(int(versiculos))
	if int(postagem) == int(versiculos):
		postagem = postagem-1


	ureq = requests.get("https://bibleapi.co/api/verses/nvi/" + livro + "/" + str(cap+1) + "/" + str(postagem+1))
	textof = json.loads(ureq.text)
	textopost = textof["text"]
	#print(textof)
	book = textof["book"]["name"]
	#print(book)
	chap = str(cap+1)
	vers = str(postagem+1)



	api.update_status(f"{book}: capítulo {chap}: versículo {vers}: {textopost}")

	time.sleep(1800)
