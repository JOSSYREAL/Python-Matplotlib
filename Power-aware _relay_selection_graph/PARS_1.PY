import matplotlib.pyplot as plt

#plt.style.use("grayscale")
#unpacking, where fig rep the figure, and axes are the plot space
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

#initial total power of each node on x-axis
initial_power = ["P", "1.1P", "1.2P","1.3P", "1.5P", "1.6P", "1.7P", "1.8P", "1.9P", "2P"]

#pars I, pars II and pars III on y-axis
pars_I = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748]
pars_II = [45372, 48876, 53850, 57287, 63016,65998, 70003, 70000, 71496, 75370]
pars_III = [37810, 43515, 46823, 49293, 53437,56373, 62375, 66674, 68745, 68746]


#to plot the line graph,linestyle= dashed line, cross marker, k= black color, clip_on = False in order to make the markers visible at the border edge
ax1.plot(initial_power, pars_I,color = "k", marker="X", label = "PARS I", linewidth=0.7,
         markeredgecolor="k",markeredgewidth=0.7,markerfacecolor="white", clip_on= False)
ax1.plot(initial_power, pars_II,color = "k",  marker="o", label = "PARS II", linewidth= 0.9,
         markeredgecolor="k",markeredgewidth=0.7,markerfacecolor="white", clip_on= False)
ax1.plot(initial_power, pars_III,color = "k", marker="v",markersize=7,markeredgecolor="k",markeredgewidth=0.7,
         markerfacecolor="white",linewidth = 0.7, label= "PARS III", clip_on= False)

#to plot the line graph,linestyle= dashed line, cross marker, k= black color, clip_on = False in order to make the markers visible at the border edge
ax2.plot(initial_power, pars_I,color = "k", marker="X", label = "PARS I", linewidth=0.7,
         markeredgecolor="k",markeredgewidth=0.7,markerfacecolor="white", clip_on= False)
ax2.plot(initial_power, pars_II,color = "k",  marker="o", label = "PARS II", linewidth= 0.9,
         markeredgecolor="k",markeredgewidth=0.7,markerfacecolor="white", clip_on= False)
ax2.plot(initial_power, pars_III,color = "k", marker="v",markersize=7,markeredgecolor="k",markeredgewidth=0.7,
         markerfacecolor="white",linewidth = 0.7, label= "PARS III", clip_on= False)
#to let the x-axis start and stop not at 0
ax1.set_xlim("P","2P")
#to let the x-axis start and stop not at 0
ax2.set_xlim("P","2P")
# add label to the the title, x and y axes
ax1.set_xlabel("Normalized average network lifetime")
ax1.set_ylabel("Initial total power of each node")
ax1.set_title("Under AF Cooperation Scheme")
# add label to the the title, x and y axes
ax2.set_xlabel("Normalized average network lifetime")
ax2.set_ylabel("Initial total power of each node")
ax2.set_title("Under DF Cooperation Scheme")
#plt.xticks(initial_power)
#to show label
#so here we use the it as a class method being passed, loc =to set the legend location
leg1 =ax1.legend(loc= (0.02,0.8), shadow= True, frameon= True)
leg2 =ax2.legend(loc= (0.02,0.8), shadow= True, frameon= True)
#to set the legend enclosing or edge color
leg1.get_frame().set_edgecolor("0.1")
leg2.get_frame().set_edgecolor("0.1")
#to set the legend edge/frame size, to remove the edges set it 0.0
leg1.get_frame().set_linewidth(1)
leg2.get_frame().set_linewidth(1)
# to not allow the axis grid to be on top of the data
ax1.set_axisbelow(True)
ax2.set_axisbelow(True)
#to turn on the minor ticks that are required for the minor grid
ax1.minorticks_on()
ax2.minorticks_on()
#inserting both the major and minor grid and customizing them
ax1.grid(True, which="major", axis="both",color= "gray",linestyle="--",linewidth=0.5)
ax1.grid(True, which="minor", axis= "both", linestyle=":",linewidth="0.5",color="gray")
ax2.grid(True, which="major", axis="both",color= "gray",linestyle="--",linewidth=0.5)
ax2.grid(True, which="minor", axis= "both", linestyle=":",linewidth="0.5",color="gray")
#to set the border/spines of the figure color to black
ax1.spines["top"].set_color("black")
ax1.spines["left"].set_color("black")
ax1.spines["right"].set_color("black")
ax1.spines["bottom"].set_color("black")
ax2.spines["top"].set_color("black")
ax2.spines["left"].set_color("black")
ax2.spines["right"].set_color("black")
ax2.spines["bottom"].set_color("black")


#to solve padding issues--i.e display looks more good
plt.tight_layout()

#to display the figure
plt.show()
