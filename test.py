def calculate_total(price, tax_rate):
    # 目标：计算商品含税总价（价格 + 价格*税率）
    # 注意：这里故意写错了一个计算逻辑，等会让 Codex 来找！
    total = price + tax_rate
    return total

print("最终价格是:", calculate_total(100, 0.05))
