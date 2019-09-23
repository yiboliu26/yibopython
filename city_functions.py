def city_country(city, country, population=''):
    if population:
        format = city+ ', ' + country + ' - population ' + str(population)
    else:
        format = city + ', ' +country
    return(format.title())
