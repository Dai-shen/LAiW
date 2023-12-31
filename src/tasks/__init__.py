from pprint import pprint
from typing import List, Union

import json
import lm_eval.base

from . import legal

TASK_REGISTRY = {
    # wyx-dmv-syn-data
    "syn_german": legal.Syn_german,
    # financial
    "legal_fpb": legal.FPB,
    "legal_fiqasa": legal.FIQASA,
    "legal_finqa": legal.FinQA,
    "legal_convfinqa": legal.ConvFinQA,
    "legal_headlines": legal.Headlines,
    "legal_finer_ord": legal.FinerOrd,
    "legal_fomc": legal.FOMC,
    "legal_german": legal.German,
    "legal_australian": legal.Australian,
    "legal_ectsum": legal.ECTSUM,
    "legal_edtsum": legal.EDTSUM,
    # First
    "legal_ar": legal.AR,
    "legal_er": legal.ER,
    "legal_ner": legal.NER,
    "legal_cr": legal.CR,
    "legal_js": legal.JS,
    # Second
    "legal_scm": legal.SCM,
    "legal_cp": legal.CP,
    "legal_ptp": legal.PTP,
    "legal_ctp": legal.CTP,
    "legal_lqa": legal.LQA,
    "legal_cfm": legal.CFM,
    # Third
    "legal_jrg": legal.JRG,
    "legal_cu": legal.CU,
    "legal_lc": legal.LC,
    # Tag
    "legal_jrg_tag": legal.JRG_TAG,
    "legal_lc_tag": legal.LC_TAG,
    # FYB-CER
    "legal_cer": legal.CER,
    # chatglm-ctp
    "legal_ctp0": legal.CTP0,
    "legal_ctp1": legal.CTP1,
    "legal_ctp2": legal.CTP2,
    "legal_ctp3": legal.CTP3,
    "legal_ctp4": legal.CTP4,
    "legal_ctp5": legal.CTP5,
    "legal_ctp6": legal.CTP6,
    "legal_ctp_glm": legal.CTP_GLM, 
    **legal.SM_TASKS,
}

ALL_TASKS = sorted(list(TASK_REGISTRY))

_EXAMPLE_JSON_PATH = "split:key:/absolute/path/to/data.json"


def add_json_task(task_name):
    """Add a JSON perplexity task if the given task name matches the
    JSON task specification.

    See `json.JsonPerplexity`.
    """
    if not task_name.startswith("json"):
        return

    def create_json_task():
        splits = task_name.split("=", 1)
        if len(splits) != 2 or not splits[1]:
            raise ValueError(
                "json tasks need a path argument pointing to the local "
                "dataset, specified like this: json="
                + _EXAMPLE_JSON_PATH
                + ' (if there are no splits, use "train")'
            )

        json_path = splits[1]
        if json_path == _EXAMPLE_JSON_PATH:
            raise ValueError(
                "please do not copy the example path directly, but substitute "
                "it with a path to your local dataset"
            )
        return lambda: json.JsonPerplexity(json_path)

    TASK_REGISTRY[task_name] = create_json_task()


def get_task(task_name):
    try:
        add_json_task(task_name)
        return TASK_REGISTRY[task_name]
    except KeyError:
        print("Available tasks:")
        pprint(TASK_REGISTRY)
        raise KeyError(f"Missing task {task_name}")


def get_task_name_from_object(task_object):
    for name, class_ in TASK_REGISTRY.items():
        if class_ is task_object:
            return name

    # this gives a mechanism for non-registered tasks to have a custom name anyways when reporting
    return (
        task_object.EVAL_HARNESS_NAME
        if hasattr(task_object, "EVAL_HARNESS_NAME")
        else type(task_object).__name__
    )


def get_task_dict(task_name_list: List[Union[str, lm_eval.base.Task]]):
    task_name_dict = {
        task_name: get_task(task_name)()
        for task_name in task_name_list
        if isinstance(task_name, str)
    }
    task_name_from_object_dict = {
        get_task_name_from_object(task_object): task_object
        for task_object in task_name_list
        if not isinstance(task_object, str)
    }
    assert set(task_name_dict.keys()).isdisjoint(set(task_name_from_object_dict.keys()))
    return {**task_name_dict, **task_name_from_object_dict}
