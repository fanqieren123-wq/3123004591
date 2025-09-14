from __future__ import annotations
from pathlib import Path

def load_text(path: str) -> str:
    """UTF-8 优先读取；失败回退 GBK（忽略错误）；失败返回空串，不抛异常。"""
    p = Path(path)
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return p.read_text(encoding="gbk", errors="ignore")
        except Exception:
            return ""
    except Exception:
        return ""

def save_line_append(path: str, line: str) -> None:
    """追加写入一行；自动建父目录。"""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(line + ("\n" if not line.endswith("\n") else ""))

def only_name(path: str) -> str:
    """返回纯文件名"""
    return Path(path).name
