# MT Dataset Cleaning and Structure Pipline

This project cleans and chunks Machine Translation datasets from `.jsonl` files for training preparation.

## Features

* Filters invalid or low-quality sentence pairs
* Removes flagged, empty, or HTML-containing records
* Checks sentence length and source-target ratio
* Splits data into chunks of 10,000 pairs
* Saves Khmer (`.km`) and English (`.en`) files
* Generates a summary report (`summary.json`)

## Project Structure

```bash
├── structure_mt_dataset
└── structure_data.py            # Main script
```

## Run

```bash
python structure_data.py
```


## Output

Generated files will be in:

```bash
structure_mt_dataset/
```

Example:

```bash
sample_file/
├── chunk_0001.km
├── chunk_0001.en
└── summary.json
```
