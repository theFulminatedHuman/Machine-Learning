def multiply(A, B): 
 # Find the coefficients of both the polynomials
 na = len(A)
 nb = len(B)

 # Pad the smaller array with zeros
 if na > nb:
     B1 = np.pad(B, (0, na - nb), 'constant', constant_values=0)
     C = np.zeros(2 * na - 1)
     for i in range(2 * na - 1):
         if i < na:
             C[i] += np.dot(A[0: i + 1], np.flip(B1[0: i + 1]))
         else:
             C[i] += np.dot(A[i - na + 1: na], np.flip(B1[i - na + 1: na]))
 else:
     A1 = np.pad(A, (0, nb - na), 'constant', constant_values=0)
     C = np.zeros(2 * nb - 1)
     for i in range(2 * nb - 1):
         if i < nb:
             C[i] += np.dot(A1[0: i + 1], np.flip(B[0: i + 1]))
         else:
             C[i] += np.dot(A1[i - nb + 1: nb], np.flip(B[i - nb + 1: nb]))

 # Remove any extra zeros from the back of C
 C = list(filter(None, C))
 return C
