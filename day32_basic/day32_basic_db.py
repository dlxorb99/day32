# day32_basic_db.py

import os
from pathlib import Path
import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb # JSON데이터 처리
from dotenv import load_dotenv

RULE_VERSION = 'shipping-v1'

load_dotenv()

SQL_DIR = Path(__file__).resolve().parent / "sql"

def execute(name, params=()):
    url = os.getenv("DATABASE_URL", '').strip()
    if not url:
        raise ValueError('DATABASE_URL 환경변수를 설정하세요.')
    sql = (SQL_DIR / name).read_text(encoding='utf-8')
    with psycopg.connect(
        url,
        connect_timeout=10,
        row_factory=dict_row
    ) as conn:
        return conn.execute(sql, params).fetchall()

def save_basic(label, weight, fee):
    label = label.strip()
    params = (label, weight, fee, RULE_VERSION)
    if not label or len(label) > 80:
        raise ValueError('견적 제목은 80자 이내로 입력하세요')
    rows = execute('save_basic.sql', params)
    return rows[0]['id']

def list_basic(keyword=''):
    return execute('list_basic.sql', (f'%{keyword.strip()}%',))

def get_basic(id, fee):
    rows = execute('get_basic.sql', (fee, id))
    return rows[0] if rows else None















































































































