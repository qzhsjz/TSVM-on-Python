import svm_hps as tt
import svm_ovo as ss
import numpy as np
import kernel_gen_pol as kk


n = np.array([])
x1 = np.array([[3,3],[1,7],[2,9], [1,6]])
y1 = np.array([1,2,3,2])
x2 = np.array([[5,5], [3,12]])
y2 = np.array([1,3])

acc, prm, t = tt.svm_hps(x1,y1,n,x2,y2,ss.svm_ovo,kk.kernel_gen_pol, np.array([[0.1,100.],[0.,0.],[0.,10.],[0.,5.]]),3,5)
 
nnm = kk.kernel_gen_pol(prm[2:])

f, SX, SY, SA, t = ss.svm_ovo(x1, y1, n, prm[0], prm[1], nnm)

