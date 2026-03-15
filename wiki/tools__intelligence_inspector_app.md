# Intelligence Inspector — React App

## Overview
Full-featured React application for analyzing document intelligence vectors.
Freemium model: 10,000 free tokens, then paid tiers via Stripe.

## Features
- Document upload and analysis
- 12-dimensional intelligence vector scoring
- Radar charts and bar charts (Recharts)
- Document comparison (cosine similarity, euclidean distance, Jaccard overlap)
- Cross-dimensional coupling analysis
- Per-dimension concept breakdown
- Credit metering system with purchase modal

## Credit Tiers
- Free: 10,000 tokens
- Starter: 50,000 tokens / $5
- Professional: 250,000 tokens / $20
- Enterprise: 1,000,000 tokens / $60

## Deployment
The .jsx file is self-contained with embedded lexicon (838 primes).
Requires React + Recharts + Tailwind CSS runtime.
Stripe integration pending — purchase modal is UI-ready.

## Files
- inspector_app.jsx — React component
- intelligence_inspector.html — Standalone HTML version
- ivector_inspector.py — Python analysis engine
- ivector.db — SQLite graph database