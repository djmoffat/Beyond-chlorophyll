# Beyond Chlorophyll: Machine Learning Estimates of Diagnostic Phytoplankton Pigments from Multispectral Ocean Colour Data

> Repository accompanying the manuscript:
>
> **Beyond chlorophyll: machine learning estimates of diagnostic phytoplankton pigments from multispectral ocean colour data**

**Repository status:** This repository accompanies a manuscript currently undergoing peer review. Minor updates may occur prior to publication.

---

## Overview

Phytoplankton pigments provide important information on marine ecosystem structure, community composition, and phytoplankton functional groups. However, most satellite ocean-colour applications focus primarily on chlorophyll-*a*.

This repository contains the code used to investigate whether multispectral ocean-colour observations contain information that can be used to estimate diagnostic pigments beyond chlorophyll-*a* alone.

Two machine-learning approaches were evaluated:

- Random Forest (RF)
- TabPFN (Tabular Prior-data Fitted Network)

and compared against a baseline Random Forest model using chlorophyll-*a* as the sole predictor, and a Random Forest model trained using only Rrs.

Target pigments include:

- Chlorophyll-*b* (TChlb)
- Alloxanthin (Allo)
- 19'-Butanoyloxyfucoxanthin (But)
- Fucoxanthin (Fuco)
- 19'-Hexanoyloxyfucoxanthin (Hex)
- Peridinin (Peri)
- Zeaxanthin (Zea)

---

## Scientific Objectives

The study addresses three primary questions:

1. Can diagnostic phytoplankton pigments be estimated from multispectral ocean-colour observations?
2. Does a foundation model (TabPFN) improve predictive skill relative to a conventional Random Forest model?
3. How much additional information is provided by multispectral ocean-colour observations beyond satellite-derived chlorophyll-*a* alone?

---

## Input Variables

Model inputs include:

### Satellite-Derived Variables

- Rrs 412 nm
- Rrs 443 nm
- Rrs 490 nm
- Rrs 510 nm
- Rrs 560 nm
- Rrs 665 nm
- Chlorophyll-*a*
- Diffuse attenuation coefficient at 490 nm (Kd490)

---

## Data Partitioning

Oceanographic observations are often strongly autocorrelated in both space and time.

To evaluate model generalisation to unseen conditions, the match-up dataset was partitioned by withholding complete years for independent validation:

### Validation Years

```text
2002
2007
2012
2017
```

All remaining years were used for model development and hyperparameter optimisation.

This approach ensures that validation observations were completely withheld during model training.

---

## Model Development

Three models were developed:

### RFchl Baseline

Random Forest using only satellite-derived chlorophyll-*a* as a predictor.

### Rrs

Random Forest using only the Rrs predictor set.

### Random Forest (RF)

Random Forest using the complete predictor set.

### TabPFN

Tabular Prior-data Fitted Network (TabPFN) foundation model trained using the complete predictor set.

---

## Model Evaluation

Models were evaluated using:

- Pearson correlation coefficient (*r*)
- Bias
- Root Mean Square Difference (RMSD)
- Centred Pattern RMSD (CP-RMSD)
- Coefficient of determination (*R²*)
- Mean Absolute Error (MAE)

---

## Reproducing the Analysis

### Create the environment

Using Conda:

```bash
conda env create -f environment.yml
conda activate pigment_ml
```

### Launch Jupyter

```bash
jupyter lab
```

or

```bash
jupyter notebook
```

### Run the workflow

Open and execute:

```text
train_model_and_predict.ipynb
```

---

## Data Availability

The match-up dataset combines:

- High-performance liquid chromatography (HPLC) pigment observations
- Satellite ocean-colour products

Availability of the original observations may be subject to restrictions imposed by the source data providers.

Where permitted, processed data products required to reproduce the analyses will be made available alongside this repository.

---

## Software Environment

The analysis was developed and tested using the software environment below.

| Component | Version |
|------------|------------|
| Python | 3.13.9 |
| NumPy | 2.3.5 |
| Pandas | 2.3.3 |
| Matplotlib | 3.10.6 |
| Seaborn | 0.13.2 |
| Scikit-learn | 1.7.2 |
| SHAP | 0.52.0 |
| TabPFN | 8.0.3 |

The complete software environment required to reproduce the analysis can be recreated using either:

Exact package versions are provided in:

```text
environment.yml
```

and

```text
requirements.txt
```

---

## Reproducibility

This repository contains:

- Data preparation workflows
- Model training scripts
- Hyperparameter optimisation routines
- Evaluation workflows
- SHAP analysis code
- Spatial autocorrelation analysis code
- Figure generation scripts

All manuscript and supplementary figures can be regenerated using the notebooks provided.

---

## Citation

If you use this repository, please cite the accompanying manuscript:

```bibtex
@article{moffat2026beyondchlorophyll,
  title={Beyond chlorophyll: machine learning estimates of diagnostic phytoplankton pigments from multispectral ocean colour data},
  author={Moffat, David and others},
  year={2026}
}
```

---

## Contact

**David Moffat**  
dmof@pml.ac.uk
AI and Data Science Lead  
Plymouth Marine Laboratory

For questions regarding the repository or manuscript, please open a GitHub issue.

---

## License

This repository is released under the MIT License unless otherwise stated.
