#!/usr/bin/env python3

import os

BASE_URL = "https://huggingface.co/deepseek-ai/"
REPOS = [
    "DeepSeek-R1-Distill-Qwen-1.5B",
    "DeepSeek-R1-Distill-Qwen-7B",
    "DeepSeek-R1-Distill-Llama-8B",
    "DeepSeek-R1-Distill-Qwen-14B",
    "DeepSeek-R1-Distill-Qwen-32B",
    "DeepSeek-R1-Distill-Llama-70B",
    "DeepSeek-R1-Zero",
    "DeepSeek-R1"
]

for repo in REPOS:
    URL = f"{BASE_URL}{repo}"
    if os.path.exists(repo):
        print(f"Skipping {repo} as it already exists")
        continue
    print(f"Cloning {repo}...")
    os.system(f"git clone {URL}")
