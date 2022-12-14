import sympy as sp
import numpy as np

x, y, lamda = sp.var('x y lambda')
f = 4*x**3 + y**2
g = 2*x**2 + y**2 - 1
L = f - lamda*g


def main():
    gradL = [sp.diff(L, i) for i in [x, y]]
    eqs = gradL + [g]
    solution = sp.solve(eqs, [x, y, lamda], dict=True)
    hessian = [[sp.diff(sp.diff(L, i), j) for i in [lamda, x, y]]for j in [lamda, x, y]]
    for sol in solution:
        H = sp.Matrix(hessian)
        valor = f
        for var, val in sol.items():
            H = H.subs(var, val)
            valor = valor.subs(var, val)
        sol["f"] = valor
        H = np.linalg.det(np.array(H.tolist(), dtype=float))
        sol["h"] = H
    for sol in solution:
        if sol["h"] > 0:
            print("Se tiene un maximo local en: ")
        elif sol["h"] < 0:
            print("Se tiene un minimo local en: ")
        else:
            print("No se puede conluir nada sobre el punto critico en: ")
        print("x: ", sol[x])
        print("y: ", sol[y])
        print("Con un valor de f de: ", sol["f"], "\n")


if __name__ == '__main__':
    main()
