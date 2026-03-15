# LaTeX Strategy — All RTSG Publications

## Requirement
- ALL RTSG books use LaTeX typesetting
- Professional mathematical typography throughout
- Equations rendered as real typeset mathematics, not images
- This applies to all books in the pipeline

## Why LaTeX
- Mathematical equations must look professional and serious
- LaTeX is the gold standard for mathematical publishing
- It signals: this is real science, not pop psychology
- The equations ARE the differentiator — they must be beautiful
- Academic credibility without academic gatekeeping

## Key Equations to Feature Prominently

### The Utility Function
$$U = \frac{V}{E \times T}$$

### Cross-Dimensional Edge Count
$$\binom{k}{2} = \frac{k(k-1)}{2}$$

### Maximum Activation State
$$\binom{12}{2} = 66 \text{ edges}$$

### Will as Scalar Multiplier
$$\hat{I} = W \cdot \hat{n}$$

### Compound Intelligence Growth
$$I(t) = I_0 \cdot (1 + r)^t$$

### Percolation Threshold
$$p_c \approx \frac{7}{12} \approx 0.583$$

### Cross-Dimensional Bonus (Product Rule)
$$B_{\text{cross}} = k_1 \cdot k_2$$

### Dual-Channel Learning Bonus
$$B_{\text{dual}} = \sum_{i \in L} \sum_{j \in R} w_{ij}$$

## Production Workflow
1. Write content in markdown/plain text
2. Add LaTeX equations using $$ delimiters
3. Compile with: pdflatex or xelatex
4. Use memoir or tufte-book document class for elegant layout
5. Generate both PDF (for digital/print) and EPUB (for Kindle)

## Template Requirements
- Clean, modern design
- Georgia or similar serif font for body text
- Latin Modern Math for equations
- Wide margins for notes (Tufte-style)
- Chapter headings matching the memoir style (CHAPTER N + title + rule)
- Page headers with book title
- Consistent equation numbering

## Implementation
- Create a master LaTeX template
- All books share the same template
- Consistent visual identity across the RTSG publishing line
- The math IS the brand