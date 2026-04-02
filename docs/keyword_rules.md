# Thematic trigger rules

This document summarizes the rule-based thematic matching logic used in the released SEOBI dataset.

## Overview

Sentence-level thematic annotations in SEOBI are assigned through conservative rule-based matching. The released thematic layer covers five categories:

- Ritual
- Rain
- Agriculture
- War
- Spatial

The rules rely on visible lexical or structural cues in the sentence transcription. Only positively assigned thematic annotations are included in `data/sentence_themes.csv`.

## 1. Ritual

Ritual is assigned when a sentence contains ritual action terms or ritual-recipient expressions.

Typical signals include:
- sacrificial or ritual verbs
- ancestor-related expressions
- major deities or powers invoked in divination contexts

## 2. Rain

Rain is assigned when explicit weather-related terms are present.

Typical signals include:
- rain-related expressions
- cloud or atmospheric terms
- weather omen expressions

## 3. Agriculture

Agriculture is assigned when harvest expressions, crop names, or cultivation-related terms are present.

Typical signals include:
- harvest formulas
- crop names
- cultivation-related expressions

## 4. War

War is assigned when military action terms or conflict-related expressions are present.

Typical signals include:
- military action verbs
- conflict expressions
- expedition or attack terminology

## 5. Spatial

Spatial is assigned when directional terms or place-related expressions are present.

Typical signals include:
- directional terms
- place names
- region- or location-related expressions

## Multi-label assignment

A sentence may receive more than one thematic label if cues from multiple categories co-occur.

## Notes

This document provides a concise summary of the thematic rule logic used for the released annotations. More detailed trigger inventories or machine-readable rule resources may be added in future updates.
