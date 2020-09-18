# In-Pero: Prediction of sub-peroxisomal localisation using deep learning embeddings and logistic regression.

To use the In-Pero.py script, you first need to download and install:

#### 1) seqvec 
Instructions are available here: https://github.com/Rostlab/SeqVec.

or 

`pip install seqvec`

https://pypi.org/project/seqvec/

#### 2) UniRep and the related weight files, in this case we used the 1900_weights.

https://github.com/churchlab/UniRep

Make sure you download the 1900_weights directory and place it together with the other files in this repository.

For example you can first install awscli: 

`pip install awscli`

Then download the weights with

`aws s3 sync --no-sign-request --quiet s3://unirep-public/1900_weights/ 1900_weights`


#### 3) The pre-computed model 'LR_model2.sav' is also required.

#### 4) Additional requirements

Suggested packages:

- `numpy 1.17.2`
- `biopython 1.77`
- `tensorflow 1.14`
- `pandas 0.25.1`
- `scikit-learn 0.22`
- `seqvec 0.4.1`
- `scipy 1.4.1`





#### Usage of `In-Pero.py`


Usage:

`./In-Pero.py <filename>.fasta`


Outputs:

- Log file ('\<filename\>_output.txt') containing the entries subdivided in matrix and membrane proteins.
- The UniRep encoding
- The seqvec encoding

### This repository contains:


- In-Pero_models : directory containing all the pre-computed models
- LR_model2.sav : The LR pre-computed model 
- PP_matrix.fasta : fasta file containg the matrix proteins used for building the dataset 
- PP_membrane.fasta : fasta file contain the membrane proteins used for building the dataset

- useful scripts retrived from the UniRep Github repository (see above):
  - data_utils.py
  - unirep.py
  - utils.py
