import subprocess, os, sys
from pathlib import Path
from algos import lcs_length, lcs_similarity_pct
from io_utils import load_text, only_name
from runner import run_once

def test_lcs_basic():
    assert lcs_length("abcde","ace") == 3
    assert lcs_length("aaaa","aa") == 2
    assert lcs_length("","abc") == 0

def test_lcs_equal_text():
    s = "今天天气真好！"
    assert lcs_length(s, s) == len(s)

def test_similarity_pct():
    assert abs(lcs_similarity_pct("abcd","abxd") - (3/4*100)) < 1e-9
    assert lcs_similarity_pct("abc","") == 0.0

def test_load_text_utf8(tmp_path):
    p = tmp_path/"a.txt"
    p.write_text("中文OK", encoding="utf-8")
    assert load_text(str(p)) == "中文OK"

def test_only_name():
    assert only_name(r"C:\a\b\c.txt") == "c.txt"
    assert only_name("/a/b/c.txt") == "c.txt"

def test_run_once_e2e(tmp_path):
    orig = tmp_path/"orig.txt"; copy = tmp_path/"copy.txt"; out = tmp_path/"res.txt"
    orig.write_text("abcd", encoding="utf-8")
    copy.write_text("abxd", encoding="utf-8")
    sim = run_once(str(orig), str(copy), str(out))
    assert 0.0 <= sim <= 100.0
    assert out.read_text(encoding="utf-8")

def test_cli_process(tmp_path):
    orig = tmp_path/"orig.txt"; copy = tmp_path/"copy.txt"; out = tmp_path/"res.txt"
    orig.write_text("abcd", encoding="utf-8")
    copy.write_text("abxd", encoding="utf-8")
    r = subprocess.run([sys.executable, "main.py", str(orig), str(copy), str(out)], check=False)
    assert r.returncode == 0
