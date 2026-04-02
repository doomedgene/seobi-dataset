# SEOBI

SEOBI (Semantically Enriched Oracle Bone Inscription Dataset) is a sentence-level semantic annotation dataset for oracle bone inscriptions, built upon the [OBIMD](https://huggingface.co/datasets/Redstone-OBI/OBIMD) corpus.

This dataset accompanies the paper:

> **A sentence-level semantic annotation dataset for oracle bone inscriptions**
> *Scientific Data* (under review)

## Repository structure

```
seobi-dataset/
├── README.md
├── SCHEMA.md
├── LICENSE
├── data/
│   ├── sentences.csv          (17,150 rows)
│   ├── sentence_themes.csv    (6,407 rows)
│   ├── entity_mentions.csv    (6,260 rows)
│   └── entity_linkage.csv     (2 rows)
├── docs/
│   ├── thematic_trigger_lexicon.csv  (90 entries)
│   ├── keyword_rules.md
│   ├── entity_rules.md
│   └── undeciphered_support_rules.md
└── examples/
    └── read_seobi.py
```

## Data files

- **`sentences.csv`**: Master sentence table of curated InscriptionSentence records.
- **`sentence_themes.csv`**: Sentence-level thematic annotations (positive-only long format) across five categories: ritual, rain, agriculture, war, and spatial.
- **`entity_mentions.csv`**: Mention-level entity annotations with a three-tier schema (entity_phase, entity_type, entity_subtype) and confidence scoring.
- **`entity_linkage.csv`**: Canonical-level cross-phase linkage relations.

Field definitions for all CSV files are provided in `SCHEMA.md`.

## Cross-file linking

Records are linked across files through the composite key (`bone_id`, `group_order`), which uniquely identifies each sentence. All CSV files use UTF-8 encoding.

## License

[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Citation

## Citation

If you use this dataset, please cite:

[作者]. SEOBI: A sentence-level semantically annotated dataset for 
oracle bone inscriptions. Zenodo https://doi.org/10.5281/zenodo.19382489 (2026).
