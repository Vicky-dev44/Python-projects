from matplotlib import pyplot as plt
players = ["Rohit","Dhoni","Dhawan","Kholi"]
Team_score = [120,44,92,72]
Total = 303
explode = [0.1,0,0,0]

fig1, ax1 = plt.subplots()
ax1.pie(Team_score, explode=explode, labels=players, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.show()