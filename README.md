# ⚖️LAiW: A Chinese Legal Large Language Models Benchmark

| [English](https://github.com/Dai-shen/LAiW/blob/main/README.md) | [Chinese](https://github.com/Dai-shen/LAiW/blob/main/README_zh.md)

**LAiW：A Comprehensive Benchmark for Chinese Legal Large Language Models (LLMs)**

🔥 [LAiW Leaderboard](https://huggingface.co/spaces/daishen/SCULAiW)

🔥 [Technical Report](https://arxiv.org/abs/2310.05620)

## News

🔄 **Recent Updates**

- [2024-04-19] Update [Technical Report](https://arxiv.org/abs/2310.05620)

📅 **Earlier News**

- [2024/1/22] Added evaluation results for the general LLMs [Baichuan-7B](https://huggingface.co/baichuan-inc/Baichuan-7B).
- [2024/1/14] Provided more detailed information on the evaluation dataset [here](https://github.com/Dai-shen/LAiW/blob/main/data/README.md), along with the calculation method for the model evaluation metric [SCULAiW](https://huggingface.co/spaces/daishen/SCULAiW).
- [2024/1/12] Further confirmed and improved relevant evaluation results, optimized the layout of the evaluation leaderboard [SCULAiW](https://huggingface.co/spaces/daishen/SCULAiW), and supplemented more detailed information on evaluated models.
- [2024/1/10] Added evaluations for commercial LLMs GPT-4 and general LLMs Llama-7B, Llama13B, [Chinese-LLaMA-13B](https://github.com/ymcui/Chinese-LLaMA-Alpaca).
- [2024/1/2] Announced the scoring mechanism for the legal capabilities of LLMs in [here](#评分机制) and published the evaluation scores for LLMs in [here](#模型得分).
- [2024/1/2] Released test datasets for 14 foundational tasks [here](https://huggingface.co/daishen).
- [2024/1/1] Updated the legal capability evaluation results for [SCULAiW](https://huggingface.co/spaces/daishen/SCULAiW).
- [2024/12/31] Completed legal capability evaluations for mainstream LLMs. During the evaluation process, in addition to the models mentioned earlier, general LLMs [ChatGLM](https://huggingface.co/THUDM/chatglm-6b) and legal LLMs [Lawyer-LLaMA](https://github.com/AndrewZhe/lawyer-llama/tree/main?tab=readme-ov-file), [Fuzi-Mingcha](https://huggingface.co/SDUIRLab/fuzi-mingcha-v1_0), [Wisdom-Interrogatory](https://github.com/zhihaiLLM/wisdomInterrogatory), [LexiLaw](https://github.com/CSHaitao/LexiLaw) were added.
- [2023/10/12] Published the initial version of the [LAiW Technical Report](https://arxiv.org/abs/2310.05620).
- [2023/10/08] Released the first phase evaluation system for LAiW capabilities [here](https://github.com/Dai-shen/LAiW).
- [2023/10/08] Completed the first phase evaluation of the Basic Information Retrieval capabilities of LLMs, including commercial LLMs: ChatGPT; general LLMs: [Llama2](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf), [Ziya-LLaMA](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1), [Chinese-LLaMA](https://github.com/ymcui/Chinese-LLaMA-Alpaca), [Baichuan2](https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat); and legal LLMs: [HanFei](https://github.com/siat-nlp/HanFei), [ChatLaw](https://huggingface.co/JessyTsu1/ChatLaw-13B), [LaWGPT](https://github.com/pengxiao-song/LaWGPT).
- [2023/10/08] Released evaluation scores and calculation methods for legal capabilities and foundational tasks.

## Contents

- [⚖️LAiW: A Chinese Legal Large Language Models Benchmark](#️laiw-a-chinese-legal-large-language-models-benchmark)
  - [News](#news)
  - [Contents](#contents)
    - [Evaluation structure diagram](#evaluation-structure-diagram)
    - [Scores for LLMs](#scores-for-llms)
    - [Tasks](#tasks)
    - [Datasets](#datasets)
    - [Scoring Mechanism](#scoring-mechanism)
    - [Run](#run)
      - [1.Preparation](#1preparation)
      - [2.Output of LLM](#2output-of-llm)
    - [Contributors](#contributors)
    - [Disclaimer](#disclaimer)
    - [Acknowledgements](#acknowledgements)
    - [Cite](#cite)

### Evaluation structure diagram

<img src="https://github.com/Dai-shen/LAiW/blob/main/resources/task_framework_en.png"  width="70%" height="70%"></img>

### Scores for LLMs

According to the calculation method of the large models' [scoring mechanism](#评分机制), we have evaluated 7 mainstream legal large models and 6 general large models at this stage. The model scores are as follows:

| Model | Size | Model Domain | Total Score | BIR | LFI | CLA | Base Model |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| GPT-4 | - | General | 69.63 | 80.92 | 69.27 | 58.69 | - |
| ChatGPT | - | General | 64.09 | 75.99 | 58.32 | 57.96 | - |
| [Baichuan2-Chat](https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat) | 13B | General | 48.04 | 53.67 | 32.03 | 58.40 | - |
| [ChatGLM](https://huggingface.co/THUDM/chatglm-6b) | 6B | General | 47.01 | 51.51 | 37.08 | 52.44 | - |
| [Ziya-LLaMA](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1) | 13B | General | 45.79 | 61.47 | 29.44 | 46.45 | Llama-13B |
| [Fuzi-Mingcha](https://huggingface.co/SDUIRLab/fuzi-mingcha-v1_0) | 6B | Legal | 40.62 | 39.68 | 27.46 | 54.71 | [ChatGLM-6B](https://huggingface.co/THUDM/chatglm-6b) |
| [HanFei](https://github.com/siat-nlp/HanFei) | 7B | Legal | 35.69 | 37.42 | 16.33 | 53.31 | - |
| [LexiLaw](https://github.com/CSHaitao/LexiLaw) | 6B | Legal | 31.31 | 41.32 | 8.88 | 43.73 | [ChatGLM-6B](https://huggingface.co/THUDM/chatglm-6b) |
| [ChatLaw](https://huggingface.co/JessyTsu1/ChatLaw-13B) | 13B | Legal | 25.77 | 58.02 | 12.54 | 6.74 | [Ziya-LLaMA-13B](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1) |
| [Llama2-Chat](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) | 7B | General | 27.76 | 31.86 | 12.77 | 38.64 | - |
| [Lawyer-LLaMA](https://github.com/AndrewZhe/lawyer-llama/tree/main?tab=readme-ov-file) | 13B | Legal | 29.25 | 30.85 | 6.39 | 50.50 | [Chinese-LLaMA-13B](https://github.com/ymcui/Chinese-LLaMA-Alpaca) |
| [Chinese-LLaMA](https://github.com/ymcui/Chinese-LLaMA-Alpaca) | 13B | General | 24.99 | 21.02 | 19.16 | 34.80 | Llama-13B |
| [Chinese-LLaMA](https://github.com/ymcui/Chinese-LLaMA-Alpaca) | 7B | General | 24.91 | 22.32 | 18.25 | 34.16 | Llama-7B |
| [Baichuan](https://github.com/baichuan-inc/Baichuan-7B) | 7B | General | 22.51 | 21.20 | 15.46 | 30.86 | - |
| [LaWGPT](https://github.com/pengxiao-song/LaWGPT) | 7B | Legal | 22.69 | 15.47 | 14.27 | 38.32 | [Chinese-LLaMA-7B](https://github.com/ymcui/Chinese-LLaMA-Alpaca) |
| Llama | 13B | General | 21.00 | 18.51 | 15.08 | 29.40 | - |
| [Wisdom-Interrogatory](https://github.com/zhihaiLLM/wisdomInterrogatory) | 7B | Legal | 18.83 | 12.66 | 10.45 | 33.37 | [Baichuan-7B](https://huggingface.co/baichuan-inc/Baichuan-7B) |
| Llama | 7B | General | 16.35 | 11.12 | 15.40 | 22.54 | - |

The overall scores and scores for each level of legal capability of LLMs are ranked as follows:

![Overall Histogram](https://github.com/Dai-shen/LAiW/blob/main/resources/Overall-histogram.png)
![BIR Histogram](https://github.com/Dai-shen/LAiW/blob/main/resources/BIR-histogram.png)
![LFI Histogram](https://github.com/Dai-shen/LAiW/blob/main/resources/LFI-histogram.png)
![CLA Histogram](https://github.com/Dai-shen/LAiW/blob/main/resources/CLA-histogram.png)


### Tasks

With the joint efforts of **legal experts** and **artificial intelligence experts**, we categorize the Legal Capabilities of LLMs into three levels, ranging from easy to difficult: Basic Information Retrieval (BIR), Legal Foundation Inference (**LFI**), and Cplex Legal Application (**CLA**), totaling 14 foundational tasks. The diagram above shows the structure of these three capability levels.

- Basic Information Retrieval. The capability of LLMs aims to address some fundamental tasks in the field of law that can be directly transferred from NLP, as well as some simple yet crucial pre-tasks in the legal domain. It includes 5 foundational tasks: Legal Article Recommendation (AR), Element Recognition (ER), Named Entity Recognition (NER), Judicial Summarization (JS), and Case Recognition (CR).
- Legal Foundation Inference. This capability aims to test some basic legal applications for LLMs. It includes 6 foundational tasks: Controversial Focus Mining (CFM), Similar Case Matching (SCM), Charge Prediction (CP), prison Term Prediction (PTP), Civil Trial Prediction (CTP), and Legal Question Answering (LQA).
- Legal Foundation Inference. We consider the challenging tasks that LLMs may face, such as complex reasoning in the legal field and aligning with real legal logic. Here, we focus on three tasks: Judicial Reasoning Generation (JRG), Case Understanding (CU), and Legal Consultation (LC).
  
Below is a brief description to each evaluation task.

<table>

  <tr>
  <td>Capability</td>
  <td>Task</td>
  <td>Description</td>
  </tr>

  <tr>
    <td rowspan="5">BIR</td>
    <td>Legal Article Recommendation</td>
    <td>It aims to provide relevant articles based on the description of the case.</td>
  </tr>
  <tr>
    <td>Element Recognition</td>
    <td>It analyzes and assesses each sentence to identify the pivotal elements of the case.</td>
  </tr>
  <tr>
    <td>Named Entity Recognition</td>
    <td>It aims to extract nouns and phrases with legal characteristics from various legal documents.</td>
  </tr>
  <tr>
    <td>Judicial Summarization</td>
    <td>It aims to condense, summarize, and synthesize the content of legal documents.</td>
  </tr>
  <tr>
    <td>Case Recognition</td>
    <td>It aims to determine, based on the relevant description of the case, whether it pertains to a criminal or civil matter.</td>
  </tr>

  <tr>
    <td rowspan="5">LFI</td>
    <td>Controversial Focus Mining</td>
    <td>It aims to extract the logical and interactive arguments between the defense and prosecution in legal documents, which will be analyzed as a key component for the tasks that relate to the case result.</td>
  </tr>
  <tr>
    <td>Similar Case Matching</td>
    <td>It aims to find cases that bear the closest resemblance, which is a core aspect of various legal systems worldwide, as they require consistent judgments for similar cases to ensure the fairness of the law.</td>
  </tr>
  <tr>
    <td>Criminal Judgment Prediction</td>
    <td>It involves predicting the guilt or innocence of the defendant, along with the potential sentencing, based on the results of basic legal NLP, including the facts of the case, the evidence presented, and the applicable law articles. Therefore, it is divided into two types of tasks: Charge Prediction and prison Term Prediction.</td>
  </tr>
  <tr>
    <td>Civil Trial Prediction</td>
    <td>It involves using factual descriptions to predict the judgment of the defendant in response to the plaintiff’s claim, which we should consider the Controversial Focus.</td>
  </tr>
  <tr>
    <td>Legal Question Answering</td>
    <td>It utilizes the model’s legal knowledge to address the national judicial examination, which encompasses various specific legal types.</td>
  </tr>

  <tr>
    <td rowspan="3">CLA</td>
    <td>Judicial Reasoning Generation</td>
    <td>It aims to generate relevant legal reasoning texts based on the factual description of the case. It is a complex reasoning task, because the court requires further elaboration on the reasoning behind the judgment based on the determination of the facts of the case. This task also involves aligning with the logical structure of syllogism in law</td>
  </tr>
  <tr>
    <td>Case Understanding</td>
    <td>It is expected to provide reasonable and compliant answers based on the questions posed regarding the case-related descriptions in the judicial documents, which is also a complex reasoning task.</td>
  </tr>
  <tr>
    <td>Legal Consultation</td>
    <td>It covers a wide range of legal areas and aims to provide accurate, clear, and reliable answers based on the legal questions provided by the different users. Therefore, it usually requires the sum of the aforementioned capabilities to provide professional and reliable analysis.</td>
  </tr>

</table>

### Datasets

We have reorganized and constructed the evaluation datasets for the aforementioned tasks based on existing publicly available Chinese legal datasets. These datasets are collectively referred to as the **Legal Evaluation Dataset (LED)**. We present the evaluation datasets for each foundational task. For more detailed information about the datasets, please refer to [here](https://github.com/Dai-shen/LAiW/blob/main/data/README.md).

<table>

  <tr>
    <td>Level</td>
    <td>Task</td>
    <td>Main Dataset</td>
    <td>Evaluation Dataset</td>
    <td>Data Size</td>
    <td>Category</td>
  </tr>

  <tr>
    <td rowspan="5">BIR</td>
    <td>Legal Article Recommendation</td>
    <td>CAIL-2018</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-ar">legal_ar</a></td>
    <td>1,000</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Element Recognition</td>
    <td>CAIL-2019</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-er">legal_er</a></td>
    <td>1,000</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Named Entity Recognition</td>
    <td>CAIL-2021</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-ner">legal_ner</a></td>
    <td>1040</td>
    <td>named entity recognition</td>
  </tr>
  <tr>
    <td>Judicial Summarization</td>
    <td>CAIL-2020</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-js">legal_js</a></td>
    <td>364</td>
    <td>Text Generation</td>
  </tr>
  <tr>
    <td>Case Recognition</td>
    <td>CJRC</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-cr">legal_cr</a></td>
    <td>2,000</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td rowspan="6">LFI</td>
    <td>Controversial Focus Mining</td>
    <td>LAIC-2021</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-cfm">legal_cfm</a></td>
    <td>306</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Similar Case Matching</td>
    <td>CAIL-2019</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-scm">legal_scm</a></td>
    <td>260</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Charge Prediction</td>
    <td>Criminal-S</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-cp">legal_cp</a></td>
    <td>827</td>
    <td>Classification</td>
  </tr>
  <tr>
  <td>prison Term Prediction</td>
    <td>MLMN</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-ptp">legal_ptp</a></td>
    <td>349</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Civil Trial Prediction</td>
    <td>MSJudeg</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-ctp">legal_ctp</a></td>
    <td>800</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Legal Question Answering</td>
    <td>JEC-QA</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-lqa">legal_lqa</a></td>
    <td>855</td>
    <td>Classification</td>
  </tr>

  <tr>
    <td rowspan="3">CLA</td>
    <td>Judicial Reasoning Generation</td>
    <td>AC-NLG</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-jrg">legal_jrg</a></td>
    <td>834</td>
    <td>Text Generation</td>
  </tr>
  <tr>
    <td>Case Understanding</td>
    <td>CJRC</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-cu">legal_cu</a></td>
    <td>1,054</td>
    <td>Text Generation</td>
  </tr>
  <tr>
    <td>Legal Consultation</td>
    <td>CrimeKgAssitant</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-lc">legal_lc</a></td>
    <td>916</td>
    <td>Text Generation</td>
  </tr>

</table>

### Scoring Mechanism

⭐️ socres for each task
<div align="center">

$$
S_{(Task)} = \begin{cases}
    F1 * 100, & \text{If }\quad Task\quad\in\quad Classification \\
    \frac{1}{3}*(R1 + R2 + RL) * 100, & \text{If }\quad Task \quad\in\quad Text\quad Generation \\
    Acc * 100, & \text{If }\quad Task\quad\in\quad NER
\end{cases}
$$

</div>

Currently, our evaluation benchmarks mainly consist of three types of tasks: classification tasks, text generation tasks and named entity recognition. For classification tasks, we use the F1 score. For text generation tasks, we use the average of Rouge1, Rouge2, and RougeL scores. Specifically, for legal Named Entity Recognition tasks, we use the extraction accuracy of legal entities as their score.

🌟 Scores for each LLM

For individual LLM, we first calculate the average score of tasks at each level as its legal capability score for that level. Then, we take the average of these three legal capability scores as the final evaluation score for the LLM. Model evaluation scores can be found [here](#模型得分).

### Run

We will continue to evaluate the performance of existing LLMs on these tasks according to the structure diagram of the 14 foundational tasks. For details, please refer to the [leaderboard](https://huggingface.co/spaces/daishen/SCULAiW).


#### 1.Preparation

```bash
git clone git clone https://github.com/Dai-shen/LAiW.git --recursive
cd LAiW
pip install -r requirements.txt
cd LAiW/src/financial-evaluation
pip install -e .[multilingual]
```

#### 2.Output of LLM

We select the model and legal tasks to be evaluated. By running the following code, we can obtain the model's output.

```bash
export CUDA_VISIBLE_DEVICES="1,2"
python eval.py \
    --model "hf-causal-experimental" \
    --model_args "use_accelerate=True,pretrained=$pretrained_model,tokenizer=$pretrained_model,use_fast=False,trust_remote_code=True" \
    --tasks "legal_ar,legal_er,legal_js" \
    --no_cache \
    --num_fewshot 0 \
    --write_out \
    --output_base_path ""
```

Parameter Description

- `model`: Model interface type, optional parameters can be found in `src/financial-evaluation/lm_eval/models/__init__.py`
- `tasks`: Predefined task names, you can define your own tasks in `src/tasks/_init_.py` and `src/tasks/legal.py`
- `pretrained_model`: Path to the large model (Hugging Face space or local model path)
- `output_base_path`: Model saving path

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

### Cite

If this project has been helpful to your research, please consider citing our project.

```
@article{dai2023laiw,
  title={LAiW: A Chinese legal large language models benchmark (a technical report)},
  author={Dai, Yongfu and Feng, Duanyu and Huang, Jimin and Jia, Haochen and Xie, Qianqian and Zhang, Yifang and Han, Weiguang and Tian, Wei and Wang, Hao},
  journal={arXiv preprint arXiv:2310.05620},
  year={2023}
}
```
