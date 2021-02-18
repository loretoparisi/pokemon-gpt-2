import gpt_2_simple as gpt2
from datetime import datetime

# model name can be 124M | 355M | 774M | 1558M
model_name="124M"
gpt2.download_gpt2(model_name=model_name)