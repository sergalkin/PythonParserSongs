import os
import re
import string

class SongNameFixer(object):

	# Список слов-паразитов от сайтов для скачивания музыки
	keyWatermarks = [
		'myzuka.org', 
		'myzuka.ru', 
		'Bonus Track', 
		'с сайта www.ololo.fm', 
		'www.ololo.fm', 
		'NaitiMP3.ru', 
		'get-tune.net',
		'Bonus Track',
		'mp3davalka.org',
		'muzofon.com',
		'youtubeconvert.cc',
		'mp3poisk.net',
		'Official Audio',
		'Official Music Video',
		'Music video',
		'OST',
		'zaycev.net',
		'Original Version',
		'audiopoisk.com',
		'Full',
		'Post-Hardcore.COM',
		'zvukoff.ru',
		'mixpromo.net',
		'mp3type.ru',
		'mp3.shmidt.net',
		'www.esdonkey.com',
		'naitimp3.ru',
		'mp3freex.com',
		'Album version',
		'mp3.cc',
		'Radio Edit',
		'Album Edit',
		'Demo Version',
		'MusVid.net',
		'FVOst.net',
		'Original PV',
		'mp3davalka',
		'LYRICS',
		'savemp3.net',
		'Official Lyric Video'
	]

	# Список аудио форматов
	audioFormats = [
		'.AAC',	
		'.FLAC', 
		'.MP3' , 
		'.OGG', 
		'.MP4', 
		'.WAV', 
		'.WMA', 
		'.LA', 
		'.M4A', 
		'.MID',
		'.MIDI'
	]

	def __init__(self, dir_path=None): # Конструктор с указанием пути к файлам
		if(dir_path != None):
			self.dir_path = dir_path
			os.chdir(dir_path)


	def stripAll(self): # Вызов всех методов для чистки имени файла
		self.__DeleteParasites()
		self.__stripNumbersInMiddle()

	def audioFormatChecker(self, file_ext):
		if(file_ext.upper() in self.audioFormats):
			return True
		return False

	def __DeleteParasites(self):
		for f in os.listdir():
			file_name, file_ext = os.path.splitext(f)
			if(self.audioFormatChecker(file_ext)):
				for word in self.keyWatermarks:
					file_name = re.sub(word, '',file_name)
				file_name = re.sub(r'(&quot;)|(&lt;)|(&gt;)|(&amp;)','',file_name) # Удаление html тега
				file_name = re.sub(r'^(\_)|(\_+$)','',file_name) # Удаление нижних подчеркиваний вначале и конце строки 
				file_name = re.sub(r'^(\d+\s+\-+\s+)|^(\d+\.)|^(\d+-)|^(\d+\s+)','',file_name) # Удаление цифр в начале строки
				file_name = re.sub(r'(\(\))|(\[\])|(\(\d+\s+kbps\))','',file_name) # Удаление пустых скобок и Киллобайтов
				file_name = re.sub(r'[^(\w+)|\!|\(\)|\[\]\s.-]','',file_name) # Удаление черепов и т.п.
				file_name = re.sub(r'(OP+\d+)|(^\d+\_|\_)',' ', file_name) # Удаление нижних подчеркиваний
				file_name = re.sub(r'(\s{2,})', ' ', file_name) # Удаление 2ух и более пробелов
				file_name = re.sub(r'(\-{2,})', '-', file_name) # Удаление 2ух и более -
				file_name = re.sub(r'^(\-)|(\-$)','', file_name) # Удаление - в начале строки и конце строки
				file_name = file_name.strip()
				new_name = '{}{}'.format(file_name,file_ext)
				try:
					os.rename(f,new_name)
				except FileExistsError as e:
					os.remove(f)
			
	def __stripNumbersInMiddle(self): # Удаление цифр в середине песни
		for f in os.listdir():
			file_name, file_ext = os.path.splitext(f)
			try:
				f_title = file_name.split('-')
				i = 0
				lenBefore = len(f_title)
				while i < lenBefore:
					try:
						if(isinstance(int(f_title[i]),int)):
							del f_title[i]
					except Exception as e:
						pass
					i += 1
				lenAfter = len(f_title)
				f_title = '-'.join(f_title[0:lenAfter])
				new_name = '{}{}'.format(f_title,file_ext)
				try:
					os.rename(f,new_name)
				except FileExistsError as e:
					os.remove(f)

			except Exception as e:
				pass
