### 原始数据集

我们调研现有公开法律数据集，整理得到约 60w 条数据，主要涵盖了刑事案件和民事案件，同时也包含了涉及宪法相关法、社会法、经济法等法律的案件

|        数据集         | 数据集大小 | 法律领域 |  任务类型   |      评价指标      |
|:---------------------------:|:-----:|:----:|:-------:|:--------------:|
|       CAIL2018        |   196k   |   刑事  |  多标签分类  |     Acc, F1      |
|     CAIL-2019-ER      |      69k  |  民事  |  多标签分类  |   Acc, F1    |
|     CAIL-2021-IE      |     5k |   刑事  | 命名实体识别  |    F1, P, R    |
| Criminal-S            |   77k   |  刑事  |   多分类   | Acc, P, R, F1  |
| MLMN                  |   1k  |   刑事  |   多分类   |    P, R, F1    |
| MSJudeg               |   70k |   民事  |   多分类   | F1  |
|        CAIL2019-SCM   |    9k  |   民事  |   分类   |      Acc       |
| CAIL2020-AM           |  815  |   刑事, 民事 |   选择题   |      Acc       |
|           JEC-QA      |  20k |  -  |   选择题   |      Acc       |
| CAIL-2020-TS          |   9k  |   民事   |  文本摘要   |     ROUGE      |
| CAIL-2022-TS          |   6k  |   -   |  文本摘要   |     ROUGE      |
|          AC-NLG       |   67k  |  民事  |  文本生成   |     ROUGE, BLEU      |
|            CJRC       |   10k  |   刑事, 民事  |   文本问答   |       ROUGE, BLEU       |
|  CrimeKgAssitant      |   52k |  - | 文本问答 | ROUGE, BLEU |

1. [CAIL2018](https://github.com/thunlp/CAIL)：作为 CAIL2018 刑事判决预测的数据集，旨在根据刑事法律文书中的案情描述和事实部分，预测本案涉及的相关法条，被告人被判的罪名和被告人的刑期长短
2. [CAIL-2019-ER](https://github.com/china-ai-law-challenge/CAIL2019)：刑事判决预测的数据集 给定司法文书中的相关段落，系统需针对文书中每个句子进行判断，识别其中的关键案情要素。本任务共涉及三个领域，包括婚姻家庭、劳动争议、借款合同等领域
3. [CAIL-2021-IE](https://github.com/isLouisHsu/CAIL2021-information-extraction/tree/master)：信息抽取是自然语言处理中一类基础任务，涉及命名实体识别与关联抽取等多类子任务。本任务涉及诈骗罪，主要体现为对于案件关键信息如嫌疑人、涉案物品、犯罪事实等关键信息的精确抽取
4. [Criminal-S](https://github.com/thunlp/attribute_charge)：该数据集每条样本只包含单个罪名，旨在根据案件的事实认定部分预测法官判决的相关罪名
5. [MLMN](https://github.com/gjdnju/MLMN)：该任务将刑期按照时间长短分为五个部分，分别为免予刑事处罚、拘役、1年以下有期徒刑、1年及1年以上，3年以下有期徒刑和3年及3年以上，10年以下有期徒刑。任务涉及交通肇事罪和故意伤害罪，旨在根据法律文书预测被告人的刑期类别
6. [MSJudeg](https://github.com/mly-nlp/LJP-MSJudge)：本任务是一个私人借贷纠纷的民事数据集，旨在根据案件事实描述和根据原告的诉请，预测法官的裁判结果
7. [CAIL2019-SCM](https://github.com/china-ai-law-challenge/CAIL2019/tree/master/scm)：本任务是针对多篇法律文书进行相似度的计算和判断。具体来说，对于每份文书我们提供文书的标题和事实描述，选手需要从两篇候选集文书中找到与询问文书更为相似的一篇文书
8. [CAIL2020-AM](https://github.com/china-ai-law-challenge/CAIL2020/tree/master/lbwj)：本任务旨在抽取出裁判文书中辩方诉方之间的逻辑交互论点对，即争议焦点
9. [JEC-QA](https://jecqa.thunlp.org/)：作为国家司法考试的客观题问答数据集，包含 7775 个知识驱动问题和 13297 个案情分析问题，本任务的每个问题均为单选题或者多选题
10. [CAIL-2020-TS](http://cail.cipsc.org.cn/task_summit.html?raceID=1&cail_tag=2020)：本任务是根据裁判文书原文输出对应的司法摘要文本
11. [CAIL-2022-TS](https://github.com/china-ai-law-challenge/CAIL2022/tree/main/sfzy)：本任务是利用原始舆情文本输出对应的正确、完整、简洁的涉法舆情摘要
12. [AC-NLG](https://github.com/wuyiquan/AC-NLG)：本任务是涉及私人借贷的民事数据，旨在根据案情的事实描述预测相关的法院说理文本
13. [CJRC](https://github.com/china-ai-law-challenge/CAIL2019/tree/master)：作为司法阅读理解的数据集，包含 1w 个案件和 50k 个问答对，旨在根据法律文书进行实质性的要点理解，回答相关问题
14. [CrimeKgAssitant](https://github.com/liuhuanyong/CrimeKgAssitant)：真实的中文律师对于用户法律咨询的数据集，[LAW-GPT](https://github.com/LiuHC0428/LAW-GPT) 利用ChatGPT清洗后得到52k单轮问答

### 指令微调数据集

根据中文法律大模型综合性基准 [LAiW](https://github.com/Dai-shen/LAiW) 评测框架的 <strong>13</strong> 项基础任务，构造法律指令微调数据集 [Legal Instruction Tuning Dataset (LIT)](https://huggingface.co/datasets/daishen/LIT)。数据集划分比例 `train/valid/test=7/1/2`，其中 `train.jsonl` 和 `vaild.jsonl` 用作模型训练，`test.jsonl` 作为 [LAiW](https://github.com/Dai-shen/LAiW) 的评测数据集，以引导和推进大模型开发和评测工作。（当前阶段仅公开每个任务的测试数据集 `test.jsonl`，可在 [LAiW](https://github.com/Dai-shen/LAiW) 下载）
<table>

  <tr>
    <td>能力层级</td>
    <td>任务</td>
    <td>主要数据集</td>
    <td>指令微调数据集</td>
    <td>数据集大小</td>
    <td>类别</td>
  </tr>

  <tr>
    <td rowspan="5">法律NLP基础能力</td>
    <td>法条推送</td>
    <td>CAIL-2018</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_ar">legal_ar</a></td>
    <td>5k</td>
    <td>分类</td>
  </tr>
  <tr>
    <td>要素识别</td>
    <td>CAIL-2019</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_er">legal_er</a></td>
    <td>5k</td>
    <td>分类</td>
  </tr>
  <tr>
    <td>命名实体识别</td>
    <td>CAIL-2021</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_ner">legal_ner</a></td>
    <td>5,195</td>
    <td>命名实体识别</td>
  </tr>
  <tr>
    <td>司法要点摘要</td>
    <td>CAIL-2020</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_js">legal_js</a></td>
    <td>1,814</td>
    <td>文本生成</td>
  </tr>
  <tr>
    <td>案件识别</td>
    <td>CJRC</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_cr">legal_cr</a></td>
    <td>10k</td>
    <td>分类</td>
  </tr>
  <tr>
    <td rowspan="6">法律知识理解能力</td>
    <td>争议焦点挖掘</td>
    <td>Private</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_cfm">legal_cfm</a></td>
    <td>1,525</td>
    <td>分类</td>
  </tr>
  <tr>
    <td>类案匹配</td>
    <td>CAIL-2019</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_scm">legal_scm</a></td>
    <td>1.3k</td>
    <td>分类</td>
  </tr>
  <tr>
    <td rowspan="2">刑事判决预测</td>
    <td>Criminal-S</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_cp">legal_cp</a></td>
    <td>4,133</td>
    <td>分类</td>
  </tr>
  <tr>
    <td>MLMN</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_ptp">legal_ptp</a></td>
    <td>1,743</td>
    <td>分类</td>
  </tr>
  <tr>
    <td>民事裁判预测</td>
    <td>MSJudeg</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_ctp">legal_ctp</a></td>
    <td>4k</td>
    <td>分类</td>
  </tr>
  <tr>
    <td>法律问答</td>
    <td>JEC-QA</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_lqa">legal_lqa</a></td>
    <td>4,271</td>
    <td>分类</td>
  </tr>

  <tr>
    <td rowspan="3">法律知识应用能力</td>
    <td>司法说理生成</td>
    <td>AC-NLG</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_jrg">legal_jrg</a></td>
    <td>4,169</td>
    <td>文本生成</td>
  </tr>
  <tr>
    <td>案情理解</td>
    <td>CJRC</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_cu">legal_cu</a></td>
    <td>5,265</td>
    <td>文本生成</td>
  </tr>
  <tr>
    <td>法律咨询</td>
    <td>CrimeKgAssitant</td>
    <td><a href="https://huggingface.co/datasets/daishen/LIT/tree/main/legal_lc">legal_lc</a></td>
    <td>4,575</td>
    <td>文本生成</td>
  </tr>

</table>
