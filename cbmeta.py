def ListImdb(): #352
	AddDir("Reload" , "", 40, isFolder=False)
	file = OpenURL("http://cbplay.000webhostapp.com/imdb/imdb.txt")
	chList = json.loads(file)
	#chList = common.ReadList(file)
	#chList = sorted(chList, key=lambda k: k['nome'], reverse=False)
	i = 0
	#ST(chList)
	for channel in reversed(chList):
		if i == 3: break
		try:
			mm = mg.get_tmdb_details(tmdb_id=channel["id"], title="", year="", media_type="movies", manual_select=False, ignore_cache=False)
			mm['tagline'] = mm['genre']
			#ST(mm)
			#AddDir(mm['title'] + " / " + channel["name"].encode("utf-8"), channel["url"].encode("utf-8"), 96, "", "", isFolder=False, IsPlayable=True, background=channel["name"].encode("utf-8"), metah=mm, DL="["+str(mm['rating'])+"]", index = i)
			#AddDir(channel["nome"] + " (" + channel["ano"]+")", channel["url"].encode("utf-8"), 96, "", "", isFolder=False, IsPlayable=True, background=channel["name"].encode("utf-8"), metah=mm, DL="["+str(mm['rating'])+"]", index = i)
			#mm['title'] = unquote(mm['title'])
			AddDir(mm['title'] + " (" + str(channel["ano"])+")", channel["url"], 96, "", "", isFolder=False, IsPlayable=True, background=channel["name"], metah=mm, index = i)
		except:
			pass
		i += 1
