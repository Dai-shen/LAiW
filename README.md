# SCULaiw: Legal Evaluation Framework (BIAN)

狴犴：中文法律大模型综合性基准

## 任务评估结构图

<img src="https://github.com/Dai-shen/SCULaiw/blob/main/resources/task_framwork.png"  width="50%" height="50%"></img>

### 总榜单

|  排名  | 模型 | 模型类别 | 机构 | 总分 | 语言理解能力 | 法律应用能力 |
|:----:| :----:| :----: | :----:| :----: | :----: | :----: |
|  -   | gpt4 | 通用 | OpenAI | - | - | - |
| -    | gpt-3.5-turbo | 通用 | OpenAI | - | - | - |
|  -   | ChatLaw | 法律 | Peking University | - | - | - |
|  -   | Zhihai-Luwen | 法律 | ZJU, Alibaba, e.t. | - | - | - |
|  -   | LaWGPT | 法律 | Personal Team | - | - | - |
|  -   | Lawyer LLaMA | 法律 | Peking University team | - | - | - |
|  -   | LexiLaw | 法律 | Tsinghua IR Group | - | - | - |
| -  |  fuzi.mingcha | 法律 | SDU, CUPL, e.t.| -  | - | - |
|  -   | internlm-chat | 通用 | InternLM Team | - | - | - |
|  -   | baichuan | 通用 | Baichuan Inc. | - | - | - |
|  -   | chatglm | 通用 | Tsinghua & Zhipu | - | - | - |
|  -   | llama | 通用 | Meta AI | - | - | - |
|  -   | llama-2-chat | 通用 | Meta AI | - | - | - |
|  -   | Ziya-llama | 通用 | IDEA-CCNL | - | - | - |
|  -   | Chinese-llama | 通用 | Yiming Cui | - | - | - |



### 通用大模型榜单

| 排名 |         模型         |    基模型    |        机构        | 总分 | 信息抽取 | 要素识别 | 文本摘要 | 法律文书生成 | 法律知识问答 | 案情分析 | 类案匹配 | 法律判决预测 | 诉请判决预测 | 争议焦点挖掘 |
|:----:|:------------------:|:---------:|:----------------:| :----: | :----: | :----: | :----:| :----: | :----: | :----: | :----:| :----: | :----: |:-----:|
| - |        gpt4        |     -     |      OpenAI      | - | - | - | - | - | - | - | - | - | - |   -    |
| - |   gpt-3.5-turbo    |     -     |      OpenAI      | - | - | - | - | - | - | - | - | - | - |   -    |
| - |  internlm-chat-7b  |     -     |  InternLM Team   | - | - | - | - | - | - | - | - | - | - |   -    |
| - |    baichuan-7B     |     -     |  Baichuan Inc.   | - | - | - | - | - | - | - | - | - | - |   -    |
| - |     chatglm-6b     |     -     | Tsinghua & Zhipu | - | - | - | - | - | - | - | - | - | - |   -    |
| - |    chatglm2-6b     |     -     | Tsinghua & Zhipu | - | - | - | - | - | - | - | - | - | - |   -    |
| - |      llama-7b      |     -     |     Meta AI      | - | - | - | - | - | - | - | - | - | - |   -    |
| - |     llama-13b      |     -     |     Meta AI      | - | - | - | - | - | - | - | - | - | - |   -    |
| - | llama-2-7b-chat-hf |     -     |     Meta AI      | - | - | - | - | - | - | - | - | - | - |   -    |
| - |   Ziya-LLaMA-13B   | llama-13b |    IDEA-CCNL     | - | - | - | - | - | - | - | - | - | - |   -    |
| - |  Chinese-llama-7b  | llama-7b  |    Yiming Cui    | - | - | - | - | - | - | - | - | - | - |   -    |
| - | Chinese-llama-13b  | llama-13b |    Yiming Cui    | - | - | - | - | - | - | - | - | - | - |   -    |

### 中文法律大模型榜单

| 排名 |      模型      |        基模型        |                机构                | 总分 | 信息抽取 | 要素识别 | 文本摘要 | 法律文书生成 | 法律知识问答 | 案情分析 | 类案匹配 | 法律判决预测 | 诉请判决预测 | 争议焦点挖掘 |
|:--:|:------------:|:-----------------:|:--------------------------------:| :----: | :----: | :----: | :----:| :----: | :----: | :----: | :----:| :----: | :----: | :----: |
| -  |   ChatLaw    |  Ziya-LLaMA-13B   |        Peking University         | - | - | - | - | - | - | - | - | - | - | - |
| -  |    智海-录问     |    Baichuan-7B    |         ZJU,Alibaba,e.t.         | - | - | - | - | - | - | - | - | - | - | - |
| -  |  LawGPT-zh   |    ChatGLM-6B     |          Personal Team           | - | - | - | - | - | - | - | - | - | - | - |
| -  |    LawGPT    | Chinese-LLaMA-7b  |          Personal Team           | - | - | - | - | - | - | - | - | - | - | - |
| -  | Lawyer LLaMA | Chinese-LLaMA-13B | Personal(Peking University team) | - | - | - | - | - | - | - | - | - | - | - |
| -  |   LexiLaw    |    ChatGLM-6B     |   Personal(Tsinghua IR Group)    | - | - | - | - | - | - | - | - | - | - | - |
| -  | fuzi.mingcha |   ChatGLM-6B      |  SDU, CPUL, e.t.  | - | - | - | - | - | - | - | - | - | - | - |
| -  | HanFei  | HanFei | UCAS (SIAT-NLP) | - | - | - | - | - | - | - | - | - | - | - |

### 评测

#### 环境准备

```bash
git clone git clone https://github.com/Dai-shen/SCULaiw.git --recursive
cd SCULaiw
pip install -r requirements.txt
cd SCULaiw/src/financial-evaluation
pip install -e .[multilingual]
```

#### 自动评估

```bash
python eval.py \
    --model "hf-causal-llama" \
    --model_args "use_accelerate=True,pretrained=daishen/model,tokenizer=daishen/model,use_fast=False" \
    --tasks "legal_ar,legal_cp,legal_ptp"
```

### 任务

我们评估法律NLP的两个重要板块：\
一，法律信息抽取，包含命名实体识别，要素识别，文本摘要三个子任务\
二，法律应用能力，包含法律文书生成，法律知识问答，案情分析，类案匹配，法律判决预测，诉请判决预测，争议焦点挖掘。\
下面是各个子任务的描述。

|   任务   | 描述                                                                                                                                                |
|:------:|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| 命名实体识别 | 从各种法律文件中提取具有司法特征的名词和短语并进行合并的过程，如与赃物、嫌疑人有关的法律文件。                                                                                                   |
|  要素识别  | 在司法领域，案件要素识别任务的主要目的是从案件描述中自动提取关键事实描述。在给定司法文书的相关段落之后，系统对每句话进行分析和判断，以确定关键的案件要素。                                                                     |
|  文本摘要  | 法律文本摘要是对法律文本进行摘要整理的过程，旨在产生一个较短的文本，保留较长文本的大部分含义。                                                                                                   |
|   法律文书生成    | 法律文书生成，这里特指根据司法裁判文书中的“事实认定”内容生成“本院认为”文本。                                                                                                          |
|   法律知识问答    | 法律知识问答，旨在回答法律领域的问题。法律专业人员工作的重要组成部分之一就是为非专业人员提供可靠、高质量的法律咨询服务。                                                                                      |
|   案情分析    | 案情分析，是在充分理解案件描述之后回答此案件相关的问题。                                                                                                                      |
|   类案匹配    | 在英美法系国家，如美国、加拿大和印度，司法裁决是根据过去类似的代表性案例做出的。因此，如何识别最相似的案件是英美法系在判决中首要关注的问题。                                                                            |
|   法律判决预测    | 法律判决预测，它根据事实描述自动预测判断结果，具体包括罪名预测、相关法条预测和刑期预测三个子任务。                                                                                                 |
|   诉请判决预测    | 法院案件的这项任务通常使用事实描述来预测其对原告诉请的判决。                                                                                                                    |
|   争议焦点挖掘    | 在法院的庭审过程中，裁判文书起着记录辩、诉双方观点证据的重要作用。本任务旨在抽取出裁判文书中辩方诉方之间的逻辑交互论点对，即争议焦点。                                                                               |

### 数据集 (legal Instruction Dataset)

|             数据集             |     任务      | 数据集大小 | 文本类型 | 法律领域 |  任务类型   |      评价指标      | 来源 |
|:---------------------------:|:-----------:|:-----:|:----:|:----:|:-------:|:--------------:| :----: |
|        CAIL-2021-IE         |   命名实体识别    |   -   | json |  刑事  | 命名实体识别  |    F1, P, R    | [[1]](https://github.com/isLouisHsu/CAIL2021-information-extraction/tree/master) |
|        CAIL-2019-ER         |    要素识别     |   -   | json |  民事  |  多标签分类  |   Acc,Mac-F1   | [[2]](https://github.com/china-ai-law-challenge/CAIL2019) |
| CAIL-2020-TS & CAIL-2022-TS |    文本摘要     | 3762  | json |  -   |  文本摘要   |     ROUGE      | [[3]](http://cail.cipsc.org.cn/task_summit.html?raceID=1&cail_tag=2020) [[4]](https://github.com/china-ai-law-challenge/CAIL2022/tree/main/sfzy)  |
|       Court-View-Gen        |   法律文书生成    |   -   | json |  刑事  |  文本生成   |     ROUGE      | [[5]](https://github.com/oceanypt/Court-View-Gen) |
|           AC-NLG            |   法律文书生成    |   -   | json |  民事  |  文本生成   |     ROUGE      | [[6]](https://github.com/wuyiquan/AC-NLG)  |
|           JEC-QA            |   法律知识问答    |   -   | json |  民事  |   多选题   |      Acc       | [[7]](https://jecqa.thunlp.org/)  |
|            CJRC             |    案情分析     |   -   | json |  民事  |   单选题   |       F1       | [[8]](https://github.com/china-ai-law-challenge/CAIL2019/tree/master)  |
|        CAIL2019-SCM         |    类案匹配     |   -   | json |  民事  |   二分类   |      Acc       | [[9]](https://github.com/china-ai-law-challenge/CAIL2019/tree/master/scm)  |
|           LecaRd            |    类案匹配     |   -   | json |  民事  | 文本相似度排序 |     ROUGE      | [[10]](https://github.com/myx666/LeCaRD)  |
|          CAIL2018           | 法律判决预测-法条预测 |   -   | json |  刑事  |  多标签分类  |     ROUGE      | [[11]](https://github.com/thunlp/CAIL)  |
| Criminal-S | 法律判决预测-罪名预测 |   -   | json |  刑事  |   多分类   | Acc, P, R, F1  | [[12]](https://github.com/thunlp/attribute_charge) |
| MLMN | 法律判决预测-刑期预测 |   -   | json |  刑事  |   多分类   |    P, R, F1    | [[13]](https://github.com/gjdnju/MLMN) |
| MSJudeg |   诉请判决预测    |   -   | json |  民事  |   多分类   | Mac-F1, Mic-F1 | [[14]](https://github.com/mly-nlp/LJP-MSJudge) |
| CAIL2020-AM & CAIL2021-AM |   争议焦点挖掘    |   -   | json |  -   |   多选题   |      Acc       | [[15]](https://github.com/china-ai-law-challenge/CAIL2020/tree/master/lbwj) [[16]](https://github.com/china-ai-law-challenge/CAIL2020/tree/master/lbwj) |

#### 评价指标

| 任务类型 | 评价指标 | 说明                                                  |
|----|------|-----------------------------------------------------|
| 分类 | 准确率  | 这个指标表示正确预测的观测结果与总观测结果的比率。它的计算方式是（真正例 + 真负例）/ 总样例个数。 |
