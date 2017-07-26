#!/bin/bash

# Be sure to replace '../fasttext/models' with the directory
# where you store your pre-trained models

cgrs_sess=95
while [ "$cgrs_sess" -lt 115 ]; do
    echo "Querying vectors for Senate $cgrs_sess"
    cat ./queries/namelist_S"$cgrs_sess".txt | ../fasttext/fasttext print-word-vectors\
     ../fasttext/models/nyt_1981-2016.bin > ./queried_vectors/nyt_97-114/S"$cgrs_sess".vec
    cgrs_sess=$((cgrs_sess + 1))
done