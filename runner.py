from __future__ import annotations
import sys
import argparse
from algos import lcs_similarity_pct
from io_utils import load_text, save_line_append, only_name

def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="基于 LCS 的字符级相似度检测")
    p.add_argument("original", help="原文文件路径")
    p.add_argument("copied",   help="抄袭版文件路径")
    p.add_argument("output",   help="答案文件路径（结果将追加写入）")
    return p.parse_args(argv[1:])

def format_result_line(orig_path: str, copy_path: str, sim_pct: float) -> str:
    return (
        f"The similarity rate between document {only_name(orig_path)} "
        f"and ducument {only_name(copy_path)} is {sim_pct:.2f}%"
    )

def run_once(original_path: str, copied_path: str, output_path: str) -> float:
    s1 = load_text(original_path)
    s2 = load_text(copied_path)
    if not s1 or not s2:
        save_line_append(
            output_path,
            f"{only_name(original_path)}文件与{only_name(copied_path)}文件的重复率为0.00%（检测到空文件）",
        )
        return 0.0

    sim = lcs_similarity_pct(s1, s2)
    save_line_append(output_path, format_result_line(original_path, copied_path, sim))
    return sim

def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        _ = run_once(args.original, args.copied, args.output)
        return 0
    except Exception:
        return 2

if __name__ == "__main__":
    sys.exit(main(sys.argv))
