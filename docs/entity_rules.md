# Entity annotation rules

This document summarizes the rule-based procedures used to derive entity annotations in the released SEOBI dataset.

## Overview

Entity recognition in SEOBI combines three deterministic procedures:

1. direct matching
2. period-based inference
3. generic pattern matching

These procedures are used to derive the released entity annotations in `data/entity_mentions.csv`.

## 1. Direct matching

Direct matching identifies explicitly named entities through lexicon lookup and canonical name normalization.

Typical outputs include named living persons, deities, ancestors, and other explicitly attested entity forms.

## 2. Period-based inference

Period-based inference resolves generic references, such as `王` (“king”), by using the temporal annotation of the sentence as period context and linking the mention to a period-compatible ruler when supported by the annotation rules.

## 3. Generic pattern matching

Generic pattern matching captures formulaic role expressions that do not uniquely identify an individual but still support entity annotation.

These pattern-based matches are retained as generic entity records when applicable.

## Entity schema

The released entity annotations follow a three-level schema:

- `entity_phase`: living or posthumous
- `entity_type`: human, deity, or ancestor
- `entity_subtype`: finer-grained role- or identity-level category

Additional mention-level fields, including `entity_role`, `confidence`, `rule_hit`, and `linked_entity_id`, are documented in `docs/SCHEMA.md`.

## Linkage

Strongly supported canonical linkage relations are summarized in `data/entity_linkage.csv`.

Mention-level linkage information, where applicable, is represented in `data/entity_mentions.csv` through the `linked_entity_id` field.

## Notes

This document provides a concise summary of the released entity annotation logic. More detailed rule refinements or implementation-specific scripts may be added in future updates.
