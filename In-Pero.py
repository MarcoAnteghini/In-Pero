#!/usr/bin/env python


import pickle
import os
import numpy as np
from Bio import SeqIO
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf

def is_fasta(filename):
    with open(filename, "r") as handle:
        fasta = SeqIO.parse(handle, "fasta")
        return any(fasta)

tf.set_random_seed(42)
np.random.seed(42)

fastafile=sys.argv[1]


from unirep import babbler1900 as babbler

# Where model weights are stored.
# Here we consider the directory where the script is executed. Insert the proper path below if needed.
MODEL_WEIGHT_PATH = "."
b = babbler('1900_weights')

print('UniRep Encoding:')
with open(fastafile, "r") as handle:
    if is_fasta(fastafile):
        fasta = SeqIO.parse(handle, "fasta")
        d={}
        for record in fasta:
            try:
                sequence=record.seq
                ids=record.id
                d[ids.split('|')[1]] = sequence
                    
            except:
                print('Something wrong','\n','fasta file should start with >sp|ID|ORGANISM')
                pass
                     
        c=0
        for keys in d:
            try:
                ur = b.get_rep(d[keys])
                tosave1 = np.asarray(ur[0])
        #        tosave2 = np.asarray(ur[1])
        #        tosave3 = np.asarray(ur[2])
# We here save just one of the 3 arrays that Unirep produces.
                np.save(keys+'_UniRep1', tosave1)
        #        np.save(ids.split('|')[1]+'_UniRep2', tosave2)
        #        np.save(ids.split('|')[1]+'_UniRep3', tosave3)
                c=c+1
                print('ID:',keys,' '*20,c,'/',len(d))
            except:
                pass
#        print('Not encoded:',to_check)
                       
    else:
        print('YOU HAVE TO INPUT A CORRECT FASTA FILE')

from subprocess import Popen, PIPE
print('\n'*2)
print('SeqVec encoding:','\n')

p1 = Popen(["seqvec", "-i", fastafile, "-o", fastafile[:-6]+str('_seqvec.npz'),"--protein","True"], stdout=PIPE)

p1.communicate()

filename='LR_model2.sav'

LR_model = pickle.load(open(filename, 'rb'))

unireps = {}
for filenames in os.listdir('.'):
    if filenames.endswith('UniRep1.npy'):
        unireps[filenames.split('_')[0]] = np.load(filenames)

seqvecs = {}
seqvec_archive = np.load(fastafile[:-6]+str('_seqvec.npz'), allow_pickle=True)
for uniprotid in seqvec_archive.files:
    seqvecs[uniprotid] = seqvec_archive[uniprotid]

final_d={}
for keys in seqvecs.keys():
    for k in unireps.keys():
        if k==keys:
            final_d[k]= np.concatenate([seqvecs[k], unireps[k]])

membrane, matrix = [],[]
for uniprotid in final_d:
    pred = LR_model.predict(final_d[uniprotid].reshape(1, -1))[0]
    if pred==1:
        membrane.append(uniprotid)
    else:
        matrix.append(uniprotid)
print('\n'*2)
print('Matrix proteins: ',matrix)
print('Membrane proteins: ',membrane)



notenc=set(seqvecs.keys())-set(unireps.keys())

    



output = open(fastafile[:-6]+str('_output.txt'), 'w')
output.write("%s\n" % 'pred membrane:')
for e in membrane:
    output.write("%s\n" % e)
output.write("%s\n" % 'pred matrix:')
for e in matrix:
    output.write("%s\n" % e)
output.write("%s\n" % 'not encoded:')
for e in notenc:
    output.write("%s\n" % e)
output.close()


