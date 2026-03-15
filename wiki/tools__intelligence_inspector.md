# Intelligence Inspector

## What It Does
Maps any document to a 12-dimensional intelligence vector. Each document becomes a miniature mind — scored by breadth, depth, density, and cross-dimensional reach.

## Metrics
- **Intelligence Vector**: 12-dimensional score (one per I-vector axis)
- **Magnitude**: total intelligence volume |v|
- **Balance**: entropy-based measure of dimensional coverage
- **Coverage**: % of tokens matched to graph nodes
- **Concept Density**: average graph connectivity of matched concepts
- **Cross-Dimensional Couplings**: which dimensions co-activate

## Comparison
Documents can be compared via:
- Cosine similarity (directional alignment)
- Euclidean distance (absolute difference)
- Jaccard overlap (shared active dimensions)
- Per-dimension breakdown
- Magnitude ratio (relative intelligence volume)

## Components
- Python engine: ivector_inspector.py
- Web interface: intelligence_inspector.html
- Graph database: ivector.db (838 primes, 71K edges)
- Root encoding: nrt_roots.json (NRT-Lang CVC codes)

## Status
Layer 0 operational. Web interface functional with embedded lexicon.