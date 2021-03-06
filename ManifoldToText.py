import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# based on https://scikit-learn.org/dev/auto_examples/manifold/plot_swissroll.html#sphx-glr-auto-examples-manifold-plot-swissroll-py

# This import is needed to modify the way figure behaves
from mpl_toolkits.mplot3d import Axes3D
from sklearn import manifold, datasets
from Simulator import Simulator
from PoincareMapper import PoincareMapper
import Equation
import math
import numpy as np
#----------------------------------------------------------------------
#

eq = Equation.Rossler()
sim = Simulator(eq)

angles = np.linspace(0,2*np.pi,8)

print("Integrating data")
data = sim.states(duration=400.04,split = 0.04)[2000:]
data = sim.interpolateCurve()
np.savetxt('RosslerData.txt',data)


# print("Computing embedding of data")
# embedding= manifold.LocallyLinearEmbedding(n_neighbors = 12, n_components=2,method = 'hessian',eigen_solver='dense').fit_transform(data)
# #embedding= manifold.TSNE(n_components=2,init= 'pca').fit_transform(data)
# #manifoldData = embedding.fit_transform(data)
# np.savetxt('LTSALorentz.txt',embedding)
print(len(data))
print(len(embedding))


# Modified provides a smoother manifold, the return map still sucks
# Hessians manifold is weird.... and the return maps suck
