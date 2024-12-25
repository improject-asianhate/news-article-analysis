# 美國反亞裔歧視之新聞文章分析

### **2024 資管專題**

指導老師：李家岩老師、張慈芬老師

團隊成員：邱秉辰、陳定宏、陳郁婷、陳鵬仁、劉正悅、李承軒

---

### 工作空間

- [Google Drive for Project (permission needed)](https://drive.google.com/drive/folders/1oaA9ghmqPmFSD_meWqtYQig7zIvgB1EM?usp=drive_link)

- [Workspace in Notion (permission needed)](https://www.notion.so/bensonchiu/112-2-113-1-60305e2bd1c24fa0837f48e1565cfd6d?pvs=4)

---

### 檔案架構

```
.
├── code/
│   ├── 113-1/
│   │   ├── README.md
│   │   ├── llm_article_processor/
│   │   │   └── ...
│   │   ├── llm_rag_article_processor/
│   │   │   └── ...
│   │   ├── concept_tree_qa/
│   │   │   └── ...
│   │   └── others/
│   │       └── ...
│   └── 112-2/
│       ├── lda/
│       │   └── ...
│       ├── results/
│       │   └── ...
│       ├── word_cloud/
│       │   └── ...
│       ├── wordbook/
│       │   └── ...
│       └── others/
│           └── ....
└── README.md
```

### 113-1

#### 摘要

- 我們透過大型語言模型 (LLMs)、檢索增強生成 (RAG) 與 Graph RAG 技術，回答三大研究問題 
- 我們開發了 InsightLink 系統，主要的兩大功能為「使用 LLM 做新聞文章內容分析」及「互動式資料視覺化儀表板」

#### 程式碼

- LLM 單篇文章分析

  - 分析文章的基本資訊、種族歧視主題、裡面的人物與組織
    - [純 LLM 版](./codes/113-1/llm_article_processor)
    - [LLM + RAG 版](./codes/113-1/llm_rag_article_processor)
  - [分析文章與概念樹的連結](./codes/113-1/concept_tree_qa)

  > :warning: example_articles 的資料夾是空的，文章之後需要自己放進去

- 不同類型文章之間的比較

  - Method 1: [RAG](https://github.com/henrylee0324/comparison_rag)
  - Method 2: [Graph RAG ](https://github.com/imbensonchiu/newspaper-graph-rag)
    - [成果海報（以介紹 Graph RAG 為主）](https://www.canva.com/design/DAGWXKobcfg/vrjacegt4HxFfm-mVTrbnQ/edit?utm_content=DAGWXKobcfg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

- InsightLink 

  - [GitHub Repository](https://github.com/imbensonchiu/insight-link)
    - 前端框架使用 Next.js
    - UI 使用 shadcn 
    - 資料庫使用 Neon   
  - [Demo video](https://drive.google.com/file/d/12sM_1oQ7kaWYBlHilrqn82XbWRaUZtHm/view)

#### 詳細內容

- [113-1 期末報告連結]()

---

### 112-2

#### 摘要

- 我們對亞裔歧視的概念進行探索，建構出相關的概念樹
- 我們運用文字探勘 (LDA 與 Clustering) 對不同維度之間的報導概念差異進行探討

#### 程式碼

- 可從 [112-2](./code/112-2) 找到

#### 期末報告

- [112-2 期末報告連結](https://docs.google.com/presentation/d/1AM99quQ1s88QbL5Se3yBWukyEsYE6JW0z_l-zfxYTT4/edit?usp=sharing)
