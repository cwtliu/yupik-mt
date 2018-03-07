#! /bin/bash

#SBATCH --job-name=yupik
#SBATCH --ntasks=10
#SBATCH --partition=normal
#SBATCH --cpus-per-task=1

for i in {1..70}
do
    srun -n1 --exclusive python parser.py ../data/parser/yupik_dev_$i.txt > ../data/parser/yupik_dev_parsed_$i.txt &
done
wait
