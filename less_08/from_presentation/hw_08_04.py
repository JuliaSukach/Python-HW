# Создать метакласс


def change_president(self, new_president):
    self.president = new_president


def country_init(self, country, president, region=None):
    self.country = country
    self.president = president
    self.region = region


Country = type('Country', (), {'__init__': country_init, 'change_president': change_president})

first_country = Country(country='Brazil', president='Bolsonaro')
assert first_country.country == 'Brazil'
assert first_country.president == 'Bolsonaro'

first_country.change_president('Lula')

assert first_country.president == 'Lula'

Region = type('Region', (Country,), {})
first_region = Region(country='Spain', president='Puigdemont', region='Catalonia')

assert first_region.country == 'Spain'
assert first_region.region == 'Catalonia'
assert first_region.president == 'Puigdemont'



