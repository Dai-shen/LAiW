# ⚖️LAiW: A Chinese Legal Large Language Models Benchmark

**LAiW：中文法律大模型综合性基准（狴犴）**

🔥 [LAiW最新榜单](https://huggingface.co/spaces/daishen/LAiW)

🔥 [技术报告](XXXXX)，即将发布

## 新闻

💻 **最近更新** **[2023/10/08]**

- 公布 [LAiW](https://github.com/Dai-shen/LAiW) 能力评测体系
- 完成第一阶段大模型的法律 NLP 基础能力评测工作,包含通用大模型: ChatGPT ，[Llama2](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)，[Ziya-LLaMA](https://huggingface.co/IDEA-CCNL/Ziya-LLaMA-13B-v1)，[Chinese-LLaMA](https://github.com/ymcui/Chinese-LLaMA-Alpaca)，[Baichuan2](https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat); 以及法律大模型:[HanFei](https://github.com/siat-nlp/HanFei)，[ChatLaw](https://huggingface.co/JessyTsu1/ChatLaw-13B)，[LawGPT](https://github.com/pengxiao-song/LaWGPT) 
- 公布法律能力和基础任务的评测分数及计算方式

## 目录

- [⚖️LAiW: A Chinese Legal Large Language Models Benchmark](#️laiw-a-chinese-legal-large-language-models-benchmark)
  - [新闻](#新闻)
  - [目录](#目录)
    - [任务评测结构图](#任务评测结构图)
    - [评测任务](#评测任务)
    - [LIT：指令微调数据集](#lit指令微调数据集)
    - [评分机制](#评分机制)
    - [评测](#评测)
      - [环境准备](#环境准备)
      - [自动评估](#自动评估)
    - [项目参与者](#项目参与者)
    - [免责声明](#免责声明)
    - [致谢](#致谢)


### 任务评测结构图

<img src="https://github.com/Dai-shen/LAiW/blob/main/resources/task_framwork.png"  width="50%" height="50%"></img>

### 评测任务

我们经过 <strong>法学专家</strong> 的多次指导，从法学角度上评测法律 NLP 的<strong>三</strong>大能力，共计<strong>13</strong>个基础任务

- 法律 NLP 基础能力：主要评测法律基础任务、 NLP 基础任务和法律信息抽取的能力，包括法条推送、要素识别、命名实体识别、司法要点摘要和案件识别 5 个基础任务
- 法律基础应用能力：主要评测大模型对法律领域知识的基础应用能力，包括争议焦点挖掘、类案匹配、刑事裁判预测、民事裁判预测和法律问答 5 个基础任务
- 法律复杂应用能力：进一步评测大模型对法律领域知识的复杂应用能力，包括司法说理生成、案情理解和法律咨询 3 个基础任务
  
下面是评测任务的具体描述

<table>

  <tr>
  <td>能力</td>
  <td>任务</td>
  <td>描述</td>
  </tr>

  <tr>
    <td rowspan="5">法律NLP基础能力</td>
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
    <td rowspan="5">法律基础应用能力</td>
    <td>争议焦点挖掘</td>
    <td>在法院的庭审过程中，裁判文书起着记录辩、诉双方观点证据的重要作用。本任务旨在抽取出裁判文书中辩方诉方之间的逻辑交互论点对，即争议焦点</td>
  </tr>
  <tr>
    <td>类案匹配</td>
    <td>司法裁决通常是根据过去类似的代表性案例做出的。因此，如何识别最相似的案件是判决中一个首要关注的问题</td>
  </tr>
  <tr>
    <td>刑事裁判预测</td>
    <td>根据事实描述自动预测裁判结果，本任务旨在根据案件事实、证据和适用的法律，对被告人的定罪与否以及可能的刑期进行预测</td>
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
    <td rowspan="3">法律复杂应用能力</td>
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

### LIT：指令微调数据集

我们调研现有中文法律的公开数据集，重新整理构建了指令微调数据集 **Legal Instruction Tuning Dataset (LIT)** ，详情可见[LAiW-DataSet](https://github.com/Dai-shen/LAiW-DataSet)。这里展示 **LIT** 中用于各个基础任务评测的评测数据集。**LIT** 数据集进一步整理中，等待后续公布

<table>

  <tr>
    <td>能力层级</td>
    <td>任务</td>
    <td>主要数据集</td>
    <td>评测数据集</td>
    <td>数据集大小</td>
  </tr>

  <tr>
    <td rowspan="5">法律NLP基础能力</td>
    <td>法条推送</td>
    <td>CAIL-2018</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-ar">legal_ar</a></td>
    <td>1,000</td>
  </tr>
  <tr>
    <td>要素识别</td>
    <td>CAIL-2019</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-er">legal_er</a></td>
    <td>1,000</td>
  </tr>
  <tr>
    <td>命名实体识别</td>
    <td>CAIL-2021</td>
    <!-- <td><a href="https://huggingface.co/datasets/daishen/legal-ner">legal_ner</a></td>
    <td>156</td> -->
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>司法要点摘要</td>
    <td>CAIL-2020</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-js">legal_js</a></td>
    <td>364</td>
  </tr>
  <tr>
    <td>案件识别</td>
    <td>CJRC</td>
    <td><a href="https://huggingface.co/datasets/daishen/legal-cr">legal_cr</a></td>
    <td>2,000</td>
  </tr>

  <tr>
    <td rowspan="5">法律知识理解能力</td>
    <td>刑事判决预测</td>
    <td>Criminal-S<br>MLMN</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>民事裁判预测</td>
    <td>MSJudeg</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>法律问答</td>
    <td>JEC-QA</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>争议焦点挖掘</td>
    <td>Private</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>类案匹配</td>
    <td>CAIL-2019</td>
    <td></td>
    <td></td>
  </tr>

  <tr>
    <td rowspan="3">法律知识应用能力</td>
    <td>司法说理生成</td>
    <td>AC-NLG</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>案情理解</td>
    <td>CJRC</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>法律咨询</td>
    <td>CrimeKgAssitant</td>
    <td></td>
    <td></td>
  </tr>

</table>

### 评分机制

📚 最新版本 V1.0：

- 对于每一项评测能力，其分数为所评测的所有基础子任务分数的平均值
- 对于每项特定的基础任务，使用 **LIT** 的评测数据集，根据大模型在该任务上的输出与真实标签，客观的计算相应评估指标，作为模型在该任务上的分数 （评估指标取值范围均为 0-1 之间）


### 评测

- 我们将按照评测结构图中的13个基础任务持续评测现存大模型在这些任务上的表现，详情可见[模型评测榜单](https://huggingface.co/spaces/daishen/LAiW)。
- 评测模型不仅有未开源的 ChatGPT 和 GPT-4，而且还有 [Baichuan2](https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat), [chatglm2](https://huggingface.co/THUDM/chatglm2-6b)，[HanFei](https://github.com/siat-nlp/HanFei)，[Lawyer LLaMa](https://github.com/AndrewZhe/lawyer-llama/tree/main), [智海-录问](https://modelscope.cn/models/wisdomOcean/wisdomInterrogatory/summary) 等开源的通用大模型和中文法律大模型

#### 环境准备

```bash
git clone git clone https://github.com/Dai-shen/LAiW.git --recursive
cd LAiW
pip install -r requirements.txt
cd LAiW/src/financial-evaluation
pip install -e .[multilingual]
```

#### 自动评估

```bash
python eval.py \
    --model "hf-causal-experimental" \
    --model_args "use_accelerate=True,pretrained=baichuan-inc/Baichuan2-13B-Chat,tokenizer=baichuan-inc/Baichuan2-13B-Chat,use_fast=False" \
    --tasks "legal_ar,legal_er,legal_ner"
```


### 项目参与者
本项目由来自于中科院深圳先进院得理法律人工智能联合实验室的何万伟、温嘉宝、张磊、程浩、秦博文、李云水、李之健，深圳市大数据研究院、港中文深圳的蒋峰、陈俊颖同学合作开发，指导教师为深圳市大数据研究院、港中文深圳的王本友助理教授和中科院深圳先进院的杨敏副研究员。

### 免责声明
本项目相关资源仅供学术研究之用，严禁用于商业用途。使用涉及第三方代码的部分时，请严格遵循相应的开源协议。模型生成的内容受模型计算、随机性和量化精度损失等因素影响，本项目无法对其准确性作出保证，本项目不承担任何法律责任，亦不对因使用相关资源和输出结果而可能产生的任何损失承担责任。

### 致谢
本项目参考了以下开源项目，在此对相关项目和研究开发人员表示感谢。

Bloom: https://huggingface.co/bigscience/bloom

Facebook LLaMA: https://github.com/facebookresearch/llama

Stanford Alpaca: https://github.com/tatsu-lab/stanford_alpaca

Self-instruct: https://github.com/yizhongw/self-instruct
