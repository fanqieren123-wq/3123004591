from __future__ import annotations
import sys
import argparse
# 导入算法模块中的LCS相似度计算函数
from algos import lcs_similarity_pct
# 导入IO工具模块
from io_utils import load_text, save_line_append, only_name

def parse_args(argv: list[str]) -> argparse.Namespace:
    """解析命令行参数
    
    Args:
        argv: 命令行参数列表
        
    Returns:
        解析后的参数命名空间对象
    """
    p = argparse.ArgumentParser(description="基于 LCS 的字符级相似度检测")
    p.add_argument("original", help="原文文件路径")
    p.add_argument("copied",   help="抄袭版文件路径")
    p.add_argument("output",   help="答案文件路径（结果将追加写入）")
    return p.parse_args(argv[1:])

def format_result_line(orig_path: str, copy_path: str, sim_pct: float) -> str:
    """格式化结果行字符串
    
    Args:
        orig_path: 原文文件路径
        copy_path: 抄袭文件路径
        sim_pct: 相似度百分比
        
    Returns:
        格式化后的结果字符串
    """
    return (
        f"The similarity rate between document {only_name(orig_path)} "
        f"and ducument {only_name(copy_path)} is {sim_pct:.2f}%"
    )

def run_once(original_path: str, copied_path: str, output_path: str) -> float:
    """执行一次相似度检测流程
    
    Args:
        original_path: 原文文件路径
        copied_path: 抄袭文件路径
        output_path: 输出结果文件路径
        
    Returns:
        计算得到的相似度百分比
    """
    # 读取两个文件的内容
    s1 = load_text(original_path)
    s2 = load_text(copied_path)
    # 如果任一文件为空，则记录空文件信息并返回0.0
    if not s1 or not s2:
        save_line_append(
            output_path,
            f"{only_name(original_path)}文件与{only_name(copied_path)}文件的重复率为0.00%（检测到空文件）",
        )
        return 0.0

    # 计算相似度并保存结果
    sim = lcs_similarity_pct(s1, s2)
    save_line_append(output_path, format_result_line(original_path, copied_path, sim))
    return sim

def main(argv: list[str]) -> int:
    """主函数
    
    Args:
        argv: 命令行参数列表
        
    Returns:
        程序退出码：0表示成功，2表示异常
    """
    args = parse_args(argv)
    try:
        # 执行相似度检测
        _ = run_once(args.original, args.copied, args.output)
        return 0
    except Exception:
        # 发生异常时返回错误码2
        return 2

if __name__ == "__main__":
    # 程序入口点，调用main函数并退出
    sys.exit(main(sys.argv))