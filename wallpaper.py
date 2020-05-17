import praw
import requests
import urllib
import random
import os

save_path = "/mnt/2ADAC21CDAC1E463/Others/Wallpapers/"

def Reddit():
	# Logging in reddit
	reddit = praw.Reddit(client_id=os.environ.get("reddit_client_id"),
			     client_secret=os.environ.get("reddit_client_secret"),
			     username=os.environ.get("reddit_user"),
			     password=os.environ.get("reddit_pass"),
			     user_agent=os.environ.get("reddit_user"))

	# Getting The Image
	print("Finding A Wallpaper...")
	subs = ["earthporn", "CityPorn", "SpacePorn"]
	subreddit = reddit.subreddit(random.choice(subs))
	posts_limit = 100
	hot_earth=subreddit.hot(limit=posts_limit)
	posts = []
	for post in hot_earth:
		url = post.url
		posts.append(url)

	# Storing The Image
	file = posts[random.randint(1, posts_limit)]
	name = random.randint(1, 100000)
	photos_path = save_path + str(name) + "." +file.split(".")[-1]
	print("Downloading The Wallpaper...")
	urllib.request.urlretrieve(file, photos_path)

	current_wall = save_path + "/Current/current" + "." + photos_path.split(".")[-1]
	command = "cp " + photos_path + " " + current_wall
	os.system(command)

	# Setting this image as the wallpaper
	set_wall = "gsettings set org.gnome.desktop.background picture-uri file://" + current_wall
	os.system(set_wall)
	print("Done")

def offline():
	print("Finding A Wallpaper ...")
	pics_path = "/mnt/2ADAC21CDAC1E463/Pics/Wallpapers Screensavers/Walls"
	os.chdir(pics_path)
	all_pics = os.listdir()
	pic = f'"{random.choice(all_pics)}"'

	current_wall = (save_path + "Current/current" + "." + pic.split(".")[-1])[:-1]
	command = "cp " + pic + " " + current_wall
	print(current_wall, command)
	os.system(command)

	set_wall = "gsettings set org.gnome.desktop.background picture-uri file://" + current_wall
	os.system(set_wall)
	print("Done")

def choose():
	choice = input("Where Do You Want Your Wallpaper From? \n1)Reddit\n2)Offline Pics\n")
	if choice == "1":
		try:
			Reddit()
		except:
			print("No Internet Connection Available\nTry Again")
	elif choice == "2":
		offline()
	else:
		print("Invalid Select Again")
		choose()

choose()

