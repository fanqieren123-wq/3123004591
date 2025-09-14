

```markdown
# LCS 相似度检测项目

一个基于 **最长公共子序列（LCS）算法** 的文本相似度检测工具，支持中文文本。

---

## ✨ 功能特性
- **文本相似度计算**：计算两份文本的最长公共子序列并输出相似率（百分比）。
- **中文友好**：UTF-8 优先，自动 GBK 回退。
- **性能优化**：滚动数组降低内存使用，适合大文本。
- **自动化测试**：`pytest` + `coverage` 生成覆盖率报告。
- **性能分析**：`cProfile` + `SnakeViz` 生成性能热点分析。

---

## 📂 目录结构
```

.
├─ algos.py            # LCS 核心算法
├─ io\_utils.py         # 文件读写工具
├─ runner.py           # 命令行入口逻辑
├─ main.py             # 评测兼容入口（调用 runner.main）
├─ generate\_samples.py # 生成测试数据
├─ tests/              # 单元测试
├─ htmlcov/            # 覆盖率 HTML 报告
└─ result.txt          # 结果输出示例

````

---

## 🚀 安装与运行

1. 克隆仓库
   ```bash
   git clone https://github.com/你的用户名/3123004591.git
   cd 3123004591
````

2. 安装依赖（可选）

   ```bash
   pip install -r requirements.txt
   ```

   > 主要依赖：`pytest`, `pytest-cov`

3. 运行相似度检测

   ```bash
   python main.py data/orig_1.txt data/copy_1.txt result.txt
   ```

   输出示例：

   ```
   The similarity rate between document orig_1.txt and document copy_1.txt is 82.50%
   ```

---

## 🧪 测试与覆盖率

运行单元测试并生成覆盖率报告：

```bash
pytest --cov=. --cov-report=term-missing --cov-report=html
```

生成的 HTML 报告位于 `htmlcov/index.html`。

---

## 📈 性能分析

生成性能画像并查看热点函数：

```bash
python -m cProfile -o prof.out main.py data/orig_1.txt data/copy_1.txt result.txt
snakeviz prof.out
```

---

## 🗂️ 提交与版本管理

* 代码已使用 **GitHub** 进行版本管理。
* 按功能分阶段提交（至少基础功能与扩展功能两次 commit）。

---

## 📜 许可证

MIT License

````

---

### 使用方法
1. 在项目根目录创建一个名为 **README.md** 的文件。
2. 将上述内容全部复制进去。
3. 在命令行提交：
   ```bash
   git add README.md
   git commit -m "docs: 添加项目 README"
   git push origin main
````


