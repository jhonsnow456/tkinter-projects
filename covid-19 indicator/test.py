from tkinter import *
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches # to scale the data we are importing patches
from covid import Covid

class Application:
    def __init__(self, root):
        self.root = root
        root.geometry("400x200")
        root.title("Get Covid-19 Data Country Wise")

        # create the widget
        self.description = Label(root, text="Enter all countries names\nfor whom you want to get\ncovid-19 data", font="Consolas 15 bold")
        self.description.pack()
        
        self.countries_name = Label(root, text="Enter country name:")
        self.countries_name.pack()
        
        self.data = StringVar()
        self.data.set("Seperate country names using comma or space(not both)")
        
        self.entry = Entry(root, textvariable=self.data, width=55)
        self.entry.pack(pady = 10)

        Button(root, text="Get Data", command=self.showdata).pack(pady = 10)


    def showdata(self):
        covid = Covid()
        cases, confirmed, active, deaths, recovered = [], [], [], [], []
        
        try:
            self.root.update()
            countries = self.data.get() # getting countries names entered by the user
            country_names = countries.strip() # removing white spaces from the start and end of the string
            country_names = country_names.replace(" ", ",")# replacing white spaces with commas inside the string
            country_names = country_names.split(",")
            
            for x in country_names:
                cases.append(covid.get_status_by_country_name(x))
                self.root.update()
            
            for y in cases:
                confirmed.append(y["confirmed"])
                active.append(y["active"])
                deaths.append(y["deaths"])
                recovered.append(y["recovered"])
            
            # marking the color information on scaleusing patches
            confirmed_patch = mpatches.Patch(color='green', label='confirmed')
            recovered_patch = mpatches.Patch(color='red', label='recovered')
            active_patch = mpatches.Patch(color='blue', label='active')
            deaths_patch = mpatches.Patch(color='black', label='deaths')
            
            # plotting the scale on graph using legend()
            plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])
            # showing the data using graphs
            # this whole for loop section is related to matplotlib
            for x in range(len(country_names)):
                plt.bar(country_names[x], confirmed[x], color='green')
                if recovered[x] > active[x]:
                    plt.bar(country_names[x], recovered[x], color='red')
                    plt.bar(country_names[x], active[x], color='blue')
                else:
                    plt.bar(country_names[x], active[x], color='blue')
                    plt.bar(country_names[x], recovered[x], color='red')
                plt.bar(country_names[x], deaths[x], color='black')
            
            plt.title('Current Covid Cases')        
            plt.xlabel('Country Name')
            plt.ylabel('Cases(in millions)')        
            plt.show() 

        except Exception as e:
            self.data.set("Enter correct details again")


if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()