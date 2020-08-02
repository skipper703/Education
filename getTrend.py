import numpy as np
def get_trend1(x1, x2):
    res = x1*2018 + x2
    return res
def get_trend2(x1, x2, x3):
    res = (x1**2)*2018 + x2*2018 + x3
    return res
def get_trend3(x1, x2, x3, x4):
    res = (x1**3)*2018 + (x2**2)*2018 + x3*2018 + x4
    return res
def get_mistake(x1, x2):
    mistake = abs(x1-x2)/x1
    return mistake
#Input and save data
contry = input()
tourists_list = []
tourists_input = []
years = np.array([2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017])
tourists_input = input()
tourists_list = np.array([float(item) for item in tourists_input.split()])
stepen = int(input())
toch_znach = float(input())
#Calculating polyfit
poly = np.polyfit(years, tourists_list, stepen)
#Get trend of current polyfit
if stepen==1:
    prognoz2018 = get_trend1(poly[0], poly[1])
elif stepen==2:
    prognoz2018 = get_trend2(poly[0], poly[1], poly[2])
elif stepen==3:
    prognoz2018 = get_trend3(poly[0], poly[1], poly[2], poly[3])
pogreshnost = get_mistake(toch_znach, prognoz2018)
print("Страна:%6s, прогноз:%6.3fмлн чел, относительная погрешность:%4.2fпроц." % (contry, prognoz2018, pogreshnost*100))