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

- `docs/SCHEMA.md`: field descriptions for the released data tables

Additional rule documentation and usage examples may be added in later updates.

## Notes

- All CSV files are encoded in UTF-8.
- Some rare glyphs or placeholder symbols may not render correctly in spreadsheet software or under fonts without full CJK extension support.
- Sentence-level records are linked across files through shared record fields and composite sentence keys based on the source record and sentence position.

## License

License information will be added in the repository `LICENSE` file.

## Citation

Citation information will be added after the formal data release is finalized.
