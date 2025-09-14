#!/usr/bin/env python3
"""
生成个人项目报告：
  - 汇总 cProfile 的 prof.out
  - 汇总 pytest --cov 生成的 coverage.xml
  - 输出 Markdown 报告 REPORT.md
"""
from __future__ import annotations
import argparse
import datetime
import os
import pstats
import xml.etree.ElementTree as ET
from typing import List, Tuple

TEMPLATE = """# 个人项目报告（LCS 相似度检测）

## 概览
- 生成时间：{when}
- 总覆盖率：{cov:.1f}%
- 性能画像文件：{prof}

## 最耗时函数（Top-10，按累计时间）
{tops}

> 上表来自 `cProfile`。建议在报告中贴上 SnakeViz 或 VS 的截图，并圈出最耗时函数。

## 操作示例
```bash
# 生成性能画像
python -m cProfile -o {prof} main.py A.txt B.txt result.txt

# 查看热点函数
python - <<'PY'
import pstats
pstats.Stats("{prof}").sort_stats("cumtime").print_stats(20)
PY

# 生成覆盖率报告
pytest --cov=. --cov-report=term-missing --cov-report=html --cov-report=xml
# 打开 htmlcov/index.html 截图
"""

def read_coverage(xml_path: str) -> float:
    """读取 coverage.xml 中的总覆盖率百分比"""
    if not os.path.exists(xml_path):
        return 0.0
    try:
        root = ET.parse(xml_path).getroot()
        return float(root.attrib.get("line-rate", "0")) * 100.0
    except Exception:
        return 0.0

def top_funcs(prof: str, n: int = 10) -> List[Tuple[float, float, int, str]]:
    """返回 (cumtime, tottime, calls, 'file:line(func)') 列表"""
    if not os.path.exists(prof):
        return []
    st = pstats.Stats(prof)
    rows: List[Tuple[float, float, int, str]] = []
    # st.stats: {(file, line, func): (cc, nc, tt, ct, callers)}
    for (file, line, func), (cc, nc, tt, ct, callers) in st.stats.items():
        rows.append((ct, tt, nc, f"{file}:{line}({func})"))
        rows.sort(key=lambda x: x[0], reverse=True) # 按 cumtime 降序
    return rows[:n]

def rows_to_md(rows: List[Tuple[float, float, int, str]]) -> str:
    if not rows:
        return "无性能数据，请先生成 prof.out"
    md = [
    "| # | 函数 | 调用数 | tottime(s) | cumtime(s) |",
    "|---:|------|------:|----------:|----------:|",
    ]
    for i, (ct, tt, nc, desc) in enumerate(rows, 1):
        md.append(f"| {i} | {desc} | {nc} | {tt:.6f} | {ct:.6f} |")
    return "\n".join(md)

def main():
    ap = argparse.ArgumentParser(description="生成项目性能+覆盖率报告")
    ap.add_argument("--prof", default="prof.out", help="cProfile 输出文件")
    ap.add_argument("--covxml", default="coverage.xml", help="pytest --cov 生成的 XML")
    ap.add_argument("--out", default="REPORT.md", help="输出 Markdown 文件")
    args = ap.parse_args()

  
    cov = read_coverage(args.covxml)
    tops_md = rows_to_md(top_funcs(args.prof))
    md = TEMPLATE.format(
        when=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        cov=cov,
        prof=args.prof,
        tops=tops_md,
    )

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"[OK] 报告已生成：{args.out}")

if __name__ == "__main__":
    main()
