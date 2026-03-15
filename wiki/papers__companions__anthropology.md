---
title: "Anthropology Companion Paper"
version: "2.0.0"
last_updated: "2026-03-05"
status: ARXIV-READY
arxiv_category: "physics.soc-ph"
---

# Anthropology Companion Paper

**Jean-Paul Niko** · February 2026

% ═══════════════════════════════════════════════════════════════════════════════

% ═══ Three-Space Notation ═══
\newcommand{\QS}{\mathcal{Q}}
\newcommand{\PS}{\mathcal{P}}
\newcommand{\CSp}{\mathcal{C}_S}
\newcommand{\Inst}{\mathfrak{I}}
\newcommand{\Qp}{\mathbb{Q}_p}

\title{\textcolor{sectionblue}{**Intelligence Filters and Cultural Cognition:  [0.3em]
A Mathematical Framework for Enculturation, Translation,  
and Cognitive Diversity**}}

\author{Jean-Paul Niko  
  
\small `triptomean.com`}

\date{February 2026}

!!! abstract "Abstract"
    
We present a mathematical framework for cultural cognition grounded in the Intelligence as Geometry (RTSG) theory.  Every cognitive agent carries an *intelligence vector* $\bI \in \\mathbb{R}^{n(e)}_{\geq 0}$ measuring capacity across eight cognitive types.  *Cultural filters* $\Phi_{\mathrm{cult}} \in [0,1]^8$ model enculturation as diagonal contractions that selectively develop certain cognitive types while attenuating others, depending on the ecological and social demands of the cultural environment.  We prove a *Conceptual Irreversibility Theorem* (CIT) showing that filter effects cannot be fully undone, formalizing the structural observation bias inherent in cross-cultural understanding: the anthropologist's comprehension is always $\Phi_A \circ \Phi_B(\bI_{\mathrm{raw}})$, which is provably distinct from the native's $\Phi_B(\bI_{\mathrm{raw}})$.  L\'evi-Strauss's structural anthropology is reinterpreted as the claim that cultures have underlying *compatibility matrices* $\bK$ whose eigenvectors correspond to binary oppositions.  We use the framework to formalize indigenous knowledge systems as alternative filter configurations that may achieve higher intelligence in specific types than Western-filtered cognition, and argue mathematically for the preservation of cultural-cognitive diversity as a species-level adaptive strategy.  The framework replaces the qualitative opposition between universalism and relativism with a precise mathematical structure: universal type space, culturally variable filters.
The three-space ontology grounds these results in the instantiation process: culture is shared instantiation norms, indigenous knowledge is alternative convergence conditions, and the WEIRD problem is projection bias in $\QS \to \PS$ mapping.

**Keywords:** enculturation, cultural cognition, intelligence filters, cross-cultural translation, structural anthropology, cognitive diversity, WEIRD bias

---

% ═══════════════════════════════════════════════════════════════════════════════

## Introduction

% ═══════════════════════════════════════════════════════════════════════════════

Anthropology has long grappled with a fundamental tension: the desire to understand other cultures on their own terms versus the impossibility of fully escaping one's own cultural lens.  Geertz's [Geertz1973] "thick description" aims at interpretive fidelity, but the question of *how much* fidelity is achievable---and what structural limits exist on cross-cultural comprehension---has remained qualitative.  Similarly, the debate between universalism and cultural relativism has been conducted largely in philosophical terms, without a mathematical framework that could clarify what is universal, what is culturally variable, and how the two are related.

This paper introduces such a framework, drawn from the Intelligence as Geometry (RTSG) theory [Niko2026].  The central idea is to separate *cognitive architecture*---the universal type space in which intelligence is defined---from *cognitive development*---the culturally specific process by which raw capacity is shaped into effective competence.  Architecture is universal; development is cultural.  The mathematical object that connects them is the *filter*: a diagonal operator that models how each culture selectively amplifies and attenuates components of the intelligence vector.

This separation resolves the universalism--relativism debate by precision.  Universalism is correct about the type space: all humans (indeed, all sufficiently complex cognitive agents) operate in the same eight-dimensional space of cognitive types.  Relativism is correct about the filters: different cultures develop profoundly different regions of this space, and there is no neutral standpoint from which to compare them.  The framework makes both claims simultaneously without contradiction, because they concern different mathematical objects.

% ═══════════════════════════════════════════════════════════════════════════════

## The Intelligence Vector and Type Space

% ═══════════════════════════════════════════════════════════════════════════════

!!! definition "Intelligence Vector"
 \tA{}
An agent's cognitive profile is a vector $\bI = (I_L, I_G, I_S, I_A, I_K, I_N, I_E, I_{\mathrm{Mu}}) \in \\mathbb{R}^{n(e)}_{\geq 0}$, where the components measure capacity in Linguistic ($L$), Symbolic ($G$), Spatial ($S$), Kinesthetic ($A$), Auditory ($K$), Social ($N$), Intrapersonal ($E$), and Naturalistic ($\mathrm{Mu}$) types.

The type space $T = \{L, G, S, A, K, N, E, \mathrm{Mu}\}$ is proposed as *universal*: it characterizes the cognitive architecture available to all humans, regardless of cultural background.  This is a strong empirical claim that draws on converging evidence from neuroanatomy, developmental psychology, and comparative cognition.  The eight types correspond to identifiable neural circuit complexes that are present across all known human populations, though their relative development varies enormously.

!!! remark "Remark"

The type space may ultimately need to be extended to accommodate cognitive modalities that are not well-captured by the current variable dimensions (12 for humans)---for example, chemosensory intelligence in cultures with highly developed olfactory classification systems, or proprioceptive specialization in cultures with extreme physical practices.  The framework is agnostic about the exact number of types; what matters is that the space is finite, universal, and fixed at the architectural level.

% ═══════════════════════════════════════════════════════════════════════════════

## Cultural Filters: Enculturation Formalized

% ═══════════════════════════════════════════════════════════════════════════════

!!! definition "Cultural Filter"
 \tA{}
A cultural filter is a diagonal operator $\Phi_{\mathrm{cult}} = \operatorname{diag}(\phi_1, \ldots, \phi_8)$ with $\phi_t \in [0,1]$ for each type $t$.  Applied to a raw intelligence vector:
\begin{keyeq}
\[
\bI_{\mathrm{effective}} = \Phi_{\mathrm{cult}}(\bI_{\mathrm{raw}})
\]
\end{keyeq}
Each entry $\phi_t$ encodes the degree to which culture $C$ develops, reinforces, and rewards cognitive type $t$.

Enculturation, in this framework, is the progressive application of the cultural filter over the developmental period.  An infant begins with $\bI_{\mathrm{raw}}$; by adulthood, their effective intelligence is $\bI_{\mathrm{eff}} = \Phi_{\mathrm{cult}}(\bI_{\mathrm{raw}})$.  The filter is not imposed in a single moment but accumulated through thousands of interactions, practices, rewards, and sanctions that together shape which cognitive types flourish and which atrophy.

### Filter profiles of different cultural systems

Different cultural-ecological niches produce characteristically different filter profiles:

!!! example "Oral Cultures"
 \tB{}
Cultures without writing systems develop filters that emphasize mnemonic, auditory, and social types:
\[
\Phi_{\mathrm{oral}} \approx \operatorname{diag}(0.7, 0.3, 0.6, 0.6, 0.9, 0.8, 0.6, 0.7)
\]
The high auditory component ($\phi_K = 0.9$) reflects the centrality of oral performance; the high social component ($\phi_N = 0.8$) reflects the communal nature of knowledge transmission.  The symbolic component ($\phi_G = 0.3$) is low not because abstract reasoning is absent but because it is expressed through oral genres (riddles, genealogies, navigational chants) rather than written notation.

!!! example "Literate-Scientific Cultures"
 \tB{}
Post-Enlightenment Western cultures develop filters that emphasize symbolic and linguistic types:
\[
\Phi_{\mathrm{Western}} \approx \operatorname{diag}(0.9, 0.9, 0.6, 0.3, 0.5, 0.5, 0.6, 0.3)
\]
The dominance of $\phi_L$ and $\phi_G$ reflects the centrality of text and formal reasoning in educational and credentialing institutions.  The low kinesthetic ($\phi_A = 0.3$) and naturalistic ($\phi_{\mathrm{Mu}} = 0.3$) components reflect the de-emphasis of embodied and ecological knowledge in formal education [Ingold2000].

!!! example "Maritime-Navigational Cultures"
 \tB{}
Polynesian and Micronesian maritime cultures develop distinctive profiles:
\[
\Phi_{\mathrm{maritime}} \approx \operatorname{diag}(0.5, 0.3, 0.95, 0.8, 0.5, 0.6, 0.6, 0.7)
\]
The exceptional spatial component ($\phi_S = 0.95$) reflects navigational expertise documented by Hutchins [Hutchins1995] and others.  This is not a simpler version of Western navigation---it is a different and, in its domain, *superior* filter configuration that produces higher $I_S$ than Western-filtered cognition achieves.

\begin{intuition}
The crucial point: these are not "more" or "less" intelligent cultures.  They are different *filter configurations* optimized for different ecological and social demands.  "Intelligence" measured by any single filter's standards is culturally biased *by construction*, because the measuring instrument is itself a filter product.  The RTSG framework makes this bias mathematically explicit rather than leaving it as a qualitative objection.
\end{intuition}

% ═══════════════════════════════════════════════════════════════════════════════

## Conceptual Irreversibility and Fieldwork Epistemology

% ═══════════════════════════════════════════════════════════════════════════════

The most consequential theorem for anthropological methodology is the Conceptual Irreversibility Theorem (CIT), which establishes structural limits on cross-cultural understanding.

!!! theorem "Kernel Lemma"
 \tA{}
For composed filters, $\ker(\Phi_2 \circ \Phi_1) \supseteq \ker(\Phi_1)$.  Filters can only further attenuate; they cannot restore what earlier filters have suppressed.

!!! theorem "Conceptual Irreversibility Theorem (CIT)"
 \tA{}
For any non-trivial filter $\Phi$, there exists no inverse filter $\Phi^{-1}$ such that $\Phi^{-1} \circ \Phi = \Id$.  Filter effects are structurally irreversible.

### The anthropologist's structural bias

Consider an anthropologist raised in culture $A$ studying culture $B$.  "Going native"---immersing oneself in culture $B$'s practices and categories---amounts to applying $\Phi_B$ on top of the already-applied $\Phi_A$.  The anthropologist's understanding is:
\begin{keyeq}
\[
\bI_{\mathrm{anthro}} = \Phi_B \circ \Phi_A (\bI_{\mathrm{raw}}) \neq \Phi_B(\bI_{\mathrm{raw}}) = \bI_{\mathrm{native}}
\]
\end{keyeq}

!!! proposition "Structural Observation Bias"
 \tA{}
The anthropologist's understanding of culture $B$ is *provably* different from a native's understanding, regardless of the anthropologist's skill, empathy, or length of immersion.  The difference arises because $\Phi_A$ has already attenuated certain cognitive types that $\Phi_B$ would have developed, and this attenuation is irreversible (CIT).

This is not a counsel of despair.  The proposition does not say that cross-cultural understanding is impossible---only that it is *structurally incomplete* in a way that can be precisely characterized.  The dimensions along which the anthropologist's understanding diverges from the native's are exactly the types where $\phi^A_t \ll 1$: the types that the anthropologist's home culture has suppressed.

### Thick description and the Heyting Gap

The RTSG framework provides a formal interpretation of Geertz's "thick description."  In the full theory, each culture's conceptual system forms a *Heyting algebra*---a logical structure with more truth values than the classical Boolean $\{\text{true}, \text{false}\}$.  The *Heyting Gap* $\Hgap = |\Omega_{\mathrm{co}}| - 2$ measures how many "intermediate" truth values exist in a conceptual system.

!!! definition "Heyting Gap"
 \tB{}
The Heyting Gap $\Hgap$ of a conceptual system measures the number of truth values beyond the Boolean pair $\{\top, \bot\}$.  Different cultures may have different $\Hgap$ values for different conceptual domains.

!!! proposition "Thick Description as Gap Minimization"
 \tB{}
Geertz's "thick description" is the attempt to minimize the Heyting Gap when translating between cultural conceptual systems.  The CIT proves that this Gap is always strictly positive: $\Hgap > 0$ for any non-trivial cross-cultural translation.

The irreducible Heyting Gap is the mathematical formalization of what anthropologists have experienced as the persistent "remainder" in translation---the aspects of cultural meaning that resist expression in the observer's categories no matter how sensitive the observer is.  This remainder is not a failure of methodology but a structural feature of cross-system translation, as fundamental as the impossibility of lossless compression in information theory.

% ═══════════════════════════════════════════════════════════════════════════════

## L\'evi-Strauss Formalized

% ═══════════════════════════════════════════════════════════════════════════════

L\'evi-Strauss's [LeviStrauss1962] structural anthropology---the claim that beneath the surface diversity of cultural phenomena lie universal structures of the human mind---receives a precise mathematical interpretation in the RTSG framework.

!!! proposition "Structural Anthropology as $\bK$-Theory"
 \tB{}
L\'evi-Strauss's claim that cultures share deep structural similarities is the claim that different cultures have $\bK$ matrices with shared spectral properties (eigenvalue distributions).  Surface diversity corresponds to different filter configurations $\Phi_{\mathrm{cult}}$; structural universality corresponds to the shared architecture of $\bK$.

### Binary oppositions as eigenvectors

L\'evi-Strauss's ubiquitous binary oppositions---nature/culture, raw/cooked, male/female---correspond to eigenvectors of $\bK$ with specific symmetry properties.  An eigenvector $\mathbf{v}$ of $\bK$ satisfying $\bK \mathbf{v} = \lambda \mathbf{v}$ defines a direction in the type space along which cross-type interaction is maximally coherent.  Binary oppositions arise when two eigenvectors with opposite signs partition the type space into complementary halves.

!!! example "The Raw and the Cooked"
 \tB{}
L\'evi-Strauss's [LeviStrauss1964] (1964) analysis of the raw/cooked opposition translates to a specific filter transformation $\Phi_{\mathrm{cult}}$ applied to the sensory-evaluative types.  "Cooking" is the cultural filter that transforms raw sensory experience (high $I_{\mathrm{Mu}}$, naturalistic engagement with food) into culturally coded evaluative categories (high $I_E$, internalized standards of taste, preparation, and propriety).  The opposition is between the unfiltered and the filtered states of the same cognitive material.

### Universality of $\bK$ versus variability of $\Phi$

The framework resolves a long-standing puzzle in structural anthropology: why do the *same* structural patterns recur across cultures that have had no historical contact?  The answer is that $\bK$---the compatibility structure between cognitive types---is grounded in neural architecture and is therefore species-universal.  The eigenvectors of $\bK$ define the natural "axes of opposition" that all cultures must navigate.  What varies is which eigenvectors each culture emphasizes, how they are labeled, and which filter configurations they produce.

This explains why binary oppositions are cross-culturally recurrent (they are eigenvectors of a shared $\bK$) while their specific content varies (different cultures apply different filters to the same underlying structure).

% ═══════════════════════════════════════════════════════════════════════════════

## Indigenous Knowledge Systems

% ═══════════════════════════════════════════════════════════════════════════════

The filter framework provides a non-hierarchical formalization of indigenous knowledge systems [Turnbull2000] that avoids both romanticization and dismissal.

!!! proposition "Filter Superiority in Specific Types"
 \tB{}
A culture with filter $\Phi_A$ may achieve strictly higher effective intelligence than culture $B$ in specific types: $\phi^A_t > \phi^B_t$ for some $t$, even if $\phi^A_s < \phi^B_s$ for other $s$.  There is no culture whose filter is uniformly superior across all types.

!!! example "Polynesian Navigation"
 \tB{}
Polynesian navigators achieve extraordinary spatial intelligence ($I_S$) through training regimes that Western education does not replicate.  Hutchins [Hutchins1995] documents navigational cognition that integrates wave patterns, star maps, wind direction, and body sense into a distributed cognitive system achieving spatial performance that exceeds Western-trained navigators in open-ocean conditions without instruments.  In RTSG terms: $\phi^{\mathrm{Polynesian}}_S > \phi^{\mathrm{Western}}_S$.

!!! example "Aboriginal Songlines"
 \tB{}
Australian Aboriginal songlines integrate auditory, spatial, and mnemonic types ($I_K + I_S + I_E$) into a navigational-ceremonial system that encodes geographic, ecological, and cosmological knowledge in musical form.  The effective intelligence in the auditory-spatial-mnemonic subspace exceeds what literate cultures typically develop, precisely because the cultural filter allocates more developmental resources to these types.

!!! example "Amazonian Ethnobotany"
 \tB{}
Ethnobotanical knowledge systems among Amazonian peoples achieve naturalistic intelligence ($I_{\mathrm{Mu}}$) that Western pharmacology has only recently begun to appreciate.  The identification, classification, and combinatorial use of thousands of plant species represents a filter configuration that produces $\phi^{\mathrm{Amazonian}}_{\mathrm{Mu}} \gg \phi^{\mathrm{Western}}_{\mathrm{Mu}}$.

These are not claims about "noble savages" or romantic primitivism.  They are precise mathematical statements: different filter configurations develop different regions of the intelligence type space to different degrees.  Western-filtered cognition excels in symbolic and linguistic types; other cultural systems excel in spatial, kinesthetic, auditory, or naturalistic types.  Neither is "more intelligent" than the other---they are intelligent *differently*, in ways that reflect the adaptive demands of their respective environments.

% ═══════════════════════════════════════════════════════════════════════════════

## The WEIRD Problem Formalized

% ═══════════════════════════════════════════════════════════════════════════════

Henrich, Heine, and Norenzayan [Henrich2010] demonstrated that the behavioral science literature is overwhelmingly based on WEIRD (Western, Educated, Industrialized, Rich, Democratic) populations, raising questions about the generalizability of its findings.  The RTSG framework provides a mathematical formalization of this concern.

!!! definition "WEIRD Filter"
 \tB{}
The WEIRD filter is a specific $\Phi_{\mathrm{WEIRD}}$ that emphasizes linguistic and symbolic types:
\[
\Phi_{\mathrm{WEIRD}} \approx \operatorname{diag}(0.9, 0.9, 0.5, 0.3, 0.4, 0.5, 0.6, 0.2)
\]
The research instruments developed within WEIRD cultures are calibrated to this filter: they measure $\bI_{\mathrm{eff}} = \Phi_{\mathrm{WEIRD}}(\bI_{\mathrm{raw}})$ and mistakenly interpret the result as $\bI_{\mathrm{raw}}$.

!!! proposition "Test Bias as Filter Mismatch"
 \tA{}
A cognitive test designed under filter $\Phi_A$ measures $\Phi_A(\bI_{\mathrm{raw}})$, not $\bI_{\mathrm{raw}}$.  When administered to a population developed under filter $\Phi_B$, the test measures neither $\bI_{\mathrm{raw}}$ nor $\Phi_B(\bI_{\mathrm{raw}})$ but the doubly-filtered $\Phi_A \circ \Phi_B(\bI_{\mathrm{raw}})$, which underestimates actual capacity in types where $\Phi_A$ and $\Phi_B$ attenuate different components.

This formalizes what cross-cultural psychologists have argued qualitatively: IQ tests are not culture-neutral instruments but products of specific filter configurations.  Their results are informative about $\Phi(\bI)$, not about $\bI$ alone.  The framework does not reject psychometric measurement---it contextualizes it by making the filter explicit.

% ═══════════════════════════════════════════════════════════════════════════════

## Cognitive Diversity as Species-Level Strategy

% ═══════════════════════════════════════════════════════════════════════════════

The RTSG framework provides a mathematical argument for the preservation of cultural-cognitive diversity that goes beyond ethical or aesthetic considerations to show that diversity has quantifiable adaptive value at the species level.

!!! definition "Species-Level Synergy"
 \tB{}
The *species-level synergy* is the bundle synergy of the entire human population considered as a cognitive bundle:
\[
\Syn_{\mathrm{species}} = \Syn(\{\bI_{\mathrm{eff},1}, \ldots, \bI_{\mathrm{eff},N}\})
\]
This measures the total cognitive capacity of the species, including all cross-type interactions.

!!! proposition "Diversity--Synergy Theorem for Species"
 \tB{}
Species-level synergy is maximized when the population exhibits high filter diversity across cultures.  Cultural homogenization (convergence of all $\Phi_{\mathrm{cult}}$ toward a single profile) reduces $\Syn_{\mathrm{species}}$ because it eliminates the cross-type interactions that arise from complementary specializations.

\begin{intuition}
This is the cognitive analog of genetic diversity in evolutionary biology.  Just as a species with low genetic diversity is vulnerable to environmental change because it lacks the variation needed for adaptive response, a species with low cognitive-filter diversity is vulnerable to novel challenges because it lacks the cognitive variation needed for creative response.  Monoculture---the global homogenization of cultural filters toward a single (WEIRD) profile---is the cognitive equivalent of a population bottleneck.
\end{intuition}

!!! proposition "Portfolio Argument for Cultural Preservation"
 \tB{}
Each distinct cultural filter $\Phi_i$ represents an investment in a specific region of the intelligence type space.  The optimal species-level "portfolio" diversifies across filter configurations to minimize the risk that any particular environmental challenge finds the species cognitively unprepared.  Losing a cultural tradition is analogous to losing a genetic lineage: it may be irreversible (CIT) and eliminates optionality.

This argument is distinct from the ethical case for cultural preservation (which concerns rights and dignity) and the aesthetic case (which concerns the intrinsic value of cultural diversity).  It is a structural-mathematical argument: filter diversity is a resource, filter homogenization is a risk, and filter loss is irreversible.

% ═══════════════════════════════════════════════════════════════════════════════

## Cross-Cultural Translation: Limits and Strategies

% ═══════════════════════════════════════════════════════════════════════════════

The CIT establishes that perfect cross-cultural translation is impossible, but the framework also provides strategies for maximizing translation fidelity within structural limits.

!!! definition "Translation Loss"
 \tB{}
The *translation loss* from culture $A$ to culture $B$ for a concept $c$ is:
\[
\mathcal{L}(c; A \to B) = \|c_A - \Phi_B \circ \Phi_A^{-1}(c_A)\|
\]
Since $\Phi_A^{-1}$ does not exist (CIT), translation must proceed through the overlap subspace---the set of types where both cultures retain non-trivial capacity.

!!! proposition "Translation through Overlap"
 \tB{}
Cross-cultural translation is most faithful when it proceeds through the *overlap subspace* $T_{\mathrm{overlap}}(A,B) = \{t : \phi^A_t > \epsilon \text{ and } \phi^B_t > \epsilon\}$.  Translation fidelity is bounded by the dimension of this overlap.

\begin{intuition}
This explains why certain cross-cultural translations are easier than others.  Music translates relatively well between cultures because the auditory type ($I_K$) tends to be moderately developed across many filter configurations---the overlap subspace includes $K$.  Legal concepts translate poorly between common-law and customary-law systems because the relevant evaluative and symbolic types are filtered through incompatible configurations with small overlap.
\end{intuition}

The framework also explains the distinctive value of *bilingual* or *bicultural* individuals: they carry two filter configurations simultaneously, providing a wider effective overlap subspace for translation.  The bicultural translator's comprehension is not $\Phi_A \circ \Phi_B(\bI)$ (sequential application) but something closer to $\max(\Phi_A, \Phi_B)$ applied component-wise (retaining the higher development from each culture), making them more effective translators than monocultural speakers of either language.

% ═══════════════════════════════════════════════════════════════════════════════

## Testable Predictions

% ═══════════════════════════════════════════════════════════════════════════════

[nosep]

- **Filter profile prediction.**  Different cultural-ecological niches produce predictably different filter profiles.  *Test*: administer comprehensive cognitive batteries to populations in diverse cultural settings, factor-analyze the results, and compare to predicted filter configurations.

- **Translation loss prediction.**  Cross-cultural translation fidelity correlates with overlap subspace dimension.  *Test*: measure cognitive profiles of bilingual translators, compute overlap, and predict translation quality ratings.

- **Structural bias prediction.**  Anthropological accounts of culture $B$ by observers from culture $A$ systematically underrepresent concepts that rely on types attenuated by $\Phi_A$.  *Test*: compare ethnographies of the same culture written by observers with different cultural backgrounds; the divergences should align with the predicted filter differences.

- **Knowledge loss prediction.**  When a cultural tradition is lost (language death, displacement), the intelligence types it uniquely developed should show declining population-level capacity.  *Test*: longitudinal study of communities undergoing rapid cultural change, measuring cognitive profiles before and after.

- **Diversity--innovation prediction.**  Societies with higher filter diversity (measured across coexisting subcultures) should show higher rates of creative problem-solving on novel challenges.  *Test*: compare innovation metrics across societies with varying degrees of internal cognitive diversity.

% ═══════════════════════════════════════════════════════════════════════════════

## Three-Space Anthropology

The three-space ontology (Part XIII) grounds cultural anthropology in the instantiation process.

**Culture as shared instantiation norms.**  A culture is a set of convergence conditions---$\QS$-structures whose instantiation is collectively agreed upon by a community.  Different cultures instantiate different subsets of $\QS$, producing genuinely different physical realities ($\PS$-configurations).  The cultural filter $F_{\mathrm{cult}}$ is not merely an attenuation of individual capacity but a *constraint on which instantiations are socially supported*.  Ethnographic fieldwork is the study of a community's instantiation norms.

**Thick description as fiber documentation.**  Geertz's "thick description" is the anthropologist's attempt to document the experiential fiber at a particular substrate state---not just what people *do* (the $\PS$-trace) but the space of possible interpretations (the $\CSp$-fiber) and which interpretations the culture selects (the community's shared actualization).  The Heyting gap between the anthropologist's conceptual topos and the subject's ensures this documentation is always lossy---but the loss is structured and measurable via the CIT.

**Indigenous knowledge as alternative convergence conditions.**  Indigenous knowledge systems represent convergence conditions different from those of Western science.  They are not "primitive approximations" to scientific truth but *alternative instantiation paths*---different routes through $\QS$ that access different $\PS$-structures.  Ethnobotanical knowledge, navigational traditions, and ecological management practices may access $\QS$-regions that Western scientific instantiation does not reach.  The three-space framework provides a formal basis for recognizing indigenous knowledge as genuinely complementary rather than merely culturally valuable.

**The WEIRD problem as projection bias.**  The WEIRD problem (Western, Educated, Industrialized, Rich, Democratic) is a projection bias: WEIRD psychology describes the intelligence profiles and filter chains of a particular cultural subgroup, then generalizes to all humans.  In three-space terms, WEIRD science maps one community's $\QS \to \PS$ channels and assumes they are universal.  The species-relative basis insight (Part VI-B) shows this is false even within *Homo sapiens*: different cultural filter chains activate different $\QS$-regions, producing genuinely different cognitive profiles, not merely different "levels" along universal dimensions.

## Discussion

% ═══════════════════════════════════════════════════════════════════════════════

This paper has presented a mathematical framework for cultural cognition that resolves several persistent tensions in anthropological theory.  The universalism--relativism debate is dissolved by distinguishing universal type space from culturally variable filters.  The structural observation bias of fieldwork is proven rather than merely asserted.  Indigenous knowledge systems are formalized without hierarchy.  And cultural diversity is shown to have quantifiable adaptive value at the species level.

The framework has important limitations.  The eight-type decomposition may not capture all culturally relevant cognitive dimensions.  The diagonal filter model is a simplification; real cultural influences may have off-diagonal effects.  And the empirical program required to estimate filter profiles cross-culturally is demanding and raises its own methodological challenges (the instruments themselves carry filter bias, creating a bootstrapping problem).

Nevertheless, the contribution is significant: a mathematical language that makes qualitative anthropological insights precise, falsifiable, and commensurable with formal theories in cognitive science, information theory, and evolutionary biology.  The framework does not replace ethnographic practice---it provides a formal scaffolding that can help anthropologists articulate what they already know and identify what they might be missing.

The deepest implication may be for the discipline's self-understanding.  The CIT proves that cross-cultural understanding is *structurally* incomplete---not because anthropologists are insufficiently skilled or empathetic, but because the mathematics of filter composition forbids lossless translation.  This is not a failure to be lamented but a structural feature to be understood and worked with.  The Heyting Gap is always positive.  The question is not whether it can be eliminated but how it can be minimized---and that is a question the framework can help answer.

% ═══════════════════════════════════════════════════════════════════════════════
% BIBLIOGRAPHY
% ═══════════════════════════════════════════════════════════════════════════════

## References

*See PDF for full bibliography.*
---

## v2 Integration: Expressive Modalities & Observer-Instantiation (TMP-20260217)

**Every expressive practice is a language:** Dance, ritual, material culture, cuisine, oral tradition — each is a projection of the group's collective RTSG graph. Anthropological comparison = comparison of RTSG graph structures.

**Cultural originality ratio:** G(culture)_own / G(culture)_absorbed measures originality. Neither high nor low is superior — it characterizes the culture's position in the collective consciousness graph.

**Observer-instantiation:** Cultural practices involving consciousness-directed attention (ritual, meditation, collective performance) are RTSG instantiation events — moments where CS entangles with quantum space Q to produce shared physical reality P. The anthropological record = the accumulated integral of cultural instantiation events over time.

---

## Filter Formalism Extensions *(v2 — 2026)*

### Lévi-Strauss Algebraically

Lévi-Strauss's structural anthropology — the claim that beneath surface diversity of cultural phenomena lie universal structures of the human mind — receives a precise mathematical interpretation in RTSG. The raw/cooked opposition translates to a specific filter transformation Φ_cult applied to the sensory-evaluative types. "Cooking" is the cultural filter that transforms raw sensory experience (high I_N, naturalistic engagement with food) into culturally coded evaluative categories (high I_IE, internalized standards of taste, preparation, and propriety). The opposition is between the unfiltered and filtered states of the same cognitive material.

### Polynesian Navigation as Superior Filter Configuration

Polynesian navigators achieve extraordinary spatial intelligence (I_S) through training regimes that Western education does not replicate. Hutchins (1995) documents navigational cognition integrating wave patterns, star maps, wind direction, and body sense into a distributed cognitive system exceeding Western-trained navigators in open-ocean conditions. In RTSG: φ^Polynesian_S > φ^Western_S. This is not a simpler version of Western navigation — it is a different and, in its domain, *superior* filter configuration.

### WEIRD Critique Formalized

Henrich, Heine, and Norenzayan (2010) demonstrated that behavioral science is overwhelmingly based on WEIRD (Western, Educated, Industrialized, Rich, Democratic) populations. The RTSG framework formalizes this concern: WEIRD studies sample a narrow region of filter space and report results as universal. The universal claim is valid only for the architectural layer (the 8D type space itself); all developmental claims are filter-relative.

Architecture is universal. Development is cultural. The mathematical object connecting them is the filter — a diagonal operator that models how each culture selectively amplifies and attenuates components of the intelligence vector.
