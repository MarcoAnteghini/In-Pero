# In-Pero: Prediction of sub-peroxisomal localisation using deep learning embeddings and logistic regression.

To use the In-Pero.py script, you first need to download and install:

1) seqvec 
Instructions are available here: https://github.com/Rostlab/SeqVec.

Another possipility is also simply use: 
<pip install seqvec>
https://pypi.org/project/seqvec/

2) UniRep and the related weight files, in this case we used the 1900_weights.

https://github.com/churchlab/UniRep

Make sure you download the 1900_weights directory and place it toghether with the other files in this repository.


3) The pre-computed model 'LR_model2.sav' is also required.

You can also check the List_of_used_packeges for building your own conda environment.

Important are: 
Numpy
Biopython
Tensorflow 1
Pandas
Scikit





Usage of In-Pero.py

./In-Pero.py file.fasta


Output:
Log file containing the entries subdivided in matrix and membrane proteins.
