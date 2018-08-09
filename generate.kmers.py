import csv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('infile', help='csv')
ap.add_argument('out', help='kmers')
args = ap.parse_args()


file=open(args.infile)
#0,SRR3724634,CASRGLARKPPWRNEGEGRRAAPPGGGSPGGGGAGRGESAATGLA,TRA,37,TRAV17,NA,TRAJ35


dict={}

file=open(args.infile)
reader=csv.reader(file)
next(reader,None)
for line in reader:
    sample=line[1]
    dict[sample]=set()

file.close()


print dict

file=open(args.infile)
reader=csv.reader(file)
next(reader,None)
for line in reader:
    type=line[3]
    sample=line[1]
    cdr3=line[2]
    for i in range(len(cdr3)-6+1):
        kmer=cdr3[i:i+6]
        dict[sample].add(kmer)

#desName,sraId
#alopecia areata,SRR3441819
#alopecia areata,SRR3441818




fileOut=open(args.out,'w')

for key, value in dict.items():
	for s in value:
		fileOut.write(key+","+s)
		fileOut.write('\n')



