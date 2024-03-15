# Optimizing OpenBookQA with Dataset Augmentation
This repo contains all scripts used within "Optimizing OpenBookQA: Investigating the Impact of Pretraining with Diverse Scientific Knowledge" by Rohith Leeladharan, Parum Misri, Archit Pantankar, and Oleg Ianchenko as a final project for UW CSE 447.  A description of each script and notebook is contained within the paper.

## File Structure
Below are descriptions of all folders contained within this repo.

### ./data/
Contains all processed datasets which were used within training all eight models. Inside ./data/formatting are all the scripts used to process each dataset, after they have been downloaded from HuggingFace. If you are planning to execute any of the formatting scripts, update paths as necessary inside each script.

### ./notebooks/
Contains all notebooks used to train the eight models. Note that these notebooks are all named to describe the configuration of the model that is going to be evaluated. Note that because these notebooks were originally used in Google Colab, if you intend to rerun them outside that environment, there will be certain functions that are unavailable and modification will be necessary.

After the pretraining step, the best validation accuracy checkpoint will be saved to a folder. Prior to fine-tuning, the checkpoint must be properly specified by setting the PRETRAINED_MODEL_PATH variable.