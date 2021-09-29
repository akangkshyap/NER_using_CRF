# NER_using_CRF
Named Entity Recognition using CRF toolkit

Step 1 : python NER_corpus.py


Step 2 : crf_learn -c 3.0 template train.data model -t


Step 3 : crf_test -m model test.data>result.txt


Step 4 : python NER_accuracy.py


Step 5 : python NER_run.py


