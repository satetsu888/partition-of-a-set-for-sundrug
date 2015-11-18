# partition of a set for sundrug

## 何

sundrug1000店舗記念キャンペーン( http://sundrug-1000cp.com/ )に応募するための組み合わせ問題ソルバー

いわゆる「集合分割問題」というやつを解くことができる

## 使い方

- data.txt にレシートの金額をリストアップ
- `python main.py`

## 注意

10~20個くらいのデータ個数なら１分程度で回答が出せるが、それ以上になると組み合わせ爆発で終わらない

コード内のデータ分割の仕組みをうまく使って適当なところで妥協する必要がある・・・

## 依存

- pulp
- ortoolpy
- itertools
