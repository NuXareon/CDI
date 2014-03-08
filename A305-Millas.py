
import sys
sys.path.append("C:/Users/nuXe/Documents/GitHub/CDI")

from A305h_Millas import *
from A305_EN1 import *
from A305_EN2 import *

e1=entropy(EN.values())
e1_=entropy(EN_.values())

print("Entropy of 1-letter English =", e1)
print("Entropy of 1-letter English with space =", e1_)

D = joint_distribution(EN_,EN2)
A = row_marginal(D)
B = col_marginal(D)
HA = entropy(A)
HB = entropy(B)
HAB = joint_entropy(D)

print("P(A,D) = ",D[0][3])
print("P(F,H) = ", D[5][7])
print("Row Marginal Probability for A = ", A[0])
print("Row Marginal Probability for Z = ", A[25])
print("Column Marginal Probability for A = ", B[0])
print("Column Marginal Probability for Z = ", B[25])
print("Remarks:")
print("1. Row Marginal Probabilities A coincide with EN_.")
print("2. A and B do not coincide because the characters are no independent between them.")
print("H(A,B) < H(A)+H(B):")
print(HAB, " < ", HA ,"+", HB)
print(HAB, " < ", HA+HB)
