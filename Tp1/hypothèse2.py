import random
import string
import time
from LZW import codageLZW
from CodagePlage import CodagePlage
import matplotlib.pyplot as plt

####
#####On commence a encoder des string de taille differente avec des charachtere au hazard
####

def calculate_compression_ratio(m, m_e):
    ratio = (m_e / m)
    return ratio


def random_string(stringLength = 10):
    """Generate a random string of fixed length
        link : https://pynative.com/python-generate-random-string/
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


messages = []
x = []
y_LZW = []
y_plage = []
y_mess = []

for i in range(1, 5000, 700):
    messages.append(random_string(i))
    x.append(i)

iter = 0

time_plage = time.time()
#  codage plage:
for i in messages:
    mesg, lenPlage, lenOriginal = CodagePlage(4, i)
    y_mess .append(lenOriginal)
    y_plage.append(lenPlage)
    iter += 1
    print iter
time_plage = time.time() - time_plage

time_lzw = time.time()
# Codage LZW:
for i in messages:
    _ , lenLZW = codageLZW(i)
    y_LZW.append(lenLZW)
    iter += 1
    print iter

time_lzw = time.time() - time_lzw


print(time_plage,time_lzw)

plt.plot(x, y_LZW, label="Codage LZW")
plt.plot(x, y_plage, label="Codage par plage")
plt.plot(x, y_mess, label="Encodage bianire")

plt.xlabel("Nombre de charatere du message origniale")
plt.ylabel("Taille du messages en octets")


plt.title("Evolution du taux de compression avec la taille d'un message pour des codages de types LZW et par plage")

plt.legend()

plt.show()


