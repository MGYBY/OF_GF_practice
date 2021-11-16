# import readforce function from fluidfoam package
from fluidfoam.readpostpro import readforce
import matplotlib.pyplot as plt

# sol = './postProcessing/forces/0/force_0.dat'
sol = './'

# force = readforce(sol, time_name = '0', name='force_0')
force = readforce(sol, time_name = '0', name='force')

plt.figure()

plt.plot(force[:, 0], force[:, 1])

# Setting axis labels
plt.xlabel('t (s)')
plt.ylabel('force')

# add grid
plt.grid()
plt.show()
plt.savefig("force.png")
