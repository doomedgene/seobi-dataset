# SEOBI Schema

This document describes the structure and fields of the released SEOBI data files.

## Files

The current release includes the following core data tables:

- `data/sentences.csv`
- `data/sentence_themes.csv`
- `data/entity_mentions.csv`
- `data/entity_linkage.csv`

Additional documentation and rule files are described separately in the repository README.

## General notes

- All CSV files are encoded in UTF-8.
- Some rare glyphs or placeholder symbols may not render correctly in spreadsheet software or under fonts without full CJK extension support.
- Sentence-level records are linked across files through shared record fields and composite sentence keys based on the source record and sentence position, as described below.

## 1. `sentences.csv`

This file is the master sentence table of the SEOBI release. Each row corresponds to one curated inscription sentence retained for sentence-level semantic annotation.

### Record unit
- One row per sentence.

### Key fields
- `bone_id`: Identifier of the source oracle-bone record.
- `period_class`: Paleographic period label inherited from OBIMD.
- `group_order`: Sentence order or subgroup index within the source record.
- `sentence_simple`: The normalized sentence transcription used in the current release.

### Notes
- This table contains only curated `InscriptionSentence` records retained from OBIMD.
- Other released annotation tables are linked to this table through sentence-level identifiers or composite sentence keys based on the source record and sentence position.
- Some sentences contain undeciphered characters represented by placeholder forms in the transcription.

## 2. `sentence_themes.csv`

This file records sentence-level thematic annotations in long format. Each row corresponds to one positively assigned sentence–theme pair.

### Record unit
- One row per positive sentence–theme annotation.

### Key fields
- `bone_id`: Identifier of the source oracle-bone record.
- `period_class`: Paleographic period label associated with the sentence.
- `group_order`: Sentence order or subgroup index within the source record.
- `sentence_simple`: The normalized sentence transcription.
- `theme`: The assigned thematic category. In the current release, themes include `Ritual`, `Rain`, `Agriculture`, `War`, and `Spatial`.
- `detail_json`: Optional structured notes associated with the thematic annotation, when applicable.

### Notes
- This file stores only positively assigned thematic labels.
- A single sentence may appear in multiple rows if it receives more than one thematic label.
- Thematic labels are generated through rule-based matching procedures documented in the repository rule files.

## 3. `entity_mentions.csv`

This file records sentence-level entity mentions in the released SEOBI annotation layer. Each row corresponds to one annotated entity mention and includes both mention-level information and normalized entity attributes.

### Record unit
- One row per entity mention.

### Key fields
- `bone_id`: Identifier of the source oracle-bone record.
- `period_class`: Paleographic period label associated with the sentence containing the mention.
- `group_order`: Sentence order or subgroup index within the source record.
- `sentence_simple`: The normalized sentence transcription containing the mention.
- `surface_form`: The surface form of the entity mention as represented in the sentence.
- `canonical_entity_id`: Stable identifier for the normalized entity entry, when available.
- `canonical_name`: Normalized entity name, when available.
- `entity_phase`: Phase-level classification of the mention, distinguishing `living` and `posthumous` references.
- `entity_type`: Coarse semantic type of the mention. In the current schema, this field distinguishes `human`, `deity`, and `ancestor`.
- `entity_subtype`: Finer-grained subtype label of the mention, such as role- or identity-level categories.
- `entity_role`: Functional role of the mention in context, when applicable.
- `rule_hit`: Rule or matching pattern associated with the annotation, when available.
- `confidence`: Confidence label associated with the entity annotation, when applicable.
- `linked_entity_id`: Identifier used to represent strongly supported canonical linkage relations across forms or phases, when applicable.
- `resolution_method`: Annotation method used to derive the entity record, such as direct matching, period-based inference, or generic pattern matching.

### Notes
- This table integrates both living and posthumous entity mentions in a unified schema.
- The entity schema follows a three-level structure consisting of `entity_phase`, `entity_type`, and `entity_subtype`.
- Mention-level linkage information is represented through the `linked_entity_id` field when applicable.
- Unique canonical-level linkage relations are additionally summarized in `entity_linkage.csv`.

## 4. `entity_linkage.csv`

This file records unique canonical-level linkage relations between entities in the released SEOBI annotation layer. Each row corresponds to one strongly supported linkage relation rather than all mention-level linked instances.

### Record unit
- One row per unique canonical linkage relation.

### Key fields
- `source_entity_id`: Identifier of the source entity in the linkage relation.
- `target_entity_id`: Identifier of the target entity in the linkage relation.
- `linkage_type`: Type of relation represented by the linkage, such as cross-phase identity mapping or strongly supported alias relation.

### Notes
- This file stores only unique canonical-level linkage relations.
- It does not enumerate all mention-level linked instances in the corpus.
- Mention-level linkage information, where applicable, is represented in `entity_mentions.csv` through the `linked_entity_id` field.
- The current release includes only a small number of strongly supported linkage relations because conservative criteria are used for cross-phase and alias mapping.
