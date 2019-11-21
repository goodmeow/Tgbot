import threading

from nana import BASE, SESSION
from sqlalchemy import Column, String, UnicodeText, Boolean, Integer


class MyChats(BASE):
	__tablename__ = "my_chats"
	chat_id = Column(String(14), primary_key=True)
	chat_name = Column(UnicodeText, nullable=False)
	chat_username = Column(UnicodeText)

	def __init__(self, chat_id, chat_name, chat_username):
		self.chat_id = str(chat_id)
		self.chat_name = chat_name
		self.chat_username = chat_username

	def __repr__(self):
		return "<Chat {} ({})>".format(self.chat_name, self.chat_id)

class MyChatsAdmin(BASE):
	__tablename__ = "my_chats_admin"
	chat_id = Column(String(14), primary_key=True)
	chat_name = Column(UnicodeText, nullable=False)
	chat_username = Column(UnicodeText)
	chat_status = Column(UnicodeText)

	def __init__(self, chat_id, chat_name, chat_username, chat_status):
		self.chat_id = str(chat_id)
		self.chat_name = chat_name
		self.chat_username = chat_username
		self.chat_status = chat_status

	def __repr__(self):
		return "<Chat Admin {} ({})>".format(self.chat_name, self.chat_id)

MyChats.__table__.create(checkfirst=True)
MyChatsAdmin.__table__.create(checkfirst=True)


MY_ALL_CHATS = {}
MY_ALL_ADMINS = {}
MY_CHATS_CREATOR = {}
MY_CHATS_ADMINS = {}


def update_chat(chat):
	global MY_ALL_CHATS
	if chat.id in list(MY_ALL_CHATS):
		if MY_ALL_CHATS.get(chat.id) and MY_ALL_CHATS[chat.id].get('name') == chat.title and MY_ALL_CHATS[chat.id].get('username') == chat.username:
			return
	chat_db = SESSION.query(MyChats).get(str(chat.id))
	if chat_db:
		SESSION.delete(chat_db)
	chat_db = MyChats(str(chat.id), chat.title, chat.username)
	SESSION.add(chat_db)
	SESSION.commit()
	MY_ALL_CHATS[chat.id] = {"name": chat.title, "username": chat.username}

def update_chat_admin(chat, status):
	global MY_ALL_ADMINS, MY_CHATS_CREATOR, MY_CHATS_ADMINS
	if chat.id in list(MY_ALL_ADMINS):
		if MY_ALL_ADMINS.get(chat.id) and MY_ALL_ADMINS[chat.id].get('name') == chat.title and MY_ALL_ADMINS[chat.id].get('username') == chat.username:
			return
	chat_db = SESSION.query(MyChatsAdmin).get(str(chat.id))
	if chat_db:
		SESSION.delete(chat_db)
	chat_db = MyChatsAdmin(str(chat.id), chat.title, chat.username, status)
	SESSION.add(chat_db)
	SESSION.commit()
	MY_ALL_ADMINS[chat.id] = {"name": chat.title, "username": chat.username}
	if status == "creator":
		MY_CHATS_CREATOR[chat.id] = {"name": chat.title, "username": chat.username}
	if status == "administrator":
		MY_CHATS_ADMINS[chat.id] = {"name": chat.title, "username": chat.username}

def get_all_chats():
	try:
		return SESSION.query(MyChats).all()
	finally:
		SESSION.close()

def get_all_chats_admin():
	try:
		return SESSION.query(MyChatsAdmin).all()
	finally:
		SESSION.close()

def get_all_chats_creator():
	try:
		MY_CREATOR = {}
		qall = SESSION.query(MyChatsAdmin).all()
		for x in qall:
			if x.chat_status == "creator":
				MY_CREATOR[x.chat_id] = {"name": x.chat_name, "username": x.chat_username}
		return MY_CREATOR
	finally:
		SESSION.close()

def get_all_chats_admin_only():
	try:
		MY_ADMIN = {}
		qall = SESSION.query(MyChatsAdmin).all()
		for x in qall:
			if x.chat_status == "administrator":
				MY_ADMIN[x.chat_id] = {"name": x.chat_name, "username": x.chat_username}
		return MY_ADMIN
	finally:
		SESSION.close()

def __load_mychats():
	global MY_ALL_CHATS
	try:
		MY_ALL_CHATS = {}
		qall = SESSION.query(MyChats).all()
		for x in qall:
			MY_ALL_CHATS[x.chat_id] = {"name": x.chat_name, "username": x.chat_username}
	finally:
		SESSION.close()

def __load_mychats_admin():
	global MY_ALL_ADMINS, MY_CHATS_CREATOR, MY_CHATS_ADMINS
	try:
		MY_ALL_ADMINS = {}
		MY_CHATS_CREATOR = {}
		MY_CHATS_ADMINS = {}
		qall = SESSION.query(MyChatsAdmin).all()
		for x in qall:
			MY_ALL_ADMINS[x.chat_id] = {"name": x.chat_name, "username": x.chat_username}
			if x.chat_status == "creator":
				MY_CHATS_CREATOR[x.chat_id] = {"name": x.chat_name, "username": x.chat_username}
			if x.chat_status == "administrator":
				MY_CHATS_ADMINS[x.chat_id] = {"name": x.chat_name, "username": x.chat_username}
		print(MY_ALL_ADMINS)
		print(MY_CHATS_CREATOR)
		print(MY_CHATS_ADMINS)
	finally:
		SESSION.close()

__load_mychats()
__load_mychats_admin()
