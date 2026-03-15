---
title: "Linguistics Companion Paper"
version: "2.0.0"
last_updated: "2026-03-05"
status: ARXIV-READY
arxiv_category: "cs.CL"
---

# Linguistics Companion Paper

**Jean-Paul Niko** · February 2026

\begin{center}
{\LARGE\bfseries\color{sectionblue} The Geometry of Translation Loss:  [3pt]
A Topos-Theoretic Foundation for the  [3pt]
Limits of Cross-Linguistic Communication}

{\large Jean-Paul Niko}  [4pt]
{}  [2pt]
{\small`niko@triptomean.com`}  [12pt]
{\small February 2026}
\end{center}

!!! abstract "Abstract"
    
We present a mathematical proof that perfect translation between languages is impossible, together with a precise measure of how much is lost and why. Drawing on the "Intelligence as Geometry" (RTSG) framework, we model each language as inducing a *conceptual topos*---a category with internal logic---whose subobject classifier determines the truth values available to speakers of that language. The Conceptual Irreversibility Theorem (CIT) establishes that the round-trip translation source $\to$ metalanguage $\to$ target is necessarily lossy because source and target topoi have incompatible subobject classifiers. The loss is not epistemic (Quine's indeterminacy) but *structural* (logical). We formalize the Sapir-Whorf hypothesis as a filter operator on the intelligence vector, showing how each language amplifies or attenuates specific cognitive types. The *overlap subspace* between two languages quantifies translation capacity: bilingual code-switching is recast as dynamic filter alternation to minimize total Heyting Gap, and untranslatability is precisely located as concepts outside the overlap subspace. We apply the framework to machine translation (proving that no MT system can achieve zero loss regardless of architecture), semantic distance via the nerve of the conceptual category, and bilingual cognition. The framework is compatible with both Chomskyan and usage-based approaches to grammar.

% ═══════════════════════════════════════════════════════════════════════════════

## Introduction: Translation as a Mathematical Problem

% ═══════════════════════════════════════════════════════════════════════════════

This paper presents a mathematical framework for translation loss, drawn from the Intelligence as Geometry (RTSG) program. The central result---the Conceptual Irreversibility Theorem---proves that perfect translation between any two natural languages is impossible, and provides a precise measure of the irreducible loss.

The impossibility of perfect translation has long been recognized informally. Jakobson's dictum that "languages differ essentially in what they *must* convey" [jakobson1959] identifies the phenomenon; Quine's thesis of indeterminacy of translation [quine1960] provides a philosophical argument; and every working translator knows that something is always lost. But none of these provides a *quantitative* framework: how much is lost? Why? And can the loss be minimized?

Our framework answers these questions by modeling languages as mathematical structures---specifically, as *topoi*---and proving that the structural mismatch between any two language-topoi produces irreducible translation loss. The loss is not a matter of vocabulary gaps (those are bridgeable with circumlocution) but of *logical structure*: different languages organize conceptual space according to different internal logics, and the round-trip between these logics is necessarily lossy.

The argument proceeds as follows. Section *ref:sec:CIT* develops the Conceptual Irreversibility Theorem and the Heyting Gap measure. Section *ref:sec:sapir-whorf* formalizes the Sapir-Whorf hypothesis as a filter operator. Section *ref:sec:overlap* develops the overlap subspace theory for bilingualism. Section *ref:sec:MT* applies the framework to machine translation. Section *ref:sec:nerve* uses the nerve of the conceptual category for semantic distance. Section *ref:sec:examples* provides worked examples.

% ═══════════════════════════════════════════════════════════════════════════════

## The Conceptual Irreversibility Theorem

% ═══════════════════════════════════════════════════════════════════════════════

### Conceptual Topoi

We begin by modeling the conceptual system associated with a language as a topos---a category-theoretic structure with an internal logic.

!!! definition "Conceptual Topos"
 \tB

The *conceptual topos* of a language $L$, denoted $\Cco^L$, is a category whose:
[nosep]
- **Objects** are concepts available to speakers of $L$;
- **Morphisms** are inferential relationships between concepts;
- **Subobject classifier** $\Omega_L$ determines the truth values available in $L$'s conceptual system.

The critical feature is the subobject classifier $\Omega_L$. In classical logic, $\Omega = \{0, 1\}$: every proposition is either true or false. In the conceptual topos, $\Omega_L$ is a *Heyting algebra*---it admits degrees of truth, vagueness, and context-dependence. The statement "this is art" does not have a classical truth value in any natural language; it has a *Heyting truth value* that depends on context, culture, and speaker.

!!! definition "Classical Category"
 \tA

The *classical category* $\Ccl$ is the category of formal, language-independent propositions with Boolean subobject classifier $\Omega_{\mathrm{Bool}} = \{0, 1\}$. This is the metalanguage: the space of explicit, unambiguous assertions.

Translation between languages $L_1$ and $L_2$ passes through the classical category:
\[
\Cco^{L_1} \xrightarrow{\;\alpha_{L_1}\;} \Ccl \xrightarrow{\;\iota_{L_2}\;} \Cco^{L_2}
\]
where $\alpha_{L_1}$ is *abstraction* (extracting the propositional content from $L_1$'s conceptual system) and $\iota_{L_2}$ is *instantiation* (embedding the propositional content into $L_2$'s conceptual system).

### The Main Theorem

!!! theorem "Conceptual Irreversibility Theorem"
 \tB

Neither round-trip is the identity:
\begin{keyeq}

\[\begin{aligned}
\iota_{L_1} \circ \alpha_{L_1} &\neq \Id_{\Cco^{L_1}}    
\alpha_{L_2} \circ \iota_{L_2} &\neq \Id_{\Ccl} 
\end{aligned}\]

\end{keyeq}
and no choice of functors $\alpha, \iota$ can make either round-trip an isomorphism, because the Heyting and Boolean subobject classifiers are structurally incompatible.

The proof rests on two lemmas:

!!! lemma "Abstraction Does Not Preserve $\Omega$"
 \tB

The abstraction functor $\alpha: \Cco \to \Ccl$ must map the Heyting algebra $\Omega_L$ to the Boolean algebra $\{0,1\}$. This mapping is necessarily lossy: for any Heyting element $h \notin \{0,1\}$, $\alpha$ must collapse it to either $0$ or $1$, destroying the intermediate truth value.

!!! lemma "Instantiation Collapses Truth Values"
 \tB

The instantiation functor $\iota: \Ccl \to \Cco$ embeds Boolean truth into a richer Heyting structure, but cannot reconstruct the original Heyting element: $\iota(\alpha(h)) \neq h$ whenever $h$ is genuinely Heyting (not Boolean).

\begin{keyeq}
**The CIT in one sentence:** Translation is lossy because you must pass through a Boolean bottleneck (explicit propositional content) to get between two Heyting systems (natural languages), and the round-trip through Boolean logic destroys the intermediate truth values that make each language's conceptual system distinctive.
\end{keyeq}

!!! remark "Remark"

The CIT is *not* Quine's indeterminacy of translation. Quine's argument is epistemic: we cannot *determine* the correct translation because multiple translations are compatible with all behavioral evidence. The CIT is *structural*: even if we had perfect knowledge of both languages, translation would still be lossy because the logical structures are incompatible. Quine says we *cannot know* the translation; the CIT says the translation *does not exist*.

### The Heyting Gap

!!! definition "Heyting Gap"
 \tB

The Heyting Gap between two language-topoi $\Cco^{L_1}$ and $\Cco^{L_2}$ is:
\begin{keyeq}
\[
\HGap(L_1, L_2) = 1 - \frac{|\Omega_{L_1} \cap \Omega_{L_2}|}{|\Omega_{L_1} \cup \Omega_{L_2}|}
\]
\end{keyeq}
where the intersection and union are over the shared and total truth-value structures. $\HGap = 0$ implies identical conceptual logic (perfect translation possible); $\HGap = 1$ implies completely disjoint logics (no translation possible).

!!! theorem "Gap Monotonicity"
 \tB

The more you know, the harder it is to say what you know. Formally, the Heyting Gap grows with the richness of the source conceptual system:
\begin{keyeq}
\[
\frac{\partial \HGap}{\partial |\Omega_{L_1}|} > 0
\]
\end{keyeq}
A richer conceptual system has more intermediate truth values, more of which are lost in translation.

\begin{intuition}
A child's conceptual topos is relatively simple---few intermediate truth values, relatively Boolean. A child's thoughts translate well into explicit language. An expert's conceptual topos is rich with nuance, contextual shadings, and "it depends" qualifications. The expert's thoughts translate badly---not because the expert is inarticulate but because the Heyting Gap between their internal conceptual logic and any natural language's expressive capacity has grown with expertise. This is the formal content of the "curse of knowledge."
\end{intuition}

% ═══════════════════════════════════════════════════════════════════════════════

## Sapir-Whorf Formalized: Language as Cognitive Filter

% ═══════════════════════════════════════════════════════════════════════════════

The RTSG framework models each language as inducing a *linguistic filter* on the variable-dimensional intelligence vector (n=12 for humans).

!!! definition "Linguistic Filter"
 \tB

The linguistic filter $\Fling^L: \\mathbb{R}^{n(e)} \to \\mathbb{R}^{n(e)}$ associated with language $L$ modulates the intelligence vector:
\begin{keyeq}
\[
\bI_{\mathrm{eff}}^L = \Fling^L \cdot \bI_{\mathrm{raw}}
\]
\end{keyeq}
Languages that lexically distinguish a concept amplify the corresponding intelligence component; languages that lack the distinction attenuate it.

\begin{intuition}
Jakobson's dictum formalized: "languages differ in what they *must* convey" means languages differ in which components of $\Fling$ are non-identity. If a language forces speakers to mark evidentiality in every sentence (Turkish, Quechua), then $\Fling^{\mathrm{eval}}$ is amplified---the language continually exercises evaluative processing. If a language has no obligatory tense marking (Mandarin), then $\Fling^{\mathrm{mnem}}$ for temporal indexing is attenuated relative to English.
\end{intuition}

Empirical evidence for language-specific filter effects:

\begin{center}
\small

*[Table — see PDF for formatted version]*

\end{center}

!!! remark "Remark"

Untranslatability is not binary but graded. *Schadenfreude* was once untranslatable in English (high $\HGap$) but has been borrowed, expanding the English conceptual topos to include it (reducing $\HGap$ toward zero). Language change is, in part, the expansion of overlap subspaces through lexical borrowing, calque, and conceptual contact.

% ═══════════════════════════════════════════════════════════════════════════════

## Machine Translation and the CIT

% ═══════════════════════════════════════════════════════════════════════════════

!!! proposition "MT Loss Bound"
 \tB

Any machine translation system $M$ from $L_1$ to $L_2$ operates with a composed filter:
\[
M = F_{\mathrm{arch}} \circ F_{\mathrm{data}} \circ F_{\mathrm{objective}}
\]
where $F_{\mathrm{arch}}$ is the architectural filter (transformer, RNN, etc.), $F_{\mathrm{data}}$ is the training data filter, and $F_{\mathrm{objective}}$ is the loss function filter. The MT system's "conceptual topos" is shaped by these filters. By the CIT:
\begin{keyeq}
\[
\HGap(M(L_1 \to L_2)) \geq \HGap(L_1, L_2) > 0
\]
\end{keyeq}
No MT system can achieve zero loss regardless of architecture, because the loss is structural (incompatible subobject classifiers), not computational.

\begin{intuition}
The CIT explains why MT systems fail on poetry, humor, and culturally embedded expressions---not because the systems are insufficiently powerful, but because these are precisely the domains where the Heyting Gap is largest. Poetry *exploits* the richness of a language's Heyting algebra; translation must compress this to a Boolean bottleneck and re-expand in the target's Heyting algebra. The loss is mathematically inevitable.
\end{intuition}

However, MT can *minimize* loss by maximizing the effective overlap subspace. More parallel training data expands the shared topos section; better architectures reduce the architectural filter's distortion; and domain-specific models can narrow the conceptual space to a region where the Heyting Gap is smaller.

\begin{prediction}
MT quality (measured by human evaluation, not BLEU) should correlate inversely with the Heyting Gap between source and target languages. Specifically: MT between typologically similar languages with large overlap subspaces (Spanish$\leftrightarrow$Portuguese, Czech$\leftrightarrow$Slovak) should have systematically higher quality than between typologically distant languages (Japanese$\leftrightarrow$Finnish), even controlling for training data volume.
\end{prediction}

% ═══════════════════════════════════════════════════════════════════════════════

## Semantic Distance via the Nerve

% ═══════════════════════════════════════════════════════════════════════════════

!!! definition "Nerve of the Conceptual Category"
 \tB

The nerve $N(\Cco^L)$ is a simplicial complex constructed from the conceptual topos:
[nosep]
- 0-simplices (vertices) = concepts
- 1-simplices (edges) = direct inferential relations between concepts
- $k$-simplices = chains of $k$ composable morphisms

The simplicial distance $d_N(c_1, c_2)$ between two concepts is the shortest path length in $N(\Cco^L)$.

This provides a formal framework for several phenomena:

**Cognates.** Two words in different languages are cognates when the corresponding concepts have small nerve distance across language-specific topoi: $d_N(c^{L_1}, c^{L_2}) < \epsilon$.

**False friends.** Two words with small *surface* distance (phonological similarity) but large *nerve* distance (semantic dissimilarity). French *actuellement* (currently) and English *actually* have near-zero phonological distance but nerve distance $>0$: the conceptual neighborhoods are different.

**Semantic shift.** Diachronic change in word meaning corresponds to drift of concepts through the nerve: a concept $c(t)$ follows a trajectory through $N(\Cco^L)$ over historical time. English *nice* has drifted from "foolish" (13th century) through "delicate" (16th century) to "pleasant" (18th century)---a trajectory through distant regions of the nerve.

% ═══════════════════════════════════════════════════════════════════════════════

## Worked Examples

% ═══════════════════════════════════════════════════════════════════════════════

!!! example "Russian Color Discrimination"

Russian has two basic-level blue terms: *goluboy* (light blue) and *siniy* (dark blue). English has one: *blue*. The Russian linguistic filter:
\[
\Fling^{\mathrm{Russian}}: I_{\mathrm{spat}} \mapsto I_{\mathrm{spat}} + \delta_{\mathrm{blue}}
\]
amplifies spatial-perceptual discrimination in the blue region of color space. Winawer et al. [winawer2007] confirmed that Russian speakers discriminate blue shades faster when the distinction crosses the *goluboy*/*siniy* boundary---a measurable filter effect on $I_{\mathrm{spat}}$.

The Heyting Gap for blue concepts between Russian and English is nonzero: the truth value of "this is blue" in Russian is not Boolean (it is *goluboy*-blue or *siniy*-blue, with boundary cases having intermediate truth values), while in English it is closer to Boolean (blue or not-blue, with fewer intermediate values for light/dark distinction).

!!! example "Pirah\ {a} and Exact Quantity"

The Pirah\ {a} language lacks number words beyond "few" and "many" [everett2005]. The Pirah\ {a} linguistic filter:
\[
\Fling^{\mathrm{Pirah\tilde{a}}}: I_{\mathrm{symb}} \mapsto 0 \text{ (for exact quantity)}
\]
completely attenuates the symbolic component relevant to exact numerical reasoning. Concepts like "exactly seven" are outside the Pirah\ {a} conceptual topos---they are untranslatable in the strict sense of Definition *ref:def:untranslatable*.

This is not a cognitive deficit: Pirah\ {a} speakers possess the neural substrate for numerical reasoning (the $I_{\mathrm{symb}}$ component exists in $\bI_{\mathrm{raw}}$), but their linguistic filter does not develop it. Children raised bilingually in Pirah\ {a} and Portuguese acquire exact number concepts through the Portuguese filter.

!!! example "Mandarin Temporal Metaphor"

Mandarin speakers more frequently use vertical spatial metaphors for time (earlier events are "up," later events are "down"), while English speakers use horizontal metaphors (earlier is "back," later is "ahead") [boroditsky2001]. The linguistic filter:
\[
\Fling^{\mathrm{Mandarin}}: I_{\mathrm{mnem}} \mapsto I_{\mathrm{mnem}} \otimes V_{\mathrm{vertical}}
\]
couples mnemonic temporal indexing with vertical spatial representations. The Heyting Gap for temporal concepts between Mandarin and English is nonzero: the truth value of "June comes *before* July" has different spatial connotations in each language, which are lost in translation to the other.

% ═══════════════════════════════════════════════════════════════════════════════

## Connections to Existing Theory

% ═══════════════════════════════════════════════════════════════════════════════

**Jakobson [jakobson1959**.] "Languages differ not in what they *can* express but in what they *must* express." In our framework: languages differ in which components of $\Fling$ are non-identity. Obligatory grammatical categories (tense, evidentiality, number, gender) are the non-identity components of the linguistic filter.

**Quine [quine1960**.] Indeterminacy of translation is an epistemic thesis; the CIT is a structural thesis. They are compatible but distinct: Quine says translation is underdetermined by evidence; the CIT says it is underdetermined by logic.

**Lakoff [lakoff1987**.] Cognitive linguistics claims that conceptual structure is grounded in embodied experience. In our framework, embodied experience shapes $\Fdev$ and $\Fcult$, which in turn shape the conceptual topos. Lakoff's conceptual metaphors are morphisms in the conceptual category.

**Fauconnier & Turner [fauconnier2002**.] Conceptual blending creates new concepts by composing morphisms from different regions of the nerve $N(\Cco)$. A blended concept is a new object in $\Cco$ with morphisms to the input spaces.

**G\"ardenfors.** Conceptual spaces with convexity constraints on concepts correspond to specific sheaf conditions in the topos---convexity is a local-to-global property that the sheaf condition formalizes.

**Eco [eco2003**.] Eco's view of translation as "negotiation" corresponds to finding the overlap subspace concept $c' \in \Toverlap$ that minimizes the Heyting Gap with the source concept $c$, accepting that $\HGap(c, c') > 0$.

% ═══════════════════════════════════════════════════════════════════════════════

## Limitations and Future Directions

% ═══════════════════════════════════════════════════════════════════════════════

**Topos construction.** The conceptual topos is defined abstractly; constructing it concretely for a specific language requires a comprehensive conceptual inventory that does not yet exist. The framework provides the *structure* for analysis, not the completed analysis.

**Heyting Gap measurement.** The quantitative Heyting Gap estimates (e.g., $\sim 0.7$ for *saudade*) are illustrative, not empirically calibrated. Developing operational measures of the Heyting Gap is an open research program---potentially via reaction-time experiments that measure the "cost" of cross-linguistic concept activation.

**Compositionality.** The framework models concepts holistically; the compositional structure of sentences (how word meanings combine) is not yet formalized within the topos. Extending the framework to compositional semantics is a natural next step.

**Sign languages.** The framework is developed for spoken/written languages but should extend to sign languages, where $\Fling$ operates through visual-spatial rather than auditory-phonological channels. The $\bK$ matrix predicts that sign languages should amplify $I_{\mathrm{spat}}$ and $I_{\mathrm{kin}}$ relative to spoken languages.

% ═══════════════════════════════════════════════════════════════════════════════

## Three-Space Linguistics

The three-space ontology (Part XIII) provides the deepest grounding for translation theory and the Sapir-Whorf hypothesis.

**Language as $\CSp$-navigation structure.**  A language is a system of symbols that enables efficient navigation of the CS operator $\CSp$.  Each language carves $\CSp$ into accessible regions via its vocabulary, grammar, and conceptual structure.  The Sapir-Whorf hypothesis, formalized through the cultural filter $F_{\mathrm{cult}}$, states that different languages provide different navigation structures---different ways of moving through $\CSp$---and therefore access different subsets of $\QS$-potentiality for instantiation.

**Translation loss as inter-instantiation gap.**  The CIT (Conceptual Irreversibility Theorem) applied to translation is an inter-instantiation gap: two languages instantiate overlapping but non-identical subsets of $\QS$, and translation must bridge the non-overlapping regions.  The Heyting gap between source and target languages is the volume of $\QS$-structure that the source language instantiates but the target language cannot reach through its own navigation structure.

**Bilingualism as expanded instantiation.**  A bilingual individual has access to two $\CSp$-navigation structures, and their combined instantiation capacity exceeds that of either monolingual speaker.  The bilingual advantage is not merely "two vocabularies" but access to $\QS$-regions that are navigable from one language's conceptual structure but not the other's.  Code-switching is the dynamic optimization of which navigation structure to deploy for a given instantiation task.

**Untranslatability as $\QS$-disjointness.**  Truly untranslatable concepts (*saudade*, *Schadenfreude*, *wabi-sabi*) correspond to $\QS$-regions that are navigable from one language's $\CSp$-structure but lie entirely outside another's.  These are not failures of effort but structural impossibilities: the target language's filter chain does not open the projection channel needed to instantiate that particular $\QS$-configuration.

**$p$-Adic semantics.**  The three-space ontology suggests that semantic memory is organized in $p$-adic (ultrametric) topology.  Lexical items within a language form a $\Qp$-tree where distance is semantic relatedness.  Translation between languages is a map between two different $\Qp$-trees, and the CIT guarantees this map is lossy whenever the trees have different branching structures---which they always do.

## Conclusion

% ═══════════════════════════════════════════════════════════════════════════════

We have presented a mathematical proof that perfect translation is impossible, together with a precise measure of the loss (the Heyting Gap) and a formal account of why it occurs (incompatible subobject classifiers in language-specific conceptual topoi). The framework formalizes the Sapir-Whorf hypothesis as a filter operator, provides a mathematical foundation for bilingual code-switching, explains untranslatability as absence from the overlap subspace, and proves that machine translation cannot achieve zero loss regardless of architecture. The loss is structural, not computational---a theorem of logic, not a limitation of engineering.

*This paper is a companion extraction from "Intelligence as Geometry" (Niko, 2026). The full treatment of the Conceptual Irreversibility Theorem, including all proofs and corollaries, is available in Part V of the parent document.*

% ═══════════════════════════════════════════════════════════════════════════════

## References

*See PDF for full bibliography.*
---

## v2 Integration: Language as Mind, Expressive Modalities, Style (TMP-20260217)

**Language as RTSG graph:** A living language L = RTSG graph G(L). Translation = lossy projection G(L₁) → G(L₂) with information loss at every cross-dimensional edge lacking an L₂ equivalent.

**Extended definition:** Any expressive modality is a language — music, visual art, mathematics, movement, code, cooking. Each projects the personal RTSG graph into a different dimensional substrate.

Personal language:
$$L(\xi) = f(G(\xi)_{\text{own}},\; G(\xi)_{\text{absorbed}})$$

**Style = G(ξ)_own** — the irreducible personal RTSG subgraph after factoring out absorbed influences. Style is what remains when all external influences are subtracted.

**Basic English Complexity Ratio (Niko hypothesis):**
$$\text{complexity}(D) = \frac{\text{len}(D_{\text{basic}})}{\text{len}(D_{\text{original}})}$$
Approximates Kolmogorov minimum description length; correlates with IdeaRank depth.
