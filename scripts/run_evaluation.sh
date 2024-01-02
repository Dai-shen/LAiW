gpu_devices="1,2"
tasks_name=""  # task in TASK_REGISTRY

model_name="baichuan2-13b"
pretrained_model="model_path"

file_path="../result/$model_name/$tasks_name.log"
write_out_path="../result/$model_name/write_out/"
mkdir -p "$(dirname "$file_path")"
mkdir -p "$(dirname "$write_out_path")"

export CUDA_VISIBLE_DEVICES="$gpu_devices"
echo "$file_path"
nohup python -u ../src/eval.py \
    --model "hf-causal-experimental" \
    --model_args "use_accelerate=True,pretrained=$pretrained_model,tokenizer=$pretrained_model,use_fast=False,trust_remote_code=True" \
    --tasks "$tasks_name" \
    --no_cache \
    --num_fewshot 0 \
    --write_out \
    --output_base_path "$write_out_path" \
    > "$file_path" 2>&1 &

# --model info --> src/financial-evaluation/lm_eval/models/__init__.py

