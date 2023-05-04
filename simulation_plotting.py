import numpy as np
from numpy.random import default_rng
import sklearn.cluster._kmeans as kmc
import matplotlib.pyplot as plt

rng = default_rng()
rnc = int(input('Number of settlements: '))
density = int(input("Uniform density: "))

def initial(rnc, density):
    means = []
    cov = [[1, 0], [0, 1]]
    n = density

    for i in range(rnc):
        means.append(np.random.randint(low=0, high=20, size=(2)).tolist())

    X = [np.random.multivariate_normal(means[i], cov, n) for i in range(rnc)]
    means = np.array(means)
    X = np.array(X)
    return means, X

means, X = initial(rnc, density)


def plot(rnc, X, means):
    fig, axs = plt.subplots(1, rnc)
    fig.set_figwidth(8)
    fig.set_figheight(8)
    for i in range(rnc):
        axs[i].scatter(X[i,:,0], X[i,:,1])
        axs[i].scatter(means[i,0], means[i,1], color='red')
    plt.show()

plot(rnc, X, means)

def Simulation_Plot(mode, population, initial_infected, contact_radius, recovery_chance, fatality,
                    distancing=None, distancing_duration=0, center_gather_rate=0, symptom_showing=0,
                    infected_threshold=0, travel_rate=0, vaccination_chance=0, expire_date=0):
    
    infect = rng.choice(population, size=initial_infected, replace=False).tolist()
    #st.text(f"{infect, population, initial_infected}")
    people = []
    for idx in range(population):
        plot = [np.random.randint(0, 3), np.random.randint(0, 3)] if many_cities else 0
        x = np.random.randint(0, 1000)
        y = np.random.randint(0, 1000)
        
        people.append([plot, x, y, "infected" if idx in infect else "normal"])
    
    #print(people)
        
    pass
    #people: plot_index, x, y, state
    #for default 1 plot
    #people = [ [0, x1, y1, "normal"], [0, x2, y2, "infected", ... ]
    #for many_cities
    #people = [ [[0, 1], x1, y1, "normal"], [[2, 0], x2, y2, "infected", ... ]
    return (fig, people)
