from Chromosome import Chromosome
from Network import Network
from ComputeGA import ComputeGA
from math import sqrt;

problParam={}
problParam['noChromos']=100
'''
 public static double distantaEuclidiana(float a1,float a2, float b1,float b2){
        double d1=Math.pow(a1-b1,2);
        double d2=Math.pow(a2-b2,2);
        return Math.abs(Math.sqrt(d1+d2));
    }
    '''
def getdist(a1,a2,b1,b2):
    d1=pow(a1-b1,2)
    d2=pow(a2-b2,2)
    return  abs(sqrt(d1+d2))

def read_mat():
    f = open("berlin.txt", "r")
    n = int(f.readline())
    lista_nod=[]
    mat = []
    for i in range(n):
        lista_nod.append([])
        line = f.readline()
        elems = line.split(" ")
        for j in range(1,3):
            lista_nod[-1].append(float(elems[j]))
    f.close()
    for i in range(n):
        mylinie=[]
        for j in range(n):
            dist=getdist(lista_nod[i][0],lista_nod[i][1],lista_nod[j][0],lista_nod[j][1])
            mylinie.append(dist)
        mat.append(mylinie)
    f=open("berlinMat.txt","w+")
    f.write("%d " % n)
    f.write("\n")
    for i in range(n):
        for j in range(n):
            f.write("%d," % int(mat[i][j]))
        f.write("\n")
    f.close()

def main():
    #read_mat()
    net=Network("berlinMat.txt")
    problParam['noNodes']=net.net['noNodes']
    problParam['noGen']=1000
    problParam['net']=net
    compute=ComputeGA(problParam,net)
    compute.compute_all()
    #print('best:')
    print(compute.get_best_chromo())
    compute.write_to_file("out.txt")


if __name__ == "__main__":
    main()
