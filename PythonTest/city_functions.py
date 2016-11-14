def get_city_country(city,country,population=''):
	if population:
		city_country = (city.title() + ',' + country.title() + ' - population ' + population)
	else:
		city_country = city.title() + ',' + country.title()
	return city_country

