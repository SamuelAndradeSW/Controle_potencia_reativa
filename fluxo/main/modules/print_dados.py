

import numpy as np

class Print_dados:
    def __init__(self, thetaD, volt, barras, tipobar, linhas, Pkm, Qkm, k, m, iteracoes, Q, Q_gerado, P_gerado, POT):
        self.volt = volt 
        self.barras = barras
        self.tipobar = tipobar
        self.thetaD = thetaD
        self.linhas = linhas
        self.Pkm = Pkm
        self.Qkm = Qkm
        self.k = k
        self.m = m
        self.iteracoes = iteracoes
        self.Q = Q
        self.Q_gerado = Q_gerado
        self. P_gerado = P_gerado
        self.POT = POT
        
    def print_fluxo(self):
        print("\nNúmero de iterações:", self.iteracoes,"\n")
        print("==========================================================================================================================\nVariáveis de estado\n==========================================================================================================================\n")
        print("\n{:<8} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('Barra', 'Tipo', 'V', 'Theta', 'Carga ativa', ' Carga reativa', ' Geração ativa', 'Geração reativa'))
        print("\n--------------------------------------------------------------------------------------------------------------------------\n")
        
        
        for pt in range(self.barras):
            print("{:<8} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(pt+1, self.tipobar[pt, 0], round(self.volt[pt, 0], 3), round(self.thetaD[pt, 0], 3), round(self.POT[pt, 0], 3)*10**2, round(self.Q[pt, 0], 3)*10**2, round(self.P_gerado[pt, 0], 3), round(self.Q_gerado[pt, 0], 3) ))
        print("\n Legenda: \n Tipo barra = 0 - Barra PQ \n Tipo barra = 1 - Barra PV \n Tipo barra = 2 - Barra REFERENCIA \n" )
        
        print("\n\n\n\n=================================================================\nFluxo de carga\n=================================================================\n")
        print("{:<8} {:<15} {:<15} {:<15} \n-------------------------------------------------------------\n".format('De', 'Para', 'Pkm (MW)', 'Qkm (Mvar)'))
        
        for fp in range(self.linhas):
            p = self.k[fp,] - 1
            q = self.m[fp,] - 1
            print("%1s %10s %18s %15s" % (p+1, q+1, np.around(self.Pkm[p,q], 2), np.around(self.Qkm[p,q], 2)))
        
            



