-- NRTE Database Schema
-- Production-ready PostgreSQL schema for NRTE (Network Relational Topological Embedding) system
-- Handles entities, relations, dimensional embeddings, and gram matrices

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS pgvector;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Entities table: Core semantic units
CREATE TABLE entities (
    id BIGSERIAL PRIMARY KEY,
    uuid UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL CHECK (type IN ('noun', 'relation', 'thing', 'entity')),
    lojban_form VARCHAR(255),
    english VARCHAR(1024),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_entities_name ON entities(name);
CREATE INDEX idx_entities_type ON entities(type);
CREATE INDEX idx_entities_uuid ON entities(uuid);
CREATE INDEX idx_entities_created_at ON entities(created_at);

-- Relations table: Directional edges between entities
CREATE TABLE relations (
    id BIGSERIAL PRIMARY KEY,
    uuid UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4(),
    subject_id BIGINT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    predicate VARCHAR(255) NOT NULL,
    object_id BIGINT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    weight FLOAT DEFAULT 1.0,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_relations_subject_id ON relations(subject_id);
CREATE INDEX idx_relations_object_id ON relations(object_id);
CREATE INDEX idx_relations_predicate ON relations(predicate);
CREATE INDEX idx_relations_triple ON relations(subject_id, predicate, object_id);
CREATE INDEX idx_relations_created_at ON relations(created_at);

-- Dimension vectors table: Embeddings in RTSG dimensions
CREATE TABLE dimension_vectors (
    id BIGSERIAL PRIMARY KEY,
    uuid UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4(),
    entity_id BIGINT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    dimension VARCHAR(50) NOT NULL CHECK (dimension IN ('relational', 'topological', 'geometric')),
    basis_index INT NOT NULL,
    components FLOAT[] NOT NULL,
    number_system VARCHAR(50) DEFAULT 'real' CHECK (number_system IN ('real', 'complex', 'quaternion')),
    confidence FLOAT DEFAULT 1.0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_dimension_vectors_entity_id ON dimension_vectors(entity_id);
CREATE INDEX idx_dimension_vectors_dimension ON dimension_vectors(dimension);
CREATE INDEX idx_dimension_vectors_entity_dim ON dimension_vectors(entity_id, dimension);
CREATE INDEX idx_dimension_vectors_created_at ON dimension_vectors(created_at);

-- Gram cache table: Precomputed basis matrices and gram products
CREATE TABLE gram_cache (
    id BIGSERIAL PRIMARY KEY,
    uuid UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4(),
    dimension VARCHAR(50) NOT NULL CHECK (dimension IN ('relational', 'topological', 'geometric')),
    dim1 INT NOT NULL,
    dim2 INT NOT NULL,
    number_system VARCHAR(50) DEFAULT 'real',
    matrix_data JSONB NOT NULL,
    gram_product FLOAT NOT NULL,
    computed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_gram_cache_dimension ON gram_cache(dimension);
CREATE INDEX idx_gram_cache_dims ON gram_cache(dim1, dim2, dimension);
CREATE INDEX idx_gram_cache_computed_at ON gram_cache(computed_at);
CREATE UNIQUE INDEX idx_gram_cache_unique ON gram_cache(dimension, dim1, dim2, number_system);

-- Embeddings table: Vector embeddings for similarity search
CREATE TABLE embeddings (
    id BIGSERIAL PRIMARY KEY,
    uuid UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4(),
    entity_id BIGINT NOT NULL REFERENCES entities(id) ON DELETE CASCADE,
    model VARCHAR(100) NOT NULL,
    vector vector(768),
    model_version VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_embeddings_entity_id ON embeddings(entity_id);
CREATE INDEX idx_embeddings_model ON embeddings(model);
CREATE INDEX idx_embeddings_vector ON embeddings USING ivfflat (vector vector_cosine_ops)
    WITH (lists = 100);
CREATE UNIQUE INDEX idx_embeddings_entity_model ON embeddings(entity_id, model);
CREATE INDEX idx_embeddings_created_at ON embeddings(created_at);

-- Relation embeddings table: Vector embeddings for relation vectors
CREATE TABLE relation_embeddings (
    id BIGSERIAL PRIMARY KEY,
    uuid UUID NOT NULL UNIQUE DEFAULT uuid_generate_v4(),
    relation_id BIGINT NOT NULL REFERENCES relations(id) ON DELETE CASCADE,
    model VARCHAR(100) NOT NULL,
    vector vector(768),
    model_version VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_relation_embeddings_relation_id ON relation_embeddings(relation_id);
CREATE INDEX idx_relation_embeddings_model ON relation_embeddings(model);
CREATE INDEX idx_relation_embeddings_vector ON relation_embeddings USING ivfflat (vector vector_cosine_ops)
    WITH (lists = 100);
CREATE UNIQUE INDEX idx_relation_embeddings_rel_model ON relation_embeddings(relation_id, model);

-- Metadata tracking table
CREATE TABLE schema_metadata (
    id SERIAL PRIMARY KEY,
    schema_version VARCHAR(50) NOT NULL,
    last_migration TIMESTAMP WITH TIME ZONE,
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Insert initial schema version
INSERT INTO schema_metadata (schema_version, notes)
VALUES ('1.0.0', 'Initial NRTE schema with entities, relations, dimensions, and vector embeddings');
