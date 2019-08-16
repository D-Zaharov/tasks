handle = open("countries.txt", "r", encoding="utf-8")
dictionary_of_countries = {}
for line in handle:
    element = line.split(':')
    dictionary_of_countries[element[0]] = element[1]

handle.close()

list_of_countries = list(dictionary_of_countries.keys())
list_of_countries.sort()

handle = open("result.txt", "w")
for country in list_of_countries:
    capital = dictionary_of_countries.get(country)
    handle.write(country + ' - ' + capital)
handle.close

print("список успешно отсортирован и  записан в файл")