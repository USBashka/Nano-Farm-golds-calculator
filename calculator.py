from datetime import timedelta, datetime
import matplotlib.pyplot as plt


l = int(input("Уровень шахты: "))
g = int(input("Количество голдов: "))

d = 0

golds = []
levels = []

while l<2000:
    d+=1
    g+=l
    if d%5==0: g+=1
    l+=g//250
    g%=250
    
    if l>2000:
        g += (l - 2000) * 250
        l = 2000
    
    golds.append(g)
    levels.append(l)


print()
print(d, "days to get 2K")
print()
print("Wait for", (datetime.now()+timedelta(d)).strftime("%d.%m.%Y"))


plt.style.use('grayscale')

plt.plot(golds, color="r", label="Голды")
plt.plot(levels, color="b", label="Уровень")
plt.legend()
plt.grid()
plt.xlabel('День')

plt.show()
