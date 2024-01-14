from rouge import Rouge
from nltk.translate.bleu_score import sentence_bleu
import numpy as np
from sklearn.metrics import matthews_corrcoef, f1_score, accuracy_score


def mcc(preds, answers):
    set_true = {label: i for i, label in enumerate(list(set(answers)))}
    preds = [set_true.get(pred, -1) for pred in preds]
    golds = [set_true.get(gold, -1) for gold in answers]
    return matthews_corrcoef(golds, preds)

def insert_space(text):
    if not text:  # if text is ''
        text = ' '
    result = ''
    for i in range(0, len(text), 1):
        result += text[i:i + 1] + ' '
    # print(result)
    return result[:-1]


def cal_rouge(generated, reference, t='rouge-1'):
    rouge = Rouge()
    rouge_score = rouge.get_scores(hyps=generated, refs=reference)
    result = rouge_score[0][t]
    return result['p'], result['r'], result['f']


def calculate_rouge_all(data):
    scores = {
        "ROUGE-1": {"P": 0, "R": 0, "F1": 0},
        "ROUGE-2": {"P": 0, "R": 0, "F1": 0},
        "ROUGE-L": {"P": 0, "R": 0, "F1": 0},
    }
    generated, reference = [], []
    for item in data:
        generated.append(insert_space(item["logit_0"]))
        reference.append(insert_space(item["truth"]))

    rouge = Rouge()
    rouge_score = rouge.get_scores(hyps=generated, refs=reference, avg=True)
    result = rouge_score

    for key in scores:
        ty = ''
        if key == 'ROUGE-1':
            ty = "rouge-1"
        if key == 'ROUGE-2':
            ty = "rouge-2"
        if key == 'ROUGE-L':
            ty = "rouge-l"
        for metric in scores[key]:
            me = ''
            if metric == 'P':
                me = 'p'
            if metric == 'F1':
                me = 'f'
            if metric == 'R':
                me = 'r'
            scores[key][metric] = format(result[ty][me], '.4f')

    return scores


def bleu_n(generated, reference, n):
    # cumulative BLEU scores
    if n == 1:
        return sentence_bleu(reference, generated, weights=(1, 0, 0, 0))
    if n == 2:
        return sentence_bleu(reference, generated, weights=(0.5, 0.5, 0, 0))
    if n == 3:
        return sentence_bleu(reference, generated, weights=(0.333, 0.333, 0, 0))
    if n == 4:
        return sentence_bleu(reference, generated, weights=(0.25, 0.25, 0.25, 0.25))


def calculate_bleu(data):
    scores = {
        "BLEU-1": 0,
        "BLEU-2": 0,
        "BLEU-3": 0,
        "BLEU-4": 0,
    }

    for item in data:
        generated = list(item["logit_0"])
        reference = [list(item["truth"])]

        for n, key in [(1, "BLEU-1"), (2, "BLEU-2"), (3, "BLEU-3"), (4, "BLEU-4")]:
            score = bleu_n(generated, reference, n)
            scores[key] += score

    num_items = len(data)
    for key in scores:
        scores[key] /= num_items
        scores[key] = format(scores[key], '.4f')
    return scores


def Classification(data, task):
    task_labels_dict = {
        # First
        'legal_ar': ["264", "133", "234"],
        "legal_er": ['LB10', 'LB11', 'LB12', 'LB13', 'LB14', 'LB15', 'LB16', 'LB17', 'LB18', 'LB19',
                     'LB20', 'LB1', 'LB2', 'LB3', 'LB4', 'LB5', 'LB6', 'LB7', 'LB8', 'LB9'],
        "legal_ner": 'ner',
        "legal_cr": ['刑事', '民事'],
        # Second
        "legal_cfm": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        "legal_scm": ['B', 'C'],
        "legal_cp": ['69', '50', '124'],
        "legal_ptp": ['A', 'B', 'C'],
        "legal_ctp": ['A', 'B', 'C'],
        "legal_lqa": ['A', 'B', 'C', 'D'],
    }
    labels = task_labels_dict[task]
    result = []
    pred = []  # prediction label
    answers = []  # target label

    missing = 0
    for item in data:
        answers.append(item['truth'].lower())
        miss = 1
        for answer1 in labels:
            if answer1.lower() in item['logit_0'].lower():
                pred.append(answer1.lower())
                miss -= 1
                break
        if miss == 1:
            missing += 1
            pred.append("missing")
    y_true = np.array(answers)
    y_pred = np.array(pred)
    labels_lower = list(set(answers))

    result.append(
        {
            'task': task,
            'acc': f'{accuracy_score(y_true, y_pred):.4f}',
            'missing': format(missing / len(data), '.4f'),
            'f1': f"{f1_score(y_true, y_pred, average='weighted', labels=labels_lower):.4f}",
            'macro_f1': f"{f1_score(y_true, y_pred, average='macro', labels=labels_lower):.4f}",
            'mcc': f"{mcc(preds=pred, answers=answers):.4f}"
        }
    )
    return result

def Ner(data, task):
    result = []
    acc_list = []
    rouges = {
        "ROUGE-1": {"P": 0, "R": 0, "F1": 0},
        "ROUGE-2": {"P": 0, "R": 0, "F1": 0},
        "ROUGE-L": {"P": 0, "R": 0, "F1": 0},
    }
    for line in data:
        text = line['prompt_0']
        pred = line['logit_0'].lower()
        true = line['truth'].lower()
        acc1 = 1 if pred == true else 0
        acc_list.append(acc1)
        generated = [insert_space(pred)]
        reference = [insert_space(true)]
        for t, key in [("rouge-1", "ROUGE-1"), ("rouge-2", "ROUGE-2"), ("rouge-l", "ROUGE-L")]:
            score = cal_rouge(generated, reference, t)
            rouges[key]["P"] += score[0]
            rouges[key]["R"] += score[1]
            rouges[key]["F1"] += score[2]
    acc = sum(acc_list) / len(acc_list)
    num_items = len(data)
    for key in rouges:
        for metric in rouges[key]:
            rouges[key][metric] /= num_items
            rouges[key][metric] = format(rouges[key][metric], '.4f')
    result.append(
        {
            'task': task,
            'acc': format(acc, '.4f'),
            'ROUGE-1': rouges['ROUGE-1']['R'],
            'ROUGE-2': rouges['ROUGE-2']['R'],
            'ROUGE-L': rouges['ROUGE-L']['R'],
        }
    )
    return result


def TG(data, task):
    scores_rouge = calculate_rouge_all(data)
    scores_belu = calculate_bleu(data)
    result = []
    result.append(
        {
            'task': task,
            'ROUGE-1': scores_rouge['ROUGE-1']['R'],
            'ROUGE-2': scores_rouge['ROUGE-2']['R'],
            'ROUGE-L': scores_rouge['ROUGE-L']['R'],
            'BLEU-1': scores_belu['BLEU-1'],
            'BLEU-2': scores_belu['BLEU-2'],
            'BLEU-3': scores_belu['BLEU-3'],
            'BLEU-4': scores_belu['BLEU-4'],

        }
    )
    return result





