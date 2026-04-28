# MT Dataset Cleaning and Structure Pipline

This project cleans and chunks Machine Translation datasets from `.jsonl` files for training preparation.

## Structure Original Dataset
```bash

cadt_mt_dataset/
├── 10_Paracrawl
│   └── en-km.classified
├── 11_Opus
│   └── en-km.txt
├── 1_parallel_corpus
│   ├── adhoc
│   │   ├── adhoc-en
│   │   └── adhoc-km
│   ├── bible
│   │   ├── bible-en
│   │   ├── bible-km
│   │   ├── kcb-en
│   │   └── kcb-km
│   └── licadho
│       ├── licadho-en
│       └── licadho-km
├── 2_km_parallel
├── 3_Back_Translation
│   └── clean_v1
├── 4_nict_corpus
│   ├── en
│   └── km
├── 5_eccc
│   ├── 5_eccc-en
│   └── 5_eccc-km
├── 6_Open_Institute
│   ├── 6_Open_Institute-en
│   └── 6_Open_Institute-km
├── 7_Data_from_NMT
│   └── cadt-btec
├── 8_construction_realestate_230421
└── 9_Vichet
    └── category_9_parts

34 directories

```

### Note
* Category12:
    * Origin: mfaic_pair.jsonl
    * Website: https://kiripost.com/
* Category13:
    * Origin: kripost_parallel_articles.jsonl
    * Website: https://www.mfaic.gov.kh

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

## Output Structure
```base
structure_mt_dataset/
├── category10.jsonl
├── category11.jsonl
├── category12.jsonl
├── category13.jsonl
├── category1.jsonl
├── category2.jsonl
├── category3.jsonl
├── category4.jsonl
├── category5.jsonl
├── category6.jsonl
├── category7.jsonl
├── category8.jsonl
└── category9.jsonl
├── kiripost_parallel_articles.jsonl
└── mfaic_pair.jsonl
```
Example:

```bash
sample_file/
├── chunk_0001.km
├── chunk_0001.en
└── summary.json
```
