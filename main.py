from Chromosome import Chromosome
from Network import Network
from ComputeGA import ComputeGA
problParam={}
problParam['noChromos']=100

def main():
    net=Network("mat.txt")
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
