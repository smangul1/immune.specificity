import csv
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('infile', help='')
ap.add_argument('out', help='')
args = ap.parse_args()



#"","sraId","kmer","desName"
#"1","DRR006374","AGLAAF","malaria1"


dict={}
diseaseSet=set()
diseaseDict={}
kmerSet=set()



file=open(args.infile)

reader=csv.reader(file)

next(reader,None)

for line in reader:
    disease=line[3]
    kmer=line[2]
    sample=line[1]
    
    if disease not in diseaseSet:
        diseaseDict[disease]=set()
    
    diseaseDict[disease].add(sample)
    diseaseSet.add(disease)
    kmerSet.add(kmer)




file.close()



number_sample_disease={}
for key, value in diseaseDict.items():
    number_sample_disease[key]=len(value)


print "Number of phenotypes", len(diseaseSet)
print "Number of kmers", len(kmerSet)
print "Number of samples per phenotype", len(kmerSet)

print number_sample_disease


index={}
for k in kmerSet:
    dict[k]=[0] * len(diseaseSet)


k=0
for d in diseaseSet:
        index[d]=k
        k+=1


file=open(args.infile)

reader=csv.reader(file)

next(reader,None)

for line in reader:
    disease=line[3]
    kmer=line[2]
    dict[kmer][index[disease]]+=1

file.close()


print dict



file=open(args.out,"w")


for key, value in dict.items():
    
    a=map(str, value)
    
    file.write(key + ","+ ','.join(a))
    file.write("\n")






