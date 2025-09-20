from __future__ import annotations

def lcs_length(a: str, b: str) -> int:
    """LCS 长度（滚动数组，O(min(n,m)) 空间）
    
    使用动态规划计算两个字符串的最长公共子序列(Longest Common Subsequence)长度。
    通过滚动数组优化空间复杂度至 O(min(n,m))。
    
    Args:
        a: 第一个字符串
        b: 第二个字符串
    
    Returns:
        两个字符串的LCS长度
    """
    m, n = len(a), len(b)
    # 如果任一字符串为空，则LCS长度为0
    if m == 0 or n == 0:
        return 0
    # 让 b 成为较短的字符串，以减少空间使用
    if n > m:
        a, b = b, a
        m, n = n, m

    # 使用两个数组实现滚动数组优化，prev表示上一行，curr表示当前行
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
    
    # 动态规划填表过程
    for i in range(1, m + 1):
        ai = a[i - 1]
        for j in range(1, n + 1):
            # 如果字符相等，则当前LCS长度为左上角值加1
            if ai == b[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                # 否则取左边和上边的最大值
                left = curr[j - 1]
                up   = prev[j]
                curr[j] = left if left >= up else up
        # 滚动数组：将当前行变为下一轮的上一行
        prev, curr = curr, [0] * (n + 1)
    return prev[n]

def lcs_similarity_pct(original: str, copied: str) -> float:
    """返回 LCS 相似度百分比（以"抄袭文本长度"为分母）。copied 为空则 0.0。
    
    计算两个文本的相似度百分比，以copied文本长度作为分母。
    
    Args:
        original: 原始文本
        copied: 抄袭文本（作为分母）
    
    Returns:
        相似度百分比（0.0-100.0之间的浮点数）
    """
    # 如果抄袭文本为空，则相似度为0
    if not copied:
        return 0.0
    # 计算LCS长度占抄袭文本长度的百分比
    return (lcs_length(original, copied) / len(copied)) * 100.0

def safe_lcs_length(a: str, b: str) -> int:
    """超长触发 MemoryError 时返回 0（稳健性演示）
    
    对 lcs_length 函数的包装，增加异常处理机制。
    当处理超长字符串导致内存不足时，返回0而不是抛出异常。
    
    Args:
        a: 第一个字符串
        b: 第二个字符串
    
    Returns:
        LCS长度，如果发生内存错误则返回0
    """
    try:
        return lcs_length(a, b)
    except MemoryError:
        return 0