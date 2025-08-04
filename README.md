# NeuroMarkerAI 
### AI-Powered Early Detection of Brain Tumors from Serum Biomarkers  


A machine learning pipeline for non-invasive brain tumor risk prediction using circulating biomarkers (IL-6, VEGF, GFAP, etc.). Includes:  
- Automated data preprocessing  
- Explainable AI (SHAP/LIME)  
- Flask/FastAPI deployment  
- Clinical validation notebooks

```mermaid
graph TD
    A[Serum Samples] --> B(Data Cleaning)
    B --> C{Feature Selection}
    C -->|Top Biomarkers| D[Train Model]
    C -->|SHAP Analysis| E[Explainability]
    D --> F[Deploy as API]
```


![Machine Learning](https://img.shields.io/badge/ML-RandomForest-FF6F00)
![Biomarkers](https://img.shields.io/badge/Biomarkers-IL6_VEGF_GFAP-0077B5)



## Model Interpretability  
SHAP analysis reveals which serum biomarkers drive predictions:  

| Biomarker | Impact Direction | Clinical Relevance |  
|-----------|------------------|--------------------|  
| **IL-6**  | ↑ Tumor Risk     | Linked to inflammation |  
| **GFAP**  | ↑ Tumor Risk     | Glial cell damage marker |  
| **VEGF**  | ↓ Tumor Risk     | Anti-angiogenic effect |  



![SHAP Summary](assets/shap_summary.png) 
