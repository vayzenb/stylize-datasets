#!/bin/bash -l

# Job name
#SBATCH --job-name=train_stylize_ecoset

#SBATCH --mail-type=ALL
#SBATCH --mail-user=vayzenb@cmu.edu

# Submit job to cpu queue                
#SBATCH -p gpu

#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:1

# Job memory request
#SBATCH --mem=32gb

# Time limit days-hrs:min:sec
#SBATCH --time 7-00:00:00

# Exclude
#SBATCH --exclude=mind-1-30

# Standard output and error log
#SBATCH --output=train_stylize_ecoset.out

conda activate ml

python3 stylize.py --content-dir '/user_data/vayzenbe/image_sets/ecoset/train/0001_man' --style-dir '/user_data/vayzenbe/GitHub_Repos/Stylized-ImageNet/code/paintings_raw/train/' --output-dir '/lab_data/behrmannlab/image_sets/stylized-ecoset/train/0001_man'