level1 = ["robustness", "robust"]
level2 = ["artificial intelligence", "machine learning", "neural network"]
level3 = ["explainability", "explanation", "human computation", "design", "adversarial", "transparency", "unknowns", "interpretable", "reasoning", "human knowledge", "confidence", "stability", "resilience", "accuracy", "reliability", "interpretability", "accountability", "noise", "reproducibility", "trustworthy", "performance", "knowledge", "knowledge elicitation", "knowledge base", "human interpretation", "human-in-the-loop"]


queries = []

for k1 in level1:
    for k2 in level2:
        for k3 in level3:
            tmp_query = '\"{}\" AND \"{}\" AND \"{}\"'.format(k1, k2, k3)
            queries.append(tmp_query)

with open("queries_acm_csur.txt", "w") as f:
    for q in queries:
        line = "{}\n".format(q)
        f.write(line)