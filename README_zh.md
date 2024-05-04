# ⚖️LAiW: A Chinese Legal Large Language Models Benchmark

| [English](https://github.com/Dai-shen/LAiW/blob/main/README.md) | [中文](https://github.com/Dai-shen/LAiW/blob/main/README_zh.md)

**LAiW：中文法律大模型综合性基准（狴犴）**

🔥 [LAiW最新评测结果](https://huggingface.co/spaces/daishen/SCULAiW)

🔥 [技术报告与正式文章](https://arxiv.org/abs/2310.05620)

## 新闻

🔄 **最近更新**

- [2024-04-19] 更新 [正式文章](https://arxiv.org/abs/2310.05620)

📅 **更早讯息**

- [2024/1/22] 增加通用大模型 [Baichuan-7B](https://huggingface.co/baichuan-inc/Baichuan-7B) 的评测结果
- [2024/1/14] 提供评测数据集更多[详细信息](https://github.com/Dai-shen/LAiW/blob/main/data/README.md)，同时给出模型评测指标 [SCULAiW](https://huggingface.co/spaces/daishen/SCULAiW) 的计算方式
- [2024/1/12] 进一步确认和完善相关评测结果，优化评测榜单 [SCULAiW](https://huggingface.co/spaces/daishen/SCULAiW) 的布局，补充评测模型更多详细信息
- [2024/1/10] 新增商用大模型 GPT-4 和 通用大模型 Llama-7B, Llama13B, [Chinese-LLaMA-13B](https://github.com/ymcui/Chinese-LLaMA-Alpaca) 的评测
- [2024/1/2] 公布了大模型法律能力[评分机制](#评分机制)，公布大模型[评测分数](#模型得分)
- [2024/1/2] 公布了14个基础任务的[测试数据集](https://huggingface.co/daishen)
- [2024/1/1] 更新了 [SCULAiW](https://huggingface.co/spaces/daishen/SCULAiW) 法律能力评测结果
- [2024/12/31] 完成了主流大模型的法律能力评测工作。评测过程中，除前述工作提及的模型外，新增通用大模型 [ChatGLM](https://huggingface.co/THUDM/chatglm-6b) 和法律大模型 [Lawyer-LLaMA](https://github.com/AndrewZhe/lawyer-llama/tree/main?tab=readme-ov-file)，[Fuzi-Mingcha](https://huggingface.co/SDUIRLab/fuzi-mingcha-v1_0)，[Wisdom-Interrogatory](https://github.com/zhihaiLLM/wisdomInterrogatory)，[LexiLaw](https://github.com/CSHaitao/LexiLaw)
- [2023/10/12] 公布 [LAiW技术报告](https://arxiv.org/abs/2310.05620)初版
- [2023/10/08] 公布 [LAiW](https://github.com/Dai-shen/LAiW) 第一阶段能力评测体系
- [2023/10/08] 完成第一阶段大模型的基础信息检索能力评测工作,包含商用大模型：ChatGPT；通用大模型：[Llama2](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)，[Ziya-LLaMA](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1)，[Chinese-LLaMA](https://github.com/ymcui/Chinese-LLaMA-Alpaca)，[Baichuan2](https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat); 以及法律大模型：[HanFei](https://github.com/siat-nlp/HanFei)，[ChatLaw](https://huggingface.co/JessyTsu1/ChatLaw-13B)，[LaWGPT](https://github.com/pengxiao-song/LaWGPT)
- [2023/10/08] 公布法律能力和基础任务的评测分数及计算方式

## 目录

- [⚖️LAiW: A Chinese Legal Large Language Models Benchmark](#️laiw-a-chinese-legal-large-language-models-benchmark)
  - [新闻](#新闻)
  - [目录](#目录)
    - [任务评测结构图](#任务评测结构图)
    - [模型得分](#模型得分)
    - [评测任务](#评测任务)
    - [评测数据集](#评测数据集)
    - [评分机制](#评分机制)
    - [评测代码](#评测代码)
      - [1.环境准备](#1环境准备)
      - [2.模型输出](#2模型输出)
      - [3.自动评测](#3自动评测)
    - [项目参与者](#项目参与者)
    - [声明](#声明)
    - [致谢](#致谢)
    - [引用](#引用)

### 任务评测结构图

<img src="https://github.com/Dai-shen/LAiW/blob/main/resources/task_framwork.png"  width="70%" height="70%"></img>

### 模型得分

按照大模型[评分机制](#评分机制)的计算方式，现阶段我们评测了7个主流法律大模型和6个通用大模型，模型得分如下

| 模型 | 参数 | 模型领域 | 总分 | BIR | LFI | CLA | 基模型 |
| :---:| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| GPT-4 | - | 通用 | 69.63 | 80.92 | 69.27 | 58.69 | - |
| ChatGPT | - | 通用 | 64.09 | 75.99 | 58.32 | 57.96 | - |
| [Baichuan2-Chat](https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat) | 13B | 通用 | 48.04 | 53.67 | 32.03 | 58.40 | - |
| [ChatGLM](https://huggingface.co/THUDM/chatglm-6b)   | 6B | 通用 | 47.01 | 51.51 | 37.08 | 52.44 | - |
| [Ziya-LLaMA](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1) | 13B | 通用 | 45.79 | 61.47 | 29.44 | 46.45 | Llama-13B |
| [Fuzi-Mingcha](https://huggingface.co/SDUIRLab/fuzi-mingcha-v1_0)  | 6B | 法律 | 40.62 | 39.68 | 27.46 | 54.71 | [ChatGLM-6B](https://huggingface.co/THUDM/chatglm-6b) |
| [HanFei](https://github.com/siat-nlp/HanFei)   | 7B | 法律 | 35.69 | 37.42 | 16.33 | 53.31 | - |
| [LexiLaw](https://github.com/CSHaitao/LexiLaw)   | 6B | 法律 | 31.31 | 41.32 | 8.88 | 43.73 | [ChatGLM-6B](https://huggingface.co/THUDM/chatglm-6b) |
| [ChatLaw](https://huggingface.co/JessyTsu1/ChatLaw-13B)  | 13B | 法律 | 25.77 | 58.02 | 12.54 | 6.74 | [Ziya-LLaMA-13B](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1) |
| [Llama2-Chat](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)    | 7B | 通用 | 27.76 | 31.86 | 12.77 | 38.64 | - |
| [Lawyer-LLaMA](https://github.com/AndrewZhe/lawyer-llama/tree/main?tab=readme-ov-file)  | 13B | 法律 | 29.25 | 30.85 | 6.39 | 50.50 | [Chinese-LLaMA-13B](https://github.com/ymcui/Chinese-LLaMA-Alpaca) |
| [Chinese-LLaMA](https://github.com/ymcui/Chinese-LLaMA-Alpaca) | 13B | 通用 | 24.99 | 21.02 | 19.16 | 34.80 | Llama-13B |
| [Chinese-LLaMA](https://github.com/ymcui/Chinese-LLaMA-Alpaca) | 7B | 通用 | 24.91 | 22.32 | 18.25 | 34.16 | Llama-7B |
| [Baichuan](https://github.com/baichuan-inc/Baichuan-7B) | 7B | 通用 | 22.51 | 21.20 | 15.46 | 30.86 | - |
| [LaWGPT](https://github.com/pengxiao-song/LaWGPT)      | 7B | 法律 | 22.69 | 15.47 | 14.27 | 38.32 | [Chinese-LLaMA-7B](https://github.com/ymcui/Chinese-LLaMA-Alpaca) |
| Llama | 13B | 通用 | 21.00 | 18.51 | 15.08 | 29.40 | - |
| [Wisdom-Interrogatory](https://github.com/zhihaiLLM/wisdomInterrogatory) | 7B | 法律 | 18.83 | 12.66 | 10.45 | 33.37 | [Baichuan-7B](https://huggingface.co/baichuan-inc/Baichuan-7B) |
| Llama | 7B | 通用 | 16.35 | 11.12 | 15.40 | 22.54 | - |

其中，大模型法律能力评测总得分和各层级法律能力得分排名依次为

<img src="https://github.com/Dai-shen/LAiW/blob/main/resources/Overall-histogram.png"  width="100%" height="100%"></img>

<img src="https://github.com/Dai-shen/LAiW/blob/main/resources/BIR-histogram.png"  width="100%" height="100%"></img>

<img src="https://github.com/Dai-shen/LAiW/blob/main/resources/LFI-histogram.png"  width="100%" height="100%"></img>

<img src="https://github.com/Dai-shen/LAiW/blob/main/resources/CLA-histogram.png"  width="100%" height="100%"></img>

### 评测任务

我们在 <strong>法学专家与人工智能专家</strong> 的共同努力下，从法学角度和可实现性上对法律 NLP的能力进行划分．如上图所示，目前我们将其分成了<strong>3</strong>大能力，共计<strong>14</strong>个基础任务：

- 基础信息检索能力：评测法律基础任务、 NLP 基础任务和法律信息抽取的能力，包括法条推送、要素识别、命名实体识别、司法要点摘要和案件识别 5 个基础任务
- 法律基础推理能力：评测大模型对法律领域知识的基础应用能力，包括争议焦点挖掘、类案匹配、罪名预测、刑期预测和民事裁判预测和法律问答 6 个基础任务
- 法律复杂应用能力：评测大模型对法律领域知识的复杂应用能力，包括司法说理生成、案情理解和法律咨询 3 个基础任务
  
下面是各评测任务的简要介绍

<table>

  <tr>
  <td>能力</td>
  <td>任务</td>
  <td>介绍</td>
  </tr>

  <tr>
    <td rowspan="5">基础信息检索</td>
    <td>法条推送</td>
    <td>该任务是司法实践应用上的基础任务，在提供法律领域的智能化支持和辅助决策上起着重要作用，旨在根据案件描述给出其相关法条</td>
  </tr>
  <tr>
    <td>要素识别</td>
    <td>在司法领域，案件要素识别任务的主要目的是从案件描述中自动提取关键事实描述。在给定司法文书的相关段落之后，系统对每句话进行分析和判断，以确定关键的案件要素</td>
  </tr>
  <tr>
    <td>命名实体识别</td>
    <td>从各种法律文件中提取具有司法特征的名词和短语并进行合并的过程，如与赃物、嫌疑人有关的法律文件</td>
  </tr>
  <tr>
    <td>司法要点摘要</td>
    <td>裁判文书是人民法院公开审判活动、裁判理由、裁判依据和裁判结果的重要载体。司法摘要则是对裁判文书的内容进行压缩、归纳和总结，反映案件审理过程中的裁判过程、事实、理由和判决依据等</td>
  </tr>
  <tr>
    <td>案件识别</td>
    <td>民事案件和刑事案件是两种不同类型的法律案件。民事案件是解决个人纠纷和维护权益的法律程序，刑事案件是为了维护社会秩序和惩罚犯罪行为的法律程序。本任务旨在根据相关的案件描述判断其为刑事案件还是民事案件</td>
  </tr>

  <tr>
    <td rowspan="5">法律基础推理</td>
    <td>争议焦点挖掘</td>
    <td>在法院的庭审过程中，裁判文书起着记录辩、诉双方观点证据的重要作用。本任务旨在抽取出裁判文书中辩方诉方之间的逻辑交互论点对，即争议焦点</td>
  </tr>
  <tr>
    <td>类案匹配</td>
    <td>司法裁决通常是根据过去类似的代表性案例做出的。因此，如何识别最相似的案件是判决中一个首要关注的问题</td>
  </tr>
  <tr>
    <td>刑事裁判预测</td>
    <td>根据事实描述自动预测裁判结果，本任务旨在根据案件事实、证据和适用的法律，对被告人的定罪与否以及可能的刑期进行预测，因此分为罪名预测和刑期预测两类任务</td>
  </tr>
  <tr>
    <td>民事裁判预测</td>
    <td>通过分析案件相关信息和相关法律规定，预测民事诉讼中可能的判决结果或争议的解决方式。本任务旨在使用事实描述来预测其对原告诉请的裁判</td>
  </tr>
  <tr>
    <td>法律问答</td>
    <td>司法考试作为我国最难的考试，也是法律工作者生涯中极其重要的考试。本任务是针对国家司法考试的客观问答任务，包括单选题和多选题</td>
  </tr>

  <tr>
    <td rowspan="3">法律复杂应用</td>
    <td>司法说理生成</td>
    <td>人民法院在认定案件事实的基础上需要就判决理由作出进一步的阐述。本任务旨在根据案件事实描述生成相关的司法说理文本</td>
  </tr>
  <tr>
    <td>案情理解</td>
    <td>通过机器智能化地阅读理解裁判文书，可以更快速、便捷地辅助法官、律师以及普通大众获取所需信息。本任务是基于中文裁判文书的阅读理解，具体来说，模型需要基于裁判文书的案件相关描述所提出的问题而作出合理合规的回答</td>
  </tr>
  <tr>
    <td>法律咨询</td>
    <td>涵盖广泛的法律领域，包括但不限于刑法、民法、商法、劳动法、知识产权法、家庭法等。本任务旨在根据用户提供的有关法律问题，考虑适用的法律法规、相关判例和法律解释，并结合具体情况给出准确、清晰和可靠的答案</td>
  </tr>

</table>

### 评测数据集

我们基于现有中文法律的公开数据集，重新整理并构建了上述各个任务的评测数据集 **Legal Evaluation Dataset (LED)** ，我们展示了其各个基础任务评测的评测数据集。有关数据集更多详细信息请查看[这里](https://github.com/Dai-shen/LAiW/blob/main/data/README.md)

<table>

  <tr>
    <td>能力层级</td>
    <td>任务</td>
    <td>主要数据集</td>
    <td>评测数据集</td>
    <td>数据集大小</td>
    <td>类别</td>
  </tr>

  <tr>
    <td rowspan="5">基础信息检索</td>
    <td>法条推送</td>
    <td>CAIL-2018</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-ar">legal_ar</a></td>
    <td>1,000</td>
    <td>分类</td>
  </tr>
  <tr>
    <td>要素识别</td>
    <td>CAIL-2019</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-er">legal_er</a></td>
    <td>1,000</td>
    <td>分类</td>
  </tr>
  <tr>
    <td>命名实体识别</td>
    <td>CAIL-2021</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-ner">legal_ner</a></td>
    <td>1040</td>
    <td>命名实体识别</td>
  </tr>
  <tr>
    <td>司法要点摘要</td>
    <td>CAIL-2020</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-js">legal_js</a></td>
    <td>364</td>
    <td>文本生成</td>
  </tr>
  <tr>
    <td>案件识别</td>
    <td>CJRC</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-cr">legal_cr</a></td>
    <td>2,000</td>
    <td>分类</td>
  </tr>
  <tr>
    <td rowspan="6">法律基础推理</td>
    <td>争议焦点挖掘</td>
    <td>LAIC-2021</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-cfm">legal_cfm</a></td>
    <td>306</td>
    <td>分类</td>
  </tr>
  <tr>
    <td>类案匹配</td>
    <td>CAIL-2019</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-scm">legal_scm</a></td>
    <td>260</td>
    <td>分类</td>
  </tr>
  <tr>
    <td>罪名预测</td>
    <td>Criminal-S</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-cp">legal_cp</a></td>
    <td>827</td>
    <td>分类</td>
  </tr>
  <tr>
  <td>刑期预测</td>
    <td>MLMN</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-ptp">legal_ptp</a></td>
    <td>349</td>
    <td>分类</td>
  </tr>
  <tr>
    <td>民事裁判预测</td>
    <td>MSJudeg</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-ctp">legal_ctp</a></td>
    <td>800</td>
    <td>分类</td>
  </tr>
  <tr>
    <td>法律问答</td>
    <td>JEC-QA</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-lqa">legal_lqa</a></td>
    <td>855</td>
    <td>分类</td>
  </tr>

  <tr>
    <td rowspan="3">法律复杂应用</td>
    <td>司法说理生成</td>
    <td>AC-NLG</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-jrg">legal_jrg</a></td>
    <td>834</td>
    <td>文本生成</td>
  </tr>
  <tr>
    <td>案情理解</td>
    <td>CJRC</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-cu">legal_cu</a></td>
    <td>1,054</td>
    <td>文本生成</td>
  </tr>
  <tr>
    <td>法律咨询</td>
    <td>CrimeKgAssitant</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-lc">legal_lc</a></td>
    <td>916</td>
    <td>文本生成</td>
  </tr>

</table>

### 评分机制

⭐️ 任务得分
<div align="center">

$$
S_{(Task)} = \begin{cases}
    F1 * 100, & \text{If }\quad Task\quad\in\quad Classification \\
    \frac{1}{3}*(R1 + R2 + RL) * 100, & \text{If }\quad Task \quad\in\quad Text\quad Generation \\
    Acc * 100, & \text{If }\quad Task\quad\in\quad NER
\end{cases}
$$

</div>

目前，我们的评测基准主要包含分类任务，文本生成和命名实体识别任务三类。对于分类任务，我们采用F1值。对于文本生成任务，我们采用其Rouge1，Rouge2和RougeL的均值。特别地，对于法律NER任务，我们采用法律实体的提取准确率Accuracy作为其得分。

🌟 模型得分

对于单个大模型，我们首先计算每个阶段的任务平均分数作为其该项法律能力得分。然后取三项法律能力得分的均值作为大模型的最终评测分数。模型评测分数见[这里](#模型得分)。

### 评测代码

我们将按照评测结构图中的14个基础任务持续评测现有大模型在这些任务上的表现，详情可见[模型评测榜单](https://huggingface.co/spaces/daishen/SCULAiW)。

#### 1.环境准备

```bash
git clone git clone https://github.com/Dai-shen/LAiW.git --recursive
cd LAiW
pip install -r requirements.txt
cd LAiW/src/financial-evaluation
pip install -e .[multilingual]
```

#### 2.模型输出

选取待评测的模型和法律任务，运行以下代码，得到模型输出

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

参数说明

- `model`：模型接口类型，可选参数见`src/financial-evaluation/lm_eval/models/__init__.py`
- `tasks`：预定义的任务名，可在`src/tasks/_init_.py`和`src/tasks/legal.py`定义自己的任务
- `pretrained_model`：大模型路径（huggingface空间或模型本地路径）
- `output_base_path`: 模型保存路径

#### 3.自动评测

将模型输出文件保存在 `precision/eval_results/` 目录下。假设评测模型 [Fuzi-Mingcha-6B](https://huggingface.co/SDUIRLab/fuzi-mingcha-v1_0)，和 [HanFei-7B](https://github.com/siat-nlp/HanFei)，则每个模型路径下包含13个基础任务（涵盖14个评测数据集）的输出文件，文件结构应该如下：

```
eval_results/
├── Fuzi-Mingcha-6B/
│   ├── legal_ar_write_out_info.json
│   ├── legal_er_write_out_info.json
│       ......
│   ├── legal_cu_write_out_info.json
│   ├── legal_lc_write_out_info.json
├── HanFei-7B/
│   ├── legal_ar_write_out_info.json
│   ├── legal_er_write_out_info.json
│       ......
│   ├── legal_cu_write_out_info.json
│   ├── legal_lc_write_out_info.json
```

然后运行 `precision/compute_metrics.py` 对各模型各任务的输出进行自动评测，评测结果保存至 `precision/metrics_result/` 目录下
注：本项目的评测结果可在[LAiW Leaderboard](https://huggingface.co/spaces/daishen/SCULAiW)查看

### 项目参与者

本项目由四川大学（四川智慧社会智能治理重点实验室 智慧法治研究所）的代永富、冯端宇、贾昊宸、张译方、王皓，武汉大学的谢倩倩、韩玮光、黄济民，以及西南石油大学的田维共同开发。

### 声明

本项目仅供学术研究使用，严禁用于商业。我们对使用该项目的任何问题，风险或不利后果不承担任何责任。

### 致谢

本项目在构建时，参考了以下开源项目，在此对相关项目和研究开发人员表示感谢。

- [**LLMindCraft**](https://github.com/XplainMind/LLMindCraft)
- [**Awesome Chinese Legal Resources**](https://github.com/pengxiao-song/awesome-chinese-legal-resources)

### 引用

如果本项目对您的研究有所帮助，请引用本项目。

```
@article{dai2023laiw,
  title={LAiW: A Chinese legal large language models benchmark},
  author={Dai, Yongfu and Feng, Duanyu and Huang, Jimin and Jia, Haochen and Xie, Qianqian and Zhang, Yifang and Han, Weiguang and Tian, Wei and Wang, Hao},
  journal={arXiv preprint arXiv:2310.05620},
  year={2023}
}
```
