#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libraries
from requests import post

# Variables
SUCCESS = "[+]"
PROMPT = "[*]"
ERROR = "[-]"
INFO = "[?]"

def register(email, username, password):
	try:
		response = post("https://spclient.wg.spotify.com/signup/public/v1/account", headers={
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.257",
			"Connection": "close"
		}, data={
			"key": "a1e486e2729f46d6bb368d6b2bcda326",
			"displayname": username,
			"password_repeat": password,
			"password": password,
			"username": username,
			"birth_year": "2000",
			"birth_month": "07",
			"birth_day": "21",
			"gender": "male",
			"email": email,
			"iagree": "1",
		}, timeout=5).json()

		if (response["status"] == 1):
			print("%s Successfully registered @%s...\n\nEmail: %s\nUsername: %s\nPassword: %s" % (SUCCESS, username, email, username, password))
		else:
			print(response["errors"])
	except:
		pass

def getInput(prompt):
    print(prompt, end="")
    return input()

if __name__ == "__main__":
	try:
		print("%s Removal's Spotify Username Register | Version 1.0\n" % SUCCESS)

		email = input("%s Email: " % PROMPT)
		username = input("%s Username: " % PROMPT)
		password = input("%s Password: " % PROMPT)
		print("")

		register(email, username, password)
	except:
		pass