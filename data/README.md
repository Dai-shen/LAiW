### Original Dataset

We have conducted research on existing publicly available legal datasets and compiled approximately 600k records. These primarily cover criminal and civil cases, and also include cases related to constitutional law, social law, economic law, and other legal areas.

|        Dataset        | Size | Domain |  Task   |    Metric      |
|:---------------------------:|:-----:|:----:|:-------:|:--------------:|
|       CAIL2018        |   196k   |   Criminal  |  Multi-classification  |     Acc, F1      |
|     CAIL-2019-ER      |      69k  |  Civil  |  Multi-classification  |   Acc, F1    |
|     CAIL-2021-IE      |     5k |   Criminal  | Named Entity Recognition  |    F1, P, R    |
| Criminal-S            |   77k   |  Criminal  | Multi-classification  | Acc, P, R, F1  |
| MLMN                  |   1k  |   Criminal  |   Multi-classification   |    P, R, F1    |
| MSJudeg               |   70k |   Civil  |   Multi-classification   | F1  |
|        CAIL2019-SCM   |    9k  |   Civil  |   Classification   |      Acc       |
| CAIL2020-AM           |  815  |   Criminal, Civil |   Multiple-choice questions   |      Acc       |
|           JEC-QA      |  20k |  -  |   Multiple-choice questions   |      Acc       |
| CAIL-2020-TS          |   9k  |   Civil  |  Text summarization  |     ROUGE      |
| CAIL-2022-TS          |   6k  |   -   |  Text summarization   |     ROUGE      |
|          AC-NLG       |   67k  |  Civil  |  Text Generation   |     ROUGE, BLEU      |
|            CJRC       |   10k  |   Criminal, Civil  |   Text    |       ROUGE, BLEU       |
|  CrimeKgAssitant      |   52k |  - | Question-answering | ROUGE, BLEU |

1. [CAIL2018](https://github.com/thunlp/CAIL): The dataset for criminal judgment prediction in CAIL2018 aims to predict the relevant legal provisions, charges against the defendant, and the length of the defendant's sentence based on the factual descriptions and case facts in criminal legal documents.

2. [CAIL-2019-ER](https://github.com/china-ai-law-challenge/CAIL2019): The dataset for criminal judgment prediction in CAIL-2019 requires systems to judge each sentence in judicial documents and identify key case elements. This task involves three domains: marriage and family, labor disputes, and loan contracts.

3. [CAIL-2021-IE](https://github.com/isLouisHsu/CAIL2021-information-extraction/tree/master): Information extraction involves tasks such as named entity recognition and relation extraction. This task focuses on fraud cases and requires precise extraction of key information such as suspects, items involved, and criminal facts.

4. [Criminal-S](https://github.com/thunlp/attribute_charge): Each sample in this dataset contains a single charge and aims to predict the relevant charges judged by judges based on the factual determination part of the case.

5. [MLMN](https://github.com/gjdnju/MLMN): This task categorizes sentences into five parts based on the length of the sentence: no criminal punishment, detention, imprisonment for less than 1 year, imprisonment for 1 year or more but less than 3 years, and imprisonment for 3 years or more but less than 10 years. The task involves traffic accident and intentional injury cases, predicting the category of the defendant's sentence based on legal documents.

6. [MSJudeg](https://github.com/mly-nlp/LJP-MSJudge): This task involves civil data on private lending disputes and aims to predict the judge's verdict based on the case facts and the plaintiff's claims.

7. [CAIL2019-SCM](https://github.com/china-ai-law-challenge/CAIL2019/tree/master/scm): This task involves calculating and judging the similarity of multiple legal documents. Specifically, given the title and factual description of each document, participants need to find the most similar document from a candidate set for each query document.

8. [CAIL2020-AM](https://github.com/china-ai-law-challenge/CAIL2020/tree/master/lbwj): This task aims to extract logical interaction arguments between defense and prosecution in judgment documents, i.e., points of contention.

9. [JEC-QA](https://jecqa.thunlp.org/): As a dataset for objective question and answer in the national judicial examination, it contains 7775 knowledge-driven questions and 13297 case analysis questions, each of which is a multiple-choice question or a multiple-choice question.

10. [CAIL-2020-TS](http://cail.cipsc.org.cn/task_summit.html?raceID=1&cail_tag=2020): This task involves generating judicial summary texts based on the original judgment documents.

11. [CAIL-2022-TS](https://github.com/china-ai-law-challenge/CAIL2022/tree/main/sfzy): This task involves generating correct, complete, and concise legal sentiment summaries based on original public opinion texts.

12. [AC-NLG](https://github.com/wuyiquan/AC-NLG): This task involves civil data related to private lending and aims to predict relevant court reasoning texts based on factual descriptions of cases.

13. [CJRC](https://github.com/china-ai-law-challenge/CAIL2019/tree/master): As a dataset for judicial reading comprehension, it contains 10,000 cases and 50,000 question-answer pairs, aiming to provide a substantive understanding of legal documents and answer related questions.

14. [CrimeKgAssitant](https://github.com/liuhuanyong/CrimeKgAssitant): A dataset of real Chinese lawyer consultations, cleaned by LAW-GPT, resulting in 52k single-turn question-answer pairs.

### Instruction Datasets

According to the comprehensive benchmark framework LAiW for Chinese legal LLMs, consisting of 14 basic tasks, we constructed the Legal Instruction Tuning Dataset (LIT). The dataset is available at [Legal Instruction Tuning Dataset (LIT)](https://huggingface.co/datasets/daishen/LIT). The dataset is split with a ratio of `train/valid/test=7/1/2`. The `train.jsonl` and `valid.jsonl` files are used for model training, while `test.jsonl` serves as the evaluation dataset for LAiW to guide and advance the development and evaluation of LLMs. (At the current stage, only the test datasets `test.jsonl` for each task are publicly available, which can be downloaded from [LAiW](https://github.com/Dai-shen/LAiW)).

<table>

  <tr>
    <td>Level</td>
    <td>Task</td>
    <td>Main Dataset</td>
    <td>Instruction Dataset</td>
    <td>Size</td>
    <td>Type</td>
  </tr>

  <tr>
    <td rowspan="5">BIR</td>
    <td>Legal Article Recommendation</td>
    <td>CAIL-2018</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_ar">legal_ar</a></td>
    <td>5k</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Element Recognition</td>
    <td>CAIL-2019</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_er">legal_er</a></td>
    <td>5k</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Named Entity Recognition</td>
    <td>CAIL-2021</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_ner">legal_ner</a></td>
    <td>5,195</td>
    <td>Named Entity Recognition</td>
  </tr>
  <tr>
    <td>Judicial Summarization</td>
    <td>CAIL-2020</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_js">legal_js</a></td>
    <td>1,814</td>
    <td>Text Generation</td>
  </tr>
  <tr>
    <td>Case Recognition</td>
    <td>CJRC</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_cr">legal_cr</a></td>
    <td>10k</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td rowspan="6">LFI</td>
    <td>Controversial Focus Mining</td>
    <td>Private</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_cfm">legal_cfm</a></td>
    <td>1,525</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Similar Case Matching</td>
    <td>CAIL-2019</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_scm">legal_scm</a></td>
    <td>1.3k</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Charge Prediction</td>
    <td>Criminal-S</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_cp">legal_cp</a></td>
    <td>4,133</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>prison Term Prediction</td>
    <td>MLMN</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_ptp">legal_ptp</a></td>
    <td>1,743</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Civil Trial Prediction</td>
    <td>MSJudeg</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_ctp">legal_ctp</a></td>
    <td>4k</td>
    <td>Classification</td>
  </tr>
  <tr>
    <td>Legal Question Answering</td>
    <td>JEC-QA</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_lqa">legal_lqa</a></td>
    <td>4,271</td>
    <td>Classificationn</td>
  </tr>

  <tr>
    <td rowspan="3">CLA</td>
    <td>Judicial Reasoning Generation</td>
    <td>AC-NLG</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_jrg">legal_jrg</a></td>
    <td>4,169</td>
    <td>Text Generation</td>
  </tr>
  <tr>
    <td>Case Understanding</td>
    <td>CJRC</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_cu">legal_cu</a></td>
    <td>5,265</td>
    <td>Text Generation</td>
  </tr>
  <tr>
    <td>Legal Consultation</td>
    <td>CrimeKgAssitant</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_lc">legal_lc</a></td>
    <td>4,575</td>
    <td>Text Generation</td>
  </tr>

</table>
