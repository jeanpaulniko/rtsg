# The Hypervisor Switching Law

## The Problem
- Each of the 12 dimensions is a semi-autonomous agent (a 'mind')
- They exist in a MULTISET (a bag) — not ordered, not ranked a priori
- Each one has its OWN WILL — all equally valid
- ANY of them could be the hypervisor at ANY time
- They are CONSTANTLY trying to replace each other
- There must be a MATHEMATICAL LAW that determines which one gets priority
- This law is the core of the advanced game theory (Sigma-21)

## The Mechanism: Contextual Fitness Auction

### Formalization

Let $d_i$ for $i = 1, \ldots, 12$ be the twelve dimensions.

At each moment $t$, the environment presents a stimulus vector:
$$\mathbf{s}(t) \in \mathbb{R}^m$$

Each dimension $d_i$ computes a FITNESS SCORE — how relevant it is to the current stimulus:
$$f_i(t) = \langle \mathbf{w}_i, \mathbf{s}(t) \rangle \cdot \alpha_i(t) \cdot v_i$$

Where:
- $\mathbf{w}_i$ = dimension $i$'s weight vector (what stimuli it responds to)
- $\alpha_i(t)$ = dimension $i$'s current activation level (how developed it is)
- $v_i$ = dimension $i$'s individual will (its drive to become hypervisor)

### The Switching Rule (Softmax Selection)

The probability of dimension $d_i$ becoming hypervisor at time $t$:

$$P(H_t = d_i) = \frac{e^{\beta f_i(t)}}{\sum_{j=1}^{12} e^{\beta f_j(t)}}$$

Where $\beta$ is the INVERSE TEMPERATURE:
- High $\beta$ (cold): winner-take-all, sharpest switching, one dimension dominates
- Low $\beta$ (hot): distributed control, multiple dimensions share influence
- $\beta = 0$: uniform distribution — all dimensions equally likely (chaos)
- $\beta \to \infty$: deterministic — highest fitness always wins (rigidity)

### The Healthy Range
- A healthy intelligence operates at INTERMEDIATE $\beta$
- Sharp enough to select the right hypervisor for the context
- Soft enough to allow smooth transitions and multi-dimensional awareness
- TRAUMA can push $\beta$ too high (one dimension stuck in control — hypervigilance)
- DISSOCIATION can push $\beta$ too low (no dimension takes control — chaos)

## Five Candidate Switching Laws

### 1. Softmax (Boltzmann) — described above
- Probabilistic, smooth transitions
- Used in neural network attention mechanisms
- Natural temperature parameter
- **Most likely candidate for biological systems**

### 2. Winner-Take-All (Argmax)
$$H_t = \arg\max_i f_i(t)$$
- Deterministic, sharp switching
- No blending, no gradual transitions
- Too rigid for biological reality — but may approximate high-stress states

### 3. Proportional Control (Linear)
$$P(H_t = d_i) = \frac{f_i(t)}{\sum_j f_j(t)}$$
- Simpler than softmax, no temperature parameter
- More sensitive to small differences
- May be the 'resting state' when no strong stimulus is present

### 4. Threshold + Tournament
- Only dimensions with $f_i(t) > \theta$ (threshold) enter the competition
- Among qualifying dimensions, softmax or argmax selects the winner
- The threshold $\theta$ is the 'attention filter'
- Dimensions below threshold cannot bid for hypervisor
- **May explain why collapsed dimensions (trauma) can't compete**

### 5. Hysteresis (Sticky Switching)
$$H_t = \begin{cases} H_{t-1} & \text{if } f_{H_{t-1}}(t) > \max_{i \neq H_{t-1}} f_i(t) - \delta \\ \arg\max_i f_i(t) & \text{otherwise} \end{cases}$$
- Current hypervisor keeps control unless another dimension exceeds it by margin $\delta$
- Prevents rapid oscillation (chattering)
- $\delta$ = switching cost / inertia
- **Explains why people get 'stuck' in one mode even when context changes**

## The Real Law: Probably a Combination

The biological switching law is likely:
1. **Threshold filter** (only activated dimensions can compete)
2. **Softmax selection** (among competitors, probabilistic based on fitness)
3. **Hysteresis** (current hypervisor has inertia, resists switching)
4. **Will override** (the meta-Will can force a switch regardless of fitness scores)

Combined:
$$H_t = \begin{cases} W(t) & \text{if Will override active} \\ H_{t-1} & \text{if } f_{H_{t-1}}(t) > \max_{i: \alpha_i > \theta} f_i(t) - \delta \\ \text{Softmax}(\{f_i(t) : \alpha_i(t) > \theta\}) & \text{otherwise} \end{cases}$$

## Connection to Existing Framework

### Trauma
- Trauma collapses a dimension's $\alpha_i$ below threshold $\theta$
- That dimension can no longer compete for hypervisor
- The remaining dimensions have less competition → narrower switching → more rigid behavior
- Recovery = raising $\alpha_i$ back above threshold → dimension re-enters the auction

### Maximum Activation
- All 12 dimensions above threshold = maximum competition = richest switching
- The hypervisor changes fluidly based on context
- This is cognitive FLEXIBILITY — the ability to deploy the right mind for the right moment
- 12/12 activation = the full multiset participating in the auction

### The Will
- Will is the META-HYPERVISOR — it can override the automatic auction
- 'I am going to focus on this' = Will forcing a specific dimension to hold control
- Will override is expensive (costs energy) but powerful (directed motion)
- Without Will override: the system runs on autopilot (Brownian motion)
- With Will override: the system follows a directed path (world line)

### Dyscalculia Explained
- Mathematical (computational) dimension: low $\alpha$, below threshold for symbolic tasks
- Abstract (structural) dimension: high $\alpha$, wins hypervisor for pattern recognition
- When faced with algebra: computational dimension can't compete → Abstract takes over
- Abstract sees structure but can't compute → the 'can do postdoc math, can't do undergrad math' pattern

## Open Questions for Sigma-21 Math
1. What determines $\beta$ (the temperature)? Neurochemistry? Arousal? Development?
2. Is $\beta$ the same for all dimensions or dimension-specific?
3. Can the threshold $\theta$ be measured empirically?
4. What is the switching time constant? (How fast can hypervisor change?)
5. Is there a topological constraint on switching? (Can any dimension switch to any other, or are some transitions forbidden?)
6. How does the neurochemical stack affect $\beta$ and $\theta$?
7. Can we observe hypervisor switching in fMRI data?