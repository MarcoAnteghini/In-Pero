# In-Pero: Prediction of sub-peroxisomal localisation using deep learning embeddings and logistic regression.

To use the In-Pero.py script, you first need to download and install seqvec. 
Instructions are available here: https://github.com/Rostlab/SeqVec.
Another possipility is also simply use: pip install seqvec (https://pypi.org/project/seqvec/)

In addition, also UniRep is required (https://github.com/churchlab/UniRep)

You can also dowload the directory 1900_weights and the files ulits.py, unirep.py from here.

Finally the pre-computed model 'LR_model2.sav' is also required.

You can also check the List_of_used_packeges for building your on conda environment.



Usage of In-Pero.py

./In-Pero.py file.fasta


Output:
Log file containing the entries subdivided in matrix and membrane proteins.
