def ListSeason(url,background): #532
	lista = CRsession("https://api.crunchyroll.com/list_collections.0.json?series_id="+url,crsession)
	#ST(lista)
	mmm = mg.get_tvshow_details(title="",tmdb_id=background, ignore_cache=MUcache, lang=MUlang)
	collection = []
	reseason = str(lista['data'])
	for l in lista['data']:
		#if not "'season': '1'" in str(lista['data']) and "'season': '0'" in reseason and not "Dub" in l['name']:
		if not "'season': '1'" in str(lista['data']) and "'season': '0'" in reseason and not "Dub" in l['name']:
			collection.append({"1" : l['collection_id'] })
			#collection.append( { collection[1] : l['collection_id'] } )
		elif not "Dub" in l['name']:
			collection.append({l['season'] : l['collection_id'] })
			#collection[l['season']] = l['collection_id']
	#ST(collection)
	for s in collection:
		for season in s:
			metasea=mergedicts(mmm[-1],mmm[int(season)])
			AddDir2(s[season], url, 533, "", "", info=s[season], isFolder=True, background=season, metah=metasea)
	AddDir("---------- Autoplay ----------" , "", 40, isFolder=False)
	for s in collection:
		for season in s:
			metasea=mergedicts(mmm[-1],mmm[int(season)])
			metasea['mediatype'] = "episode"
			AddDir2(metasea['name'], url, 535, "", "", info=s[season], isFolder=False, IsPlayable=True, background=season, metah=metasea)
