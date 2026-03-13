# seobi-dataset
SEOBI: A sentence-level semantically annotated dataset for oracle bone inscriptions.
# SEOBI

SEOBI (Semantically Enriched Oracle Bone Inscription Dataset) is a sentence-level semantically annotated dataset for oracle bone inscriptions. The current release provides curated inscription sentences together with thematic annotations, entity mentions, and canonical linkage records.

## Repository contents

The current repository includes the following core data files:

- `data/sentences.csv`: master sentence table of curated inscription sentences
- `data/sentence_themes.csv`: sentence-level thematic annotations in long format
- `data/entity_mentions.csv`: unified entity mention table
- `data/entity_linkage.csv`: unique canonical-level linkage relations between entities

Additional documentation files are provided in the `docs/` directory.

## Documentation

The repository currently includes the following documentation files:

- `docs/SCHEMA.md`: field descriptions for the released data tables
- `docs/keyword_rules.md`: summary of the thematic trigger rules used in the released thematic annotations
- `docs/entity_rules.md`: summary of the rule-based entity annotation procedures
- `docs/undeciphered_support_rules.md`: summary of the conservative support procedure for partially deciphered sentences

## Usage example

- `examples/read_seobi.py`: minimal example showing how to load the released data tables and retrieve thematic annotations and entity mentions for a sample sentence
## Repository structure

```text
seobi-dataset/
├── README.md
├── LICENSE
├── data/
│   ├── sentences.csv
│   ├── sentence_themes.csv
│   ├── entity_mentions.csv
│   └── entity_linkage.csv
├── docs/
│   └── SCHEMA.md
└── examples/

## Notes

- All CSV files are encoded in UTF-8.
- Some rare glyphs or placeholder symbols may not render correctly in spreadsheet software or under fonts without full CJK extension support.
- Sentence-level records are linked across files through shared record fields and composite sentence keys based on the source record and sentence position.

## License

License information will be added in the repository `LICENSE` file.

## Citation

Citation information will be added after the formal data release is finalized.
