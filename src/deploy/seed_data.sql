-- NRTE Seed Data
-- Initializes the 3 RTSG dimensions with their basis matrices and definitions

-- Insert dimension basis vectors and gram matrices
-- Note: We start by populating the dimension definitions as entities

-- Insert dimension entities
INSERT INTO entities (name, type, english, metadata)
VALUES
    ('relational', 'entity', 'Relational Dimension - Network Structure Properties',
     '{"category": "dimension", "basis_size": 5, "coordinates": ["Symmetry", "Connectivity", "Centrality", "Flow", "Clustering"]}'),
    ('topological', 'entity', 'Topological Dimension - Shape and Topology Properties',
     '{"category": "dimension", "basis_size": 5, "coordinates": ["Genus", "Betti-0", "Betti-1", "Euler-χ", "Boundary"]}'),
    ('geometric', 'entity', 'Geometric Dimension - Spatial and Curvature Properties',
     '{"category": "dimension", "basis_size": 5, "coordinates": ["Curvature", "Volume", "Area", "Geodesic-L", "Torsion"]}')
ON CONFLICT (name) DO NOTHING;

-- Relational dimension: Symmetry, Connectivity, Centrality, Flow, Clustering
-- Basis matrix: 5x5 correlation matrix of relational properties
INSERT INTO gram_cache (dimension, dim1, dim2, number_system, matrix_data, gram_product)
VALUES
    ('relational', 1, 1, 'real', '{"value": 1.0}', 1.0),
    ('relational', 1, 2, 'real', '{"value": 0.8}', 0.8),
    ('relational', 1, 3, 'real', '{"value": 0.3}', 0.3),
    ('relational', 1, 4, 'real', '{"value": 0.5}', 0.5),
    ('relational', 1, 5, 'real', '{"value": 0.7}', 0.7),
    ('relational', 2, 1, 'real', '{"value": 0.8}', 0.8),
    ('relational', 2, 2, 'real', '{"value": 1.0}', 1.0),
    ('relational', 2, 3, 'real', '{"value": 0.6}', 0.6),
    ('relational', 2, 4, 'real', '{"value": 0.4}', 0.4),
    ('relational', 2, 5, 'real', '{"value": 0.5}', 0.5),
    ('relational', 3, 1, 'real', '{"value": 0.3}', 0.3),
    ('relational', 3, 2, 'real', '{"value": 0.6}', 0.6),
    ('relational', 3, 3, 'real', '{"value": 1.0}', 1.0),
    ('relational', 3, 4, 'real', '{"value": 0.7}', 0.7),
    ('relational', 3, 5, 'real', '{"value": 0.2}', 0.2),
    ('relational', 4, 1, 'real', '{"value": 0.5}', 0.5),
    ('relational', 4, 2, 'real', '{"value": 0.4}', 0.4),
    ('relational', 4, 3, 'real', '{"value": 0.7}', 0.7),
    ('relational', 4, 4, 'real', '{"value": 1.0}', 1.0),
    ('relational', 4, 5, 'real', '{"value": 0.6}', 0.6),
    ('relational', 5, 1, 'real', '{"value": 0.7}', 0.7),
    ('relational', 5, 2, 'real', '{"value": 0.5}', 0.5),
    ('relational', 5, 3, 'real', '{"value": 0.2}', 0.2),
    ('relational', 5, 4, 'real', '{"value": 0.6}', 0.6),
    ('relational', 5, 5, 'real', '{"value": 1.0}', 1.0)
ON CONFLICT (dimension, dim1, dim2, number_system) DO NOTHING;

-- Topological dimension: Genus, Betti-0, Betti-1, Euler-χ, Boundary
-- Basis matrix: 5x5 correlation matrix of topological properties
INSERT INTO gram_cache (dimension, dim1, dim2, number_system, matrix_data, gram_product)
VALUES
    ('topological', 1, 1, 'real', '{"value": 1.0}', 1.0),
    ('topological', 1, 2, 'real', '{"value": 0.2}', 0.2),
    ('topological', 1, 3, 'real', '{"value": 0.9}', 0.9),
    ('topological', 1, 4, 'real', '{"value": 0.4}', 0.4),
    ('topological', 1, 5, 'real', '{"value": 0.1}', 0.1),
    ('topological', 2, 1, 'real', '{"value": 0.2}', 0.2),
    ('topological', 2, 2, 'real', '{"value": 1.0}', 1.0),
    ('topological', 2, 3, 'real', '{"value": 0.3}', 0.3),
    ('topological', 2, 4, 'real', '{"value": 0.8}', 0.8),
    ('topological', 2, 5, 'real', '{"value": 0.5}', 0.5),
    ('topological', 3, 1, 'real', '{"value": 0.9}', 0.9),
    ('topological', 3, 2, 'real', '{"value": 0.3}', 0.3),
    ('topological', 3, 3, 'real', '{"value": 1.0}', 1.0),
    ('topological', 3, 4, 'real', '{"value": 0.2}', 0.2),
    ('topological', 3, 5, 'real', '{"value": 0.7}', 0.7),
    ('topological', 4, 1, 'real', '{"value": 0.4}', 0.4),
    ('topological', 4, 2, 'real', '{"value": 0.8}', 0.8),
    ('topological', 4, 3, 'real', '{"value": 0.2}', 0.2),
    ('topological', 4, 4, 'real', '{"value": 1.0}', 1.0),
    ('topological', 4, 5, 'real', '{"value": 0.3}', 0.3),
    ('topological', 5, 1, 'real', '{"value": 0.1}', 0.1),
    ('topological', 5, 2, 'real', '{"value": 0.5}', 0.5),
    ('topological', 5, 3, 'real', '{"value": 0.7}', 0.7),
    ('topological', 5, 4, 'real', '{"value": 0.3}', 0.3),
    ('topological', 5, 5, 'real', '{"value": 1.0}', 1.0)
ON CONFLICT (dimension, dim1, dim2, number_system) DO NOTHING;

-- Geometric dimension: Curvature, Volume, Area, Geodesic-L, Torsion
-- Basis matrix: 5x5 correlation matrix of geometric properties
INSERT INTO gram_cache (dimension, dim1, dim2, number_system, matrix_data, gram_product)
VALUES
    ('geometric', 1, 1, 'real', '{"value": 1.0}', 1.0),
    ('geometric', 1, 2, 'real', '{"value": 0.5}', 0.5),
    ('geometric', 1, 3, 'real', '{"value": 0.4}', 0.4),
    ('geometric', 1, 4, 'real', '{"value": 0.6}', 0.6),
    ('geometric', 1, 5, 'real', '{"value": 0.3}', 0.3),
    ('geometric', 2, 1, 'real', '{"value": 0.5}', 0.5),
    ('geometric', 2, 2, 'real', '{"value": 1.0}', 1.0),
    ('geometric', 2, 3, 'real', '{"value": 0.8}', 0.8),
    ('geometric', 2, 4, 'real', '{"value": 0.3}', 0.3),
    ('geometric', 2, 5, 'real', '{"value": 0.2}', 0.2),
    ('geometric', 3, 1, 'real', '{"value": 0.4}', 0.4),
    ('geometric', 3, 2, 'real', '{"value": 0.8}', 0.8),
    ('geometric', 3, 3, 'real', '{"value": 1.0}', 1.0),
    ('geometric', 3, 4, 'real', '{"value": 0.5}', 0.5),
    ('geometric', 3, 5, 'real', '{"value": 0.4}', 0.4),
    ('geometric', 4, 1, 'real', '{"value": 0.6}', 0.6),
    ('geometric', 4, 2, 'real', '{"value": 0.3}', 0.3),
    ('geometric', 4, 3, 'real', '{"value": 0.5}', 0.5),
    ('geometric', 4, 4, 'real', '{"value": 1.0}', 1.0),
    ('geometric', 4, 5, 'real', '{"value": 0.7}', 0.7),
    ('geometric', 5, 1, 'real', '{"value": 0.3}', 0.3),
    ('geometric', 5, 2, 'real', '{"value": 0.2}', 0.2),
    ('geometric', 5, 3, 'real', '{"value": 0.4}', 0.4),
    ('geometric', 5, 4, 'real', '{"value": 0.7}', 0.7),
    ('geometric', 5, 5, 'real', '{"value": 1.0}', 1.0)
ON CONFLICT (dimension, dim1, dim2, number_system) DO NOTHING;
