# Mammal Classification Project

A personal experiment using CLIP (Contrastive Language-Image Pre-Training) model for zero-shot mammal image classification.

## Overview

This project uses the OpenAI CLIP model to classify mammal images without specific training. It tests how well a general-purpose vision model can distinguish between different mammal species.

## Data

Uses the "Happy Mammals" dataset from Kaggle, containing 128x128 pixel images of various mammal species.

## Setup

1. Install required packages:
```bash
pip install transformers kagglehub pandas pandasql
```

2. Run the Jupyter notebook to:
   - Load the CLIP model
   - Download the dataset
   - Process images
   - Generate classification results

## Notes

This is a personal exploration project to experiment with zero-shot image classification using transformer models.
