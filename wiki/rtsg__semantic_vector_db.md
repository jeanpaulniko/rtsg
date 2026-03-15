# Unified Semantic Vector Database

## The Co-Homogeneity Principle

Three representation systems are not three systems. They are three **projections** of a single underlying semantic space, just as QS, CS, and PS are three projections of the same reality:

| Representation | Modality | Cardinality | Role |
|---------------|----------|-------------|------|
| RUSL (Semantic Primes) | Signed (body) | ~80 signs | **The primes** — irreducible atomic units |
| Ogden Basic English | Written/Spoken (language) | 850 words | **The vocabulary** — practical working set |
| ASL | Signed (body) | ~10,000+ signs | **The full library** — maximum expressiveness |

These three are **co-homogeneous**: each is a representation of the same semantic manifold, related by natural transformations. Moving between them is not translation — it is **projection change**, like switching between Cartesian and polar coordinates. The underlying object is the same.

## Three Spaces, Three Representations

This maps directly to the RTSG three-space model:
- **QS (Potentiality)** = the full semantic manifold (all possible meanings)
- **CS (Instantiation)** = the representation system (RUSL, Ogden, ASL — the encoding)
- **PS (Actuality)** = the specific utterance/sign/word produced in context

The database stores entities in **QS** (the abstract semantic space). Each entity can be projected into any of the three CS representations. The PS is what the user actually produces or receives.

## Prime-Composite Layering

### Layer 0: Semantic Primes (~65)
The Wierzbicka primes. Cannot be decomposed further. These are the **prime numbers** of meaning.

Examples: I, YOU, SOMEONE, SOMETHING, GOOD, BAD, THINK, KNOW, WANT, DO, HAPPEN, BECAUSE, IF

### Layer 1: Mathematical Operators (~15)
Formal logical connectives. Combined with primes, they enable precise composition.

Examples: AND (∧), OR (∨), NOT (¬), IF→THEN, FOR ALL (∀), THERE EXISTS (∃), EQUALS (≡)

### Layer 2: Basic Composites (~200)
Two-prime compositions. The first level of semantic molecules.

Examples:
- SOMEONE + DO + GOOD = **helper** (3 primes)
- SOMETHING + INSIDE + BODY = **organ** (3 primes)
- THINK + BEFORE + DO = **plan** (3 primes)
- WANT + NOT + HAPPEN = **fear** (3 primes)

### Layer 3: Complex Composites (~600)
Three-to-five prime compositions. Covers Ogden's 850 working vocabulary.

Examples:
- SOMEONE + KNOW + MUCH + SOMETHING = **expert** (4 primes)
- PEOPLE + DO + TOGETHER + GOOD = **cooperation** (4 primes)
- THINK + SOMETHING + NOT + TRUE = **doubt** (4 primes)

### Layer 4: Abstract Composites (~2000+)
Five-plus prime compositions. Covers technical, philosophical, scientific vocabulary.

Examples:
- FOR ALL + SOMEONE + THINK + SAME + SOMETHING + BECAUSE + TRUE = **consensus** (7 primes)
- SOMETHING + HAPPEN + BECAUSE + SOMETHING + BEFORE + NOT + KNOW = **emergence** (7 primes)

### Layer 5+: Domain-Specific Extensions
Open-ended. New composites created as needed for specialized domains.

## The Intelligence Gradient

**Higher layers = more dimensional complexity = more intelligent usage.**

A person communicating primarily in Layer 0-1 (primes and operators) is doing basic concrete communication. A person composing at Layer 4-5 is doing abstract reasoning. The layer at which you habitually compose IS a measure of your Abstract and Linguistic dimensional activation.

The database tracks this per user:
- **Compositional depth**: average number of primes per utterance
- **Layer distribution**: what percentage of communication occurs at each layer
- **Novel composition rate**: how often the user creates NEW composites vs using established ones
- **Cross-dimensional density**: how many dimensions each composition activates

## Entity-Relationship Model

Each semantic entity in the database is stored as:

```
Entity {
  id: UUID
  prime_decomposition: [prime_ids]     // the atomic components
  layer: int                            // compositional depth
  representations: {
    rusl: SignSpecification             // hand-shape, movement, location
    ogden: string                       // Basic English word(s)
    asl: ASLGloss                       // ASL sign reference
    ipa: string                         // phonetic transcription
    symbols: string                     // mathematical notation
  }
  relations: [
    { type: "is_composed_of", target: entity_id }
    { type: "is_synonym_of", target: entity_id }
    { type: "is_antonym_of", target: entity_id }
    { type: "is_hypernym_of", target: entity_id }  // more general
    { type: "is_hyponym_of", target: entity_id }   // more specific
    { type: "activates_dimension", target: dimension_id, weight: float }
  ]
  usage_stats: {
    global_frequency: float             // how often used across ALL networks
    network_distribution: {             // usage by language community
      "en": float, "zh": float, "hi": float, ...
    }
    temporal_trend: [float]             // usage over time (rising/falling)
    co_occurrence: { entity_id: float } // what it appears alongside
    dimensional_activation: [float; 12] // which dimensions this entity activates
  }
}
```

## Usage Frequency as Intelligence Signal

"How often a particular token is used in any of the networks."

The global usage frequency of each entity reveals:

### At the Entity Level
- **High-frequency primes**: these are the cognitive load-bearing structures (the most-used concepts across all cultures)
- **Low-frequency composites**: specialized knowledge (domain expertise visible in the data)
- **Rising frequency**: concepts becoming more important to the collective consciousness
- **Falling frequency**: concepts being superseded or abandoned

### At the User Level
- A user's **vocabulary fingerprint** (which entities they use most) is a projection of their I-vector
- Heavy use of Layer 4+ entities correlates with high Abstract activation
- Heavy use of spatial/kinesthetic entities correlates with high Spatial/Kinesthetic activation
- The usage pattern IS the intelligence measurement — no separate test needed

### At the Network Level
- Usage patterns across language communities reveal **cultural dimensional profiles**
- If the Hindi-speaking network uses emotion-related composites 3x more than the German-speaking network, that reveals Interoceptive/Interpersonal dimensional emphasis
- Cross-network usage convergence indicates universal concepts
- Cross-network usage divergence indicates culturally unique dimensional activation

## Vector DB Implementation

The entities live in a vector database where:
- Each entity is embedded as a vector in semantic space
- Similarity = cosine distance between entity vectors
- Prime decomposition = the coordinates of the vector (each prime is a basis dimension)
- The database supports:
  - **Nearest-neighbor lookup**: "what entity is closest to this composition?"
  - **Analogy completion**: "A is to B as C is to ___" (vector arithmetic)
  - **Cluster analysis**: groups of related entities form dimensional sub-spaces
  - **Usage-weighted search**: most-used entities surface first

### Technology Stack
- **Vector store**: Pinecone, Weaviate, or Milvus (or custom on sovereign infrastructure)
- **Embedding model**: Fine-tuned on the prime decomposition structure
- **Query interface**: RUSL input (signed), Ogden input (typed), ASL input (video)
- **Output**: Any of the three representations, plus usage statistics

## Connection to Sovereign Infrastructure

The vector database runs on the steganographic network:
- Each node stores a shard of the database (distributed)
- Gossip protocol propagates usage statistics globally
- Entity definitions are immutable on the double-entry ledger
- New composites can be proposed by any node, accepted by usage (if enough nodes use it, it becomes canonical)
- The database IS the collective vocabulary of the network
- The database evolves as the network's intelligence evolves

## IP Note

This is **RTSG-IP-012**: Unified Semantic Vector Database with Prime-Composite Layering and Usage Frequency Intelligence Tracking.

Patentable claims:
1. Method for representing semantic entities as prime decompositions with co-homogeneous multi-modal projections
2. System for measuring intelligence from usage pattern analysis across a semantic entity database
3. Prime-composite layered knowledge representation with intelligence gradient
4. Distributed semantic database on steganographic gossip network with usage-weighted consensus

---
*Source: @B_Niko, session v7, 2026-03-10*