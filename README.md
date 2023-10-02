# ⚖️SCULaiw: Legal Evaluation Framework (BIAN)

**狴犴：中文法律大模型综合性基准**

🔥 [SCULaiw最新榜单](https://huggingface.co/spaces/daishen/SCULaiw)

## 新闻

💻 **最近更新** **[2023/10/02]** 

- 公布 [SCULaiw](https://github.com/Dai-shen/SCULaiw) 能力评测体系
- 完成 ChatGPT ，[Llama2](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)，[Baichuan2](https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat)，[HanFei](https://github.com/siat-nlp/HanFei)，[ChatLaw](https://huggingface.co/JessyTsu1/ChatLaw-13B)，[LawGPT](https://github.com/pengxiao-song/LaWGPT) 等大模型的 法律 NLP 基础能力评测工作
- 公布法律能力和基础任务评测分数计算方式

## Contents

- [⚖️SCULaiw: Legal Evaluation Framework (BIAN)](#️sculaiw-legal-evaluation-framework-bian)
  - [新闻](#新闻)
  - [Contents](#contents)
    - [任务评测结构图](#任务评测结构图)
    - [评测](#评测)
      - [环境准备](#环境准备)
      - [自动评估](#自动评估)
    - [任务](#任务)
    - [指令微调数据集](#指令微调数据集)
    - [评分机制](#评分机制)

### 任务评测结构图

<img src="https://github.com/Dai-shen/SCULaiw/blob/main/resources/task_framwork.png"  width="50%" height="50%"></img>

### 评测

- 我们将按照评测结构图中的13个基础任务持续评测现存大模型在这些任务上的表现，详情可见[模型评测榜单](https://huggingface.co/spaces/daishen/SCULaiw)。
- 评测模型不仅有未开源的 ChatGPT 和 GPT-4，而且还有 [Baichuan2](https://huggingface.co/baichuan-inc/Baichuan2-13B-Chat), [chatglm2](https://huggingface.co/THUDM/chatglm2-6b)，[HanFei](https://github.com/siat-nlp/HanFei)，[Lawyer LLaMa](https://github.com/AndrewZhe/lawyer-llama/tree/main), [智海-录问](https://modelscope.cn/models/wisdomOcean/wisdomInterrogatory/summary) 等开源的通用大模型和中文法律大模型

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
    --model "hf-causal-experimental" \
    --model_args "use_accelerate=True,pretrained=baichuan-inc/Baichuan2-13B-Chat,tokenizer=baichuan-inc/Baichuan2-13B-Chat,use_fast=False" \
    --tasks "legal_ar,legal_er,legal_ner"
```

### 任务

我们经过 <strong>法学专家</strong> 的多次指导，从法学角度上评测法律 NLP 的<strong>三</strong>大能力，共计<strong>13</strong>个基础任务

- 法律 NLP 基础能力：主要评测法律基础任务、 NLP 基础任务和法律信息抽取的能力，包括法条推送、要素识别、命名实体识别、司法要点摘要和案件识别 5 个基础任务
- 法律知识理解能力：主要评测大模型对相关法律文本的知识理解的能力，包括刑事裁判预测、民事裁判预测、法律问答、争议焦点挖掘和类案匹配 5 个基础任务
- 法律知识应用能力：进一步评测大模型对法律领域知识的应用能力，包括司法说理生成、案情理解和法律咨询 3 个基础任务
  
下面是评测任务的具体描述

<table>

  <tr>
  <td>能力</td>
  <td>任务</td>
  <td>描述</td>
  </tr>

  <tr>
    <td rowspan="5">法律NLP<br>基础能力</td>
    <td>法条推送</td>
    <td>该任务是司法实践应用上的基础任务，在提供法律领域的智能化支持和辅助决策上起着重要作用，旨在根据案件描述给出其相关法条</td>
  </tr>
  <tr>
    <td>要素识别</td>
    <td>在司法领域，案件要素识别任务的主要目的是从案件描述中自动提取关键事实描述。在给定司法文书的相关段落之后，系统对每句话进行分析和判断，以确定关键的案件要素</td>
  </tr>
  <tr>
    <td>案件识别</td>
    <td>民事案件和刑事案件是两种不同类型的法律案件。民事案件是解决个人纠纷和维护权益的法律程序，刑事案件是为了维护社会秩序和惩罚犯罪行为的法律程序。本任务旨在根据相关的案件描述判断其为刑事案件还是民事案件</td>
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
    <td rowspan="5">法律知识<br>理解能力</td>
    <td>争议焦点挖掘</td>
    <td>在法院的庭审过程中，裁判文书起着记录辩、诉双方观点证据的重要作用。本任务旨在抽取出裁判文书中辩方诉方之间的逻辑交互论点对，即争议焦点</td>
  </tr>
  <tr>
    <td>类案匹配</td>
    <td>在英美法系国家，如美国、加拿大和印度，司法裁决是根据过去类似的代表性案例做出的。因此，如何识别最相似的案件是英美法系在判决中首要关注的问题</td>
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
    <td rowspan="3">法律知识<br>应用能力</td>
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

### 指令微调数据集

这里展示用于各个基础任务关于大模型的三大法律能力评测的指令微调数据集 SCULaiw-DataSet-FT，有关数据集更多详细信息可见 [SCULaiw-DataSet](https://github.com/Dai-shen/SCULaiw-DataSet)。数据集 SCULaiw-DataSet-FT 整理中，等待后续公布

<table>

  <tr>
    <td>能力层级</td>
    <td>任务</td>
    <td>原始数据集</td>
    <td>指令微调<br>数据集</td>
    <td>指令微调<br>数据集大小</td>
  </tr>

  <tr>
    <td rowspan="5">法律NLP<br>基础能力</td>
    <td>法条推送</td>
    <td>CAIL-2018</td>
    <td><a href="https://www.example.com">legal_ar</a></td>
    <td>5k</td>
  </tr>
  <tr>
    <td>要素识别</td>
    <td>CAIL-2019</td>
    <td><a href="https://www.example.com">legal_er</a></td>
    <td>5k</td>
  </tr>
  <tr>
    <td>命名实体识别</td>
    <td>CAIL-2021</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>司法要点摘要</td>
    <td>CAIL-2020</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>案件识别</td>
    <td>CJRC</td>
    <td><a href="https://www.example.com">legal_er</a></td>
    <td>10k</td>
  </tr>

  <tr>
    <td rowspan="5">法律知识<br>理解能力</td>
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
    <td>Undisclosed</td>
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
    <td rowspan="3">法律知识<br>应用能力</td>
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

- 对于每一项评测能力，其分数为所评测的所有基础子任务分数的平均值，并且模型在四项能力的总分也取平均数，总分都为100分
- 对于每项能力特定的基础任务，使用已构建的指令微调数据集，根据大模型在该任务上的输出与真实标签客观的计算相应的评估指标，作为模型在该任务上的分数 （评估指标取值范围均为 0-1 之间，任务评分 = 评估指标 * 100）
