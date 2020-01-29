import random
import string
import time
from run_len import calculate_compression_ratio
import matplotlib.pyplot as plt

####
#####On commence a encoder des string de taille differente avec des charachtere au hazard
####

def codagePlage(mes):
    pass

def codageLZW(mes):
    pass

def randomString(stringLength=10):
    """Generate a random string of fixed length
        link : https://pynative.com/python-generate-random-string/
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


messages = []
x = []
y_LZW = []
y_plage = []

for i in range(10,5000,200):
    messages.append(randomString(i))
    x.append(i)


for i in messages:
    y_LZW.append(calculate_compression_ratio(len(i),len(codageLZW(i))))
    y_plage.append(calculate_compression_ratio(len(i),len(codagePlage(i))))

plt.plot(x, y_LZW, label="Codage LZW")
plt.plot(x, y_plage, label="Codage par plage")


plt.xlabel("Nombre de charatere du message")
plt.ylabel("taux de compression")


plt.title("Evolution du taus de compression avec la taille d'un message pour des codages de types LZW et par plage")

ptl.show()


