variable X

| Feature                | What you collect                              |
| ---------------------- | --------------------------------------------- |
| Polymer concentration  | e.g., 5% w/v, 10% w/v                         |
| Gelatin concentration  | e.g., 5% w/v, 10% w/v                         |
| Crosslinker            | EDC, genipin, UV, etc.                        |
| Crosslinking condition | concentration, time, temperature, UV exposure |
| Pore size              | μm                                            |
| Porosity               | %                                             |
| Water uptake           | %                                             |
| Fabrication method     | 3D printing, freeze-drying, casting, etc.     |
| Stiffness              | kPa — **I strongly recommend adding this**    |
| Material/polymer type  | Gelatin, GelMA, gelatin+alginate, etc.        |


dataset could start as:

Paper_ID
Scaffold_ID
Polymer
Polymer_concentration
Gelatin_concentration
Crosslinker
Crosslinking_condition
Fabrication_method
Pore_size_um
Porosity_pct
Water_uptake_pct
Stiffness_kPa



hepaticc-fun targets Y

| Target            | Meaning                      |
| ----------------- | ---------------------------- |
| Cell viability    | Whether hepatocytes survive  |
| Albumin secretion | Hepatic synthetic function   |
| Urea production   | Hepatic metabolic function   |
| CYP3A4 activity   | Drug-metabolism function     |
| CYP1A2 activity   | Drug-metabolism function     |
| ALB expression    | Hepatocyte function/identity |
| CYP3A4 expression | Metabolic function           |
| HNF4α expression  | Hepatocyte phenotype         |


I would initially focus on:

Y1 = Viability
Y2 = Albumin
Y3 = Urea
Y4 = CYP3A4


build separate regression models:

Scaffold properties
       ↓
 ┌───────────────┐
 │ ML model      │
 └───────────────┘
       ↓
Albumin
Urea
CYP3A4
Viability



Example of one ML record:
Polymer = Gelatin
Polymer concentration = 10 %
Gelatin concentration = 10 %
Crosslinker = EDC
Crosslinking condition = 15 mM, 1 hour
Fabrication = Extrusion 3D printing
Pore size = 700 μm
Porosity = 65 %
Water uptake = 450 %
Stiffness = 3.2 kPa

Hepatocyte viability = 91 %
Albumin = 125 ng/mL
Urea = 42 μg/mL
CYP3A4 = 78 %



That becomes one experimental scaffold condition / row.

Polymer concentration ─┐
Gelatin concentration ─┤
Crosslinker ───────────┤
Crosslinking condition ┤
Pore size ─────────────┤
Porosity ──────────────┤──→ ML ──→ Albumin
Water uptake ──────────┤          Urea
Fabrication ───────────┤          CYP3A4
Stiffness ─────────────┘          Viability


Don't make "hepatic liver function" a single arbitrary number initially. --->Albumin + Urea + CYP activity + Viability

Instead, retain the actual experimental endpoints:

Albumin + Urea + CYP activity + Viability

research question --
Can machine-learning models predict hepatic cellular function from the physicochemical and fabrication properties of engineered 3D liver scaffolds?

pipeline --

Literature
   ↓
Extract scaffold properties
   ↓
Extract hepatic experimental outcomes
   ↓
Standardize units
   ↓
Data cleaning
   ↓
EDA
   ↓
PCA / clustering
   ↓
ML regression
   ↓
SVR / Random Forest / XGBoost
   ↓
Albumin / Urea / CYP3A4 / Viability prediction
   ↓
SHAP / feature importance
   ↓
Identify important scaffold properties
   ↓
Candidate scaffold design



