-- =============================================================================
-- NRTE Brain-Graph Database v2.0
-- Implements: Token/Engram → Prime → Composite → Pattern → Topology hierarchy
-- With: connection counting per dimension, tube thickness (Physarum model),
--        hyperbolic + ultrametric embedding, temporal activation tracking
-- Author: Jean-Paul Niko / RTSG Framework
-- =============================================================================

CREATE EXTENSION IF NOT EXISTS pgvector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- =============================================================================
-- LAYER 0: TOKENS / ENGRAMS
-- The atomic reusable morphemes — prefixes, suffixes, roots, phonemes
-- These are shared across primes (like "un-" participates in many words)
-- Mathematically: elements of the free monoid Σ*
-- =============================================================================

CREATE TABLE tokens (
    id BIGSERIAL PRIMARY KEY,
    uuid UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4(),
    symbol VARCHAR(255) NOT NULL UNIQUE,          -- the morpheme string
    token_type VARCHAR(50) NOT NULL CHECK (token_type IN (
        'root', 'prefix', 'suffix', 'infix',
        'phoneme', 'grapheme', 'semantic_atom'
    )),
    lojban_form VARCHAR(255),                      -- Lojban equivalent if any
    frequency BIGINT DEFAULT 0,                    -- how many primes use this token
    -- Connection tracking (total across all primes that contain this token)
    total_connections BIGINT DEFAULT 0,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_tokens_symbol ON tokens(symbol);
CREATE INDEX idx_tokens_type ON tokens(token_type);
CREATE INDEX idx_tokens_frequency ON tokens(frequency DESC);

-- =============================================================================
-- LAYER 1: PRIMES
-- Irreducible semantic units. Each prime factors into tokens.
-- Each prime is typed into one of the 12 intelligence dimensions.
-- Mathematically: Spec(ι) ∈ ℕ^12 (prime spectrum)
-- =============================================================================

CREATE TABLE primes (
    id BIGSERIAL PRIMARY KEY,
    uuid UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    -- Which intelligence dimension this prime belongs to
    dimension VARCHAR(50) NOT NULL CHECK (dimension IN (
        'I_L',   -- linguistic
        'I_M',   -- mathematical
        'I_S',   -- spatial
        'I_K',   -- kinesthetic
        'I_N',   -- naturalistic
        'I_A',   -- abstract/algorithmic
        'I_P',   -- interpersonal
        'I_IE',  -- interoceptive/emotional
        'I_Pr',  -- proprioceptive
        'I_Sigma', -- somatic-integrative
        'I_mu',  -- musical
        'I_E'    -- empathic-resonance
    )),
    -- The prime's "weight" in its dimension (how fundamental it is)
    weight FLOAT DEFAULT 1.0,
    lojban_form VARCHAR(255),
    english VARCHAR(1024),
    -- Connection counting: total edges from this prime to all others
    total_connections BIGINT DEFAULT 0,
    -- Connection count per dimension (the tube thickness map)
    connections_by_dim JSONB DEFAULT '{
        "I_L": 0, "I_M": 0, "I_S": 0, "I_K": 0, "I_N": 0, "I_A": 0,
        "I_P": 0, "I_IE": 0, "I_Pr": 0, "I_Sigma": 0, "I_mu": 0, "I_E": 0,
        "temporal": 0
    }',
    -- Temporal: when was this prime last activated?
    last_activated TIMESTAMPTZ DEFAULT NOW(),
    activation_count BIGINT DEFAULT 0,
    -- Tube thickness: derived from connection frequency (Physarum model)
    -- thickness = |Q(x)| where Q is flow through this node
    tube_thickness FLOAT DEFAULT 1.0,
    -- Decay rate γ (tubes that aren't used atrophy)
    decay_rate FLOAT DEFAULT 0.01,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_primes_name ON primes(name);
CREATE INDEX idx_primes_dimension ON primes(dimension);
CREATE INDEX idx_primes_thickness ON primes(tube_thickness DESC);
CREATE INDEX idx_primes_connections ON primes(total_connections DESC);
CREATE INDEX idx_primes_last_activated ON primes(last_activated DESC);

-- Junction: which tokens compose each prime (and in what order)
CREATE TABLE prime_tokens (
    id BIGSERIAL PRIMARY KEY,
    prime_id BIGINT NOT NULL REFERENCES primes(id) ON DELETE CASCADE,
    token_id BIGINT NOT NULL REFERENCES tokens(id) ON DELETE CASCADE,
    position INT NOT NULL,           -- order of token in the prime
    role VARCHAR(50) DEFAULT 'component', -- root, prefix, suffix, etc.
    UNIQUE(prime_id, token_id, position)
);

CREATE INDEX idx_prime_tokens_prime ON prime_tokens(prime_id);
CREATE INDEX idx_prime_tokens_token ON prime_tokens(token_id);

-- =============================================================================
-- LAYER 2: COMPOSITES (ENTITIES)
-- Concepts built from products of primes. Each composite has a prime spectrum.
-- Extends the original NRTE entities table.
-- Mathematically: composite = ∏ p_i^{a_i}, spectrum Spec(ι) ∈ ℕ^12
-- =============================================================================

CREATE TABLE composites (
    id BIGSERIAL PRIMARY KEY,
    uuid UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4(),
    name VARCHAR(512) NOT NULL,
    -- NRTE type classification
    nrte_type VARCHAR(50) NOT NULL CHECK (nrte_type IN (
        'noun', 'relation', 'thing', 'entity',
        'pattern', 'topology', 'geometry', 'multidimensional'
    )),
    -- The prime spectrum: how this composite factors into primes per dimension
    -- e.g., {"I_L": [3, 7], "I_M": [2], "I_S": [5, 11]} means
    -- this concept = prime_3 × prime_7 (linguistic) × prime_2 (math) × ...
    prime_spectrum JSONB DEFAULT '{}',
    -- Hierarchical layer (how many levels above primes)
    layer INT DEFAULT 2 CHECK (layer >= 2),
    lojban_form VARCHAR(255),
    english VARCHAR(2048),
    -- === CONNECTION TRACKING (the core of the brain-graph) ===
    -- Total connections to all other composites/primes/patterns
    total_connections BIGINT DEFAULT 0,
    -- Connections broken down by dimension + temporal
    connections_by_dim JSONB DEFAULT '{
        "I_L": 0, "I_M": 0, "I_S": 0, "I_K": 0, "I_N": 0, "I_A": 0,
        "I_P": 0, "I_IE": 0, "I_Pr": 0, "I_Sigma": 0, "I_mu": 0, "I_E": 0,
        "temporal": 0
    }',
    -- Connections to different structural types
    connections_to_nouns BIGINT DEFAULT 0,
    connections_to_relations BIGINT DEFAULT 0,
    connections_to_things BIGINT DEFAULT 0,
    connections_to_entities BIGINT DEFAULT 0,
    connections_to_patterns BIGINT DEFAULT 0,
    connections_to_topologies BIGINT DEFAULT 0,
    connections_to_geometries BIGINT DEFAULT 0,
    -- === PHYSARUM / TUBE THICKNESS ===
    tube_thickness FLOAT DEFAULT 1.0,
    -- Flow through this node: |Q| = Σ (edge_weight × activation_freq)
    flow_magnitude FLOAT DEFAULT 0.0,
    decay_rate FLOAT DEFAULT 0.01,
    -- === TEMPORAL ===
    last_activated TIMESTAMPTZ DEFAULT NOW(),
    activation_count BIGINT DEFAULT 0,
    -- Temporal connections: how many times this was activated in each time window
    temporal_histogram JSONB DEFAULT '{
        "last_hour": 0, "last_day": 0, "last_week": 0,
        "last_month": 0, "last_year": 0, "lifetime": 0
    }',
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_composites_name ON composites(name);
CREATE INDEX idx_composites_type ON composites(nrte_type);
CREATE INDEX idx_composites_layer ON composites(layer);
CREATE INDEX idx_composites_connections ON composites(total_connections DESC);
CREATE INDEX idx_composites_thickness ON composites(tube_thickness DESC);
CREATE INDEX idx_composites_flow ON composites(flow_magnitude DESC);
CREATE INDEX idx_composites_last_activated ON composites(last_activated DESC);
CREATE INDEX idx_composites_spectrum ON composites USING GIN (prime_spectrum);

-- Junction: which primes compose each composite (with multiplicity)
CREATE TABLE composite_primes (
    id BIGSERIAL PRIMARY KEY,
    composite_id BIGINT NOT NULL REFERENCES composites(id) ON DELETE CASCADE,
    prime_id BIGINT NOT NULL REFERENCES primes(id) ON DELETE CASCADE,
    multiplicity INT DEFAULT 1,     -- how many times this prime appears
    UNIQUE(composite_id, prime_id)
);

CREATE INDEX idx_composite_primes_composite ON composite_primes(composite_id);
CREATE INDEX idx_composite_primes_prime ON composite_primes(prime_id);

-- =============================================================================
-- EDGES: THE BRAIN GRAPH CONNECTIONS
-- Directed weighted hyperedges between any nodes (primes, composites, patterns)
-- Each edge has dimension, thickness, temporal data
-- =============================================================================

CREATE TABLE edges (
    id BIGSERIAL PRIMARY KEY,
    uuid UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4(),
    -- Source and target can be primes or composites
    source_type VARCHAR(20) NOT NULL CHECK (source_type IN ('prime', 'composite')),
    source_id BIGINT NOT NULL,
    target_type VARCHAR(20) NOT NULL CHECK (target_type IN ('prime', 'composite')),
    target_id BIGINT NOT NULL,
    -- Relation label (the predicate in the triple)
    predicate VARCHAR(255) NOT NULL,
    -- Which dimension does this edge live in?
    dimension VARCHAR(50) CHECK (dimension IN (
        'I_L', 'I_M', 'I_S', 'I_K', 'I_N', 'I_A',
        'I_P', 'I_IE', 'I_Pr', 'I_Sigma', 'I_mu', 'I_E',
        'cross_dimensional', 'temporal'
    )),
    -- === TUBE THICKNESS (Physarum model) ===
    -- weight evolves by: dw/dt = |Q(w)| - γw
    -- where Q = flow through this edge, γ = decay
    weight FLOAT DEFAULT 1.0,
    tube_thickness FLOAT DEFAULT 1.0,
    flow FLOAT DEFAULT 0.0,          -- current flow |Q| through this edge
    decay_rate FLOAT DEFAULT 0.01,
    -- === TEMPORAL ===
    last_traversed TIMESTAMPTZ DEFAULT NOW(),
    traversal_count BIGINT DEFAULT 0,
    -- Temporal weight: recent traversals count more
    -- temporal_weight = Σ exp(-λ(t_now - t_i)) over all traversals
    temporal_weight FLOAT DEFAULT 1.0,
    -- === DISTANCE METRICS ===
    -- Hyperbolic distance (Poincaré ball model)
    hyperbolic_distance FLOAT,
    -- Ultrametric distance (p-adic, for categorical boundaries)
    ultrametric_distance FLOAT,
    -- GL Green's function distance: d = -log G(source, target)
    gl_distance FLOAT,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_edges_source ON edges(source_type, source_id);
CREATE INDEX idx_edges_target ON edges(target_type, target_id);
CREATE INDEX idx_edges_predicate ON edges(predicate);
CREATE INDEX idx_edges_dimension ON edges(dimension);
CREATE INDEX idx_edges_thickness ON edges(tube_thickness DESC);
CREATE INDEX idx_edges_flow ON edges(flow DESC);
CREATE INDEX idx_edges_last_traversed ON edges(last_traversed DESC);
CREATE INDEX idx_edges_traversal_count ON edges(traversal_count DESC);
CREATE INDEX idx_edges_triple ON edges(source_type, source_id, predicate, target_type, target_id);

-- =============================================================================
-- HYPEREDGES: Multi-way connections (K^(p) tensors, p >= 3)
-- For three-way synergies, team dynamics, etc.
-- =============================================================================

CREATE TABLE hyperedges (
    id BIGSERIAL PRIMARY KEY,
    uuid UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4(),
    -- The order p of this hyperedge (3 = triple, 4 = quadruple, etc.)
    arity INT NOT NULL CHECK (arity >= 3),
    predicate VARCHAR(255),
    dimension VARCHAR(50),
    weight FLOAT DEFAULT 1.0,
    tube_thickness FLOAT DEFAULT 1.0,
    flow FLOAT DEFAULT 0.0,
    last_traversed TIMESTAMPTZ DEFAULT NOW(),
    traversal_count BIGINT DEFAULT 0,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Members of each hyperedge
CREATE TABLE hyperedge_members (
    id BIGSERIAL PRIMARY KEY,
    hyperedge_id BIGINT NOT NULL REFERENCES hyperedges(id) ON DELETE CASCADE,
    member_type VARCHAR(20) NOT NULL CHECK (member_type IN ('prime', 'composite')),
    member_id BIGINT NOT NULL,
    role VARCHAR(50) DEFAULT 'participant',
    position INT DEFAULT 0
);

CREATE INDEX idx_hyperedge_members_edge ON hyperedge_members(hyperedge_id);
CREATE INDEX idx_hyperedge_members_member ON hyperedge_members(member_type, member_id);

-- =============================================================================
-- EMBEDDINGS: Hyperbolic + Ultrametric + GL Green's function
-- Replaces cosine similarity with the true brain-graph metric
-- =============================================================================

-- Poincaré ball embeddings (hyperbolic space for hierarchy)
CREATE TABLE hyperbolic_embeddings (
    id BIGSERIAL PRIMARY KEY,
    entity_type VARCHAR(20) NOT NULL CHECK (entity_type IN ('token', 'prime', 'composite')),
    entity_id BIGINT NOT NULL,
    -- Poincaré ball coordinates (inside unit ball, ||x|| < 1)
    -- Higher dimensions capture more hierarchical structure
    coordinates vector(64),
    -- The curvature parameter (controls how fast distance grows)
    curvature FLOAT DEFAULT -1.0,
    -- Layer in hierarchy (affects radial position in Poincaré ball)
    hierarchy_depth INT DEFAULT 0,
    model_version VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(entity_type, entity_id)
);

CREATE INDEX idx_hyperbolic_entity ON hyperbolic_embeddings(entity_type, entity_id);

-- p-adic / ultrametric embeddings (one per prime p, for categorical boundaries)
CREATE TABLE ultrametric_embeddings (
    id BIGSERIAL PRIMARY KEY,
    entity_type VARCHAR(20) NOT NULL CHECK (entity_type IN ('token', 'prime', 'composite')),
    entity_id BIGINT NOT NULL,
    -- Which prime p defines this ultrametric
    prime_p INT NOT NULL,  -- 2, 3, 5, 7, 11, ...
    -- p-adic valuation of the entity (determines ultrametric distance)
    valuation INT DEFAULT 0,
    -- p-adic expansion coefficients (first N digits in base p)
    expansion JSONB DEFAULT '[]',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(entity_type, entity_id, prime_p)
);

CREATE INDEX idx_ultrametric_entity ON ultrametric_embeddings(entity_type, entity_id);
CREATE INDEX idx_ultrametric_prime ON ultrametric_embeddings(prime_p);

-- Standard vector embeddings (for compatibility with existing ML pipelines)
CREATE TABLE vector_embeddings (
    id BIGSERIAL PRIMARY KEY,
    entity_type VARCHAR(20) NOT NULL CHECK (entity_type IN ('token', 'prime', 'composite')),
    entity_id BIGINT NOT NULL,
    model VARCHAR(100) NOT NULL,
    vector vector(768),
    model_version VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(entity_type, entity_id, model)
);

CREATE INDEX idx_vector_embeddings_entity ON vector_embeddings(entity_type, entity_id);
CREATE INDEX idx_vector_embeddings_vector ON vector_embeddings
    USING ivfflat (vector vector_cosine_ops) WITH (lists = 100);

-- =============================================================================
-- PHYSARUM DYNAMICS: Tracking the slime mold optimization
-- The GL functional: S[W] = ∫(|∂W|² + α|W|² + (β/2)|W|⁴)dν
-- Maps to: gradient_cost + maintenance_cost + saturation_penalty
-- =============================================================================

CREATE TABLE network_state (
    id BIGSERIAL PRIMARY KEY,
    -- Global network statistics (updated periodically)
    total_nodes BIGINT DEFAULT 0,
    total_edges BIGINT DEFAULT 0,
    total_flow FLOAT DEFAULT 0.0,
    -- GL functional components
    gradient_cost FLOAT DEFAULT 0.0,     -- Σ |∂W|² across all edges (penalizes long connections)
    maintenance_cost FLOAT DEFAULT 0.0,  -- α Σ |W|² across all nodes (metabolic cost)
    saturation_penalty FLOAT DEFAULT 0.0,-- (β/2) Σ |W|⁴ (nonlinear tube limit)
    total_action FLOAT DEFAULT 0.0,      -- S[W] = sum of above (the quantity being minimized)
    -- Spectral gap of the network Laplacian
    spectral_gap FLOAT,
    -- Average tube thickness
    mean_thickness FLOAT DEFAULT 1.0,
    -- Network entropy (how evenly distributed are the connections?)
    entropy FLOAT DEFAULT 0.0,
    snapshot_at TIMESTAMPTZ DEFAULT NOW()
);

-- =============================================================================
-- DIMENSION STATISTICS: Per-dimension connection summaries
-- "How many connections in each dimension including time"
-- =============================================================================

CREATE TABLE dimension_stats (
    id BIGSERIAL PRIMARY KEY,
    entity_type VARCHAR(20) NOT NULL CHECK (entity_type IN ('token', 'prime', 'composite')),
    entity_id BIGINT NOT NULL,
    -- Per-dimension connection counts
    conn_I_L BIGINT DEFAULT 0,
    conn_I_M BIGINT DEFAULT 0,
    conn_I_S BIGINT DEFAULT 0,
    conn_I_K BIGINT DEFAULT 0,
    conn_I_N BIGINT DEFAULT 0,
    conn_I_A BIGINT DEFAULT 0,
    conn_I_P BIGINT DEFAULT 0,
    conn_I_IE BIGINT DEFAULT 0,
    conn_I_Pr BIGINT DEFAULT 0,
    conn_I_Sigma BIGINT DEFAULT 0,
    conn_I_mu BIGINT DEFAULT 0,
    conn_I_E BIGINT DEFAULT 0,
    -- Temporal connections (edges that have time dimension)
    conn_temporal BIGINT DEFAULT 0,
    -- Cross-dimensional edges (connecting different dimension types)
    conn_cross_dim BIGINT DEFAULT 0,
    -- Total
    conn_total BIGINT DEFAULT 0,
    -- Derived: which dimension has the most connections? (dominant channel)
    dominant_dimension VARCHAR(50),
    -- The tube thickness is proportional to this
    -- thickness = f(conn_total, activation_frequency, recency)
    computed_thickness FLOAT DEFAULT 1.0,
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(entity_type, entity_id)
);

CREATE INDEX idx_dim_stats_entity ON dimension_stats(entity_type, entity_id);
CREATE INDEX idx_dim_stats_total ON dimension_stats(conn_total DESC);
CREATE INDEX idx_dim_stats_dominant ON dimension_stats(dominant_dimension);

-- =============================================================================
-- TROPICAL SEMIRING LAYER
-- The cost of assembling primes from tokens is a min-plus problem
-- tropical addition: a ⊕ b = min(a, b)
-- tropical multiplication: a ⊗ b = a + b
-- The optimal token combination minimizes total assembly cost
-- =============================================================================

CREATE TABLE tropical_costs (
    id BIGSERIAL PRIMARY KEY,
    prime_id BIGINT NOT NULL REFERENCES primes(id) ON DELETE CASCADE,
    -- The min-plus cost of assembling this prime from tokens
    assembly_cost FLOAT NOT NULL DEFAULT 0.0,
    -- Which token path achieves the minimum cost?
    optimal_path JSONB DEFAULT '[]',  -- ordered list of token IDs
    -- Alternative paths (within ε of optimal)
    alternative_paths JSONB DEFAULT '[]',
    computed_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_tropical_prime ON tropical_costs(prime_id);
CREATE INDEX idx_tropical_cost ON tropical_costs(assembly_cost);

-- =============================================================================
-- FUNCTIONS: Physarum dynamics, thickness computation, activation
-- =============================================================================

-- Update tube thickness using Physarum dynamics: dx/dt = |Q(x)| - γx
CREATE OR REPLACE FUNCTION update_tube_thickness(
    p_entity_type VARCHAR,
    p_entity_id BIGINT,
    p_flow FLOAT
) RETURNS FLOAT AS $$
DECLARE
    current_thickness FLOAT;
    current_decay FLOAT;
    new_thickness FLOAT;
BEGIN
    IF p_entity_type = 'prime' THEN
        SELECT tube_thickness, decay_rate INTO current_thickness, current_decay
        FROM primes WHERE id = p_entity_id;
        new_thickness := GREATEST(0.01, current_thickness + p_flow - current_decay * current_thickness);
        UPDATE primes SET tube_thickness = new_thickness, updated_at = NOW() WHERE id = p_entity_id;
    ELSIF p_entity_type = 'composite' THEN
        SELECT tube_thickness, decay_rate INTO current_thickness, current_decay
        FROM composites WHERE id = p_entity_id;
        new_thickness := GREATEST(0.01, current_thickness + p_flow - current_decay * current_thickness);
        UPDATE composites SET tube_thickness = new_thickness, updated_at = NOW() WHERE id = p_entity_id;
    END IF;
    RETURN new_thickness;
END;
$$ LANGUAGE plpgsql;

-- Record an activation event (traverse an edge, activate a concept)
CREATE OR REPLACE FUNCTION activate_entity(
    p_entity_type VARCHAR,
    p_entity_id BIGINT,
    p_dimension VARCHAR DEFAULT NULL
) RETURNS VOID AS $$
BEGIN
    IF p_entity_type = 'prime' THEN
        UPDATE primes SET
            activation_count = activation_count + 1,
            last_activated = NOW(),
            total_connections = total_connections + 1,
            connections_by_dim = CASE
                WHEN p_dimension IS NOT NULL THEN
                    jsonb_set(connections_by_dim, ARRAY[p_dimension],
                        to_jsonb((connections_by_dim->>p_dimension)::int + 1))
                ELSE connections_by_dim
            END,
            updated_at = NOW()
        WHERE id = p_entity_id;
    ELSIF p_entity_type = 'composite' THEN
        UPDATE composites SET
            activation_count = activation_count + 1,
            last_activated = NOW(),
            total_connections = total_connections + 1,
            connections_by_dim = CASE
                WHEN p_dimension IS NOT NULL THEN
                    jsonb_set(connections_by_dim, ARRAY[p_dimension],
                        to_jsonb((connections_by_dim->>p_dimension)::int + 1))
                ELSE connections_by_dim
            END,
            updated_at = NOW()
        WHERE id = p_entity_id;
    END IF;
    -- Update tube thickness via Physarum dynamics
    PERFORM update_tube_thickness(p_entity_type, p_entity_id, 0.1);
END;
$$ LANGUAGE plpgsql;

-- Traverse an edge (activates both endpoints, increases edge thickness)
CREATE OR REPLACE FUNCTION traverse_edge(p_edge_id BIGINT) RETURNS VOID AS $$
DECLARE
    e RECORD;
BEGIN
    SELECT * INTO e FROM edges WHERE id = p_edge_id;
    IF NOT FOUND THEN RETURN; END IF;
    -- Update edge
    UPDATE edges SET
        traversal_count = traversal_count + 1,
        last_traversed = NOW(),
        tube_thickness = GREATEST(0.01, tube_thickness + 0.1 - decay_rate * tube_thickness),
        flow = flow + 1.0,
        temporal_weight = temporal_weight + 1.0
    WHERE id = p_edge_id;
    -- Activate both endpoints
    PERFORM activate_entity(e.source_type, e.source_id, e.dimension);
    PERFORM activate_entity(e.target_type, e.target_id, e.dimension);
END;
$$ LANGUAGE plpgsql;

-- Compute the GL action (total network cost)
CREATE OR REPLACE FUNCTION compute_gl_action() RETURNS FLOAT AS $$
DECLARE
    grad_cost FLOAT;
    maint_cost FLOAT;
    sat_penalty FLOAT;
    total FLOAT;
    alpha FLOAT := 0.1;   -- maintenance parameter
    beta FLOAT := 0.05;   -- saturation parameter
BEGIN
    -- |∂W|² = sum of squared thickness differences across edges
    SELECT COALESCE(SUM(POWER(
        COALESCE((SELECT tube_thickness FROM composites WHERE id = e.source_id AND e.source_type = 'composite'),
                 (SELECT tube_thickness FROM primes WHERE id = e.source_id AND e.source_type = 'prime'), 1.0) -
        COALESCE((SELECT tube_thickness FROM composites WHERE id = e.target_id AND e.target_type = 'composite'),
                 (SELECT tube_thickness FROM primes WHERE id = e.target_id AND e.target_type = 'prime'), 1.0)
    , 2)), 0) INTO grad_cost FROM edges e;
    -- α|W|² = maintenance cost of all nodes
    SELECT alpha * COALESCE(SUM(POWER(tube_thickness, 2)), 0) INTO maint_cost
    FROM (SELECT tube_thickness FROM primes UNION ALL SELECT tube_thickness FROM composites) AS all_nodes;
    -- (β/2)|W|⁴ = saturation penalty
    SELECT (beta/2.0) * COALESCE(SUM(POWER(tube_thickness, 4)), 0) INTO sat_penalty
    FROM (SELECT tube_thickness FROM primes UNION ALL SELECT tube_thickness FROM composites) AS all_nodes;

    total := grad_cost + maint_cost + sat_penalty;
    INSERT INTO network_state (total_nodes, total_edges, gradient_cost, maintenance_cost,
        saturation_penalty, total_action, mean_thickness, snapshot_at)
    SELECT
        (SELECT COUNT(*) FROM primes) + (SELECT COUNT(*) FROM composites),
        (SELECT COUNT(*) FROM edges),
        grad_cost, maint_cost, sat_penalty, total,
        (SELECT AVG(tube_thickness) FROM (
            SELECT tube_thickness FROM primes UNION ALL SELECT tube_thickness FROM composites
        ) t),
        NOW();
    RETURN total;
END;
$$ LANGUAGE plpgsql;

-- Recompute dimension_stats for an entity
CREATE OR REPLACE FUNCTION recompute_dimension_stats(
    p_entity_type VARCHAR,
    p_entity_id BIGINT
) RETURNS VOID AS $$
DECLARE
    dims VARCHAR[] := ARRAY['I_L','I_M','I_S','I_K','I_N','I_A','I_P','I_IE','I_Pr','I_Sigma','I_mu','I_E'];
    d VARCHAR;
    cnt BIGINT;
    max_cnt BIGINT := 0;
    max_dim VARCHAR := 'I_L';
    total BIGINT := 0;
BEGIN
    INSERT INTO dimension_stats (entity_type, entity_id)
    VALUES (p_entity_type, p_entity_id)
    ON CONFLICT (entity_type, entity_id) DO NOTHING;

    FOREACH d IN ARRAY dims LOOP
        SELECT COUNT(*) INTO cnt FROM edges
        WHERE ((source_type = p_entity_type AND source_id = p_entity_id)
            OR (target_type = p_entity_type AND target_id = p_entity_id))
          AND dimension = d;
        EXECUTE format('UPDATE dimension_stats SET conn_%s = $1, updated_at = NOW()
            WHERE entity_type = $2 AND entity_id = $3', d)
            USING cnt, p_entity_type, p_entity_id;
        total := total + cnt;
        IF cnt > max_cnt THEN max_cnt := cnt; max_dim := d; END IF;
    END LOOP;

    -- Temporal and cross-dimensional
    SELECT COUNT(*) INTO cnt FROM edges
    WHERE ((source_type = p_entity_type AND source_id = p_entity_id)
        OR (target_type = p_entity_type AND target_id = p_entity_id))
      AND dimension = 'temporal';

    SELECT COUNT(*) INTO cnt FROM edges
    WHERE ((source_type = p_entity_type AND source_id = p_entity_id)
        OR (target_type = p_entity_type AND target_id = p_entity_id))
      AND dimension = 'cross_dimensional';

    UPDATE dimension_stats SET
        conn_total = total,
        dominant_dimension = max_dim,
        computed_thickness = GREATEST(0.01, LOG(total + 1)),
        updated_at = NOW()
    WHERE entity_type = p_entity_type AND entity_id = p_entity_id;
END;
$$ LANGUAGE plpgsql;

-- Decay all tube thicknesses (run periodically — the forgetting mechanism)
CREATE OR REPLACE FUNCTION global_decay() RETURNS VOID AS $$
BEGIN
    UPDATE primes SET tube_thickness = GREATEST(0.01, tube_thickness * (1.0 - decay_rate));
    UPDATE composites SET tube_thickness = GREATEST(0.01, tube_thickness * (1.0 - decay_rate));
    UPDATE edges SET tube_thickness = GREATEST(0.01, tube_thickness * (1.0 - decay_rate));
END;
$$ LANGUAGE plpgsql;

-- =============================================================================
-- VIEWS: Useful queries
-- =============================================================================

-- Most connected entities (highest tube thickness = most important concepts)
CREATE VIEW v_thickest_nodes AS
SELECT 'prime' as node_type, id, name, tube_thickness, total_connections,
       connections_by_dim, last_activated
FROM primes
UNION ALL
SELECT 'composite', id, name, tube_thickness, total_connections,
       connections_by_dim, last_activated
FROM composites
ORDER BY tube_thickness DESC;

-- Busiest edges (most traversed = strongest associations)
CREATE VIEW v_busiest_edges AS
SELECT e.id, e.predicate, e.dimension, e.tube_thickness, e.traversal_count,
       e.source_type, e.source_id, e.target_type, e.target_id,
       e.hyperbolic_distance, e.ultrametric_distance, e.gl_distance
FROM edges e
ORDER BY e.traversal_count DESC;

-- Dimension connection profile for any entity
CREATE VIEW v_dimension_profiles AS
SELECT entity_type, entity_id, dominant_dimension, conn_total,
    conn_I_L, conn_I_M, conn_I_S, conn_I_K, conn_I_N, conn_I_A,
    conn_I_P, conn_I_IE, conn_I_Pr, conn_I_Sigma, conn_I_mu, conn_I_E,
    conn_temporal, conn_cross_dim, computed_thickness
FROM dimension_stats
ORDER BY conn_total DESC;

-- =============================================================================
-- SCHEMA METADATA
-- =============================================================================

INSERT INTO network_state (total_nodes, total_edges, total_action, snapshot_at)
VALUES (0, 0, 0, NOW());

-- Version tracking
CREATE TABLE IF NOT EXISTS schema_metadata (
    id SERIAL PRIMARY KEY,
    schema_version VARCHAR(50) NOT NULL,
    last_migration TIMESTAMPTZ,
    notes TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

INSERT INTO schema_metadata (schema_version, notes)
VALUES ('2.0.0', 'NRTE Brain-Graph v2: token/engram layer, prime decomposition, Physarum tube dynamics, hyperbolic + ultrametric embeddings, GL action computation, dimension-aware connection tracking, temporal activation, tropical semiring assembly costs');
