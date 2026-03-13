import pandas as pd
from pathlib import Path

# Resolve repository root from this script location
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

# Load released SEOBI tables
sentences = pd.read_csv(DATA_DIR / "sentences.csv", encoding="utf-8")
themes = pd.read_csv(DATA_DIR / "sentence_themes.csv", encoding="utf-8")
entities = pd.read_csv(DATA_DIR / "entity_mentions.csv", encoding="utf-8")
linkage = pd.read_csv(DATA_DIR / "entity_linkage.csv", encoding="utf-8")

print("Loaded SEOBI tables:")
print(f"- sentences.csv: {len(sentences)} rows")
print(f"- sentence_themes.csv: {len(themes)} rows")
print(f"- entity_mentions.csv: {len(entities)} rows")
print(f"- entity_linkage.csv: {len(linkage)} rows")

print("\nColumn overview:")
print("sentences.csv:", list(sentences.columns))
print("sentence_themes.csv:", list(themes.columns))
print("entity_mentions.csv:", list(entities.columns))
print("entity_linkage.csv:", list(linkage.columns))

# Example: retrieve all thematic labels for one sentence using composite sentence keys
if not sentences.empty:
    sample = sentences.iloc[0]
    bone_id = sample["bone_id"]
    period_class = sample["period_class"]
    group_order = sample["group_order"]

    print("\nSample sentence:")
    print(sample["sentence_simple"])

    theme_rows = themes[
        (themes["bone_id"] == bone_id) &
        (themes["period_class"] == period_class) &
        (themes["group_order"] == group_order)
    ]

    entity_rows = entities[
        (entities["bone_id"] == bone_id) &
        (entities["period_class"] == period_class) &
        (entities["group_order"] == group_order)
    ]

    print("\nAssociated thematic annotations:")
    if theme_rows.empty:
        print("  None")
    else:
        for _, row in theme_rows.iterrows():
            print(f"  - {row['theme']}")

    print("\nAssociated entity mentions:")
    if entity_rows.empty:
        print("  None")
    else:
        for _, row in entity_rows.iterrows():
            surface = row.get("surface_form", "")
            canon = row.get("canonical_name", "")
            phase = row.get("entity_phase", "")
            print(f"  - {surface} | canonical={canon} | phase={phase}")
