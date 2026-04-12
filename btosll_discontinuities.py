import numpy as np
from scipy.special import p_roots

def kallen(a: np.cdouble, b: np.cdouble, c: np.cdouble) -> np.cdouble:
    return a**2 + b**2 + c**2 - 2*a*b - 2*a*c - 2*b*c

def sqkallen(a: np.cdouble, b: np.cdouble, c: np.cdouble) -> np.cdouble:
    return np.sqrt(a-(np.sqrt(b)-np.sqrt(c))**2,dtype=np.cdouble) * np.sqrt(a-(np.sqrt(b)+np.sqrt(c))**2,dtype=np.cdouble)

def z_map(s: np.cdouble, sthr: float , s0: float) -> np.cdouble:
    return np.where(np.imag(s)==0,np.conj((np.sqrt(sthr-s,dtype=np.cdouble)-np.sqrt(sthr-s0))/(np.sqrt(sthr-s,dtype=np.cdouble)+np.sqrt(sthr-s0))),(np.sqrt(sthr-s,dtype=np.cdouble)-np.sqrt(sthr-s0))/(np.sqrt(sthr-s,dtype=np.cdouble)+np.sqrt(sthr-s0)))

class Triangle_Disc:
    def __init__(self, case: str, *masses: float) -> None:
        self.p1,self.p3,self.m1,self.m2,self.m3 = masses
        self.p1sq,self.p3sq,self.m1sq,self.m2sq,self.m3sq = self.p1**2,self.p3**2,self.m1**2,self.m2**2,self.m3**2

        self.t1 = (self.m2+self.m3)**2
        self.t2 = (self.p1-self.p3)**2
        self.t3 = (self.p1+self.p3)**2
        self.tpl = self.tplus()
        self.tmn = self.tminus()

        self.modlog_Y_c1 = self.p1sq + self.p3sq + self.m2sq + self.m3sq - 2*self.m1sq
        self.modlog_Y_c0 = (self.p1sq-self.p3sq)*(self.m2sq-self.m3sq)

        if case == 'a':
            self.modlog = self.modlog_a
            self.prefactor = self.prefactor_a
        
        elif case == 'b':
            self.modlog = self.modlog_bd
            self.prefactor = self.prefactor_bc
        
        elif case == 'c':
            self.modlog = self.modlog_c
            self.prefactor = self.prefactor_bc

        elif case == 'd':
            self.modlog = self.modlog_bd
            self.prefactor = self.prefactor_d

    def __call__(self, t: float) -> np.cdouble:
        return self.disc(t)

    def tplus(self) -> np.cdouble:
        return (self.p1sq*(self.m1sq+self.m3sq)+self.p3sq*(self.m1sq+self.m2sq)-self.p1sq*self.p3sq-(self.m1sq-self.m2sq)*(self.m1sq-self.m3sq)-sqkallen(self.p1sq,self.m1sq,self.m2sq)*sqkallen(self.p3sq,self.m1sq,self.m3sq))/(2*self.m1sq)

    def tminus(self) -> np.cdouble:
        return (self.p1sq*(self.m1sq+self.m3sq)+self.p3sq*(self.m1sq+self.m2sq)-self.p1sq*self.p3sq-(self.m1sq-self.m2sq)*(self.m1sq-self.m3sq)+sqkallen(self.p1sq,self.m1sq,self.m2sq)*sqkallen(self.p3sq,self.m1sq,self.m3sq))/(2*self.m1sq)

    def modlog_Y(self, t: float) -> float:
        return t**2 - t*self.modlog_Y_c1 + self.modlog_Y_c0

    def modlog_a(self, t: float) -> np.cdouble:
        kallenprod = kallen(t,self.m2sq,self.m3sq)*kallen(t,self.p1sq,self.p3sq)
        a = self.modlog_Y(t)
        b = np.sqrt(np.abs(kallenprod))
        return np.where(t>=np.real(self.tpl), np.log(np.abs((a-b)/(a+b)))/b, (np.log(np.abs((a-b)/(a+b)))-1j*np.pi)/b) + (0.+0.j)

    def modlog_c(self, t: float) -> np.cdouble:
        kallenprod = kallen(t,self.m2sq,self.m3sq)*kallen(t,self.p1sq,self.p3sq)
        a = self.modlog_Y(t)
        b = np.sqrt(np.abs(kallenprod))
        return np.where(t>=np.real(self.tpl), np.log(np.abs((a-b)/(a+b)))/b, np.where(t<=np.real(self.tmn) ,np.log(np.abs((a-b)/(a+b)))/b, (np.log(np.abs((a-b)/(a+b)))-1j*np.pi)/b)) + (0.+0.j)

    def modlog_bd(self, t: float) -> np.cdouble:
        kallenprod = kallen(t,self.m2sq,self.m3sq)*kallen(t,self.p1sq,self.p3sq)
        a = self.modlog_Y(t)
        b = np.sqrt(np.abs(kallenprod))
        return np.log(np.abs((a-b)/(a+b)))/b + (0.+0.j)
    
    def prefactor_a(self, t: float) -> float:
        return t**2
    
    def prefactor_bc(self, t: float) -> float:
        return t**2 * np.sqrt(1-self.t1/t,dtype=np.cdouble)
    
    def prefactor_d(self, t: float) -> float:
        return t * np.sqrt(1-self.t1/t,dtype=np.cdouble)

    def disc(self, t: float) -> np.cdouble:
        return np.where(t > self.t1, 2j * self.prefactor(t) * (2*self.modlog_Y(t)+(self.modlog_Y(t)**2-kallen(t,self.m2sq,self.m3sq)*kallen(t,self.p1sq,self.p3sq))*self.modlog(t)) / (kallen(t,self.m2sq,self.m3sq)*kallen(t,self.p1sq,self.p3sq)), 0.+0.j)

class FF_disc:
    def __init__(self, case: str) -> None:
        self.case = case # options: 'a', 'b', 'c', 'd'
        self.mc = np.sqrt(0.1)
        x,w=p_roots(100)

        if self.case == 'a':
            m23 = 0
            self.muthrsq = 4*self.mc**2
            mumidsq = 1
            mucutsq = 7.5
            self.mu0sq = 0
            self.params_a = [-0.037159974978173506, 0.06443532509333029, -0.03338141503872886, 0.005585821305068587]
            self.spectral = self.spectral_ab
            self.disc = self.disc_abd
        
        elif self.case == 'b':
            m23 = 1
            self.muthrsq = 4*self.mc**2
            mumidsq = 2
            mucutsq = 12
            self.mu0sq = -4*self.mc**2
            self.params_a = [0.24536385474981248, 0.32624248081465773, -0.5002681482445575, 0.7882384023013085]
            self.spectral = self.spectral_ab
            self.disc = self.disc_abd
        
        elif self.case == 'c':
            m23 = self.mc
            self.muthrsq = self.mc**2
            mumidsq = 0.47
            mucutsq = 13
            self.mu0sq = -self.mc**2
            self.params_a = [-1.9994731897895952, 0.1732470321087656, -0.3037634924331857, -0.710470549090449, -1.2725821916836675, -0.9562697997571012, -0.4861398029206371, 0.016915200806158492]
            self.params_c = [6.700517604761433, 15.23336250306805]
            self.spectral = self.spectral_c
            self.disc = self.disc_c

        elif self.case == 'd':
            m23 = self.mc
            self.muthrsq = (1+self.mc)**2
            mumidsq = 3
            mucutsq = 30
            self.mu0sq = 0
            self.mumnsq = (1-self.mc)**2
            self.params_a = [625.729787664862, -845.0200456754759, 1136.229943958402, -952.6679301034515, 803.382669757803]
            self.param_b = 1310.6541913634815
            self.spectral = self.spectral_d
            self.disc = self.disc_abd

        self.tthr = 4*m23**2
        
        self.order_a = len(self.params_a)

        self.musq_vals = np.concatenate(((self.muthrsq+mumidsq)/2+(mumidsq-self.muthrsq)/2*x,(mumidsq+mucutsq)/2+(mucutsq-mumidsq)/2*x))
        self.musq_weights = np.concatenate(((mumidsq-self.muthrsq)*w,(mucutsq-mumidsq)*w))
        self.musq_spectral = self.spectral(self.musq_vals)
        self.musq_triangles = [Triangle_Disc(case,*[1,0,np.sqrt(musq),m23,m23]) for musq in self.musq_vals]

    def __call__(self, t: np.cdouble) -> np.cdouble:
        return self.disc(t)
    
    def disc_abd(self, t: float) -> np.cdouble:
        discval = 0.+0.j
        for f,w,s in zip(self.musq_triangles,self.musq_weights,self.musq_spectral):
            discval += np.where(t<self.tthr, 0.+0.j, w*s*f(t))
        return discval
    
    def disc_c(self, t: float) -> np.cdouble:
        discval = 0.+0.j
        for f,w,s in zip(self.musq_triangles,self.musq_weights,self.musq_spectral):
            discval += np.where(t<self.tthr, 0.+0.j, w*s*f(t))
        sigma_t = np.where(t<self.tthr, 0.+0.j, np.sqrt(1-self.tthr/t,dtype=np.cdouble))
        discval += np.where(t<self.tthr, 0.+0.j, 1j*(self.params_c[0] * np.conj(np.log(t-1,dtype=np.cdouble)) + self.params_c[1]) / (t - 1) * t * (t * sigma_t + self.tthr / 2 * np.log((1-sigma_t)/(1+sigma_t),dtype=np.cdouble)) / (t-self.tthr))
        return discval
    
    def spectral_ab(self, musq: float) -> float:
        zmusq = z_map(musq,self.muthrsq,self.mu0sq)
        return np.imag((zmusq-1)*sum([self.params_a[i]*zmusq**i for i in range(self.order_a)]))
    
    def spectral_c(self, musq: float) -> float:
        zmusq = z_map(musq,self.muthrsq,self.mu0sq)
        return np.imag((zmusq-1)**2*sum([self.params_a[i]*zmusq**i for i in range(self.order_a)]))
    
    def spectral_d(self, musq: float) -> float:
        zmusq = z_map(musq,self.muthrsq,self.mu0sq)
        musq_sqkallen = np.sqrt((musq-self.muthrsq)*(musq-self.mumnsq)) 
        return np.imag((zmusq-1)**2*sum([self.params_a[i]*zmusq**i for i in range(self.order_a)])) + self.param_b * np.log(musq_sqkallen / musq) / musq_sqkallen

f27a_disc = FF_disc('a')
f27b_disc = FF_disc('b')
f27c_disc = FF_disc('c')
f27d_disc = FF_disc('d')