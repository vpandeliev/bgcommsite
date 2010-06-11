# -*- coding: iso-8859-15 -*-
from bgcomm.posts.models import *


class SideMenuItem():
    def __init__(self, bg, en, fr, link):
        self.bg = bg
        self.en = en
        self.fr = fr
        self.link = link

	def text(lg):
		if lg=="bg":
			return self.bg
		elif lg=="en":
			return self.en
		elif lg=="fr":
			return self.fr
		else:
			return ""
		
affiliates = [
SideMenuItem("Танцов състав 'Родина'","Rodina Dance Troupe", "Le danse Rodina","rodina"),
SideMenuItem("БУРЕТО","Student theatre BURETO", "Theatre d'etudiants BURETO","bureto"),
SideMenuItem("Посолство","Embassy", "L'embassade","embassy"),
SideMenuItem("Българска Фондация в Отава","Ottawa Region Bulgarian Foundation", "La Fondation Bulgare d'Outaouai","foundation"),
]


def menu_bg(request):
	return menus[0]
def menu_en(request):
	return menus[1]
def menu_fr(request):
	return menus[2]



bgmenu = {
"aff": affiliates,
"affiliates": "Афилиати",
"title": "Българска Общност - NCRBC",
"bg": True,
"en": False,
"prefix": "bg",
"home": "Начало",
"about": "За нас",
"links": "Връзки",
"school": "Училище",
"photos": "Снимки",
"contact": "Пишете ни",
"forum": "Форум",
"lg1link": "/en",
"lg1": "media/en.png",
"lg2link": "/fr",
"lg2": "media/fr.png",
"posted": "Автор ",
"more": "Още...",
"back": "Обратно",
"ad": "Реклама",
"sponsors": "Спонсори",
"archive": "Архив",
"adcall": "Рекламирайте тук",
"calendar": "Календар",
"at": "в",
"oclock": "часа",
"address": "Адрес",
"contactperson": "Отговорник",
"phone": "Телефон",
"email": "E-mail адрес",
"news": "Новини и предстоящи събития",
"sps": "Спонсори",
"sponsors": "Благодарим на следните спонсори за подкрепата:",
"flickr": "За всички наши снимки посетете ни на",
"subj":"Тема",
"mess":"Съобщение",
"optional":"незадължително поле",
"submit":"Изпрати",
"allads": "Всички реклами",
"adtitle": "Ползвайте тези бизнеси и услуги:",

}
enmenu = {
"aff": affiliates,
"affiliates": "Affiliates",
"title": "Bulgarian Community - NCRBC",
"bg": False,
"en": True,
"prefix": "en",
"home": "Home",
"about": "About Us",
"links": "Links",
"school": "School",
"photos": "Photos",
"contact": "Contact",
"forum": "Forum",
"lg1link": "/bg",
"lg1": "media/bg.png",
"lg2link": "/fr",
"lg2": "media/fr.png",
"posted": "Posted by ",
"more": "Read more...",
"back": "Back",
"ad": "Advertisement",
"sponsors": "Sponsors",
"archive": "Archive",
"adcall": "Advertise here",
"calendar": "Calendar",
"at": "at",
"oclock": "h.",
"address": "Address",
"contactperson": "Contact",
"phone": "Phone",
"email": "E-mail",
"news": "News and upcoming events",
"sps": "Sponsors",
"sponsors": "We gratefully acknowledge the support of the following sponsors:",
"flickr": "For all our photos find us on",
"subj":"Subject",
"mess":"Message",
"optional":"optional",
"submit":"Send",
"allads": "All ads",
"adtitle": "Support these Bulgarian businesses:",
}
frmenu = {
"aff": affiliates,
"affiliates": "Amis",
"title": "Comminaute Bulgare - NCRBC",
"bg": False,
"en": False,
"prefix": "fr",
"home": "Acueill",
"about": "L'about",
"links": "Les Links",
"school": "L'ecole",
"photos": "Les Photos",
"contact": "Contacte",
"forum": "Forum",
"lg1link": "/bg",
"lg1": "media/bg.png",
"lg2link": "/en",
"lg2": "media/en.png",
"posted": "Auteur ",
"more": "Plus...",
"back": "Dehors! Calvaire!",
"ad": "Avertissements",
"sponsors": "Sponseurs",
"archive": "L'archive",
"adcall": "Postez un avertissement",
"calendar": "Calendrier",
"at": "a",
"oclock": "heure",
"address": "Addresse",
"contactperson": "Contacte",
"phone": "Telephone",
"email": "Courriel",
"news": "Nouvelles et evenements",
"sps": "Les sponseurs",
"sponsors": "Les sponseurs putin!:",
"flickr": "Trouvez toutes nos photos sur",
"subj":"Sujet",
"mess":"Message",
"optional":"optionnel",
"submit":"Envoyez",
"allads": "Toutes les avertissements",
"adtitle": "Aidez les firmes bulgares:",
}
menus = [bgmenu, enmenu, frmenu]