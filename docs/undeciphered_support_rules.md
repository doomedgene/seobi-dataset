# Undeciphered character support rules

This document summarizes the conservative support procedure used in SEOBI for sentences containing undeciphered characters.

## Overview

A substantial portion of curated oracle bone inscription sentences contains one or more undeciphered characters. Instead of excluding all such sentences from annotation, SEOBI applies a conservative rule-based support procedure to retain partial thematic or entity-related annotation when sufficient textual evidence remains visible.

This support procedure is designed for coverage extension under incomplete decipherment. It does not aim to provide full character decipherment.

## Evidence types

The current support procedure uses two main types of evidence:

1. structural patterns
2. contextual keywords

## 1. Structural patterns

Structural patterns rely on recurrent formulaic constructions in oracle bone syntax. When a partially undeciphered expression matches a strongly attested structural pattern, the sentence may still support a candidate annotation.

Typical cases include kinship or ritual-recipient patterns that remain interpretable despite incomplete character identification.

## 2. Contextual keywords

Contextual keywords rely on deciphered tokens that remain visible in the sentence. When explicit thematic cues are preserved, the sentence may still receive a candidate thematic annotation.

For example, the presence of a weather-related term can support a Rain annotation even if other characters in the same sentence remain undeciphered.

## Annotation scope

The support procedure may contribute to two types of annotation outcomes:

- thematic annotations
- entity-related candidate annotations

Where applicable, entity-related inferred records may additionally be filtered using confidence labels in the released entity annotation layer.

## Notes

This document provides a concise summary of the released support logic for partially deciphered sentences. More implementation-specific details may be added in future updates.
