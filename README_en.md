# ⚖️LAiW: A Chinese Legal Large Language Models Benchmark

| [English](https://github.com/Dai-shen/LAiW/blob/main/README_en.md) | [中文](https://github.com/Dai-shen/LAiW/blob/main/README.md)

**LAiW：A Comprehensive Benchmark for Chinese Legal Large Language Models (LLMs)**

🔥 [LAiW Leaderboard](https://huggingface.co/spaces/daishen/LAiW)

🔥 [Technical Report](https://arxiv.org/abs/2310.05620)

## News

💻 **Recent Updates** **[2023/10/12]**

- Open-sourcing the [Technical Report](https://arxiv.org/abs/2310.05620)

💻 **Earlier News** **[2023/10/08]**

- Publish the [LAiW](https://github.com/Dai-shen/LAiW) capability evaluation framework.
- The evaluation work for the first phase of LLMs on the capability of basic legal NLP has been completed. It includes general LLMs: ChatGPT, [Llama2](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf), [Ziya-LLaMA](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1), [Chinese-LLaMA](https://github.com/ymcui/Chinese-LLaMA-Alpaca), [Baichuan2](https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat); as well as legal LLMs: [HanFei](https://github.com/siat-nlp/HanFei), [ChatLaw](https://huggingface.co/JessyTsu1/ChatLaw-13B), [LawGPT](https://github.com/pengxiao-song/LaWGPT).
- The calculation method for evaluating scores of legal competence and basic tasks.

## Contents

- [⚖️LAiW: A Chinese Legal Large Language Models Benchmark](#️laiw-a-chinese-legal-large-language-models-benchmark)
  - [News](#news)
  - [Contents](#contents)
    - [Evaluation structure diagram](#evaluation-structure-diagram)
    - [Tasks](#tasks)
    - [Datasets](#datasets)
    - [Scoring Mechanism](#scoring-mechanism)
    - [Evaluation](#evaluation)
      - [Preparation](#preparation)
      - [Automated Assessment](#automated-assessment)
    - [Contributors](#contributors)
    - [Disclaimer](#disclaimer)
    - [Acknowledgements](#acknowledgements)

### Evaluation structure diagram

<img src="https://github.com/Dai-shen/LAiW/blob/main/resources/task_framework_en.png"  width="70%" height="70%"></img>

### Tasks

With the joint efforts of **legal experts** and **artificial intelligence experts**, we categorize the Legal Capabilities of LLMs into three levels, ranging from easy to difficult: the capability of basic legal NLP, the capability of basic legal application, and the capability of complex legal application, totaling 13 foundational tasks. The diagram above shows the structure of these three capability levels.

- The capability of basic legal NLP. The capability of LLMs aims to address some fundamental tasks in the field of law that can be directly transferred from NLP, as well as some simple yet crucial pre-tasks in the legal domain. It includes 5 foundational tasks: Legal Article Recommendation (AR), Element Recognition (ER), Named Entity Recognition (NER), Judicial Summarization (JS), and Case Recognition (CR).
- The capability of basic legal application. This capability aims to test some basic legal applications for LLMs. It includes 5 foundational tasks: Controversial Focus Mining (CFM), Similar Case Matching (SCM), Criminal Judgment Prediction (CJP), Civil Trial Prediction (CTP), and Legal Question Answering (LQA).
- The capability of complex legal application. We consider the challenging tasks that LLMs may face, such as
complex reasoning in the legal field and aligning with real legal logic. Here, we focus on three tasks: Judicial Reasoning Generation (JRG), Case Understanding (CU), and Legal Consultation (LC).
  
Below is a brief description to each evaluation task.

<table>

  <tr>
  <td>Capability</td>
  <td>Task</td>
  <td>Description</td>
  </tr>

  <tr>
    <td rowspan="5">The capability of basic legal NLP</td>
    <td>AR</td>
    <td>Legal Article Recommendation aims to provide relevant articles based on the description of the case.</td>
  </tr>
  <tr>
    <td>ER</td>
    <td>Element Recognition analyzes and assesses each sentence to identify the pivotal elements of the case.</td>
  </tr>
  <tr>
    <td>NER</td>
    <td>Named Entity Recognition aims to extract nouns and phrases with legal characteristics from various legal documents.</td>
  </tr>
  <tr>
    <td>JS</td>
    <td>Judicial Summarization aims to condense, summarize, and synthesize the content of legal documents.</td>
  </tr>
  <tr>
    <td>CR</td>
    <td>Case Recognition aims to determine, based on the relevant description of the case, whether it pertains to a criminal or civil matter.</td>
  </tr>

  <tr>
    <td rowspan="5">The capability of basic legal application</td>
    <td>CFM</td>
    <td>Controversial Focus Mining aims to extract the logical and interactive arguments between the defense and prosecution in legal documents, which will be analyzed as a key component for the tasks that relate to the case result.</td>
  </tr>
  <tr>
    <td>SCM</td>
    <td>Similar Case Matching aims to find cases that bear the closest resemblance, which is a core aspect of various legal systems worldwide, as they require consistent judgments for similar cases to ensure the fairness of the law.</td>
  </tr>
  <tr>
    <td>CJP</td>
    <td>Criminal Judgment Prediction task involves predicting the guilt or innocence of the defendant, along with the potential sentencing, based on the results of basic legal NLP, including the facts of the case, the evidence presented, and the applicable law articles.</td>
  </tr>
  <tr>
    <td>CTP</td>
    <td>Civil Trial Prediction task involves using factual descriptions to predict the judgment of the defendant in response to the plaintiff’s claim, which we should consider the Controversial Focus.</td>
  </tr>
  <tr>
    <td>LQA</td>
    <td>Legal Question Answering utilizes the model’s legal knowledge to address the national judicial examination, which encompasses various specific legal types.</td>
  </tr>

  <tr>
    <td rowspan="3">The capability of complex legal application</td>
    <td>JRG</td>
    <td>Judicial Reasoning Generation aims to generate relevant legal reasoning texts based on the factual description of the case. It is a complex reasoning task, because the court requires further elaboration on the reasoning behind the judgment based on the determination of the facts of the case. This task also involves aligning with the logical structure of syllogism in law</td>
  </tr>
  <tr>
    <td>CU</td>
    <td>Case Understanding is expected to provide reasonable and compliant answers based on the questions posed regarding the case-related descriptions in the judicial documents, which is also a complex reasoning task.</td>
  </tr>
  <tr>
    <td>LC</td>
    <td>Legal Consultation covers a wide range of legal areas and aims to provide accurate, clear, and reliable answers based on the legal questions provided by the different users. Therefore, it usually requires the sum of the aforementioned capabilities to provide professional and reliable analysis.</td>
  </tr>

</table>

### Datasets

Based on existing publicly available datasets of Chinese law, we have reorganized and constructed evaluation datasets for each of the aforementioned tasks, called the **Legal Evaluation Dataset (LED)**. In the future, we will merge and release the **LED** dataset together with corresponding fine-tuning datasets [LAiW-DataSet](https://github.com/Dai-shen/LAiW-DataSet) that can be used for training LLMs. Currently, we are only presenting the evaluation datasets from LED that are used for assessing the foundational tasks in the first phase.

<table>

  <tr>
    <td>Capability</td>
    <td>Task</td>
    <td>Main Dataset</td>
    <td>Evaluation Dataset</td>
    <td>Data Size</td>
  </tr>

  <tr>
    <td rowspan="5">The capability of basic legal NLP</td>
    <td>AR</td>
    <td>CAIL-2018</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-ar">legal_ar</a></td>
    <td>1,000</td>
  </tr>
  <tr>
    <td>ER</td>
    <td>CAIL-2019</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-er">legal_er</a></td>
    <td>1,000</td>
  </tr>
  <tr>
    <td>NER</td>
    <td>CAIL-2021</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>JS</td>
    <td>CAIL-2020</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-js">legal_js</a></td>
    <td>364</td>
  </tr>
  <tr>
    <td>CR</td>
    <td>CJRC</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-cr">legal_cr</a></td>
    <td>2,000</td>
  </tr>

  <tr>
    <td rowspan="5">The capability of basic legal application</td>
    <td>CFM</td>
    <td>Undisclosed</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>SCM</td>
    <td>CAIL-2019</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CJP</td>
    <td>Criminal-S<br>MLMN</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CTP</td>
    <td>MSJudeg</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>LQA</td>
    <td>JEC-QA</td>
    <td></td>
    <td></td>
  </tr>

  <tr>
    <td rowspan="3">The capability of complex legal application</td>
    <td>JRG</td>
    <td>AC-NLG</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>CU</td>
    <td>CJRC</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>LC</td>
    <td>CrimeKgAssitant</td>
    <td></td>
    <td></td>
  </tr>

</table>

### Scoring Mechanism

📚 V1.0：

- For each specific basic task, we currently use F1 score for classification tasks and ROUGE-1 for text generation tasks to calculate automated evaluation scores, which represent the performance for LLMs on that task (evaluation metric values range between 0 and 1).
- For each evaluation capability, we will allocate task difficulty weights based on the assessments of legal experts. The scores on each task will be weighted and averaged to determine the overall capability score.

### Evaluation

- We will continue to evaluate the performance of existing LLMs on these basic tasks outlined in the evaluation framework diagram. For more details, please refer to our [LAiW Leaderboard](https://huggingface.co/spaces/daishen/LAiW)。
- Currently, the evaluation code supports commercial models like ChatGPT, as well as open-source general LLMs such as [Baichuan2](https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat), [chatglm2](https://huggingface.co/THUDM/chatglm2-6b). Additionally, we have also assessed three Chinese Legal LLMs sunch as [HanFei](https://github.com/siat-nlp/HanFei), [Lawyer LLaMa](https://github.com/AndrewZhe/lawyer-llama/tree/main), and [智海-录问](https://modelscope.cn/models/wisdomOcean/wisdomInterrogatory/summary).

#### Preparation

```bash
git clone git clone https://github.com/Dai-shen/LAiW.git --recursive
cd LAiW
pip install -r requirements.txt
cd LAiW/src/financial-evaluation
pip install -e .[multilingual]
```

#### Automated Assessment

```bash
python eval.py \
    --model "hf-causal-experimental" \
    --model_args "use_accelerate=True,pretrained=baichuan-inc/Baichuan2-13B-Chat,tokenizer=baichuan-inc/Baichuan2-13B-Chat,use_fast=False" \
    --tasks "legal_ar,legal_er,legal_ner"
```

### Contributors

- Sichuan University: Yongfu Dai, Duanyu Feng, Haochen Jia, Yifang Zhang and Hao Wang
- Wuhan University: Qianqian Xie, Weiguang Han and [Jimin Huang](https://jimin.chancefocus.com/)
- Southwest Petroleum University: Wei Tian

### Disclaimer

This project is provided for academic and educational purposes only. We do not take responsibility for any issues, risks, or adverse consequences that may arise from the use of this project.

### Acknowledgements

This project is built upon the following open-source projects, and we are really thankful for them:

- [**LLMindCraft**](https://github.com/XplainMind/LLMindCraft)
- [**Awesome Chinese Legal Resources**](https://github.com/pengxiao-song/awesome-chinese-legal-resources)
