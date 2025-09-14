from __future__ import annotations

def lcs_length(a: str, b: str) -> int:
    """LCS 长度（滚动数组，O(min(n,m)) 空间）"""
    m, n = len(a), len(b)
    if m == 0 or n == 0:
        return 0
    # 让 b 成更短的一边，减少列数
    if n > m:
        a, b = b, a
        m, n = n, m

    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
    for i in range(1, m + 1):
        ai = a[i - 1]
        for j in range(1, n + 1):
            if ai == b[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                left = curr[j - 1]
                up   = prev[j]
                curr[j] = left if left >= up else up
        prev, curr = curr, [0] * (n + 1)
    return prev[n]

def lcs_similarity_pct(original: str, copied: str) -> float:
    """返回 LCS 相似度百分比（以“抄袭文本长度”为分母）。copied 为空则 0.0。"""
    if not copied:
        return 0.0
    return (lcs_length(original, copied) / len(copied)) * 100.0

def safe_lcs_length(a: str, b: str) -> int:
    """超长触发 MemoryError 时返回 0（稳健性演示）"""
    try:
        return lcs_length(a, b)
    except MemoryError:
        return 0
