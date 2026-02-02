import matplotlib.pyplot as plt 
sales_percentages = [11.9, 11.2, 10.8, 10.2, 9.8, 9.2, 8.9, 7.1, 6.4, 5.6, 2.5, 2.1, 4.3]
car_names = ["Dzire", "Baleno", "Swift", "Wagon R", "Brezza", "Fronx", "Ertiga", "Grand Vitara", "Eeco", "Alto K10", "S-Presso", "Celerio", "Others"]
color_names = ["blue", "green", "red", "cyan", "magenta", "yellow", "black", "purple", "orange", "brown", "pink", "gray", "olive"]
#gap list represent gap between 2 slice in pie chart, must give gap for each and every slice
gap_list =  [0.1] * len(sales_percentages)
# print(explode_list)
plt.pie(sales_percentages,labels=car_names,colors=color_names,autopct='%.1f%%',startangle=90,explode=gap_list,shadow=True)
plt.title("Maruti suzuki 2026 sales breakup")
plt.show()