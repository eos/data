import eos
import numpy as np

def gamma(params, posterior):
    af = eos.AnalysisFile('./analysis.yaml')
    analysis = af.analysis(posterior)
    parameters = analysis.parameters
    parameters.set('qbcu::Re{c1}',  params[0])
    parameters.set('qbcu::Re{c2}',  params[1])
    parameters.set('qbcu::Re{c3}',  params[2])
    parameters.set('qbcu::Re{c4}',  params[3])
    parameters.set('qbcu::Re{c5}',  params[4])
    parameters.set('qbcu::Re{c6}',  params[5])
    parameters.set('qbcu::Re{c7}',  params[6])
    parameters.set('qbcu::Re{c8}',  params[7])
    parameters.set('qbcu::Re{c9}',  params[8])
    parameters.set('qbcu::Re{c10}', params[9])
    dbcu = eos.Observable.make("B::Gamma(dbcu)", analysis.parameters, eos.Kinematics(), eos.Options(model = "WET")).evaluate()
    sbcu = eos.Observable.make("B::Gamma(sbcu)", analysis.parameters, eos.Kinematics(), eos.Options(model = "WET")).evaluate()
    return dbcu + sbcu

def extract_quadratic_form(posterior):
    """
    Extracts the quadratic matrix M from the quadratic function f(x).
    """
    # Calculate the quadratic matrix M such that Gamma(x) = C^dagger . M . C

    M = np.zeros((10,10))
    # compute diagonal
    for i in range(10):
        e_i = np.zeros(10)
        e_i[i] = 1
        M[i,i] = gamma(e_i, posterior)
    # compute off-diagonal
    for i in range(10):
        e_i = np.zeros(10)
        e_i[i] = 1
        for j in range(i+1,10):
            e_j = np.zeros(10)
            e_j[j] = 1
            M[i,j] = (gamma(e_i + e_j, posterior) - M[i,i] - M[j,j]) / 2
            M[j,i] = M[i,j]

    return M


# Extract the matrix M numerically using numdifftools
M_numerical = extract_quadratic_form("WET-2")

# define projection matrices projection method
def p_matrix(i, j):
    p = np.zeros((2,10))
    p[0,i] = 1
    p[1,j] = 1
    return p

# projected matrix (Gamma_exp_red = 0.476312, Gamma_SM = 0.1734810284496481)
def m_ij(i,j,SM):
    mxp = np.matmul(np.linalg.inv(M_numerical), np.transpose(p_matrix(i, j)))
    pxmxp = np.matmul(p_matrix(i,j), mxp)
    if SM == True:
        return np.linalg.inv(pxmxp) / (0.476312 - 0.1734810284496481)
    elif SM == False:
        return np.linalg.inv(pxmxp) / 0.476312

# get ellipse parametrization from projected matrix m_ij
def get_parametrization(i,j,SM):
    M_ij = m_ij(i,j,SM)
    a = M_ij[0,0]
    b = M_ij[1,1]
    c = 2 * M_ij[0,1]
    return a, b, c

# define ellipse for parameters a,b,c
def ellipse(a,b,c,x,y):
    return a * x**2 + b * y**2 + c * x * y - 1

# plot ellipses
def plot_ellipses(ax, start, stop, SM=True):
    nWC = stop - start + 1
    #define meshgrid for plotting
    x_ellipse = np.linspace(-12, 12, 2500)
    y_ellipse = np.linspace(-12, 12, 2500)
    X, Y = np.meshgrid(x_ellipse, y_ellipse)
    # compute ellipse parametrizations
    aArray = np.zeros((nWC, nWC))
    bArray = np.zeros((nWC, nWC))
    cArray = np.zeros((nWC, nWC))
    for i in range(1, nWC):
        for j in range(i):
            params = get_parametrization(i + start - 1, j + start - 1, SM)
            aArray[i,j] = params[0]
            bArray[i,j] = params[1]
            cArray[i,j] = params[2]
    # plot ellipses
    for i in range(1, nWC):
        for j in range(i):
            Z = ellipse(aArray[i][j],bArray[i][j],cArray[i][j],X, Y)
            ax[i,j].contour(Y, X, Z, levels=[0], colors='C2')