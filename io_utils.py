from __future__ import annotations
from pathlib import Path

def load_text(path: str) -> str:
    """UTF-8 优先读取；失败回退 GBK（忽略错误）；失败返回空串，不抛异常。
    
    尝试以不同编码格式读取文本文件，优先使用UTF-8编码，失败后尝试GBK编码。
    
    Args:
        path: 文件路径
        
    Returns:
        文件内容字符串，读取失败时返回空字符串
    """
    p = Path(path)
    try:
        # 首先尝试使用UTF-8编码读取文件
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            # UTF-8失败时，尝试使用GBK编码并忽略错误
            return p.read_text(encoding="gbk", errors="ignore")
        except Exception:
            # 所有尝试都失败时返回空字符串
            return ""
    except Exception:
        # 其他异常情况也返回空字符串
        return ""

def save_line_append(path: str, line: str) -> None:
    """追加写入一行；自动建父目录。
    
    将一行文本追加写入到指定文件中，如果文件或目录不存在会自动创建。
    
    Args:
        path: 文件路径
        line: 要写入的行内容
    """
    p = Path(path)
    # 创建父目录（如果不存在），exist_ok=True避免目录已存在时的异常
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        # 确保每行以换行符结尾
        f.write(line + ("\n" if not line.endswith("\n") else ""))

def only_name(path: str) -> str:
    """返回纯文件名
    
    从完整路径中提取文件名部分（包含扩展名）。
    
    Args:
        path: 完整文件路径
        
    Returns:
        文件名字符串
    """
    return Path(path).name