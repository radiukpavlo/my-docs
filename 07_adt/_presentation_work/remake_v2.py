from pathlib import Path

out = Path(__file__).resolve().parent.parent/'CMR_Audit_Presentation_v2'

def write(name, text):
    (out/name).write_text(text.strip()+'\n', encoding='utf-8')

write('content/table-8.tex',r'''
\tabkey{8}{tab:acdc_sota_comparison}
\begin{tabularx}{\linewidth}{@{}Yccc@{}}
\toprule
\textbf{Metric} & \textbf{Khened} & \textbf{Isensee} & \textbf{Study}\\
\midrule
Diagnostic accuracy & 0.960 & 0.920 & \cellcolor{dexpiBlueLight}0.860\\
LVEDV MAE (mL) & 4.20 & 5.10 & \cellcolor{dexpiBlueLight}4.88\\
LVEF MAE (pp) & 2.50 & 2.10 & \cellcolor{dexpiRedLight}9.17\\
RVEF MAE (pp) & 5.30 & 4.70 & \cellcolor{dexpiBlueLight}7.52\\
Mass MAE (g) & 6.30 & 7.30 & \cellcolor{dexpiBlueLight}3.83\\
Rule coverage & -- & -- & \cellcolor{dexpiGreenLight}0.640\\
Rule balanced acc. & -- & -- & \cellcolor{dexpiGreenLight}0.644\\
\bottomrule
\end{tabularx}
''')

write('content/table-9.tex',r'''
\tabkey{9}{tab:acdc_correlation_bias}
\begin{tabularx}{\linewidth}{@{}Yccc@{}}
\toprule
\textbf{Index} & \textbf{Khened} & \textbf{Isensee} & \textbf{Study}\\
\midrule
LVEF & \pair{0.989}{-0.5} & \pair{0.991}{+0.5} & \cellcolor{dexpiBlueLight}\pair{0.863}{-1.93}\\
RVEF & \pair{0.858}{-2.2} & \pair{0.925}{-3.0} & \cellcolor{dexpiBlueLight}\pair{0.815}{+3.56}\\
LVEDV & \pair{0.997}{+0.6} & \pair{0.997}{+1.5} & \cellcolor{dexpiBlueLight}\pair{0.710}{-2.12}\\
Mass & \pair{0.990}{-2.9} & \pair{0.986}{-4.0} & \cellcolor{dexpiRedLight}\pair{0.517}{-1.46}\\
\midrule
Coverage & -- & -- & 0.640\\
Abstention & -- & -- & 0.360\\
Conflict & -- & -- & 0.313\\
\bottomrule
\end{tabularx}
''')

write('content/table-1.tex',r'''
\tabkey{1}{tab:cohort_qc_evidence}
\begin{tabularx}{\linewidth}{@{}p{53mm}ccY@{}}
\toprule
\textbf{Audit item} & \textbf{ACDC} & \textbf{M\&Ms} & \textbf{Scope / interpretation}\\
\midrule
Patient-level cases & 150 & 100 & ACDC: 85 / 15 / 50 train / validation / test; M\&Ms: external only.\\
Semantic validation checks & 10/10 & 10/10 & All programmed gates passed.\\
Native overlay panels & 53 & 65 & End-diastolic / end-systolic image--mask panels.\\
Semantic targets per case & 28 & 28 & Same semantic schema in both cohorts.\\
Pending manual review & -- & -- & 92 cases across both cohorts; no dataset-specific split reported.\\
\bottomrule
\end{tabularx}
''')

write('content/table-2.tex',r'''
\tabkey{2}{tab:transition_aggregate_errors}
\begin{tabularx}{\linewidth}{@{}Yccc@{}}
\toprule
\textbf{Cohort / split} & \textbf{SD-NRMSE} & \textbf{RMSE} & \textbf{MAE}\\
\midrule
ACDC / train & $0.510\pm0.148$ & 33.18 & 26.49\\
ACDC / val. & $0.814\pm0.409$ & 58.42 & 46.49\\
ACDC / test & $0.767\pm0.246$ & 51.65 & 38.64\\
M\&Ms / ext. & \cellcolor{dexpiRedLight}$1.726\pm1.177$ & 85.35 & 69.81\\
\bottomrule
\end{tabularx}
''')

write('content/table-3.tex',r'''
\tabkey{3}{tab:high_impact_transition_results}
\figkey{3}{fig:high_impact_correlations}
\begin{tabularx}{\linewidth}{@{}Yrrrr@{}}
\toprule
\textbf{Target} & \textbf{RMSE} & \makecell{\textbf{MAE}\\\textbf{95\% CI}} & \makecell{\textbf{Pearson}\\\textbf{$r$}} & \textbf{Bias}\\
\midrule
ED wall thickness (mm) & 0.83 & \makecell[r]{0.59\\(0.46--0.79)} & \scorebar{0.928}{dexpiGreenDark} & $-0.11$\\
LVEF (pp) & 11.38 & \makecell[r]{9.17\\(7.52--11.16)} & \scorebar{0.863}{dexpiGreenDark} & $-1.93$\\
RVEF (pp) & 8.87 & \makecell[r]{7.52\\(6.33--8.91)} & \scorebar{0.815}{dexpiGreenDark} & $+3.56$\\
LVEDV (mL) & 5.86 & \makecell[r]{4.88\\(4.02--5.75)} & \scorebar{0.710}{dexpiGreenDark} & $-2.12$\\
RVEDV (mL) & 9.75 & \makecell[r]{6.37\\(4.89--9.19)} & \scorebar{0.766}{dexpiGreenDark} & $-3.13$\\
LV mass, ED (g) & 4.60 & \makecell[r]{3.83\\(3.17--4.58)} & \scorebar{0.517}{dexpiGreenDark} & $-1.46$\\
\bottomrule
\end{tabularx}
''')

write('content/table-4.tex',r'''
\tabkey{4}{tab:semantic_classifier_performance}
\begin{tabularx}{\linewidth}{@{}Y*{6}{C}@{}}
\toprule
\textbf{Split} & \textbf{Accuracy} & \textbf{Bal. acc.} & \textbf{Macro-F1} & \textbf{AUROC} & \textbf{ECE} & \textbf{$n$}\\
\midrule
Validation & 0.933 & 0.933 & 0.931 & 1.000 & 0.103 & 15\\
Test & \cellcolor{dexpiGreenLight}0.860 & 0.860 & 0.861 & 0.973 & \cellcolor{dexpiRedLight}0.179 & 50\\
\bottomrule
\end{tabularx}
''')

write('content/table-5.tex',r'''
\tabkey{5}{tab:rulebook_performance}
\begin{tabularx}{\linewidth}{@{}Y*{7}{C}@{}}
\toprule
\textbf{Split} & \textbf{Coverage} & \textbf{Abstain} & \textbf{Bal. acc.} & \textbf{Macro-F1} & \textbf{Conflict} & \textbf{Conf. seen} & \textbf{$n$}\\
\midrule
Train & 0.565 & 0.435 & 1.000 & 1.000 & 0.229 & 0.565 & 85\\
Validation & 0.667 & 0.333 & 1.000 & 1.000 & 0.300 & 0.533 & 15\\
Test & \cellcolor{dexpiBlueLight}0.640 & \cellcolor{dexpiRedLight}0.360 & \cellcolor{dexpiGreenLight}0.644 & 0.612 & 0.313 & 0.560 & 50\\
\bottomrule
\end{tabularx}
''')

write('content/table-6.tex',r'''
\tabkey{6}{tab:predicate_evidence_alignment}
\figkey{5}{fig:predicate_alignment_scores}
\begin{tabularx}{\linewidth}{@{}Yp{28mm}r@{}}
\toprule
\textbf{Predicate family} & \textbf{Evidence} & \textbf{Similarity}\\
\midrule
Abnormal RV / ARVC proxy & Cine-mask proxy & \scorebar{0.9008}{dexpiBlue}\\
Hypertrophic cardiomyopathy proxy & Cine-mask proxy & \scorebar{0.8564}{dexpiBlue}\\
Infarction-remodeling proxy & Cine proxy & \scorebar{0.8250}{dexpiBlue}\\
Dilated cardiomyopathy proxy & Cine-mask proxy & \scorebar{0.7858}{dexpiBlue}\\
Valvular volume review & Review proxy & \scorebar{0.7825}{dexpiGreenDark}\\
Congenital candidate review & Research approx. & \scorebar{0.6842}{dexpiGreenDark}\\
Conservative normal filter & Research filter & \scorebar{0.5462}{dexpiGreenDark}\\
Restrictive / noncompaction / inflammatory / infiltrative & Unsupported & \textcolor{dexpiRedDark}{Unmatched}\\
\bottomrule
\end{tabularx}
''')

write('content/table-7.tex',r'''
\tabkey{7}{tab:perturbation_summary}
\begin{tabularx}{\linewidth}{@{}Yrrr@{}}
\toprule
\textbf{Perturbation} & \makecell{\textbf{Formal}\\\textbf{change}} & \makecell{\textbf{Semantic}\\\textbf{change}} & \makecell{\textbf{Mask-count}\\\textbf{change}}\\
\midrule
Intensity +5\% & $1.1\!\times\!10^{-8}$ & $8.8\!\times\!10^{-6}$ & 0.000000\\
Shift $x$, 1 px & 0.002591 & 0.622935 & 0.000000\\
Shift $y$, 1 px & 0.002135 & 0.545662 & 0.000000\\
Rotation $2^\circ$ & \cellcolor{dexpiRedLight}0.053114 & \cellcolor{dexpiRedLight}9.821420 & 0.000470\\
\bottomrule
\end{tabularx}
''')

write('content/equation-7.tex',r'''
\begin{equation}
\begin{aligned}
\operatorname{Sim}(P_y,R_i)=\max\!\Biggl\{0,\;&
\frac{\sum_j w_j\phi_j(P_y,R_i)}{\sum_jw_j}\\
&-\gamma_cC_i-\gamma_mM_i-\gamma_uU_i+\gamma_aA_i\Biggr\}.
\end{aligned}
\tag{7}\label{eq:predicate_rule_similarity}
\end{equation}
''')

write('charts/figure-2.tex',r'''
\figkey{2}{fig:transition_split_errors}
\begin{tikzpicture}[x=1mm,y=.25mm]
\foreach \y in {0,50,100} {
  \draw[dexpiBlue!18] (0,\y)--(92,\y);
  \node[anchor=east,font=\scriptsize,text=dexpiBlueDark] at (-1,\y) {\y};
}
\foreach \x/\rmse/\mae/\lab in {12/51.65/38.64/Test,34/33.18/26.49/Train,56/58.42/46.49/Val.,78/85.35/69.81/External} {
 \fill[dexpiBlue] (\x-4,0) rectangle (\x,\rmse);
 \fill[dexpiGreenDark] (\x+1,0) rectangle (\x+5,\mae);
 \node[anchor=north,font=\scriptsize,text=dexpiBlueDark] at (\x+.5,-5) {\lab};
}
\end{tikzpicture}
''')

write('charts/figure-4.tex',r'''
\figkey{4}{fig:classifier_rulebook_outcomes}
\begin{tikzpicture}[x=1mm,y=1mm]
\foreach \x/\lab in {0/0,32/.5,64/1} {
 \draw[dexpiBlue!15] (\x,0)--(\x,30);
 \node[font=\scriptsize,anchor=north,text=dexpiBlueDark] at (\x,-1) {\lab};
}
\foreach \y/\val/\lab/\col in {
28/.640/Rule coverage/dexpiBlue,
23/.360/Rule abstention/dexpiRedDark,
18/.644/Rule bal. acc./dexpiGreenDark,
13/.612/Rule macro-F1/dexpiGreenDark,
8/.860/Classifier acc./dexpiBlue,
3/.973/Classifier AUROC/dexpiBlue} {
 \node[font=\scriptsize,anchor=east,text=dexpiBlueDark] at (-2,\y) {\lab};
 \fill[\col] (0,\y-1.3) rectangle (64*\val,\y+1.3);
 \node[font=\scriptsize,anchor=west,text=dexpiBlueDark] at (65,\y) {\pgfmathprintnumber[fixed,precision=3,zerofill]{\val}};
}
\end{tikzpicture}
''')

write('main.tex',r'''
% !TEX program = pdflatex
% Second edition: restored KhNU template design; enlarged evidence layouts.
\documentclass[12pt,aspectratio=169,xcolor={dvipsnames,table}]{beamer}
\geometry{paperwidth=240mm,paperheight=135mm}
\usetheme{KhNU}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,booktabs,tabularx,array,graphicx,makecell}
\usetikzlibrary{calc,positioning,arrows.meta}
\renewcommand{\normalsize}{\fontsize{14}{16.5}\selectfont}
\renewcommand{\small}{\fontsize{12}{14}\selectfont}
\renewcommand{\footnotesize}{\fontsize{11.5}{13}\selectfont}
\renewcommand{\scriptsize}{\fontsize{10.5}{12}\selectfont}
\renewcommand{\large}{\fontsize{17}{20}\selectfont}
\renewcommand{\Large}{\fontsize{21}{24}\selectfont}
\renewcommand{\LARGE}{\fontsize{23}{27}\selectfont}
\setbeamercolor{normal text}{fg=dexpiBlueDark,bg=white}
\setbeamersize{text margin left=9mm,text margin right=9mm}
\setbeamertemplate{navigation symbols}{}
% Original KhNU diagonal motif, scaled to this 16:9 canvas.
\usebackgroundtemplate{\begin{tikzpicture}[remember picture,overlay]
\fill[dexpiLightBlue] ([xshift=-60mm]current page.north east)--(current page.north east)--([yshift=12mm]current page.south east)--([xshift=-90mm,yshift=12mm]current page.south east)--cycle;
\end{tikzpicture}}
\setbeamertemplate{frametitle}{%
\vspace{2mm}\begin{minipage}[c][12mm][c]{.89\linewidth}
{\Large\bfseries\color{dexpiBlue}\insertframetitle\par}
\end{minipage}\hfill\includegraphics[height=12mm]{logos/logo_adt-ismddc.png}\par
{\color{dexpiBlue}\rule{\linewidth}{.6pt}}\vspace{1mm}}
% Date, section, KhNU identity, page number and slash follow the supplied footer.
\setbeamertemplate{footline}{%
\begin{tikzpicture}[remember picture,overlay]
\draw[dexpiBlue,line width=1pt] ([xshift=-2mm,yshift=2mm]current page.south west)--([xshift=8mm,yshift=-8mm]current page.south west);
\end{tikzpicture}%
\hspace*{9mm}\begin{minipage}[c][10mm][c]{28mm}{\scriptsize\color{dexpiBlue}2026\par}\end{minipage}%
\begin{minipage}[c][10mm][c]{151mm}{\scriptsize\color{dexpiBlue}\insertsection\par}\end{minipage}%
\begin{minipage}[c][10mm][c]{26mm}\centering\includegraphics[height=9mm]{img/khnu_logo_blank.png}\end{minipage}%
\begin{minipage}[c][10mm][c]{17mm}\raggedleft{\scriptsize\color{dexpiBlue}\insertframenumber\,/\,10\par}\end{minipage}}
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.17}
\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
\newcolumntype{C}{>{\centering\arraybackslash}X}
\setlength{\abovedisplayskip}{3pt}
\setlength{\belowdisplayskip}{3pt}
\hypersetup{colorlinks=true,urlcolor=dexpiBlue,linkcolor=dexpiBlue,
pdftitle={Auditing Deep Learning for Cardiac MRI Through Semantic Transitions and Conflict-Aware Production Rules},
pdfauthor={Pavlo Radiuk; Oleksander Barmak; Iurii Krak}}
\newcommand{\matA}{\mathbf A}\newcommand{\matB}{\mathbf B}
\newcommand{\matT}{\mathbf T}\newcommand{\hatB}{\widehat{\mathbf B}}
\DeclareMathOperator*{\argmin}{arg\,min}
\newcounter{auditalgorithm}
\newcommand{\captext}[1]{{\scriptsize\color{dexpiBlueDark}#1\par}}
\newcommand{\captionhead}[1]{{\small\bfseries\color{dexpiBlue}#1\par}\vspace{1.5mm}}
% Exact polygon heading construction from the supplied theme, with readable type.
\setlength{\dexpiblocktitleht}{7mm}\setlength{\dexpiblockpad}{2mm}
\setbeamerfont{block title}{size=\small,series=\bfseries}
\newcommand{\card}[3][]{\par\noindent\begingroup
\dexpipolygontitle{block title #1}{\small\bfseries #2}\par\vspace{-2pt}
\begin{beamercolorbox}[wd=\linewidth,sep=2mm]{block body #1}{\small #3\par}\end{beamercolorbox}\endgroup\par}
\newcommand{\messagebox}[2][example]{\begin{beamercolorbox}[wd=\linewidth,sep=2mm]{block body #1}{\small\bfseries #2\par}\end{beamercolorbox}}
\newcommand{\tabkey}[2]{\setcounter{table}{\numexpr#1-1\relax}\refstepcounter{table}\label{#2}}
\newcommand{\figkey}[2]{\setcounter{figure}{\numexpr#1-1\relax}\refstepcounter{figure}\label{#2}}
\newcommand{\pair}[2]{\makecell[c]{$#1$\\$#2$}}
\newcommand{\scorebar}[2]{\makecell[r]{#1\\\begin{tikzpicture}[x=1mm,y=1mm,baseline=0]
\fill[dexpiBlue!12] (0,0) rectangle (15,1.6);\fill[#2] (0,0) rectangle (15*#1,1.6);
\end{tikzpicture}}}
\newcommand{\eqn}[1]{{\normalsize\input{content/equation-#1.tex}}}
\newcommand{\supportlogos}{\includegraphics[height=10mm]{logos/logo_ceur.png}\hspace{7mm}\includegraphics[height=10mm]{logos/logo_cs.png}\hspace{7mm}\includegraphics[height=12mm]{logos/logo_icst.png}\hspace{7mm}\includegraphics[height=12mm]{logos/logo_khnu.png}}
\begin{document}

% 1. Template-based photographic title polygon and institutional identity.
{\usebackgroundtemplate{}\begin{frame}[plain]
\normalsize
\begin{tikzpicture}[remember picture,overlay,x=1mm,y=1mm,shift={(current page.south west)}]
\begin{scope}\clip (135,20)--(240,20)--(240,135)--(154,135)--cycle;
\node[anchor=south west,inner sep=0] at (115,0) {\includegraphics[height=135mm]{img/StockSnap_REB7CJXE8C.jpg}};\end{scope}
\fill[dexpiLightBlue] (109,0)--(128,0)--(153,135)--(134,135)--cycle;
\fill[dexpiBlue] (128,0)--(240,0)--(240,20)--(132,20)--cycle;
\fill[dexpiBlue] (0,45)--(187,45)--(198,100)--(0,100)--cycle;
\node[anchor=north west,inner sep=0] at (9,130) {\includegraphics[height=20mm]{img/khnu_logo_colored.png}};
\node[anchor=north west,text width=177mm,inner sep=0,text=white] at (9,95) {\Large\bfseries Auditing Deep Learning for Cardiac MRI\\[1mm]Through Semantic Transitions and\\[1mm]Conflict-Aware Production Rules};
\node[anchor=north west,text width=173mm,inner sep=0,text=white] at (9,59) {\small A post-hoc semantic audit of cardiac MRI\\Deterministic descriptors; explicit evidence limits};
\node[anchor=north west,text width=122mm,inner sep=0,text=dexpiBlue] at (9,39) {\small\bfseries Pavlo Radiuk\textsuperscript{1}\quad Oleksander Barmak\textsuperscript{1}\\Iurii Krak\textsuperscript{2,3}};
\node[anchor=north west,text width=120mm,inner sep=0,text=dexpiBlue] at (9,26) {\scriptsize\textsuperscript{1}Khmelnytskyi National University\\\textsuperscript{2}Taras Shevchenko National University of Kyiv\\\textsuperscript{3}V.M. Glushkov Institute of Cybernetics};
\node[anchor=north west,text width=118mm,inner sep=0,text=dexpiBlue] at (9,8) {\scriptsize ICST-ODESA\quad |\quad September 22--24, 2026};
\draw[dexpiBlue,line width=1pt] (-2,2)--(8,-8);
\end{tikzpicture}
\end{frame}}

\section{Relevance and research gap}
% 2. Transposed, unscaled comparison tables.
\begin{frame}[t]{Why CMR predictions need an audit trail}
\small
\messagebox{The research gap: connect image-derived evidence to recognizable measurements and explicit decision logic.}
\vspace{2mm}
\begin{columns}[T,onlytextwidth]
\column{.49\textwidth}
\captionhead{Table 8. Accuracy and absolute error}
{\small\input{content/table-8.tex}\par}
\vspace{3mm}\card[alerted]{Comparison boundary}{Different splits and objectives prevent a controlled ranking. Published systems target diagnosis; this study targets auditability.}
\column{.49\textwidth}
\captionhead{Table 9. Correlation, bias, and audit outputs}
\captext{Each index cell: Pearson $r$ above signed bias.}
\vspace{1mm}{\small\input{content/table-9.tex}\par}
\end{columns}
\vspace{2mm}\captext{Khened / Isensee challenge systems: Bernard et al. (2018), \textit{IEEE TMI} 37, 2514--2525. Study: proposed transition + semantic baseline / rule audit. pp = percentage points; bias: EF in pp, LVEDV in mL, mass in g.}
\end{frame}

\section{Purpose and objectives}
% 3. Three native theme block colors and readable cohort table.
\begin{frame}[t]{Purpose: traceable semantics and decisions}
\small
\begin{columns}[T,onlytextwidth]
\column{.32\textwidth}\card{01 / Align}{Link each patient to images, masks, features, labels, and QC evidence.}
\column{.32\textwidth}\card[example]{02 / Reconstruct}{Map 128 formal coordinates to 28 interpretable CMR measurements.}
\column{.32\textwidth}\card[alerted]{03 / Audit}{Expose rule support, conflict, missing evidence, and abstention.}
\end{columns}
\vspace{4mm}\captionhead{Table 1. Cohorts and quality-control evidence}
{\small\input{content/table-1.tex}\par}
\vspace{3mm}\messagebox[alerted]{92 triaged cases await review; this is unresolved workload, not 92 confirmed errors.}
\vspace{2mm}\captext{ACDC: five balanced categories. M\&Ms: Multi-Centre, Multi-Vendor and Multi-Disease cohort. All held-out cohorts remained untouched during fitting. Release: \texttt{v5\_native\_image\_dss\_100}.}
\end{frame}

\section{Methods}
% 4. Figure 1 is redrawn as an editable, large-label diagram.
\begin{frame}[t]{From CMR inputs to auditable rules}
\small
\figkey{1}{fig:cmr_audit_architecture}
\begin{columns}[T,onlytextwidth]
\column{.30\textwidth}\card{1 / Formal representation}{\textbf{Native cine images + masks}\\End-diastolic / end-systolic phases\\[3mm]
57 intensity and occupancy descriptors\\[3mm]
\textbf{Fixed projection: 128 coordinates}\\$\mathbf A\in\mathbb R^{m\times128}$\\[3mm]
Patient alignment + feature-level QC}
\column{.035\textwidth}{\normalsize\vspace{28mm}$\longrightarrow$}
\column{.30\textwidth}\card[example]{2 / Semantic transition}{\textbf{Training-only measured $\mathbf B$}\\28 CMR targets\\[3mm]
\textbf{Regularized transition $\mathbf T$}\\Ridge regression; frozen after fitting\\[3mm]
\textbf{Reconstructed $\widehat{\mathbf B}$}\\Volumes, EF, mass, wall thickness, shape}
\column{.035\textwidth}{\normalsize\vspace{28mm}$\longrightarrow$}
\column{.30\textwidth}\card[alerted]{3 / Rules and guarded outputs}{\textbf{Frozen tertile states $\mathbf S$}\\Training-quantile discretization\\[3mm]
\textbf{Rulebook $\mathcal R$: 200 rules}\\Exact match + clinical alignment\\[3mm]
One supported consequent, or\\\textbf{conflict / typed abstention}\\Missing or unstable evidence stays visible}
\end{columns}
\vspace{3mm}\captext{Figure 1. Post-hoc CMR audit architecture, redrawn from the manuscript with larger labels. This release uses tertiles; full WEDD was not evaluated.}
\vspace{4mm}\refstepcounter{auditalgorithm}\label{alg:cmr_audit_pipeline}
\captionhead{Algorithm 1. Eight steps, one frozen audit chain}
\messagebox{Lock + QC $\rightarrow$ fit $\rightarrow$ discretize $\rightarrow$ induce $\rightarrow$ guard $\rightarrow$ align $\rightarrow$ evaluate $\rightarrow$ perturb}
\end{frame}

% 5. Equations 1–4.
\begin{frame}[t]{Methods: semantic transition and discretization}
\small
\begin{columns}[T,onlytextwidth]
\column{.57\textwidth}
\card{Regularized semantic transition}{\eqn{1}\eqn{2}\eqn{3}}
\vspace{3mm}\card[example]{Fit on 85 training cases only}{Median imputation; 1st--99th percentile clipping; standardization and centering. Five-fold training CV selects $\lambda=3$.}
\column{.40\textwidth}
\card[example]{Frozen symbolic states}{\eqn{4}}
\vspace{3mm}\card[alerted]{Scope of the experiment}{Deterministic descriptors, not a trained deep encoder. Tertiles approximate the parent WEDD stage.}
\vspace{3mm}\captext{57 descriptors $\rightarrow$ 128 coordinates; 32 direct channels retained. Fixed projection seed: 20260611.}
\end{columns}
\vspace{3mm}\captext{$\mathbf A_z$: standardized formal features; $\mathbf B_c$: centered targets; $\boldsymbol\mu_B$: training target means. Transition coefficients express associations, not causal effects.}
\end{frame}

% 6. Equations 5–7; similarity wrapped, not reduced.
\begin{frame}[t]{Methods: rules, guards, and clinical alignment}
\small
\begin{columns}[T,onlytextwidth]
\column{.49\textwidth}
\card{Compact production rules}{\eqn{5}\textbf{At most 3 antecedents}; support $\geq3$ training cases; confidence $\geq0.60$.}
\vspace{3mm}\card[alerted]{Reason-coded abstention}{\small\input{content/equation-6.tex}}
\vspace{2mm}\captext{Guard $\Gamma(x)$ checks QC, reconstruction stability, prerequisites, no match, and contradictory consequents. $\rho(x)$ records the reason; $\mathcal Y(x)$ is the fired-label set.}
\column{.49\textwidth}
\card[example]{Physician-style alignment}{\small\input{content/equation-7.tex}}
\vspace{2mm}\captext{$\phi_j$: compatibility; $w_j$: clinical weights. $C_i,M_i,U_i,A_i$: conflict, missing evidence, instability, and safe abstention.}
\vspace{3mm}\card[alerted]{Eligibility comes first}{Support, confidence, prerequisite, and validity gates must pass. A high similarity score cannot replace missing evidence.}
\end{columns}
\vspace{3mm}\messagebox{Soft similarity never overrides the abstention guard. Cine-supported proxies remain evidence-bounded.}
\end{frame}

\section{Experiments and results}
% 7. Figure 3 is integrated into Table 3 to eliminate duplicate tiny labels.
\begin{frame}[t]{Results: reconstruction and external shift}
\small
\begin{columns}[T,onlytextwidth]
\column{.48\textwidth}
\captionhead{Table 2. Reconstruction over 28 targets}
{\footnotesize\input{content/table-2.tex}\par}
{\small\input{content/equation-8.tex}}
\captext{NRMSE uses ACDC-training SD. Mixed-unit mean RMSE / MAE are descriptive.}
\vspace{2mm}\centering\input{charts/figure-2.tex}\par
\vspace{1mm}\captext{Figure 2. Split-wise errors: \textcolor{dexpiBlue}{\textbf{RMSE}} / \textcolor{dexpiGreenDark}{\textbf{MAE}}. First three splits: ACDC; external: M\&Ms.}
\column{.50\textwidth}
\captionhead{Table 3 + Figure 3. Held-out fidelity}
{\footnotesize\input{content/table-3.tex}\par}
\vspace{2mm}\captext{$n=50$; 1,000-resample BCa 95\% CIs for MAE. Green bars show Pearson $r$ on a common 0--1 scale. ED = end-diastolic; pp = percentage points.}
\end{columns}
\vspace{3mm}\messagebox[alerted]{External NRMSE rises 2.25-fold. LVEDV bias: $-2.12\rightarrow-136.0$ mL; mass bias: $-1.46\rightarrow-96.6$ g.}
\end{frame}

% 8. Full-width tables, enlarged chart labels and concise interpretation.
\begin{frame}[t]{Results: classification and selective auditing}
\small
\captionhead{Table 4. Measured-semantic logistic-regression comparator}
{\small\input{content/table-4.tex}\par}
\vspace{2mm}\captionhead{Table 5. 200-rule audit: report coverage with selective accuracy}
{\small\input{content/table-5.tex}\par}
\vspace{2mm}
\begin{columns}[T,onlytextwidth]
\column{.56\textwidth}\centering\input{charts/figure-4.tex}\par
\captext{Figure 4. Held-out outcomes. Rule balanced accuracy and macro-F1 use non-abstained cases.}
\column{.41\textwidth}\card[example]{32 covered / 18 abstained}{Test $n=50$. Classifier accuracy: 0.860 [0.76, 0.94], row-bootstrap 95\% CI.}
\vspace{2mm}\captext{Conflict: among covered cases. Conf. seen: among all cases during resolution. ECE: 10 equal-mass bins.}
\end{columns}
\end{frame}

% 9. Figure 5 embedded in the evidence table; equations remain readable.
\begin{frame}[t]{Results: predicate alignment and robustness}
\small
\begin{columns}[T,onlytextwidth]
\column{.49\textwidth}
\captionhead{Table 6 + Figure 5. Admissible alignment}
{\footnotesize\input{content/table-6.tex}\par}
\vspace{2mm}\captext{Bars: common 0--1 scale. Similarity is not clinician agreement. Valvular and congenital proxies support review only; unsupported predicates remain unmatched.}
\column{.49\textwidth}
\captionhead{Table 7. Perturbations: 12 cases, 48 runs}
{\footnotesize\input{content/table-7.tex}\par}
\vspace{2mm}{\small\input{content/equation-9.tex}\input{content/equation-10.tex}}
\vspace{2mm}\card[alerted]{Orientation sensitivity}{A $2^\circ$ rotation causes the largest drift despite nearly preserved mask counts.}
\vspace{2mm}\captext{$Q$: fixed 12-case set; $\tau$: perturbation; $\varepsilon$: stabilizer. Semantic drift combines units and ranks sensitivity only. Native orientation; no rotation augmentation.}
\end{columns}
\end{frame}

\section{Conclusions and contact}
% 10. Three-color interpretation, complete contacts, supplied supporting logos.
\begin{frame}[t]{Conclusions and author contacts}
\small
\begin{columns}[T,onlytextwidth]
\column{.49\textwidth}
\card[example]{Contribution}{A traceable semantic-to-rule audit chain makes supported evidence and failure visible.}
\vspace{3mm}\card[alerted]{Current limits}{Domain shift, sparse rules, and orientation sensitivity restrict use to research auditing.}
\vspace{3mm}\card{Next validation}{Frozen deep encoders; full WEDD; orientation normalization; vendor recalibration; expert QC and prospective clinician studies.}
\column{.48\textwidth}
\card{Authors and correspondence}{\textbf{Pavlo Radiuk}\textsuperscript{1} (corresponding author)\\\href{mailto:radiukp@khmnu.edu.ua}{radiukp@khmnu.edu.ua}\\[2mm]
\textbf{Oleksander Barmak}\textsuperscript{1}\\\href{mailto:barmako@khmnu.edu.ua}{barmako@khmnu.edu.ua}\\[2mm]
\textbf{Iurii Krak}\textsuperscript{2,3}\\\href{mailto:iurii.krak@knu.ua}{iurii.krak@knu.ua}}
\vspace{3mm}\captext{\textsuperscript{1}Khmelnytskyi National University\\\textsuperscript{2}Taras Shevchenko National University of Kyiv\\\textsuperscript{3}V.M. Glushkov Institute of Cybernetics}
\end{columns}
\vspace{3mm}\captext{Supporting organizations and conference identities supplied with the presentation}
\vspace{2mm}\supportlogos
\end{frame}
\end{document}
''')
print('Rebuilt all 10 frames, 9 tables, 5 figure presentations, and template-based typography.')
