import time
import math
import os

from nana import app, setbot, Command

from pyrogram import Filters
from gsearch.googlesearch import search


__MODULE__ = "Search"
__HELP__ = """
Search from search engine.

──「 **Google search** 」──
-> `google`
Search somethings with google search engine.
Since google restirect fast search or bot detection, it will failing for sometimes.
"""

@app.on_message(Filters.user("self") & Filters.command(["google"], Command))
async def google_search(client, message):
	if len(message.text.split()) == 1:
		await message.edit("Usage: `google how to search from google`")
		return
	text = message.text.split(None, 1)[1]
	results = search(text)
	teks = "<b>Search results from</b> <code>{}</code>\n".format(text)
	if results == []:
		await message.edit("Please try again later:\n`{}`".format(text), parse_mode="markdown")
		return
	for x in range(len(results)):
		teks += '<b>{}.</b> <a href="{}">{}</a>\n'.format(x+1, results[x][1], results[x][0])
	await message.edit(teks, parse_mode="html", disable_web_page_preview=True)
