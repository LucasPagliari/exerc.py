import numpy as np

vetor = np.array([0, 1, 2, 3, 4, 5, 6])
print(type(vetor))

print(vetor.cumsum())

# Tamanho e Dimensões
print(vetor.shape)
print('\n')

# Cria um vetor com progressão aritmética - start, stop, step
vetor2 = np.arange(0., 4.5, .5)
print(vetor2.dtype)
print('\n')

x = np.arange(0., 10., .25)
print(x)
print('\n')

# Cria um array com zeros
print(np.zeros(10))
print('\n')

# Cria uma matriz identidade
z = np.eye(3)
print(z)
print('\n')

# Matriz criada a partir da diagonal
d = np.diag(np.array([1, 2, 3, 4]))
print(d)
print('\n')

print(np.linspace(0, 9))