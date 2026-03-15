import { useState, useMemo, useCallback } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ScatterChart, Scatter, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar } from "recharts";

// ============================================================
// RTSG DIMENSION EXPLORER
// Interactive prototype for visualizing inner products between
// the three RTSG spaces across different number systems and
// mathematical perspectives.
// ============================================================

// --- Data Model ---

const DIMENSIONS = {
  relational: {
    name: "Relational (R)",
    color: "#3b82f6",
    description: "Network topology, adjacency, connectivity patterns",
    basisLabels: ["Symmetry", "Connectivity", "Centrality", "Flow", "Clustering"],
    // Default basis vectors in R^5 representation
    defaultBasis: [
      [1, 0.8, 0.3, 0.5, 0.7],
      [0.8, 1, 0.6, 0.4, 0.5],
      [0.3, 0.6, 1, 0.7, 0.2],
      [0.5, 0.4, 0.7, 1, 0.6],
      [0.7, 0.5, 0.2, 0.6, 1],
    ],
  },
  topological: {
    name: "Topological (T)",
    color: "#10b981",
    description: "Continuity, holes, genus, Betti numbers, boundaries",
    basisLabels: ["Genus", "Betti-0", "Betti-1", "Euler-χ", "Boundary"],
    defaultBasis: [
      [1, 0.2, 0.9, 0.4, 0.1],
      [0.2, 1, 0.3, 0.8, 0.5],
      [0.9, 0.3, 1, 0.2, 0.7],
      [0.4, 0.8, 0.2, 1, 0.3],
      [0.1, 0.5, 0.7, 0.3, 1],
    ],
  },
  geometric: {
    name: "Geometric (G)",
    color: "#f59e0b",
    description: "Curvature, volume, area, metric structure, geodesics",
    basisLabels: ["Curvature", "Volume", "Area", "Geodesic-L", "Torsion"],
    defaultBasis: [
      [1, 0.5, 0.4, 0.6, 0.3],
      [0.5, 1, 0.8, 0.3, 0.2],
      [0.4, 0.8, 1, 0.5, 0.4],
      [0.6, 0.3, 0.5, 1, 0.7],
      [0.3, 0.2, 0.4, 0.7, 1],
    ],
  },
};

const NUMBER_SYSTEMS = {
  real: { name: "ℝ (Real)", description: "Standard real numbers" },
  complex: { name: "ℂ (Complex)", description: "Complex plane with phase" },
  padic2: { name: "ℚ₂ (2-adic)", description: "2-adic numbers, ultrametric" },
  padic3: { name: "ℚ₃ (3-adic)", description: "3-adic numbers" },
  padic5: { name: "ℚ₅ (5-adic)", description: "5-adic numbers" },
  adelic: { name: "𝔸 (Adelic)", description: "Full adelic product" },
};

const PERSPECTIVES = {
  algebra: { name: "Algebra", description: "Matrix form, eigenvalues, determinant" },
  geometry: { name: "Geometry", description: "Shape visualization, curvature" },
  topology: { name: "Topology", description: "Graph structure, connectivity" },
  numberTheory: { name: "Number Theory", description: "Prime decomposition, p-adic norms" },
  categoryTheory: { name: "Category Theory", description: "Morphisms, functors, natural transformations" },
  analysis: { name: "Analysis", description: "Spectral decomposition, eigenvalue distribution" },
};

// --- Mathematical Computations ---

function computeInnerProduct(v1, v2, numberSystem) {
  const n = Math.min(v1.length, v2.length);
  let result = { real: 0, imag: 0 };

  for (let i = 0; i < n; i++) {
    switch (numberSystem) {
      case "real":
        result.real += v1[i] * v2[i];
        break;
      case "complex": {
        const phase1 = Math.PI * v1[i] * 0.5;
        const phase2 = Math.PI * v2[i] * 0.5;
        result.real += v1[i] * v2[i] * Math.cos(phase1 - phase2);
        result.imag += v1[i] * v2[i] * Math.sin(phase1 - phase2);
        break;
      }
      case "padic2":
      case "padic3":
      case "padic5": {
        const p = numberSystem === "padic2" ? 2 : numberSystem === "padic3" ? 3 : 5;
        const val = v1[i] * v2[i];
        const vp = val === 0 ? 10 : Math.floor(Math.log(Math.abs(1 / val)) / Math.log(p));
        result.real += Math.pow(p, -Math.max(0, Math.min(vp, 5)));
        break;
      }
      case "adelic": {
        let adelicVal = v1[i] * v2[i]; // archimedean
        for (const p of [2, 3, 5, 7]) {
          const val = v1[i] * v2[i];
          adelicVal *= val !== 0 ? Math.min(1, Math.pow(p, -Math.abs(val))) : 0;
        }
        result.real += adelicVal;
        break;
      }
      default:
        result.real += v1[i] * v2[i];
    }
  }
  return result;
}

function computeGramMatrix(basis, numberSystem) {
  const n = basis.length;
  const gram = Array.from({ length: n }, () => Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      const ip = computeInnerProduct(basis[i], basis[j], numberSystem);
      gram[i][j] = ip.real;
    }
  }
  return gram;
}

function computeEigenvalues(matrix) {
  // Power iteration approximation for 5x5
  const n = matrix.length;
  const eigs = [];
  let M = matrix.map((r) => [...r]);

  for (let iter = 0; iter < n; iter++) {
    let v = Array(n).fill(0).map(() => Math.random());
    let norm = Math.sqrt(v.reduce((s, x) => s + x * x, 0));
    v = v.map((x) => x / norm);

    for (let k = 0; k < 50; k++) {
      const Mv = M.map((row) => row.reduce((s, val, j) => s + val * v[j], 0));
      norm = Math.sqrt(Mv.reduce((s, x) => s + x * x, 0));
      if (norm < 1e-12) break;
      v = Mv.map((x) => x / norm);
    }
    const Mv = M.map((row) => row.reduce((s, val, j) => s + val * v[j], 0));
    const eigenval = v.reduce((s, x, i) => s + x * Mv[i], 0);
    eigs.push(eigenval);

    // Deflate
    for (let i = 0; i < n; i++)
      for (let j = 0; j < n; j++) M[i][j] -= eigenval * v[i] * v[j];
  }
  return eigs.sort((a, b) => b - a);
}

function computeCrossInnerProducts(dim1Key, dim2Key, numberSystem) {
  const d1 = DIMENSIONS[dim1Key];
  const d2 = DIMENSIONS[dim2Key];
  const results = [];
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      const ip = computeInnerProduct(d1.defaultBasis[i], d2.defaultBasis[j], numberSystem);
      results.push({
        label: `${d1.basisLabels[i]}×${d2.basisLabels[j]}`,
        value: ip.real,
        phase: ip.imag,
        i,
        j,
      });
    }
  }
  return results;
}

// --- Visualization Components ---

function MatrixView({ matrix, labels, title, color }) {
  const maxAbs = Math.max(...matrix.flat().map(Math.abs), 0.01);
  return (
    <div className="mb-4">
      <h4 className="text-sm font-semibold mb-2" style={{ color }}>
        {title}
      </h4>
      <div className="inline-block border border-gray-700 rounded">
        <table className="text-xs">
          <thead>
            <tr>
              <th className="p-1 text-gray-500"></th>
              {labels.map((l, i) => (
                <th key={i} className="p-1 text-gray-400 font-normal" style={{ maxWidth: 60, overflow: "hidden" }}>
                  {l.slice(0, 6)}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {matrix.map((row, i) => (
              <tr key={i}>
                <td className="p-1 text-gray-400 text-right pr-2" style={{ maxWidth: 60, overflow: "hidden" }}>
                  {labels[i].slice(0, 6)}
                </td>
                {row.map((val, j) => {
                  const intensity = Math.abs(val) / maxAbs;
                  const bg =
                    val >= 0
                      ? `rgba(59, 130, 246, ${intensity * 0.6})`
                      : `rgba(239, 68, 68, ${intensity * 0.6})`;
                  return (
                    <td
                      key={j}
                      className="p-1 text-center text-white font-mono"
                      style={{ background: bg, minWidth: 48 }}
                    >
                      {val.toFixed(2)}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function EigenvalueChart({ eigenvalues, color, title }) {
  const data = eigenvalues.map((v, i) => ({ index: `λ${i + 1}`, value: v }));
  return (
    <div className="mb-4">
      <h4 className="text-sm font-semibold mb-2" style={{ color }}>
        {title}
      </h4>
      <ResponsiveContainer width="100%" height={160}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#333" />
          <XAxis dataKey="index" stroke="#888" fontSize={11} />
          <YAxis stroke="#888" fontSize={11} />
          <Tooltip
            contentStyle={{ background: "#1a1a2e", border: "1px solid #444" }}
          />
          <Line
            type="monotone"
            dataKey="value"
            stroke={color}
            strokeWidth={2}
            dot={{ fill: color, r: 4 }}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

function ShapeRadar({ data, labels, color, title }) {
  const radarData = labels.map((l, i) => ({
    subject: l.slice(0, 8),
    value: Math.abs(data[i] || 0),
  }));
  return (
    <div className="mb-4">
      <h4 className="text-sm font-semibold mb-2" style={{ color }}>
        {title}
      </h4>
      <ResponsiveContainer width="100%" height={200}>
        <RadarChart data={radarData}>
          <PolarGrid stroke="#444" />
          <PolarAngleAxis dataKey="subject" stroke="#888" fontSize={10} />
          <PolarRadiusAxis stroke="#666" fontSize={9} />
          <Radar dataKey="value" stroke={color} fill={color} fillOpacity={0.2} />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
}

function CrossProductHeatmap({ crossData, dim1, dim2 }) {
  const gridSize = 5;
  const maxAbs = Math.max(...crossData.map((d) => Math.abs(d.value)), 0.01);

  return (
    <div className="mb-4">
      <h4 className="text-sm font-semibold mb-2 text-purple-400">
        Cross Inner Product: {DIMENSIONS[dim1].name} × {DIMENSIONS[dim2].name}
      </h4>
      <div className="inline-block border border-gray-700 rounded">
        <table className="text-xs">
          <thead>
            <tr>
              <th className="p-1 text-gray-500"></th>
              {DIMENSIONS[dim2].basisLabels.map((l, i) => (
                <th key={i} className="p-1 text-gray-400 font-normal">
                  {l.slice(0, 6)}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {Array.from({ length: gridSize }, (_, i) => (
              <tr key={i}>
                <td className="p-1 text-gray-400 text-right pr-2">
                  {DIMENSIONS[dim1].basisLabels[i].slice(0, 6)}
                </td>
                {Array.from({ length: gridSize }, (_, j) => {
                  const entry = crossData.find((d) => d.i === i && d.j === j);
                  const val = entry ? entry.value : 0;
                  const intensity = Math.abs(val) / maxAbs;
                  const bg =
                    val >= 0
                      ? `rgba(168, 85, 247, ${intensity * 0.6})`
                      : `rgba(239, 68, 68, ${intensity * 0.6})`;
                  return (
                    <td
                      key={j}
                      className="p-1 text-center text-white font-mono"
                      style={{ background: bg, minWidth: 48 }}
                    >
                      {val.toFixed(3)}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function TopologyView({ gram, labels, color, title }) {
  // Show connections above threshold as a simple adjacency description
  const threshold = 0.5;
  const edges = [];
  for (let i = 0; i < gram.length; i++) {
    for (let j = i + 1; j < gram[i].length; j++) {
      if (Math.abs(gram[i][j]) > threshold) {
        edges.push({ from: labels[i], to: labels[j], weight: gram[i][j] });
      }
    }
  }

  return (
    <div className="mb-4">
      <h4 className="text-sm font-semibold mb-2" style={{ color }}>
        {title} (edges with |⟨·,·⟩| {">"} {threshold})
      </h4>
      <div className="bg-gray-900 rounded p-3 text-xs font-mono space-y-1">
        {edges.length === 0 ? (
          <div className="text-gray-500">No strong connections</div>
        ) : (
          edges.map((e, i) => (
            <div key={i} className="flex items-center gap-2">
              <span className="text-blue-300">{e.from.slice(0, 8)}</span>
              <span className="text-gray-500">
                {"—"} {e.weight.toFixed(3)} {"—"}
              </span>
              <span className="text-green-300">{e.to.slice(0, 8)}</span>
              <span
                className="inline-block h-1 rounded"
                style={{
                  width: `${Math.abs(e.weight) * 80}px`,
                  background: e.weight > 0 ? color : "#ef4444",
                }}
              />
            </div>
          ))
        )}
        <div className="text-gray-500 mt-2">
          Nodes: {labels.length} | Edges: {edges.length} | Density:{" "}
          {((2 * edges.length) / (labels.length * (labels.length - 1))).toFixed(2)}
        </div>
      </div>
    </div>
  );
}

function NumberTheoryView({ gram, labels, color, numberSystem }) {
  const det = gram.reduce((acc, row, i) => {
    // Simplified determinant via diagonal product (approximation for display)
    return acc * row[i];
  }, 1);
  const trace = gram.reduce((acc, row, i) => acc + row[i], 0);

  const primeDecomp = [2, 3, 5, 7, 11].map((p) => ({
    prime: p,
    valuation: Math.abs(det) > 0.01 ? Math.round(Math.log(Math.abs(det)) / Math.log(p) * 10) / 10 : 0,
    norm: Math.pow(p, -Math.abs(trace) / 10),
  }));

  return (
    <div className="mb-4">
      <h4 className="text-sm font-semibold mb-2" style={{ color }}>
        Number Theory View ({NUMBER_SYSTEMS[numberSystem].name})
      </h4>
      <div className="bg-gray-900 rounded p-3 text-xs font-mono space-y-2">
        <div>
          <span className="text-gray-400">det(G) ≈ </span>
          <span className="text-yellow-300">{det.toFixed(4)}</span>
        </div>
        <div>
          <span className="text-gray-400">tr(G) = </span>
          <span className="text-yellow-300">{trace.toFixed(4)}</span>
        </div>
        <div className="text-gray-400 mt-1">Prime decomposition (approx):</div>
        {primeDecomp.map((pd) => (
          <div key={pd.prime} className="flex items-center gap-2">
            <span className="text-purple-300 w-8">p={pd.prime}</span>
            <span className="text-gray-400">v_p ≈ {pd.valuation.toFixed(1)}</span>
            <span className="text-gray-400">|·|_p ≈ {pd.norm.toFixed(4)}</span>
            <span
              className="inline-block h-2 rounded"
              style={{
                width: `${pd.norm * 100}px`,
                background: `hsl(${pd.prime * 40}, 70%, 50%)`,
              }}
            />
          </div>
        ))}
      </div>
    </div>
  );
}

function CategoryView({ dim1, dim2, crossData }) {
  const totalIP = crossData.reduce((s, d) => s + d.value, 0) / crossData.length;
  const isIso = Math.abs(totalIP) > 0.3;
  const isMono = crossData.every((d) => d.value >= -0.1);

  return (
    <div className="mb-4">
      <h4 className="text-sm font-semibold mb-2 text-pink-400">Category Theory View</h4>
      <div className="bg-gray-900 rounded p-3 text-xs font-mono space-y-2">
        <div className="text-gray-300">
          Objects: <span className="text-blue-300">{DIMENSIONS[dim1].name}</span>,{" "}
          <span className="text-green-300">{DIMENSIONS[dim2].name}</span>
        </div>
        <div className="text-gray-300">
          Morphism (inner product functor): ⟨−,−⟩ :{" "}
          {DIMENSIONS[dim1].name.charAt(0)} × {DIMENSIONS[dim2].name.charAt(0)} → 𝕜
        </div>
        <div className="text-gray-300">
          Average coupling: <span className="text-yellow-300">{totalIP.toFixed(4)}</span>
        </div>
        <div className="text-gray-300">
          Morphism type:{" "}
          <span className={isIso ? "text-green-400" : "text-red-400"}>
            {isIso ? "Strong coupling (quasi-isomorphism)" : "Weak coupling (sparse)"}
          </span>
        </div>
        <div className="text-gray-300">
          Positivity:{" "}
          <span className={isMono ? "text-green-400" : "text-yellow-400"}>
            {isMono ? "Monotone (all ≥ 0)" : "Mixed sign (non-monotone)"}
          </span>
        </div>
        <div className="mt-2 text-gray-500">
          Natural transformation: the inner product defines a bifunctor
          from the product category R×T×G to the base field,
          with the number system as the codomain object.
        </div>
      </div>
    </div>
  );
}

// --- Main App ---

export default function RTSGExplorer() {
  const [dim1, setDim1] = useState("relational");
  const [dim2, setDim2] = useState("topological");
  const [numberSystem, setNumberSystem] = useState("real");
  const [perspective, setPerspective] = useState("algebra");

  const gram1 = useMemo(
    () => computeGramMatrix(DIMENSIONS[dim1].defaultBasis, numberSystem),
    [dim1, numberSystem]
  );
  const gram2 = useMemo(
    () => computeGramMatrix(DIMENSIONS[dim2].defaultBasis, numberSystem),
    [dim2, numberSystem]
  );
  const eigs1 = useMemo(() => computeEigenvalues(gram1), [gram1]);
  const eigs2 = useMemo(() => computeEigenvalues(gram2), [gram2]);
  const crossData = useMemo(
    () => computeCrossInnerProducts(dim1, dim2, numberSystem),
    [dim1, dim2, numberSystem]
  );

  const d1 = DIMENSIONS[dim1];
  const d2 = DIMENSIONS[dim2];

  return (
    <div className="min-h-screen bg-gray-950 text-white p-4" style={{ fontFamily: "system-ui, sans-serif" }}>
      {/* Header */}
      <div className="max-w-6xl mx-auto">
        <h1 className="text-2xl font-bold mb-1">RTSG Dimension Explorer</h1>
        <p className="text-gray-400 text-sm mb-6">
          Relational Three-Space Geometry — Interactive inner product visualization
        </p>

        {/* Controls */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">
          {/* Dimension 1 */}
          <div>
            <label className="text-xs text-gray-400 block mb-1">Dimension 1</label>
            <select
              value={dim1}
              onChange={(e) => setDim1(e.target.value)}
              className="w-full bg-gray-800 border border-gray-700 rounded px-3 py-2 text-sm"
            >
              {Object.entries(DIMENSIONS).map(([k, v]) => (
                <option key={k} value={k}>
                  {v.name}
                </option>
              ))}
            </select>
          </div>

          {/* Dimension 2 */}
          <div>
            <label className="text-xs text-gray-400 block mb-1">Dimension 2</label>
            <select
              value={dim2}
              onChange={(e) => setDim2(e.target.value)}
              className="w-full bg-gray-800 border border-gray-700 rounded px-3 py-2 text-sm"
            >
              {Object.entries(DIMENSIONS).map(([k, v]) => (
                <option key={k} value={k}>
                  {v.name}
                </option>
              ))}
            </select>
          </div>

          {/* Number System */}
          <div>
            <label className="text-xs text-gray-400 block mb-1">Number System</label>
            <select
              value={numberSystem}
              onChange={(e) => setNumberSystem(e.target.value)}
              className="w-full bg-gray-800 border border-gray-700 rounded px-3 py-2 text-sm"
            >
              {Object.entries(NUMBER_SYSTEMS).map(([k, v]) => (
                <option key={k} value={k}>
                  {v.name}
                </option>
              ))}
            </select>
          </div>

          {/* Math Perspective */}
          <div>
            <label className="text-xs text-gray-400 block mb-1">Perspective</label>
            <select
              value={perspective}
              onChange={(e) => setPerspective(e.target.value)}
              className="w-full bg-gray-800 border border-gray-700 rounded px-3 py-2 text-sm"
            >
              {Object.entries(PERSPECTIVES).map(([k, v]) => (
                <option key={k} value={k}>
                  {v.name}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Info Bar */}
        <div className="bg-gray-900 rounded-lg p-3 mb-6 flex flex-wrap gap-4 text-xs">
          <div>
            <span className="text-gray-500">Dim 1: </span>
            <span style={{ color: d1.color }}>{d1.name}</span>
            <span className="text-gray-600"> — {d1.description}</span>
          </div>
          <div>
            <span className="text-gray-500">Dim 2: </span>
            <span style={{ color: d2.color }}>{d2.name}</span>
            <span className="text-gray-600"> — {d2.description}</span>
          </div>
          <div>
            <span className="text-gray-500">Field: </span>
            <span className="text-purple-300">{NUMBER_SYSTEMS[numberSystem].name}</span>
          </div>
          <div>
            <span className="text-gray-500">View: </span>
            <span className="text-pink-300">{PERSPECTIVES[perspective].name}</span>
          </div>
        </div>

        {/* Main Content Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Left Column: Dimension 1 */}
          <div className="bg-gray-900 rounded-lg p-4 border border-gray-800">
            <h3 className="font-semibold mb-3" style={{ color: d1.color }}>
              {d1.name}
            </h3>

            {(perspective === "algebra" || perspective === "analysis") && (
              <>
                <MatrixView
                  matrix={gram1}
                  labels={d1.basisLabels}
                  title="Gram Matrix ⟨eᵢ, eⱼ⟩"
                  color={d1.color}
                />
                <EigenvalueChart
                  eigenvalues={eigs1}
                  color={d1.color}
                  title="Eigenvalue Spectrum"
                />
              </>
            )}

            {perspective === "geometry" && (
              <ShapeRadar
                data={gram1[0]}
                labels={d1.basisLabels}
                color={d1.color}
                title="Geometric Shape (basis 1 profile)"
              />
            )}

            {perspective === "topology" && (
              <TopologyView
                gram={gram1}
                labels={d1.basisLabels}
                color={d1.color}
                title="Topological Graph"
              />
            )}

            {perspective === "numberTheory" && (
              <NumberTheoryView
                gram={gram1}
                labels={d1.basisLabels}
                color={d1.color}
                numberSystem={numberSystem}
              />
            )}

            {perspective === "categoryTheory" && (
              <div className="text-xs text-gray-400 p-3 bg-gray-800 rounded font-mono">
                <div className="text-blue-300 mb-2">Object: {d1.name}</div>
                <div>Endomorphism ring: Mat₅({NUMBER_SYSTEMS[numberSystem].name})</div>
                <div>dim = 5, rank(G) = {eigs1.filter((e) => Math.abs(e) > 0.01).length}</div>
                <div>
                  Positive definite: {eigs1.every((e) => e > -0.01) ? "Yes" : "No"}
                </div>
              </div>
            )}
          </div>

          {/* Right Column: Dimension 2 */}
          <div className="bg-gray-900 rounded-lg p-4 border border-gray-800">
            <h3 className="font-semibold mb-3" style={{ color: d2.color }}>
              {d2.name}
            </h3>

            {(perspective === "algebra" || perspective === "analysis") && (
              <>
                <MatrixView
                  matrix={gram2}
                  labels={d2.basisLabels}
                  title="Gram Matrix ⟨eᵢ, eⱼ⟩"
                  color={d2.color}
                />
                <EigenvalueChart
                  eigenvalues={eigs2}
                  color={d2.color}
                  title="Eigenvalue Spectrum"
                />
              </>
            )}

            {perspective === "geometry" && (
              <ShapeRadar
                data={gram2[0]}
                labels={d2.basisLabels}
                color={d2.color}
                title="Geometric Shape (basis 1 profile)"
              />
            )}

            {perspective === "topology" && (
              <TopologyView
                gram={gram2}
                labels={d2.basisLabels}
                color={d2.color}
                title="Topological Graph"
              />
            )}

            {perspective === "numberTheory" && (
              <NumberTheoryView
                gram={gram2}
                labels={d2.basisLabels}
                color={d2.color}
                numberSystem={numberSystem}
              />
            )}

            {perspective === "categoryTheory" && (
              <div className="text-xs text-gray-400 p-3 bg-gray-800 rounded font-mono">
                <div className="text-green-300 mb-2">Object: {d2.name}</div>
                <div>Endomorphism ring: Mat₅({NUMBER_SYSTEMS[numberSystem].name})</div>
                <div>dim = 5, rank(G) = {eigs2.filter((e) => Math.abs(e) > 0.01).length}</div>
                <div>
                  Positive definite: {eigs2.every((e) => e > -0.01) ? "Yes" : "No"}
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Cross-Dimensional Analysis */}
        <div className="mt-6 bg-gray-900 rounded-lg p-4 border border-purple-900">
          <h3 className="font-semibold mb-3 text-purple-400">
            Cross-Dimensional Analysis: {d1.name} × {d2.name}
          </h3>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <CrossProductHeatmap crossData={crossData} dim1={dim1} dim2={dim2} />

            {perspective === "categoryTheory" ? (
              <CategoryView dim1={dim1} dim2={dim2} crossData={crossData} />
            ) : (
              <div>
                <h4 className="text-sm font-semibold mb-2 text-purple-400">
                  Inner Product Distribution
                </h4>
                <ResponsiveContainer width="100%" height={200}>
                  <ScatterChart>
                    <CartesianGrid strokeDasharray="3 3" stroke="#333" />
                    <XAxis
                      type="number"
                      dataKey="value"
                      name="⟨R,T⟩"
                      stroke="#888"
                      fontSize={11}
                    />
                    <YAxis
                      type="number"
                      dataKey="phase"
                      name="Phase"
                      stroke="#888"
                      fontSize={11}
                    />
                    <Tooltip
                      contentStyle={{ background: "#1a1a2e", border: "1px solid #444" }}
                    />
                    <Scatter data={crossData} fill="#a855f7" />
                  </ScatterChart>
                </ResponsiveContainer>
              </div>
            )}
          </div>

          {/* Summary Stats */}
          <div className="mt-4 grid grid-cols-2 md:grid-cols-4 gap-3 text-xs">
            <div className="bg-gray-800 rounded p-2">
              <div className="text-gray-500">Total coupling</div>
              <div className="text-lg font-mono text-purple-300">
                {(crossData.reduce((s, d) => s + d.value, 0) / crossData.length).toFixed(4)}
              </div>
            </div>
            <div className="bg-gray-800 rounded p-2">
              <div className="text-gray-500">Max |⟨·,·⟩|</div>
              <div className="text-lg font-mono text-blue-300">
                {Math.max(...crossData.map((d) => Math.abs(d.value))).toFixed(4)}
              </div>
            </div>
            <div className="bg-gray-800 rounded p-2">
              <div className="text-gray-500">Spectral gap (D1)</div>
              <div className="text-lg font-mono text-green-300">
                {(eigs1[0] - eigs1[eigs1.length - 1]).toFixed(4)}
              </div>
            </div>
            <div className="bg-gray-800 rounded p-2">
              <div className="text-gray-500">Spectral gap (D2)</div>
              <div className="text-lg font-mono text-yellow-300">
                {(eigs2[0] - eigs2[eigs2.length - 1]).toFixed(4)}
              </div>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-6 text-center text-xs text-gray-600">
          RTSG v6.0 Dimension Explorer — Relational Three-Space Geometry Framework
        </div>
      </div>
    </div>
  );
}
