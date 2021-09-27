positionsDistances = []
positionsRates = []
rates = []
distances = []
count = -1
employee = int(input("Введите кол-во сотрудников: "))
if employee in range(1, 1001):
    for i in range(employee):
        distances.append(int(input("Введите расстояние в км для "+str(i+1)+"-ого сотрудника: ")))
        positionsDistances.append(i + 1)
        if distances[i] > 1000:
            print("Расстояние не может превышать 1000км!")
    for i in range(employee):
        rates.append(int(input("Введите тариф за проезд одного км для "+str(i+1)+"-ого такси: ")))
        positionsRates.append(i + 1)
        if rates[i] > 10000:
            print("Тариф не может превышать 10000 за проезд одного километра!")
    positionsDistances1, distances1 = zip(*sorted(zip(positionsDistances, distances)))
    rates1, positionsRates1 = zip(*sorted(zip(rates, positionsRates)))
    for i in range(employee):
        print(str(positionsDistances1[i])+"-ый пассажир с расстоянием маршрута "+str(distances1[i])+"км поедет в такси "
                                                                                                   "№ "+str(
            positionsRates1[count])+" с тарифом "+str(rates1[count]))
        count -= 1

else:
    print("Количесвто сотрудников должно быть не меньше единицы и не больше тысячи!")
