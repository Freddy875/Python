Sets = {"Element1","Element2","Eelement3","Element4"}
print(Sets)

if "Element1" in Sets:
    print("Yes")

CountryList = []
for i in range(5):
    Country = input("Please enter your Country: ")
    CountryList.append(Country)

CountrySet = set(CountryList)

print(CountryList)
print(CountrySet)

if "Mexico" in CountrySet:
    print("attended")
    
Dictionary = {"Key":"Value","Key2":"Value","Key3":"Value"}
    
CountryDictionary = {}

for Country in CountryList:
    if Country in CountryDictionary:
        CountryDictionary[Country] += 1
    else:
        CountryDictionary[Country] = 1
        
print(CountryDictionary)