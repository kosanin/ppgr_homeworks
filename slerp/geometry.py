import numpy as np
import math

def Rx(alpha):
    return np.matrix([
        [1, 0, 0],
        [0, math.cos(alpha), -math.sin(alpha)],
        [0, math.sin(alpha), math.cos(alpha)]
    ])

def Ry(alpha):
    return np.matrix([
        [math.cos(alpha), 0, math.sin(alpha)],
        [0, 1, 0],
        [-math.sin(alpha), 0, math.cos(alpha)]

    ])

def Rz(alpha):
    return np.matrix([
        [math.cos(alpha), -math.sin(alpha), 0],
        [math.sin(alpha), math.cos(alpha), 0],
        [0, 0, 1]
    ])

def normalize(v):
    """

    :param v: vektor
    :return: normalizovan vektor
    """
    return v / np.linalg.norm(v)


def eulerA2(phi, theta, psi):
    """

    :param phi: ugao rotacije oko X ose
    :param theta: ugao rotacije oko Y ose
    :param psi:  ugao rotacije oko Z ose
    :return: matrica rotacije
    """
    return np.linalg.multi_dot([Rz(psi), Ry(theta), Rx(phi)])

def eigenvector(A):
    """

    :param A: lista listi / matrica
    :return: jedinicni sopstveni vektor za lambda = 1
    """
    T = A - np.identity(3)
    # koristimo flatten jer je T matrica pa np.cross vraca [[...]]
    v = np.cross(T[0], T[1]).flatten()
    if not any(v):
        tmp = np.cross(T[1], T[2]).flatten()
        if not any(tmp):
            v = np.cross(T[0], T[2]).flatten()
        else:
            v = tmp
            
    return v / np.linalg.norm(v)

def perpVec(v):
    """

    :param v: jedinicni vektor
    :return:
    """

    # TODO nije uzeta greska u obzir
    # npr 1.123000e-18 == 0 => True ?

    u = [0, 1, 0]
    for pair in zip(u, v):
        if pair[0] != pair[1]:
            return u

    return [1.0, 0, 0]

def axisAngle(A):
    """

    :param A: matrica / lista listi
    :return: prava rotacije, ugao rotacije
    """

    p = eigenvector(A)
    u = normalize(np.cross(p, perpVec(p)))
    # np.dot vraca [[...]] pa transformisemo u listu listi i uzimamo prvi element
    u_ = normalize(np.dot(A, u).tolist()[0])

    scalar_prod = np.dot(u, u_)
    if scalar_prod > 1: scalar_prod = 1.0
    elif scalar_prod < -1: scalar_prod = -1.0

    phi = math.acos(scalar_prod)

    # ako je mesoviti proizvod manji od nule, menjamo orijentaciju
    if np.linalg.det([p, u, u_]) < 0:
        p = -p

    return (p, phi)


def axisAngle2Q(p, phi):
    """

    :param p: prava rotacije
    :param phi: ugao rotacije
    :return: kvaternion td Cq = Rp(phi)
    """
    w = math.cos(phi / 2)

    # x, y, z
    v = math.sin(phi / 2) * normalize(p)

    return np.append(v, w)


def Q2AxisAngle(q):
    """

    :param q: jedinicni kvaternion = niz duzine 4
    :return: jedinicni vektor p; ugao rotacije phi td Cq = Rp(phi)
    """
    if (q[3] < 0):
        q = (-1) * q

    phi = 2 * math.acos(q[3])

    if (abs(q[3]) == 1):
        p = [1, 0, 0]
    else:
        p = q[:3] / np.linalg.norm(q[:3])

    return (p, phi)

def slerp(q1, q2, t, tm):

    cos_theta = np.dot(q1, q2)
    if cos_theta < 0:
        q1 = list(map(lambda x: -x, q1))
        cos_theta = -cos_theta
    
    if cos_theta > 0.995:
        return q1
    
    theta = math.acos(cos_theta)
    c2 = t / tm
    c1 = 1 - c2
    sin_theta = math.sin(theta)
    coef_a = math.sin(theta * c1) / sin_theta
    coef_b = math.sin(theta * c2) / sin_theta

    qs = np.dot(coef_a, q1) + np.dot(coef_b, q2)
    return normalize(qs)

def eulerAngles2quaternion(phi, theta, psi):
    A = eulerA2(phi, theta, psi)
    p, alpha = axisAngle(A)
    return axisAngle2Q(p, alpha)