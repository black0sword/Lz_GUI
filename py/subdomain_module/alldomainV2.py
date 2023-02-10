import subprocess
#a0 = "cd ESD &  python  ESD.py  1.txt"
a1 = "cd OneForAll  & python OneForAll.py  --brute --targets  1.txt  run"
#a2 = "cd subDomainsBrute &  python  subDomainsBrute.py  -t 100  --full  1.txt"
a3 = "cd subfinder  & subfinder.exe  -dL 1.txt  -o    ok.txt"
 
def main():
    #p0 = subprocess.Popen(a0, shell=True)
    #print(p0.wait())
    p3 = subprocess.Popen(a3, shell=True)
    print(p3.wait())
    p1 = subprocess.Popen(a1, shell=True)
    print(p1.wait())
    #p2 = subprocess.Popen(a2, shell=True)
    #print(p2.wait())

if __name__ == '__main__':
    main()