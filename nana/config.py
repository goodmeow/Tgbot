# Buat file config.py baru dalam dir dan impor yang sama, kemudian perpanjang kelas ini.
class Config(object):
	LOGGER = True
	
	# Must be filled!
	# Register here: https://my.telegram.org/apps
	api_id = "905926"
	api_hash = "2ba1b0f83a0d0b9c8a6568c541272cf7"
	DATABASE_URL = "postgres://username:password@localhost:5432/database" # Your database URL

	# Version
	lang_code = "en" # Your language code
	device_model = "PC" # Device model
	system_version = "Linux" # OS system type

	# Use real bot for Assistant
	# Pass False if you dont want
	ASSISTANT_BOT = False
	ASSISTANT_BOT_TOKEN = ""

	# Required for some features
	AdminSettings = [242853719] # Insert int id, Add someone so they can access your assistant, leave it blank if you dont want!
	Command = ["!", "."] # Insert command prefix, if you insert "!" then you can do !ping
	# WORKER must be int (number)
	NANA_WORKER = 8
	ASSISTANT_WORKER = 2
	# If True, send notification to user if Official branch has new update after running bot
	REMINDER_UPDATE = True

	# APIs token
	thumbnail_API = "" # Register free here: https://thumbnail.ws/
	screenshotlayer_API = "" # Register free here: https://screenshotlayer.com/

	# Load or no load plugins
	# userbot
	USERBOT_LOAD = []
	USERBOT_NOLOAD = []
	# manager bot
	ASSISTANT_LOAD = []
	ASSISTANT_NOLOAD = []

	# Fill this if you want to login using session code, else leave it blank
	USERBOT_SESSION = "BQCjBKk7EinpGdUKxgmqwJwMwZCjHbAdURTyy3Pzhifn44Xacg1-M2_q596gw4OytOzpUlGkwkUXdYkAsl_TdaeeYz_eebEC-hJwAovBNpFBmIXlPk97qs2OegqTlzXWNHutsz9L6cjWmSQFtlShO8e3T10Yn8NAkAv-7PBqY3-VhcKpea93HglNkyl3W2WBjrpOk8rwuGDmVLypGPRJJKKhGju5v4jVUx-VJas4x-thzRgAeZ_TF9qG1xPBjEOHebSv-qKOGZef5-Lr-s0LoCQEyMgORtpNQnwgHDeSxVx5YbyJ8Ihe2EuO9fRHmY797J7VvHqiTcJGn2yWt2pTxOVaDnmnVwA"
	ASSISTANT_SESSION = ""

	# Pass True if you want to use test mode
	TEST_MODE = False
	TEST_DEVELOP = False

class Production(Config):
	LOGGER = False


class Development(Config):
	LOGGER = False
