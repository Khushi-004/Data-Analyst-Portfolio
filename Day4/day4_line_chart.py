import matplotlib.pyplot as plt
days=['Day 1','Day2','Day3','Day4']
commits =[1,2,1,1] # Apne hisaab se change kar sakte hai
plt.plot(days, commits, marker='o', color='green', linewidth=3)
plt.title('Data Analyst Streak')
plt.xlabel('days')
plt.ylabel('commits')
plt.grid(True)
plt.savefig('day4_streak.png')
plt.show()