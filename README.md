# FastAPI-example

FastAPI のexample リポジトリです。

## リポジトリ構成

```
.
├── Dockerfile
├── README.md
├── app
│   ├── example1.py
│   ├── main.py
│   ├── type_hints.py
│   └── type_hints_2.py
├── data
├── docker-compose.yml
├── docs
├── models
├── notebooks
├── pyproject.toml
├── requirements.txt
├── setup.cfg
├── src
│   └── __init__.py
├── tests
│   └── __init__.py
└── work
```

## 環境詳細

- Python : 3.9.6

## 事前準備

- Docker インストール

## 環境構築

- Docker イメージをビルド

```
docker build  -t myimage .
```

- Docker コンテナを起動

```
docker run -d --name myucontainer -p 80:80 myimage
```

- ブラウザーを立ち上げて下記へアクセス

```
http://127.0.0.1/items/5?q=somequery
http://192.168.99.100/items/5?q=somequery
```

- 対話的APIドキュメント

```
http://127.0.0.1/docs
http://192.168.99.100/docs
```


- その他の対話的APIドキュメント

```
http://127.0.0.1/redoc
http://192.168.99.100/redoc
```


## 動作環境

マシンスペック（Mac)

- MacBook Air (Retina, 13-inch, 2018)
- 1.6 GHz デュアルコアIntel Core i5
- 8 GB 2133 MHz LPDDR3
