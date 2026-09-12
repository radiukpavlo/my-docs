from pathlib import Path
import re, shutil

root=Path(__file__).resolve().parent.parent
out=root/'CMR_Audit_Presentation'
old=root/'_presentation_work/first-version-source'
v2=root/'CMR_Audit_Presentation_v2'

def write(path,text):
    (out/path).write_text(text.strip()+'\n',encoding='utf-8')

# Preserve the exact underlying data and semantic label keys, renumber by order.
mapping={1:8,2:9,3:1,4:2,5:3,6:4,7:5,8:6,9:7}
for new, source in mapping.items():
    s=(old/f'content/table-{source}.tex').read_text(encoding='utf-8')
    s=re.sub(r'\\setcounter\{table\}\{\d+\}\\refstepcounter\{table\}', '', s)
    write(f'content/table-{new}.tex',s)

# Two narrow comparison panels avoid the original downscaled wide tables.
for new,oldnum in [(1,8),(2,9)]:
    s=(v2/f'content/table-{oldnum}.tex').read_text(encoding='utf-8')
    s=re.sub(r'\\tabkey\{\d+\}\{([^}]+)\}',r'\\label{\1}',s)
    s=s.replace('dexpiBlueLight','bluewash').replace('dexpiGreenLight','greenwash').replace('dexpiRedLight','rosewash')
    write(f'content/table-{new}.tex',s)

# Larger full-width cohort, classifier, and rule tables, without shrink-to-fit.
for new,oldnum in [(3,1),(6,4),(7,5)]:
    s=(v2/f'content/table-{oldnum}.tex').read_text(encoding='utf-8')
    s=re.sub(r'\\tabkey\{\d+\}\{([^}]+)\}',r'\\label{\1}',s)
    s=s.replace('dexpiBlueLight','bluewash').replace('dexpiGreenLight','greenwash').replace('dexpiRedLight','rosewash')
    write(f'content/table-{new}.tex',s)

write('content/table-4.tex',r'''
\label{tab:transition_aggregate_errors}
\begin{tabularx}{\linewidth}{@{}Yrrr@{}}
\toprule
\textbf{Split} & \textbf{SD-NRMSE} & \textbf{RMSE} & \textbf{MAE}\\
\midrule
ACDC train & $0.510\pm0.148$ & 33.18 & 26.49\\
ACDC val. & $0.814\pm0.409$ & 58.42 & 46.49\\
ACDC test & $0.767\pm0.246$ & 51.65 & 38.64\\
M\&Ms ext. & \cellcolor{rosewash}$1.726\pm1.177$ & 85.35 & 69.81\\
\bottomrule
\end{tabularx}
''')

write('content/table-5.tex',r'''
\label{tab:high_impact_transition_results}
\begin{tabularx}{\linewidth}{@{}Yrrrr@{}}
\toprule
\textbf{Target} & \textbf{RMSE} & \textbf{MAE (95\% CI)} & \textbf{$r$} & \textbf{Bias}\\
\midrule
Global ED wall thickness (mm) & 0.83 & 0.59 (0.46--0.79) & 0.928 & $-0.11$\\
LVEF (pp) & 11.38 & 9.17 (7.52--11.16) & 0.863 & $-1.93$\\
RVEF (pp) & 8.87 & 7.52 (6.33--8.91) & 0.815 & $+3.56$\\
LVEDV (mL) & 5.86 & 4.88 (4.02--5.75) & 0.710 & $-2.12$\\
RVEDV (mL) & 9.75 & 6.37 (4.89--9.19) & 0.766 & $-3.13$\\
LV mass, ED (g) & 4.60 & 3.83 (3.17--4.58) & 0.517 & $-1.46$\\
\bottomrule
\end{tabularx}
''')

# Figure 5 is integrated into its evidence table to keep all labels large.
s=(v2/'content/table-6.tex').read_text(encoding='utf-8')
s=re.sub(r'\\tabkey\{\d+\}\{([^}]+)\}',r'\\label{\1}',s)
s=re.sub(r'\\figkey\{[^\n]+\n','',s)
s=s.replace('dexpiBlue','teal').replace('dexpiGreenDark','greenink')
write('content/table-8.tex',s)
s=(v2/'content/table-7.tex').read_text(encoding='utf-8')
s=re.sub(r'\\tabkey\{\d+\}\{([^}]+)\}',r'\\label{\1}',s)
s=s.replace('dexpiRedLight','rosewash')
write('content/table-9.tex',s)

for f in ['equation-7.tex','equations-9-10.tex']:
    shutil.copy2(v2/'content'/f,out/'content'/f)

write('charts/figure-2.tex',r'''
\begin{tikzpicture}[x=1mm,y=.22mm]
\foreach \y in {0,50,100} {
 \draw[muted!22] (0,\y)--(72,\y);
 \node[font=\scriptsize,anchor=east,text=muted] at (-1,\y) {\y};
}
\foreach \x/\a/\b/\lab in {8/33.18/26.49/Train,26/58.42/46.49/Val.,44/51.65/38.64/Test,62/85.35/69.81/Ext.} {
 \fill[dexpiBlue] (\x-3,0) rectangle (\x,\a);
 \fill[amberink!75] (\x+1,0) rectangle (\x+4,\b);
 \node[font=\scriptsize,anchor=north,text=ink] at (\x+.5,-5) {\lab};
}
\end{tikzpicture}
''')

write('charts/figure-3.tex',r'''
\begin{tikzpicture}[x=1mm,y=1mm]
\foreach \x/\lab in {0/0,32/.5,64/1} {
 \draw[muted!20] (\x,0)--(\x,32);
 \node[font=\scriptsize,anchor=north,text=muted] at (\x,-1) {\lab};
}
\foreach \y/\v/\lab in {29/.928/ED wall thickness,24/.863/LVEF,19/.815/RVEF,14/.766/RVEDV,9/.710/LVEDV,4/.517/LV mass} {
 \node[font=\scriptsize,anchor=east,text=ink] at (-2,\y) {\lab};
 \fill[greenink!65] (0,\y-1.5) rectangle (64*\v,\y+1.5);
 \node[font=\scriptsize,anchor=west,text=ink] at (65,\y) {\pgfmathprintnumber[fixed,precision=3,zerofill]{\v}};
}
\end{tikzpicture}
''')

s=(v2/'charts/figure-4.tex').read_text(encoding='utf-8')
s=re.sub(r'\\figkey\{[^\n]+\n','',s)
s=s.replace('dexpiBlueDark','ink').replace('dexpiGreenDark','greenink').replace('dexpiRedDark','roseink')
write('charts/figure-4.tex',s)

write('main.tex',r'''
% !TEX program = pdflatex
% First-version design, refined: sequential numbering, larger type, fuller layouts.
\documentclass[12pt,aspectratio=169,xcolor={dvipsnames,table}]{beamer}
\geometry{paperwidth=240mm,paperheight=135mm}
\usetheme{KhNU}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,booktabs,tabularx,array,graphicx,makecell}
\usepackage{lmodern}\renewcommand{\sfdefault}{phv}
\usefonttheme{professionalfonts}
\usetikzlibrary{calc,positioning,arrows.meta}
\renewcommand{\normalsize}{\fontsize{14.5}{17}\selectfont}
\renewcommand{\small}{\fontsize{12.4}{14.6}\selectfont}
\renewcommand{\footnotesize}{\fontsize{11.5}{13.5}\selectfont}
\renewcommand{\scriptsize}{\fontsize{10.5}{12.2}\selectfont}
\renewcommand{\large}{\fontsize{17}{20}\selectfont}
\renewcommand{\Large}{\fontsize{21.5}{25}\selectfont}
\renewcommand{\LARGE}{\fontsize{25.5}{30}\selectfont}
\definecolor{ink}{HTML}{142F49}
\definecolor{teal}{HTML}{087F8C}
\definecolor{muted}{HTML}{546A7C}
\definecolor{bluewash}{HTML}{EEF5FA}\definecolor{blueink}{HTML}{245884}
\definecolor{greenwash}{HTML}{E7F3EC}\definecolor{greenink}{HTML}{276449}
\definecolor{amberwash}{HTML}{FFF2DF}\definecolor{amberink}{HTML}{78521E}
\definecolor{rosewash}{HTML}{F8EBE9}\definecolor{roseink}{HTML}{833F40}
\setbeamercolor{normal text}{fg=ink,bg=white}
\setbeamercolor{frametitle}{fg=ink}
\setbeamercolor{card blue}{fg=ink,bg=bluewash}
\setbeamercolor{card green}{fg=ink,bg=greenwash}
\setbeamercolor{card amber}{fg=ink,bg=amberwash}
\setbeamercolor{card rose}{fg=ink,bg=rosewash}
\setbeamercolor{signal}{fg=white,bg=teal}
\setbeamersize{text margin left=9mm,text margin right=9mm}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{background}{}\usebackgroundtemplate{}
\setbeamertemplate{frametitle}{%
\vspace{1mm}\begin{minipage}[c][11mm][c]{.88\linewidth}
{\Large\bfseries\insertframetitle\par}\end{minipage}\hfill
\begin{minipage}[c]{17mm}\centering\includegraphics[height=12mm,width=16mm,keepaspectratio]{logos/logo_adt-ismddc.png}\end{minipage}\par
{\color{teal}\rule{\linewidth}{.6pt}}\vspace{-.5mm}}
\setbeamertemplate{footline}{%
\hspace*{9mm}\begin{minipage}{222mm}
{\color{dexpiLightBlue}\rule{\linewidth}{.4pt}}\par
\vspace{1mm}{\scriptsize\color{muted}Radiuk, Barmak \& Krak\hfill\insertsection\hfill\insertframenumber\,/\,10\par}
\vspace{2mm}\end{minipage}}
\setlength{\tabcolsep}{3pt}\renewcommand{\arraystretch}{1.03}
\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
\newcolumntype{C}{>{\centering\arraybackslash}X}
\setlength{\abovedisplayskip}{3pt}\setlength{\belowdisplayskip}{3pt}
\hypersetup{colorlinks=true,urlcolor=teal,linkcolor=teal,
pdftitle={Auditing Deep Learning for Cardiac MRI Through Semantic Transitions and Conflict-Aware Production Rules},
pdfauthor={Pavlo Radiuk; Oleksander Barmak; Iurii Krak}}
\newcommand{\matA}{\mathbf A}\newcommand{\matB}{\mathbf B}
\newcommand{\matT}{\mathbf T}\newcommand{\hatB}{\widehat{\mathbf B}}
\DeclareMathOperator*{\argmin}{arg\,min}\newcounter{auditalgorithm}
\newcommand{\captext}[1]{{\scriptsize\color{muted}#1\par}}
\newcommand{\kicker}[1]{{\small\bfseries\color{teal}#1\par}\vspace{1.5mm}}
\newcommand{\takeaway}[1]{\par\noindent\begin{beamercolorbox}[wd=\dimexpr\linewidth-3pt\relax,sep=2.2mm]{signal}{\small\bfseries #1\par}\end{beamercolorbox}\par}
\newcommand{\card}[3][blue]{\par\noindent\begin{beamercolorbox}[wd=\dimexpr\linewidth-3pt\relax,sep=3mm]{card #1}
{\small\bfseries\color{#1ink}#2\par}\vspace{1.5mm}{\small #3\par}\end{beamercolorbox}\par}
% Counters advance only in presentation order. Source label keys remain semantic.
\newcommand{\tbl}[2]{\refstepcounter{table}\kicker{Table \thetable. #2}{\footnotesize\input{content/table-#1.tex}\par}}
\newcommand{\figurecap}[2]{\refstepcounter{figure}\label{#1}\captext{\textbf{Figure \thefigure.} #2}}
\newcommand{\eqn}[1]{{\normalsize\input{content/equation-#1.tex}}}
\newcommand{\pair}[2]{\makecell[c]{$#1$\\$#2$}}
\newcommand{\scorebar}[2]{#1\hspace{1mm}\begin{tikzpicture}[x=1mm,y=1mm,baseline=0]
\fill[muted!12] (0,0) rectangle (10,1.8);\fill[#2] (0,0) rectangle (10*#1,1.8);\end{tikzpicture}}
\newcommand{\supportlogos}{\includegraphics[height=12mm]{logos/logo_ceur.png}\hspace{9mm}\includegraphics[height=12mm]{logos/logo_cs.png}\hspace{9mm}\includegraphics[height=14mm]{logos/logo_icst.png}\hspace{9mm}\includegraphics[height=14mm]{logos/logo_khnu.png}}
\begin{document}

% 1. Retain the first version's navy title and angular blue accent.
\begin{frame}[plain]
\small
\begin{tikzpicture}[remember picture,overlay]
\fill[ink] (current page.north west) rectangle ([yshift=-75mm]current page.north east);
\fill[dexpiBlue] ([xshift=-53mm]current page.north east)--(current page.north east)--([yshift=-75mm]current page.north east)--([xshift=-75mm,yshift=-75mm]current page.north east)--cycle;
\draw[teal,line width=3pt] ([xshift=9mm,yshift=-77mm]current page.north west)--([xshift=78mm,yshift=-77mm]current page.north west);
\node[anchor=north west,text width=211mm,inner sep=0pt,text=white] at ([xshift=9mm,yshift=-10mm]current page.north west) {\small CMR SEMANTICS\quad/\quad EXPLAINABLE AI\quad/\quad SELECTIVE AUDITING};
\node[anchor=north west,text width=211mm,inner sep=0pt,text=white] at ([xshift=9mm,yshift=-24mm]current page.north west) {\LARGE\bfseries Auditing Deep Learning for Cardiac MRI\\[1mm]Through Semantic Transitions and\\[1mm]Conflict-Aware Production Rules};
\node[anchor=north west,text width=211mm,inner sep=0pt,text=white] at ([xshift=9mm,yshift=-64mm]current page.north west) {\small An externally tested audit layer on deterministic image--mask descriptors};
\node[anchor=north west,text width=211mm,inner sep=0pt,text=ink] at ([xshift=9mm,yshift=-85mm]current page.north west) {\normalsize\bfseries Pavlo Radiuk\textsuperscript{1}\quad Oleksander Barmak\textsuperscript{1}\quad Iurii Krak\textsuperscript{2,3}};
\node[anchor=north west,text width=211mm,inner sep=0pt,text=ink] at ([xshift=9mm,yshift=-96mm]current page.north west) {\small\textsuperscript{1}Khmelnytskyi National University\\[1mm]\textsuperscript{2}Taras Shevchenko National University of Kyiv\\[1mm]\textsuperscript{3}V.M. Glushkov Institute of Cybernetics};
\node[anchor=north west,text width=211mm,inner sep=0pt,text=muted] at ([xshift=9mm,yshift=-122mm]current page.north west) {\scriptsize ICST-ODESA\quad |\quad September 22--24, 2026};
\end{tikzpicture}
\end{frame}

\section{Relevance}
% 2. Tables 1–2, both enlarged and transposed.
\begin{frame}[t]{Prediction quality leaves an audit gap}
\small
\begin{columns}[T,onlytextwidth]
\column{.49\textwidth}\tbl{1}{Accuracy and absolute error}
\vspace{3mm}\card[green]{The audit gap}{Connect recognizable measurements to reusable rules, provenance, conflict, and abstention.}
\column{.49\textwidth}\tbl{2}{Correlation, bias, and audit outputs}
\end{columns}
\vspace{2mm}\captext{Table 2 index cells: Pearson $r$ above signed bias. pp = percentage points; EF bias in pp, LVEDV in mL, mass in g. Khened / Isensee: Bernard et al. (2018). Study: transition + semantic baseline / rule audit.}
\vspace{3mm}\takeaway{Different splits and objectives: these comparisons provide context, not a controlled ranking.}
\end{frame}

\section{Purpose and objectives}
% 3. Table 3 and a balanced three-card layout.
\begin{frame}[t]{Make every audit output traceable}
\small
\takeaway{Purpose: translate fixed CMR representations into measurable semantics and guarded rules.}
\vspace{3mm}\begin{columns}[T,onlytextwidth]
\column{.32\textwidth}\card{01 / Align}{Patient identity, feature QC, and source provenance.}
\column{.32\textwidth}\card[green]{02 / Reconstruct}{128 formal coordinates $\rightarrow$ 28 CMR measurements.}
\column{.32\textwidth}\card[amber]{03 / Audit}{Rule support, conflict, missing evidence, and abstention.}
\end{columns}
\vspace{3mm}\tbl{3}{Cohorts and release-level quality control}
\vspace{3mm}\card[rose]{Review remains incomplete}{92 cases were triaged across both cohorts. These are pending reviews, not confirmed errors or completed expert validation.}
\end{frame}

\section{Methods}
% 4. Full-width, larger-label reconstruction of Figure 1.
\begin{frame}[t]{A frozen, patient-level audit chain}
\small
\begin{columns}[T,onlytextwidth]
\column{.30\textwidth}\card{Formal representation}{\textbf{Native cine CMR}\\ED/ES images and masks\\[3mm]
57 image--mask descriptors\\$\downarrow$ fixed projection\\\textbf{128 coordinates, $\mathbf A$}\\[3mm]
Patient identity and feature-level QC}
\column{.04\textwidth}{\small\vspace{25mm}$\longrightarrow$}
\column{.30\textwidth}\card[green]{Semantic transition}{\textbf{Training-only measured $\mathbf B$}\\28 CMR targets\\[3mm]
\textbf{Regularized transition $\mathbf T$}\\Frozen ridge regression\\[3mm]
\textbf{Reconstructed $\widehat{\mathbf B}$}\\Volumes, EF, mass, wall thickness, and shape}
\column{.04\textwidth}{\small\vspace{25mm}$\longrightarrow$}
\column{.30\textwidth}\card[amber]{Rules and audit outputs}{\textbf{Frozen tertile states $\mathbf S$}\\Training-quantile discretization\\[3mm]
\textbf{200 rules in $\mathcal R$}\\Exact match + clinical alignment\\[3mm]
One supported consequent, or\\\textbf{conflict / typed abstention}}
\end{columns}
\vspace{3mm}\figurecap{fig:cmr_audit_architecture}{Post-hoc CMR audit architecture, redrawn with larger labels. The evaluated release uses tertiles; full WEDD was not evaluated.}
\vspace{4mm}\refstepcounter{auditalgorithm}\label{alg:cmr_audit_pipeline}
\card{Algorithm 1 / Eight-step audit pipeline}{1. Lock cohorts + QC\quad 2. Fit transition\quad 3. Discretize\quad 4. Induce rules\\[1mm]
5. Guard inference\quad 6. Align predicates\quad 7. Evaluate fidelity\quad 8. Test perturbations}
\end{frame}

% 5. Enlarged equations and cards occupy the former blank space.
\begin{frame}[t]{Regularized semantic reconstruction}
\small
\begin{columns}[T,onlytextwidth]
\column{.57\textwidth}\card{Ridge fit and frozen reconstruction}{\eqn{1}\eqn{2}\eqn{3}}
\vspace{4mm}\card[amber]{Training-only preprocessing}{Median imputation; 1st--99th percentile clipping; formal standardization; target centering. Five-fold training CV selected $\lambda=3$.}
\column{.40\textwidth}\card[green]{Evaluated representation}{57 deterministic descriptors $\rightarrow$ 128 coordinates by a fixed Gaussian projection; 32 direct channels retained. Seed: 20260611.}
\vspace{4mm}\card{Frozen tertile states}{\eqn{4}}
\end{columns}
\vspace{4mm}\captext{$\mathbf A_z$: standardized formal features; $\mathbf B_c$: centered targets; $\boldsymbol\mu_B$: training means. The 28 targets cover volumes, EF, mass, wall thickness, and shape.}
\vspace{3mm}\takeaway{This experiment uses deterministic descriptors and tertiles; transition coefficients express associations.}
\end{frame}

% 6. Math typeset at readable sizes; Equation 7 wraps instead of shrinking.
\begin{frame}[t]{Rules, guards, and clinical alignment}
\small
\begin{columns}[T,onlytextwidth]
\column{.49\textwidth}\card{Compact production rules}{\eqn{5}\textbf{At most 3 antecedents}; support $\geq3$ cases; confidence $\geq0.60$.}
\vspace{3mm}\card[amber]{Guarded inference}{\small\input{content/equation-6.tex}}
\vspace{2mm}\captext{$\Gamma(x)$: guard; $\rho(x)$: reason code; $\mathcal Y(x)$: fired consequents. Guards cover severe QC, unstable reconstruction, missing prerequisites, no match, and contradictory consequents.}
\column{.49\textwidth}\card[green]{Physician-style alignment}{\small\input{content/equation-7.tex}}
\vspace{2mm}\captext{$\phi_j$: compatibility; $w_j$: clinical weights. $C_i,M_i,U_i,A_i$: conflict, missing evidence, instability, and safe abstention.}
\vspace{3mm}\card[rose]{Eligibility before similarity}{Support, confidence, prerequisite, and validity gates must pass. A high score cannot replace missing evidence.}
\end{columns}
\vspace{3mm}\takeaway{Soft similarity never overrides the abstention guard. Cine-supported proxies remain evidence-bounded.}
\end{frame}

\section{Experiments and results}
% 7. Tables 4–5, Figures 2–3; enlarged data and chart labels.
\begin{frame}[t]{Semantic fidelity and external domain shift}
\small
\begin{columns}[T,onlytextwidth]
\column{.38\textwidth}\tbl{4}{Aggregate reconstruction}
{\small\input{content/equation-8.tex}}
\captext{Across 28 targets. NRMSE uses training SD; mixed-unit RMSE / MAE means are descriptive.}
\vspace{3mm}\centering\input{charts/figure-2.tex}\par
\figurecap{fig:transition_split_errors}{Split errors: \textcolor{dexpiBlue}{\textbf{RMSE}} / \textcolor{amberink}{\textbf{MAE}}. External = M\&Ms; other splits = ACDC.}
\column{.60\textwidth}\tbl{5}{Held-out ACDC target fidelity}
\vspace{2mm}\captext{$n=50$; 1,000-resample BCa 95\% CIs for MAE. ED: end-diastolic; pp: percentage points.}
\vspace{3mm}\centering\input{charts/figure-3.tex}\par
\figurecap{fig:high_impact_correlations}{Pearson correlations for high-impact targets, shown on a common 0--1 scale.}
\end{columns}
\vspace{3mm}\takeaway{External NRMSE: $2.25\times$ test error. External bias: LVEDV $-136.0$ mL; mass $-96.6$ g.}
\end{frame}

% 8. Tables 6–7 use the full slide width.
\begin{frame}[t]{Coverage must accompany rule accuracy}
\small
\tbl{6}{Measured-semantic logistic-regression comparator}
\vspace{2mm}\tbl{7}{200-rule audit; balanced accuracy and F1 use non-abstained cases}
\vspace{2mm}\begin{columns}[T,onlytextwidth]
\column{.50\textwidth}\centering\input{charts/figure-4.tex}\par
\figurecap{fig:classifier_rulebook_outcomes}{Held-out comparator and rulebook outcomes.}
\column{.48\textwidth}\card[green]{Held-out uncertainty / 95\% CIs}{\footnotesize
Accuracy: 0.860 [0.76, 0.94]\\
Balanced accuracy: 0.860 [0.75, 0.95]\\
Macro-F1: 0.861 [0.75, 0.94]\\
AUROC: 0.973 [0.947, 0.993]\\[1mm]
Row-bootstrap intervals. \textbf{32 covered / 18 abstained} on the 50-case test split.}
\end{columns}
\vspace{2mm}\captext{Conflict: among covered cases; conf. seen: among all cases during resolution. ECE: 10 equal-mass bins. Perfect selective train/validation scores reflect over-specific granules.}
\end{frame}

% 9. Tables 8–9 and Figure 5, clearly ordered left to right.
\begin{frame}[t]{Predicate alignment and perturbation sensitivity}
\small
\begin{columns}[T,onlytextwidth]
\column{.49\textwidth}\tbl{8}{Physician-predicate evidence}
\vspace{2mm}\figurecap{fig:predicate_alignment_scores}{Admissible similarity bars in Table 8; common 0--1 scale. Unsupported predicates remain unmatched.}
\vspace{3mm}\captext{HCM / DCM: hypertrophic / dilated cardiomyopathy; MI: myocardial infarction; ARVC: arrhythmogenic right ventricular cardiomyopathy. Congenital review is a research approximation.}
\vspace{3mm}\card[green]{Evidence boundary}{Similarity is not clinician agreement. Valvular and congenital proxies support review, not diagnosis.}
\column{.49\textwidth}\tbl{9}{Perturbations: 12 cases, 48 runs}
\vspace{2mm}{\small\input{content/equations-9-10.tex}}
\vspace{2mm}\card[rose]{Orientation sensitivity}{A $2^\circ$ rotation produces the largest drift despite nearly preserved mask counts.}
\vspace{2mm}\captext{$Q$: 12 cases; $\tau$: perturbation; $\varepsilon$: stabilizer. Mixed-unit semantic drift ranks sensitivity only. Native orientation; no rotation augmentation.}
\end{columns}
\end{frame}

\section{Conclusions and contact}
% 10. Enlarge and balance concluding cards, contacts, and identity strip.
\begin{frame}[t]{Transparent auditing and next validation}
\small
\begin{columns}[T,onlytextwidth]
\column{.49\textwidth}\card[green]{What the study establishes}{A traceable semantic-to-rule audit chain; strong internal association for selected targets; visible external degradation, conflict, and abstention.}
\vspace{3mm}\card[amber]{What remains to be validated}{Frozen deep encoders; full WEDD; orientation normalization; vendor recalibration; completed expert QC and prospective clinician evaluation.}
\vspace{3mm}\card[rose]{Current scope}{Selective research auditing. Rule sparsity and domain shift preclude autonomous diagnosis or completed clinical validation.}
\column{.48\textwidth}\card{Authors and correspondence}{\textbf{Pavlo Radiuk}\textsuperscript{1} (corresponding author)\\\href{mailto:radiukp@khmnu.edu.ua}{radiukp@khmnu.edu.ua}\\[3mm]
\textbf{Oleksander Barmak}\textsuperscript{1}\\\href{mailto:barmako@khmnu.edu.ua}{barmako@khmnu.edu.ua}\\[3mm]
\textbf{Iurii Krak}\textsuperscript{2,3}\\\href{mailto:iurii.krak@knu.ua}{iurii.krak@knu.ua}}
\vspace{3mm}\captext{\textsuperscript{1}Khmelnytskyi National University\\\textsuperscript{2}Taras Shevchenko National University of Kyiv\\\textsuperscript{3}V.M. Glushkov Institute of Cybernetics}
\end{columns}
\vspace{3mm}\captext{Supporting organizations and conference identities supplied with the presentation}
\vspace{2mm}\supportlogos
\end{frame}
\end{document}
''')
print('First-version design revised in place; tables renumbered and text enlarged.')
