import telebot
from telebot import types

import requests
from bs4 import BeautifulSoup

import re
import os

import schedule
import time
import threading 
#from multiprocessing import Process
#import threading
client = telebot.TeleBot('1400292700:AAEMez63aoNdJVe6jWaJJ9am9Yl35MsjxH8')

#1 клава
keyboard = types.ReplyKeyboardMarkup()
keyboard.row('Что такое COVID-19?', '📊 Статистика')
keyboard.row('📝 Пройти тест')
keyboard.row('🔕 Отписаться от рассылки')
##
#2 клава
keyboard1 = types.ReplyKeyboardMarkup()
keyboard1.row('◀️ Назад','⚠️ Основные симптомы', '❕ Профилактика')
keyboard1.row('😩 Как справиться со стрессом','😰 Как помочь ребёнку справиться со стрессом')
keyboard1.row('✅ Больше информации')
##
#3 клава
keyboardRegion = types.ReplyKeyboardMarkup(True)
keyboardRegion.row('◀️ Назад','Киев')
keyboardRegion.row('Винницкая область','Волынская область')
keyboardRegion.row('Днепропетровская область','Донецкая область')
keyboardRegion.row('Житомирская область','Закарпатская область')
keyboardRegion.row('Запорожская область','Ивано-Франковская область')
keyboardRegion.row('Киевская область','Кировоградская область')
keyboardRegion.row('Луганская область','Львовская область')
keyboardRegion.row('Николаевская область','Одесская область')
keyboardRegion.row('Полтавская область','Ровенская область')
keyboardRegion.row('Сумская область','Тернопольская область')
keyboardRegion.row('Харьковская область','Херсонская область')
keyboardRegion.row('Хмельницкая область','Черкасская область')
keyboardRegion.row('Черниговская область','Черновицкая область')

##
##
keyboardYN1 = types.ReplyKeyboardMarkup() 
keyboardYN1.row('Да','Нет')


keyboardYN2 = types.ReplyKeyboardMarkup() 
keyboardYN2.row('Да','Нет')

keyboardYN3 = types.ReplyKeyboardMarkup() 
keyboardYN3.row('Да','Нет')


keyboardYN4 = types.ReplyKeyboardMarkup() 
keyboardYN4.row('Да','Нет')


keyboardYN5 = types.ReplyKeyboardMarkup() 
keyboardYN5.row('Да','Нет')

keyboardExit = types.ReplyKeyboardMarkup() 
keyboardExit.row('◀️ Назад')



#\\\\\\Парсинг статистики
url = 'https://index.minfin.com.ua/ua/reference/coronavirus/ukraine/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

####\\\Данные по стране
GotWell = soup.find_all('td', class_='bg-grey')
CasesPerDay = soup.find_all('small', class_='gold')
DeadPerDay = soup.find_all('small', class_ ='brown')
###Время изменения данных
TimeEdit = soup.find('li', text=re.compile('відомості '))
timeE = str(TimeEdit.text)
timeE = timeE.replace('відомості на ','Данные на ')
timeN = 'Данные на 9:00 GMT'
####
###//Данные по реогинам
RegionCases = soup.find_all('td', class_='blank larger')
NewRegionCases = soup.find_all('small', class_='gold')
AlreadyDeadRegion = soup.find_all('td', class_='blank')
NewAlreadyDeadRegion = soup.find_all('small', class_='brown')
GotWellRegion = soup.find_all('td', class_='blank')
NewGotWellRegion = soup.find_all('small', class_='green')


for i in range(len(GotWell)):
	if i == 5:
		#print(quotes[i].text)
		GotWellVariable = GotWell[i].text
		GotWellVariable = str(GotWellVariable).replace('+','')
	if i == 1:
		CasesInUkraineVariable = GotWell[i].text
	if i == 3:
		AlreadyDeadVariable = GotWell[i].text
	if i == 6:
		NewGotWellVariable = GotWell[i].text
		NewGotWellVariable = str(NewGotWellVariable).replace('+','')
for i in range(len(DeadPerDay)):
	if i == 25:
		#print(quotes[i].text)
		DeadPerDayVariable = DeadPerDay[i].text
		DeadPerDayVariable = str(DeadPerDayVariable).replace('+','')
for i in range(len(CasesPerDay)):
	if i == 25:
		#print(quotes[i].text)
		NewCasesPerDayVariable = CasesPerDay[i].text
		NewCasesPerDayVariable = str(NewCasesPerDayVariable).replace('+','')
for i in range(len(RegionCases)):
	if i == 0:
		VinnytsaRegionCases = RegionCases[i].text
	if i == 1:
		VolinRegionCases = RegionCases[i].text
	if i == 2:
		DnepropetrovskRegionCases = RegionCases[i].text
	if i == 3:
		DonetskRegionCases = RegionCases[i].text
	if i == 4:
		ZhitomirRegionCases = RegionCases[i].text
	if i == 5:
		ZakarpatieRegionCases = RegionCases[i].text
	if i == 6:
		ZaporozhieRegionCases = RegionCases[i].text 
	if i == 7:
		IvanoFrankovskRegionCases = RegionCases[i].text
	if i == 8:
		KievOblRegionCases = RegionCases[i].text
	if i == 9:
		KirovogradRegionCases = RegionCases[i].text 
	if i == 10:
		LuganskRegionCases = RegionCases[i].text
	if i == 11:
		LvivRegionCases = RegionCases[i].text
	if i == 12:
		NikolaevRegionCases = RegionCases[i].text
	if i == 13:
		OdessaRegionCases = RegionCases[i].text
	if i == 14:
		PoltavaRegionCases = RegionCases[i].text
	if i == 15:
		RovnoRegionCases = RegionCases[i].text
	if i == 16:
		SumiRegionCases = RegionCases[i].text
	if i == 17:
		TernopilRegionCases = RegionCases[i].text
	if i == 18:
		KharkovRegionCases = RegionCases[i].text
	if i == 19:
		ChersonRegionCases = RegionCases[i].text
	if i == 20:
		ChmelnitskRegionCases = RegionCases[i].text
	if i == 21:
		CherkasiRegionCases = RegionCases[i].text
	if i == 22:
		ChernovciRegionCases = RegionCases[i].text
	if i == 23:
		ChernigovRegionCases = RegionCases[i].text
	if i == 24:
		KievRegionCases = RegionCases[i].text
for i in range(len(NewRegionCases)):
		if i == 0:
			NewVinnytsaRegionCases = NewRegionCases[i].text
			NewVinnytsaRegionCases = str(NewVinnytsaRegionCases).replace('+','')
		if i == 1:
			NewVolinRegionCases = NewRegionCases[i].text
			NewVolinRegionCases = str(NewVolinRegionCases).replace('+','')
		if i == 2:
			NewDnepropetrovskRegionCases = NewRegionCases[i].text
			NewDnepropetrovskRegionCases = str(NewDnepropetrovskRegionCases).replace('+','')
		if i == 3:
			NewDonetskRegionCases = NewRegionCases[i].text
			NewDonetskRegionCases = str(NewDonetskRegionCases).replace('+','')
		if i == 4:
			NewZhitomirRegionCases = NewRegionCases[i].text
			NewZhitomirRegionCases = str(NewZhitomirRegionCases).replace('+','')
		if i == 5:
			NewZakarpatieRegionCases = NewRegionCases[i].text
			NewZakarpatieRegionCases = str(NewZakarpatieRegionCases).replace('+','')
		if i == 6:
			NewZaporozhieRegionCases = NewRegionCases[i].text   
			NewZaporozhieRegionCases = str(NewZaporozhieRegionCases).replace('+','')
		if i == 7:
			NewIvanoFrankovskRegionCases = NewRegionCases[i].text
			NewIvanoFrankovskRegionCases = str(NewIvanoFrankovskRegionCases).replace('+','')
		if i == 8:
			NewKievOblRegionCases = NewRegionCases[i].text
			NewKievOblRegionCases = str(NewKievOblRegionCases).replace('+','')
		if i == 9:
			NewKirovogradRegionCases = NewRegionCases[i].text   
			NewKirovogradRegionCases = str(NewKirovogradRegionCases).replace('+','')
		if i == 10:
			NewLuganskRegionCases = NewRegionCases[i].text
			NewLuganskRegionCases = str(NewLuganskRegionCases).replace('+','')
		if i == 11:
			NewLvivRegionCases = NewRegionCases[i].text
			NewLvivRegionCases = str(NewLvivRegionCases).replace('+','')
		if i == 12:
			NewNikolaevRegionCases = NewRegionCases[i].text
			NewNikolaevRegionCases = str(NewNikolaevRegionCases).replace('+','')
		if i == 13:
			NewOdessaRegionCases = NewRegionCases[i].text
			NewOdessaRegionCases = str(NewOdessaRegionCases).replace('+','')
		if i == 14:
			NewPoltavaRegionCases = NewRegionCases[i].text
			NewPoltavaRegionCases = str(NewPoltavaRegionCases).replace('+','')
		if i == 15:
			NewRovnoRegionCases = NewRegionCases[i].text
			NewRovnoRegionCases = str(NewRovnoRegionCases).replace('+','')
		if i == 16:
			NewSumiRegionCases = NewRegionCases[i].text
			NewSumiRegionCases = str(NewSumiRegionCases).replace('+','')
		if i == 17:
			NewTernopilRegionCases = NewRegionCases[i].text
			NewTernopilRegionCases = str(NewTernopilRegionCases).replace('+','')
		if i == 18:
			NewKharkovRegionCases = NewRegionCases[i].text
			NewKharkovRegionCases = str(NewKharkovRegionCases).replace('+','')
		if i == 19:
			NewChersonRegionCases = NewRegionCases[i].text
			NewChersonRegionCases = str(NewChersonRegionCases).replace('+','')
		if i == 20:
			NewChmelnitskRegionCases = NewRegionCases[i].text
			NewChmelnitskRegionCases = str(NewChmelnitskRegionCases).replace('+','')
		if i == 21:
			NewCherkasiRegionCases = NewRegionCases[i].text
			NewCherkasiRegionCases = str(NewCherkasiRegionCases).replace('+','')
		if i == 22:
			NewChernovciRegionCases = NewRegionCases[i].text
			NewChernovciRegionCases = str(NewChernovciRegionCases).replace('+','')
		if i == 23:
			NewChernigovRegionCases = NewRegionCases[i].text
			NewChernigovRegionCases = str(NewChernigovRegionCases).replace('+','')
		if i == 24:
			NewKievRegionCases = NewRegionCases[i].text
			NewKievRegionCases = str(NewKievRegionCases).replace('+','')
for i in range(len(AlreadyDeadRegion)):
	if i == 2:
		VinnytsaAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 9:
		VolinAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 16:
		DnepropetrovskAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 23:
		DonetskAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 30:
		ZhitomirAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 37:
		ZakarpatieAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 44:
		ZaporozhieAlreadyDeadRegion = AlreadyDeadRegion[i].text 
	if i == 51:
		IvanoFrankovskAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 58:
		KievOblAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 65:
		KirovogradAlreadyDeadRegion = AlreadyDeadRegion[i].text 
	if i == 72:
		LuganskAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 79:
		LvivAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 86:
		NikolaevAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 93:
		OdessaAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 100:
		PoltavaAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 107:
		RovnoAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 114:
		SumiAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 121:
		TernopilAlreadyDeadRegion  = AlreadyDeadRegion[i].text
	if i == 128:
		KharkovAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 135:
		ChersonAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 142:
		ChmelnitskAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 149:
		CherkasiAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 156:
		ChernovciAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 163:
		ChernigovAlreadyDeadRegion = AlreadyDeadRegion[i].text
	if i == 170:
		KievAlreadyDeadRegion = AlreadyDeadRegion[i].text
for i in range(len(NewAlreadyDeadRegion)):
	if i == 0:
		NewVinnytsaAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewVinnytsaAlreadyDeadRegion = str(NewVinnytsaAlreadyDeadRegion).replace('+','')
	if i == 1:
		NewVolinAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewVolinAlreadyDeadRegion= str(NewVolinAlreadyDeadRegion).replace('+','')
	if i == 2:
		NewDnepropetrovskAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewDnepropetrovskAlreadyDeadRegion= str(NewDnepropetrovskAlreadyDeadRegion).replace('+','') 
	if i == 3:
		NewDonetskAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewDonetskAlreadyDeadRegion= str(NewDonetskAlreadyDeadRegion).replace('+','')
	if i == 4:
		NewZhitomirAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewZhitomirAlreadyDeadRegion= str(NewZhitomirAlreadyDeadRegion).replace('+','')
	if i == 5:
		NewZakarpatieAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewZakarpatieAlreadyDeadRegion= str(NewZakarpatieAlreadyDeadRegion).replace('+','')
	if i == 6:
		NewZaporozhieAlreadyDeadRegion = NewAlreadyDeadRegion[i].text   
		NewZaporozhieAlreadyDeadRegion= str(NewZaporozhieAlreadyDeadRegion).replace('+','')
	if i == 7:
		NewIvanoFrankovskAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewIvanoFrankovskAlreadyDeadRegion= str(NewIvanoFrankovskAlreadyDeadRegion).replace('+','')
	if i == 8:
		NewKievOblAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewKievOblAlreadyDeadRegion= str(NewKievOblAlreadyDeadRegion).replace('+','')
	if i == 9:
		NewKirovogradAlreadyDeadRegion = NewAlreadyDeadRegion[i].text   
		NewKirovogradAlreadyDeadRegion= str(NewKirovogradAlreadyDeadRegion).replace('+','')
	if i == 10:
		NewLuganskAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewLuganskAlreadyDeadRegion= str(NewLuganskAlreadyDeadRegion).replace('+','')
	if i == 11:
		NewLvivAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewLvivAlreadyDeadRegion= str(NewLvivAlreadyDeadRegion).replace('+','')
	if i == 12:
		NewNikolaevAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewNikolaevAlreadyDeadRegion= str(NewNikolaevAlreadyDeadRegion).replace('+','')
	if i == 13:
		NewOdessaAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewOdessaAlreadyDeadRegion= str(NewOdessaAlreadyDeadRegion).replace('+','')
	if i == 14:
		NewPoltavaAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewPoltavaAlreadyDeadRegion= str(NewPoltavaAlreadyDeadRegion).replace('+','')
	if i == 15:
		NewRovnoAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewRovnoAlreadyDeadRegion= str(NewRovnoAlreadyDeadRegion).replace('+','')
	if i == 16:
		NewSumiAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewSumiAlreadyDeadRegion= str(NewSumiAlreadyDeadRegion).replace('+','')
	if i == 17:
		NewTernopilAlreadyDeadRegion  = NewAlreadyDeadRegion[i].text
		NewTernopilAlreadyDeadRegion= str(NewTernopilAlreadyDeadRegion).replace('+','')
	if i == 18:
		NewKharkovAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewKharkovAlreadyDeadRegion= str(NewKharkovAlreadyDeadRegion).replace('+','')
	if i == 19:
		NewChersonAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewChersonAlreadyDeadRegion= str(NewChersonAlreadyDeadRegion).replace('+','')
	if i == 20:
		NewChmelnitskAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewChmelnitskAlreadyDeadRegion= str(NewChmelnitskAlreadyDeadRegion).replace('+','')
	if i == 21:
		NewCherkasiAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewCherkasiAlreadyDeadRegion= str(NewCherkasiAlreadyDeadRegion).replace('+','')
	if i == 22:
		NewChernovciAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewChernovciAlreadyDeadRegion= str(NewChernovciAlreadyDeadRegion).replace('+','')

	if i == 23:
		NewChernigovAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewChernigovAlreadyDeadRegion= str(NewChernigovAlreadyDeadRegion).replace('+','')
	if i == 24:
		NewKievAlreadyDeadRegion = NewAlreadyDeadRegion[i].text
		NewKievAlreadyDeadRegion= str(NewKievAlreadyDeadRegion).replace('+','')
for i in range(len(GotWellRegion)):
	if i == 4:
		VinnytsaGotWellRegion = GotWellRegion[i].text
	if i == 11:
		VolinGotWellRegion = GotWellRegion[i].text
	if i == 18:
		DnepropetrovskGotWellRegion = GotWellRegion[i].text
	if i == 25:
		DonetskGotWellRegion = GotWellRegion[i].text
	if i == 32:
		ZhitomirGotWellRegion = GotWellRegion[i].text
	if i == 39:
		ZakarpatieGotWellRegion = GotWellRegion[i].text
	if i == 46:
		ZaporozhieGotWellRegion = GotWellRegion[i].text 
	if i == 53:
		IvanoFrankovskGotWellRegion = GotWellRegion[i].text
	if i == 60:
		KievOblGotWellRegion = GotWellRegion[i].text
	if i == 67:
		KirovogradGotWellRegion = GotWellRegion[i].text 
	if i == 74:
		LuganskGotWellRegion = GotWellRegion[i].text
	if i == 81:
		LvivGotWellRegion = GotWellRegion[i].text
	if i == 88:
		NikolaevGotWellRegion = GotWellRegion[i].text
	if i == 95:
		OdessaGotWellRegion = GotWellRegion[i].text
	if i == 102:
		PoltavaGotWellRegion = GotWellRegion[i].text
	if i == 109:
		RovnoGotWellRegion = GotWellRegion[i].text
	if i == 116:
		SumiGotWellRegion = GotWellRegion[i].text
	if i == 123:
		TernopilGotWellRegion  = GotWellRegion[i].text
	if i == 130:
		KharkovGotWellRegion = GotWellRegion[i].text
	if i == 137:
		ChersonGotWellRegion = GotWellRegion[i].text
	if i == 144:
		ChmelnitskGotWellRegion = GotWellRegion[i].text
	if i == 151:
		CherkasiGotWellRegion = GotWellRegion[i].text
	if i == 165:
		ChernovciGotWellRegion = GotWellRegion[i].text
	if i == 158:
		ChernigovGotWellRegion = GotWellRegion[i].text
	if i == 172:
		KievGotWellRegion = GotWellRegion[i].text
for i in range(len(NewGotWellRegion)):
	if i == 0:
		NewVinnytsaGotWellRegion = NewGotWellRegion[i].text
		NewVinnytsaGotWellRegion = str(NewVinnytsaGotWellRegion).replace('+','')
	if i == 1:
		NewVolinGotWellRegion = NewGotWellRegion[i].text
		NewVolinGotWellRegion = str(NewVolinGotWellRegion).replace('+','')
	if i == 2:
		NewDnepropetrovskGotWellRegion = NewGotWellRegion[i].text
		NewDnepropetrovskGotWellRegion = str(NewDnepropetrovskGotWellRegion).replace('+','')
	if i == 3:
		NewDonetskGotWellRegion = NewGotWellRegion[i].text
		NewDonetskGotWellRegion = str(NewDonetskGotWellRegion).replace('+','')
	if i == 4:
		NewZhitomirGotWellRegion = NewGotWellRegion[i].text
		NewZhitomirGotWellRegion = str(NewZhitomirGotWellRegion).replace('+','')
	if i == 5:
		NewZakarpatieGotWellRegion = NewGotWellRegion[i].text
		NewZakarpatieGotWellRegion = str(NewZakarpatieGotWellRegion).replace('+','')
	if i == 6:
		NewZaporozhieGotWellRegion = NewGotWellRegion[i].text   
		NewZaporozhieGotWellRegion = str(NewZaporozhieGotWellRegion).replace('+','')
	if i == 7:
		NewIvanoFrankovskGotWellRegion = NewGotWellRegion[i].text
		NewIvanoFrankovskGotWellRegion = str(NewIvanoFrankovskGotWellRegion).replace('+','')
	if i == 8:
		NewKievOblGotWellRegion = NewGotWellRegion[i].text
		NewKievOblGotWellRegion = str(NewKievOblGotWellRegion).replace('+','')
	if i == 9:
		NewKirovogradGotWellRegion = NewGotWellRegion[i].text   
		NewKirovogradGotWellRegion = str(NewKirovogradGotWellRegion).replace('+','')
	if i == 10:
		NewLuganskGotWellRegion = NewGotWellRegion[i].text
		NewLuganskGotWellRegion = str(NewLuganskGotWellRegion).replace('+','')
	if i == 11:
		NewLvivGotWellRegion = NewGotWellRegion[i].text
		NewLvivGotWellRegion = str(NewLvivGotWellRegion).replace('+','')
	if i == 12:
		NewNikolaevGotWellRegion = NewGotWellRegion[i].text
		NewNikolaevGotWellRegion = str(NewNikolaevGotWellRegion).replace('+','')
	if i == 13:
		NewOdessaGotWellRegion = NewGotWellRegion[i].text
		NewOdessaGotWellRegion = str(NewOdessaGotWellRegion).replace('+','')
	if i == 14:
		NewPoltavaGotWellRegion = NewGotWellRegion[i].text
		NewPoltavaGotWellRegion = str(NewPoltavaGotWellRegion).replace('+','')
	if i == 15:
		NewRovnoGotWellRegion = NewGotWellRegion[i].text
		NewRovnoGotWellRegion = str(NewRovnoGotWellRegion).replace('+','')
	if i == 16:
		NewSumiGotWellRegion = NewGotWellRegion[i].text
		NewSumiGotWellRegion = str(NewSumiGotWellRegion).replace('+','')
	if i == 17:
		NewTernopilGotWellRegion  = NewGotWellRegion[i].text
		NewTernopilGotWellRegion = str(NewTernopilGotWellRegion).replace('+','')
	if i == 18:
		NewKharkovGotWellRegion = NewGotWellRegion[i].text
		NewKharkovGotWellRegion = str(NewKharkovGotWellRegion).replace('+','')
	if i == 19:
		NewChersonGotWellRegion = NewGotWellRegion[i].text
		NewChersonGotWellRegion = str(NewChersonGotWellRegion).replace('+','')
	if i == 20:
		NewChmelnitskGotWellRegion = NewGotWellRegion[i].text
		NewChmelnitskGotWellRegion = str(NewChmelnitskGotWellRegion).replace('+','')
	if i == 21:
		NewCherkasiGotWellRegion = NewGotWellRegion[i].text
		NewCherkasiGotWellRegion = str(NewCherkasiGotWellRegion).replace('+','')
	if i == 23:
		NewChernovciGotWellRegion = NewGotWellRegion[i].text
		NewChernovciGotWellRegion = str(NewChernovciGotWellRegion).replace('+','')
	if i == 22:
		NewChernigovGotWellRegion = NewGotWellRegion[i].text
		NewChernigovGotWellRegion = str(NewChernigovGotWellRegion).replace('+','')
	if i == 24:
		NewKievGotWellRegion = NewGotWellRegion[i].text
		NewKievGotWellRegion = str(NewKievGotWellRegion).replace('+','')





@client.message_handler(commands = ['start'])
def get_bot_started(message):
		client.send_message(message.chat.id, '''*Добро пожаловать! Данный бот поможет узнать Вам больше о заболевании COVID‑19, а также предоставит актуальную статистикику от МОЗ.*
		\nЕсли бот перестал исправно функционировать - просто перезагрузите его.
			''', reply_markup = keyboard, parse_mode="Markdown")
		#user = []
		id1 = message.from_user.id

		somefile = open('database.txt', 'rt')
		users = somefile.read()
		somefile.close()
		somefile = open('database.txt', 'a')

		if str(id1) in users:
			somefile.close()
		else:           
			somefile.write('\n' + str(id1))
			somefile.close()
		
		
		
		
@client.message_handler(commands = ['help'])
def bot_support(message):
		client.send_message(message.chat.id, 'Если у Вас возникли какие-либо вопросы касательно пользования данным ботом или идеи по его улучшению - пишите @ace1nSleeve . ' + '\n' + '\n' + 'Открыт для сотрудничества.' , reply_markup = keyboard)


@client.message_handler(content_types = ['text'])
def get_text_Chto(message):
		if message.text == 'Что такое COVID-19?':
			someStep = client.send_message(message.chat.id, 'COVID-19 — заболевание, вызываемое новым коронавирусом, который называется SARS-CoV-2. ВОЗ впервые узнала об этом новом вирусе ВОЗ 31 декабря 2019 г., получив сообщение о группе случаев заболевания «вирусной пневмонией» в городе Ухане, Китайская Народная Республика.',reply_markup= keyboard1)
			client.register_next_step_handler(someStep, get_text_About)

		if message.text =='📊 Статистика':
			client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewCasesPerDayVariable)  + '\n☠️ *Новых смертей*: ' + str(DeadPerDayVariable) +'\n✅ *Выздоровело за сегодня*: ' + str(NewGotWellVariable) + '\n' +'\n📊 Всего случаев заболевания в Украине: ' + str(CasesInUkraineVariable) + '\n☠️ Умерло: ' + str(AlreadyDeadVariable) +'\n✅ Всего выздоровело: ' + str(GotWellVariable) +  '\n' + '\n⏰ ' + timeE, parse_mode="Markdown")
			someStep = client.send_message(message.chat.id, '\nВыберите область, данные по которой Вы хотите посмотреть:',reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)

		if message.text == '📝 Пройти тест':
			client.send_message(message.chat.id, '🦠 Алгоритм действий при подозрении на коронавирусную инфекцию ')
			someStep = client.send_message(message.chat.id, 'Известен ли Вам спектр симптомов COVID-19?',reply_markup= keyboardYN1)
			client.register_next_step_handler(someStep, get_text_YN1)


		if message.text == '🔔 Подписаться на рассылку':
			id1 = message.from_user.id

			somefile = open('database.txt', 'rt')
			users = somefile.read()
			somefile.close()
			somefile = open('database.txt', 'a')

			if str(id1) in users:
				somefile.close()
			else:           
				somefile.write('\n' + str(id1))
				somefile.close()

			keyboard = types.ReplyKeyboardMarkup()
			keyboard.row('Что такое COVID-19?', '📊 Статистика')
			keyboard.row('📝 Пройти тест')
			keyboard.row('🔕 Отписаться от рассылки')

			client.send_message(message.chat.id, 'Вы успешно подписались на рассылку уведомлений.Каждый день в 9:00 Вы будете получать новую информацию.',reply_markup= keyboard)

		if message.text == '🔕 Отписаться от рассылки':
			id1 = message.from_user.id


			with open("database.txt", "r") as somefile:
				lines = somefile.readlines()
			with open("database.txt", "w") as somefile:
				for line in lines:
					if line.strip("\n") != str(id1):
						somefile.write(line)

			keyboard = types.ReplyKeyboardMarkup()
			keyboard.row('Что такое COVID-19?', '📊 Статистика')
			keyboard.row('📝 Пройти тест')
			keyboard.row('🔔 Подписаться на рассылку')

			client.send_message(message.chat.id, 'Вы успешно отписались от рассылки уведомлений.',reply_markup= keyboard)


def get_text_YN1(message):
		keyboardYN1 = types.ReplyKeyboardMarkup() 
		keyboardYN1.row('Да','Нет')

		if message.text == 'Да':
			someStep = client.send_message(message.chat.id, 'Есть ли у Вас симптомы COVID‑19?',reply_markup= keyboardYN2)
			client.register_next_step_handler(someStep, get_text_YN2)

		if message.text == 'Нет':
			client.send_message(message.chat.id, '''К наиболее распространенным симптомам COVID-19 относятся:

🔸 Лихорадка
🔸 Сухой кашель
🔸 Утомляемость

К другим, менее распространенным симптомам, которые встречаются у ряда пациентов, относятся:

▫️ Утрата обоняния или вкусовых ощущений
▫️ Заложенность носа
▫️ Конъюнктивит (или покраснение глаз)
▫️ Боль в горле
▫️ Головная боль
▫️ Боль в мышцах или суставах
▫️ Различные виды высыпаний на коже
▫️ Тошнота или рвота
▫️ Диарея
▫️ Озноб или головокружение

Тяжелое течение COVID‑19 проявляется следующими симптомами:

🔻 Одышка
🔻 Потеря аппетита
🔻 Спутанность сознания
🔻 Упорные боли или ощущение сдавления грудной клетки
🔻 Высокая температура тела (выше 38°C)

К другим, менее распространенным симптомам относятся:

▪️ Раздражительность
▪️ Спутанность сознания
▪️ Снижение уровня сознания (иногда сопровождается судорогами)
▪️ Тревожность
▪️ Угнетенное состояние
▪️ Нарушения сна
▪️ Более тяжелые и редкие неврологические осложнения, такие как инсульт, воспалительное поражение мозга, делирий и поражение нервов''',reply_markup= keyboardYN2)
			someStep = client.send_message(message.chat.id, 'Есть ли у Вас симптомы COVID‑19?',reply_markup= keyboardYN2)
			client.register_next_step_handler(someStep, get_text_YN2)

def get_text_YN2(message):
		keyboardYN2 = types.ReplyKeyboardMarkup() 
		keyboardYN2.row('Да','Нет')

		if message.text == 'Да':
			client.send_message(message.chat.id, 'Оставайтесь дома на самоизоляции')
			someStep = client.send_message(message.chat.id, 'Есть ли у Вас семейный врач?',reply_markup= keyboardYN4)
			client.register_next_step_handler(someStep, get_text_YN4)

		if message.text == 'Нет':
			someStep = client.send_message(message.chat.id,'Беспокоит ли Вас ваше состояние здоровья?',reply_markup= keyboardYN3)
			client.register_next_step_handler(someStep, get_text_YN3)


def get_text_YN3(message):
		keyboardYN3 = types.ReplyKeyboardMarkup() 
		keyboardYN3.row('Да','Нет')


		if message.text == 'Да':
			someStep = client.send_message(message.chat.id, 'Диагностика других заболеваний',reply_markup= keyboardExit)
			client.register_next_step_handler(someStep, get_text_Exit)

		if message.text == 'Нет':
			someStep = client.send_message(message.chat.id,'Поздравляем,Вы здоровы!',reply_markup= keyboardExit)
			client.register_next_step_handler(someStep, get_text_Exit)

def get_text_YN4(message):
		keyboardYN4 = types.ReplyKeyboardMarkup() 
		keyboardYN4.row('Да','Нет')


		if message.text == 'Да':
			client.send_message(message.chat.id, 'Свяжитесь с семейным врачом по телефону и подробно расскажите ему о состоянии своего здоровья')
			someStep = client.send_message(message.chat.id, 'Подозревает ли ваш семейный врач наличие инфекции COVID‑19 у вас после консультации по телефону?',reply_markup= keyboardYN5)
			client.register_next_step_handler(someStep, get_text_YN5)

		if message.text == 'Нет':
			client.send_message(message.chat.id,'''Обратитесь в контакт-центр МОЗ по вопросам COVID‑19.
			\n☎️ Контакт-центр МОЗ по вопросам COVID-19: 
			0 800 60 20 19
				''')
			#someStep = 
			client.send_message(message.chat.id,'Если Вы уже связались с контакт-центром МОЗ, тогда рекомендуется выполнить следующие действия :')
			#client.register_next_step_handler(someStep, get_text_YN4)
			client.send_message(message.chat.id, 'Свяжитесь с семейным врачом по телефону и подробно расскажите ему о состоянии своего здоровья')
			someStep = client.send_message(message.chat.id, 'Подозревает ли ваш семейный врач наличие инфекции COVID‑19 у вас после консультации по телефону?',reply_markup= keyboardYN5)
			client.register_next_step_handler(someStep, get_text_YN5)


def get_text_YN5(message):
		keyboardYN5 = types.ReplyKeyboardMarkup() 
		keyboardYN5.row('Да','Нет')


		if message.text == 'Да':
			someStep = client.send_message(message.chat.id, '''
\n🚑 Семейный врач направляет мобильную бригаду для забора анализа на COVID-19 либо необходимо сдать тест на COVID-19 и ограничить любые социальные контакты.
\n👨‍👩‍👦 Необходимо строго соблюдать правила самоизоляции контактных членов семьи.
\n💧 Придерживайтесь обильного питьевого режима.
\n🩸 Контролируйте уровень насыщения крови кислородом(пульсоксиметрия), SpO2 > 95%.
\n🌡 При повышении температури, появлении кашля и затруднении дыхания,как можно быстрее обратитесь за медицинской помощью.
				''', reply_markup= keyboardExit)
			client.register_next_step_handler(someStep, get_text_Exit)

		if message.text == 'Нет':
			someStep = client.send_message(message.chat.id, 'Диагностика других заболеваний',reply_markup= keyboardExit)
			client.register_next_step_handler(someStep, get_text_Exit)




def get_text_Exit(message):
		keyboardExit = types.ReplyKeyboardMarkup() 
		keyboardExit.row('◀️ Назад')

		if message.text == '◀️ Назад':
			id1 = message.from_user.id

			somefile = open('database.txt', 'rt')
			users = somefile.read()
			somefile.close()
			somefile = open('database.txt', 'a')

			if str(id1) not in users:
				keyboard = types.ReplyKeyboardMarkup()
				keyboard.row('Что такое COVID-19?', '📊 Статистика')
				keyboard.row('📝 Пройти тест')
				keyboard.row('🔔 Подписаться на рассылку')
				somefile.close()
			else:           
				keyboard = types.ReplyKeyboardMarkup()
				keyboard.row('Что такое COVID-19?', '📊 Статистика')
				keyboard.row('📝 Пройти тест')
				keyboard.row('🔕 Отписаться от рассылки')
				somefile.close()



			someStep = client.send_message(message.chat.id,'Основное меню :',reply_markup = keyboard)
			client.register_next_step_handler(someStep, get_text_Chto)





def get_text_About(message):
		keyboard1 = types.ReplyKeyboardMarkup()
		keyboard1.row('◀️ Назад','⚠️ Основные симптомы', '❕ Профилактика')
		keyboard1.row('😩 Как справиться со стрессом','😰 Как помочь ребёнку справиться со стрессом')
		keyboard1.row('✅ Больше информации')

		if message.text == '✅ Больше информации':
			someStep = client.send_message(message.chat.id,'''🇺🇦 Больше актуальной информации о заболевании COVID‑19 Вы можете получить на официальном сайте МОЗ Украины:
			\nhttps://moz.gov.ua/koronavirus-2019-ncov
			\n\n🌐 Рекомендации и информация от ВОЗ:
			\nhttps://www.who.int/ru/emergencies/diseases/novel-coronavirus-2019
				''',reply_markup = keyboard1)
			client.register_next_step_handler(someStep, get_text_About)

		if message.text == '◀️ Назад':
			id1 = message.from_user.id

			somefile = open('database.txt', 'rt')
			users = somefile.read()
			somefile.close()
			somefile = open('database.txt', 'a')

			if str(id1) not in users:
				keyboard = types.ReplyKeyboardMarkup()
				keyboard.row('Что такое COVID-19?', '📊 Статистика')
				keyboard.row('📝 Пройти тест')
				keyboard.row('🔔 Подписаться на рассылку')
				somefile.close()
			else:           
				keyboard = types.ReplyKeyboardMarkup()
				keyboard.row('Что такое COVID-19?', '📊 Статистика')
				keyboard.row('📝 Пройти тест')
				keyboard.row('🔕 Отписаться от рассылки')
				somefile.close()




			someStep = client.send_message(message.chat.id,'Основное меню :',reply_markup = keyboard)
			client.register_next_step_handler(someStep, get_text_Chto)


		if message.text == '😩 Как справиться со стрессом':
			someStep = client.send_message(message.chat.id,'''
\n😔 Если вы испытываете чувство грусти, стресса,
замешательства, страха или досады в кризисной
ситуации - это нормально.Вам может стать легче от доверительного общения.
Поговорите с друзьями или членами вашей семьи.
\n\n🏠 Если вам приходится оставаться дома, не забывайте о здоровом образе жизни: правильном питании, режиме сна, физических упражнениях и общении с близкими дома, либо по электронной почте или телефону с родственниками и друзьями.
\n\n❌ Не курите и не употребляйте алкоголь или другие
психоактивные вещества, чтобы подавить свои эмоции.Если они слишком сильны, обратитесь за медицинской или
психологической помощью. Заранее подготовьте план, куда и
каким образом вы будете обращаться. 
\n\n❕ Будьте информированы. Ознакомьтесь с информацией, которая
поможет вам лучше определить риски и принять разумные
меры предосторожности. Пользуйтесь компетентными
источниками проверенной информации, например веб-сайтом
ВОЗ или местного органа общественного здравоохранения.
\n\n🌐 Если вас или членов вашей семьи беспокоят и тревожат
репортажи в СМИ, уделяйте меньше времени их
просмотру или прослушиванию.
\n\n❕ Обратитесь к своему прошлому опыту преодоления трудных
жизненных ситуаций: возможно, некоторые навыки помогут
вам совладать с эмоциями в нынешней обстановке вспышки
инфекции.

				''',reply_markup = keyboard1)
			client.register_next_step_handler(someStep, get_text_About)



		if message.text == '😰 Как помочь ребёнку справиться со стрессом':
			someStep = client.send_message(message.chat.id,'''
\n\n👶 Дети реагируют на стресс по‑разному: они могут настойчиво требовать внимания взрослых, становиться тревожными, замкнутыми, неприветливыми или избыточно оживленными, начинают мочиться в постель и т.д.

\n\n🥰 Отвечайте на подобные реакции ребенка позитивно, узнайте, что его беспокоит, и окружите любовью и вниманием.В трудные моменты детям особенно нужны любовь и внимание. Поэтому старайтесь проявлять их еще больше, чем обычно.Прислушивайтесь к ребенку, проявляйте доброту и приободряйте его.

\n\n🎲 Чтобы отвлечь ребенка, старайтесь придумывать для него игры и интересные занятия.

\n\n👨‍👩‍👦 Желательно по возможности не разлучать детей с родителями и другими членами семьи. Если же это невозможно (например, в случае госпитализации), необходимо обеспечить регулярное общение ребенка с семьей (например, по телефону) и предоставить ему необходимую моральную поддержку.

\n\n🗓 Старайтесь как можно более тщательно следовать заведенному порядку или графику, либо, учитывая смену обстоятельств, введите новый распорядок дня, в котором предусмотрено время для школьного или другого обучения, а также игр и отдыха.

\n\n🗣 Объясните ребенку, что произошло и какова текущая ситуация, и на доступном для него языке расскажите, как уберечься от заражения.В том числе спокойно расскажите ему о возможном развитии событий (например, кто‑либо из членов семьи и/или сам ребенок может почувствовать недомогание, и ему может потребоваться на некоторое время поехать в больницу, где врачи помогут ему выздороветь).
				''',reply_markup = keyboard1)
			client.register_next_step_handler(someStep, get_text_About)


		if message.text == '❕ Профилактика':
			someStep = client.send_message(message.chat.id,'''‼️ *Для предупреждения распространения COVID-19*:
\n\n⚠️ Соблюдайте правила гигиены рук. Часто мойте руки водой с мылом или обрабатывайте их спиртосодержащим антисептиком для рук.
\n⚠️ Держитесь на безопасном расстоянии от чихающих или кашляющих людей.
\n⚠️ Носите маску, когда находитесь в окружении других людей.
\n⚠️ Не прикасайтесь руками к глазам, рту или носу.
\n⚠️ При кашле или чихании прикрывайте рот и нос локтевым сгибом или платком.
\n❔ Если вы чувствуете недомогание, оставайтесь дома.
\n❓ В случае повышения температуры, появления кашля и одышки обратитесь за медицинской помощью.''', parse_mode='Markdown',reply_markup = keyboard1)
			client.register_next_step_handler(someStep, get_text_About)


		if message.text == '⚠️ Основные симптомы':
			someStep = client.send_message(message.chat.id, '''К наиболее распространенным симптомам COVID-19 относятся:

🔸 Лихорадка
🔸 Сухой кашель
🔸 Утомляемость

К другим, менее распространенным симптомам, которые встречаются у ряда пациентов, относятся:

▫️ Утрата обоняния или вкусовых ощущений
▫️ Заложенность носа
▫️ Конъюнктивит (или покраснение глаз)
▫️ Боль в горле
▫️ Головная боль
▫️ Боль в мышцах или суставах
▫️ Различные виды высыпаний на коже
▫️ Тошнота или рвота
▫️ Диарея
▫️ Озноб или головокружение

Тяжелое течение COVID‑19 проявляется следующими симптомами:

🔻 Одышка
🔻 Потеря аппетита
🔻 Спутанность сознания
🔻 Упорные боли или ощущение сдавления грудной клетки
🔻 Высокая температура тела (выше 38°C)

К другим, менее распространенным симптомам относятся:

▪️ Раздражительность
▪️ Спутанность сознания
▪️ Снижение уровня сознания (иногда сопровождается судорогами)
▪️ Тревожность
▪️ Угнетенное состояние
▪️ Нарушения сна
▪️ Более тяжелые и редкие неврологические осложнения, такие как инсульт, воспалительное поражение мозга, делирий и поражение нервов''',reply_markup = keyboard1)
			client.register_next_step_handler(someStep, get_text_About)


def get_text_StatsRegion(message):
		keyboardRegion = types.ReplyKeyboardMarkup(True)
		keyboardRegion.row('◀️ Назад','Киев')
		keyboardRegion.row('Винницкая область','Волынская область')
		keyboardRegion.row('Днепропетровская область','Донецкая область')
		keyboardRegion.row('Житомирская область','Закарпатская область')
		keyboardRegion.row('Запорожская область','Ивано-Франковская область')
		keyboardRegion.row('Киевская область','Кировоградская область')
		keyboardRegion.row('Луганская область','Львовская область')
		keyboardRegion.row('Николаевская область','Одесская область')
		keyboardRegion.row('Полтавская область','Ровенская область')
		keyboardRegion.row('Сумская область','Тернопольская область')
		keyboardRegion.row('Харьковская область','Херсонская область')
		keyboardRegion.row('Хмельницкая область','Черкасская область')
		keyboardRegion.row('Черниговская область','Черновицкая область')

		if message.text == '◀️ Назад':
			id1 = message.from_user.id

			somefile = open('database.txt', 'rt')
			users = somefile.read()
			somefile.close()
			somefile = open('database.txt', 'a')

			if str(id1) not in users:
				keyboard = types.ReplyKeyboardMarkup()
				keyboard.row('Что такое COVID-19?', '📊 Статистика')
				keyboard.row('📝 Пройти тест')
				keyboard.row('🔔 Подписаться на рассылку')
				somefile.close()
			else:           
				keyboard = types.ReplyKeyboardMarkup()
				keyboard.row('Что такое COVID-19?', '📊 Статистика')
				keyboard.row('📝 Пройти тест')
				keyboard.row('🔕 Отписаться от рассылки')
				somefile.close()




			someStep = client.send_message(message.chat.id,'Основное меню :',reply_markup = keyboard)
			client.register_next_step_handler(someStep, get_text_Chto)


		if message.text =='Винницкая область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewVinnytsaRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewVinnytsaAlreadyDeadRegion)   +'\n✅ *Выздоровело за сегодня*: ' + str(NewVinnytsaGotWellRegion) + '\n' +'\n📊 Всего случаев заболевания в Винницкой области: ' + str(VinnytsaRegionCases) + '\n☠️ Умерло: ' + str(VinnytsaAlreadyDeadRegion)   +'\n✅ Всего выздоровело: ' + str(VinnytsaGotWellRegion) ,parse_mode="Markdown", reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Волынская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewVolinRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewVolinAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewVolinGotWellRegion) + '\n' + '\n📊 Всего случаев заболевания в Волынской области: ' + str(VolinRegionCases) + '\n☠️ Умерло: ' + str(VolinAlreadyDeadRegion)  +'\n✅ Всего выздоровело: ' + str(VolinGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Днепропетровская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewDnepropetrovskRegionCases)  +'\n☠️ *Новых смертей*: ' + str(NewDnepropetrovskAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewDnepropetrovskGotWellRegion)+ '\n' + '\n📊 Всего случаев заболевания в Днепропетровской области: ' + str(DnepropetrovskRegionCases) + '\n☠️ Умерло: ' + str(DnepropetrovskAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(DnepropetrovskGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Донецкая область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: '+ str(NewDonetskRegionCases) +'\n☠️ *Новых смертей*: ' + str(NewDonetskAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewDonetskGotWellRegion)+ '\n' + '\n📊 Всего случаев заболевания в Донецкой области: ' + str(DonetskRegionCases) + '\n☠️ Умерло: ' + str(DonetskAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(DonetskGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Житомирская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewZhitomirRegionCases)  +'\n☠️ *Новых смертей*: ' + str(NewZhitomirAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewZhitomirGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Житомирской области: ' + str(ZhitomirRegionCases) + '\n☠️ Умерло: ' + str(ZhitomirAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(ZhitomirGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Закарпатская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewZakarpatieRegionCases)  +'\n☠️ *Новых смертей*: ' + str(NewZakarpatieAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewZakarpatieGotWellRegion)+ '\n' + '\n📊 Всего случаев заболевания в Закарпатской области: ' + str(ZakarpatieRegionCases) + '\n☠️ Умерло: ' + str(ZakarpatieAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(ZakarpatieGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Запорожская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewZaporozhieRegionCases)  +'\n☠️ *Новых смертей*: ' + str(NewZaporozhieAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewZaporozhieGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Запорожской области: ' + str(ZaporozhieRegionCases) + '\n☠️ Умерло: ' + str(ZaporozhieAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(ZaporozhieGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Ивано-Франковская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewIvanoFrankovskRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewIvanoFrankovskAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewIvanoFrankovskGotWellRegion)+ '\n' + '\n📊 Всего случаев заболевания в Ивано-Франковской области: ' + str(IvanoFrankovskRegionCases) + '\n☠️ Умерло: ' + str(IvanoFrankovskAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(IvanoFrankovskGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Киевская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewKievRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewKievAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewKievGotWellRegion)+ '\n' + '\n📊 Всего случаев заболевания в Киевской области: ' + str(KievRegionCases) + '\n☠️ Умерло: ' + str(KievAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(KievGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Кировоградская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewKirovogradRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewKirovogradAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewKirovogradGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Кировоградской области: ' + str(KirovogradRegionCases) + '\n☠️ Умерло: ' + str(KirovogradAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(KirovogradGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Луганская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewLuganskRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewLuganskAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewLuganskGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Луганской области: ' + str(LuganskRegionCases) + '\n☠️ Умерло: ' + str(LuganskAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(LuganskGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Львовская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewLvivRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewLvivAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewLvivGotWellRegion)+ '\n' + '\n📊 Всего случаев заболевания в Львовской области: ' + str(LvivRegionCases) + '\n☠️ Умерло: ' + str(LvivAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(LvivGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Николаевская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewNikolaevRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewNikolaevAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewNikolaevGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Николаевской области: ' + str(NikolaevRegionCases) + '\n☠️ Умерло: ' + str(NikolaevAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(NikolaevGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Одесская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewOdessaRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewOdessaAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewOdessaGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Одесской области: ' + str(OdessaRegionCases) + '\n☠️ Умерло: ' + str(OdessaAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(OdessaGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Полтавская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewPoltavaRegionCases) +'\n☠️ *Новых смертей*: ' + str(NewPoltavaAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewPoltavaGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Полтавской области: ' + str(PoltavaRegionCases) + '\n☠️ Умерло: ' + str(PoltavaAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(PoltavaGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Ровенская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewRovnoRegionCases) +  '\n☠️ *Новых смертей*: ' + str(NewRovnoAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewRovnoGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Ровенской области: ' + str(RovnoRegionCases) + '\n☠️ Умерло: ' + str(RovnoAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(RovnoGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Сумская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewSumiRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewSumiAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewSumiGotWellRegion)+ '\n' + '\n📊 Всего случаев заболевания в Сумской области: ' + str(SumiRegionCases) + '\n☠️ Умерло: ' + str(SumiAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(SumiGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Тернопольская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewTernopilRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewTernopilAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewTernopilGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Тернопольской области: ' + str(TernopilRegionCases) + '\n☠️ Умерло: ' + str(TernopilAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(TernopilGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Харьковская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewKharkovRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewKharkovAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewKharkovGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Харьковской области: ' + str(KharkovRegionCases) + '\n☠️ Умерло: ' + str(KharkovAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(KharkovGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Херсонская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewChersonRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewChersonAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewChersonGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Херсонской области: ' + str(ChersonRegionCases) + '\n☠️ Умерло: ' + str(ChersonAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(ChersonGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Хмельницкая область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewChmelnitskRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewChmelnitskAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewChmelnitskGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Хмельницкой области: ' + str(ChmelnitskRegionCases) + '\n☠️ Умерло: ' + str(ChmelnitskAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(ChmelnitskGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Черкасская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewCherkasiRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewCherkasiAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewCherkasiGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Черкаской области: ' + str(CherkasiRegionCases) + '\n☠️ Умерло: ' + str(CherkasiAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(CherkasiGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Черниговская область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewChernigovRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewChernigovAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewChernigovGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Черниговской области: ' + str(ChernigovRegionCases) + '\n☠️ Умерло: ' + str(ChernigovAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(ChernigovGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Черновицкая область':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewChernovciRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewChernovciAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewChernovciGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Черновицкой области: ' + str(ChernovciRegionCases) + '\n☠️ Умерло: ' + str(ChernovciAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(ChernovciGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)
		if message.text =='Киев':
			someStep =client.send_message(message.chat.id, '🦠 *Новых случаев заболевания*: ' + str(NewKievRegionCases) + '\n☠️ *Новых смертей*: ' + str(NewKievAlreadyDeadRegion) + '\n✅ *Выздоровело за сегодня*: ' + str(NewKievGotWellRegion) + '\n'+ '\n📊 Всего случаев заболевания в Киеве: ' + str(KievRegionCases) + '\n☠️ Умерло: ' + str(KievAlreadyDeadRegion) +'\n✅ Всего выздоровело: ' + str(KievGotWellRegion),parse_mode="Markdown",reply_markup= keyboardRegion)
			client.register_next_step_handler(someStep, get_text_StatsRegion)

def send_notification():
	somefile = open('database.txt', 'rt')
	for line in somefile.readlines():
		if line != '\n':
			id1 = int(line)
			client.send_message(id1, '🔔 *Новая информация*' + '\n\n\n🦠 *Новых случаев заболевания*: ' + str(NewCasesPerDayVariable)  + '\n☠️ *Новых смертей*: ' + str(DeadPerDayVariable) +'\n✅ *Выздоровело за сегодня*: ' + str(NewGotWellVariable) + '\n' +'\n📊 Всего случаев заболевания в Украине: ' + str(CasesInUkraineVariable) + '\n☠️ Умерло: ' + str(AlreadyDeadVariable) +'\n✅ Всего выздоровело: ' + str(GotWellVariable) +  '\n' + '\n⏰ ' + timeN, parse_mode="Markdown")
	somefile.close()

def do_schedule():
	#schedule.every().day.at("09:00").do(send_notification)
	schedule.every(30).seconds.do(send_notification)
	while True:
		schedule.run_pending()
		time.sleep(1)

def runBot():
	while 1:
		try:
			client.polling()  # работать всегда
		except Exception as e:
			print(e)  # если находим ЛЮБУЮ ошибку рестартим бота
			os.system('python bot.py')

t1 = threading.Thread(target=runBot)
t2 = threading.Thread(target=do_schedule)
	
t1.start()   
t2.start()
