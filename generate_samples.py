import random, os
def generate_sentence():
    subjects = ["我","你","他","小明","老师","学生"]
    verbs = ["喜欢","讨厌","学习","研究","使用","编写"]
    objects = ["人工智能","机器学习","Python","C++","论文","算法"]
    return random.choice(subjects)+random.choice(verbs)+random.choice(objects)+"。"

def make_copied_version(text: str) -> str:
    replacements = {"喜欢":"热爱","讨厌":"不喜欢","学习":"研究","研究":"学习","使用":"利用","编写":"撰写",
                    "人工智能":"AI","机器学习":"Machine Learning","论文":"文章","算法":"方法"}
    copied = text
    for k,v in replacements.items():
        if k in copied and random.random() < 0.5:
            copied = copied.replace(k, v, 1)
    return copied

def generate_dataset(num_pairs=5, output_dir="data"):
    os.makedirs(output_dir, exist_ok=True)
    for i in range(1, num_pairs+1):
        orig_file = os.path.join(output_dir, f"orig_{i}.txt")
        copy_file = os.path.join(output_dir, f"copy_{i}.txt")
        orig_text = "\n".join(generate_sentence() for _ in range(5))
        copy_text = "\n".join(make_copied_version(s) for s in orig_text.splitlines())
        open(orig_file, "w", encoding="utf-8").write(orig_text)
        open(copy_file, "w", encoding="utf-8").write(copy_text)
        print(f"生成: {orig_file}, {copy_file}")
    print("\n示例：python main.py data/orig_1.txt data/copy_1.txt result.txt")

if __name__ == "__main__":
    generate_dataset()
