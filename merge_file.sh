#!/bin/bash

find /result/data/ -name *.txt -exec cat {} + > DATI.csv
mv /result/data/DATI.csv /result/