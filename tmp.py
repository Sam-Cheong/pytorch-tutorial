import torch
checkpoint = torch.load('model.ckpt')
print(checkpoint.keys())  # 查看有哪些參數