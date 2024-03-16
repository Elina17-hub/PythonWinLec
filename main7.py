#


from math import pi

def find_farthest_orbit(list_of_orbits):
    list_1= [i for i in list_of_orbits if i[0] != i[1]]
  #создаем новый список.где будут   только эллипсы. исключая круги 

    list_s=[(pi * i[0] * i[1]) for i in list_1]
    #создали лист. где счтается площадь элипсв в списке list_1
    max_s=list_s.index(max(list_s))
    #ищем в списке max, далее берем индекс max записываем его в max_s
    return list_1[max_s]
orbits=[(2,3),(2.5,10),(3,9),(7,2),(6,6)]
print(*find_farthest_orbit(orbits))