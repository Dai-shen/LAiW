import json
import os
import time

from legal_metrics import Classification, Ner, TG
import warnings

warnings.filterwarnings("ignore")


# Recover（Optional）
# warnings.resetwarnings()

def get_args():
    model_names = list(os.listdir("./eval_results"))
    task_dict = {
        # First
        'legal_ar': 'cls',
        "legal_er": 'cls',
        "legal_ner": 'ner',
        "legal_js": 'tg',
        "legal_cr": 'cls',
        # Second
        "legal_cfm": 'cls',
        "legal_scm": 'cls',
        "legal_cp": 'cls',
        "legal_ptp": 'cls',
        "legal_ctp": 'cls',
        "legal_lqa": 'cls',
        # Third
        "legal_jrg": 'tg',
        "legal_cu": 'tg',
        "legal_lc": 'tg',
        # Tag
        "legal_jrg_tag": 'tg',
        "legal_lc_tag": 'tg',
    }
    return model_names, task_dict


def eval_data(data_list, tasks_dict, task):
    results = None
    if task == 'legal_ctp_glm':
        task = 'legal_ctp'
    if tasks_dict[task] == 'cls':
        results = Classification(data=data_list, task=task)
    if tasks_dict[task] == 'ner':
        results = Ner(data, task)
    if tasks_dict[task] == 'tg':
        results = TG(data, task)
    # Save results
    if not os.path.exists('./metrics_result/'):
        os.makedirs('./metrics_result/')
    save_results(result=results, result_path=f"./metrics_result/{model}.jsonl")
    return results


def save_results(result, result_path):
    with open(result_path, "a", encoding='utf-8') as file:
        for item in result:
            json.dump(item, file, ensure_ascii=False)
            file.write('\n')


if __name__ == "__main__":
    model_name, tasks_dict = get_args()
    start_time = time.time()
    for _, model in enumerate(model_name, start=1):
        tasks = list(tasks_dict.keys())
        if model not in ['GPT-4', 'ChatGPT', 'Baichuan2-13B-Chat', 'Fuzi-Mingcha-6B', 'HanFei-7B', 'Lawyer-LLaMA-13B',
                         'LexiLaw-6B']:
            tasks.remove('legal_lc_tag')
            tasks.remove('legal_jrg_tag')
        if model in ['ChatGLM-6B', 'Fuzi-Mingcha-6B', 'LexiLaw-6B']:
            tasks[tasks.index('legal_ctp')] = 'legal_ctp_glm'
        for task in tasks:
            file_path = f"./eval_results/{model}/{task}_write_out_info.json"
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                result = eval_data(data, tasks_dict, task)
        print(f"{_} --> {model} have done!")
    end_time = time.time()

    print("Consume Time (Second): ", end_time - start_time, "")
