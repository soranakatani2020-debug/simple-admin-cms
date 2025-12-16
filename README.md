# Simple Admin CMS（Flask）

## 概要
小規模事業者・個人事業主向けの  
**お問い合わせ管理機能付きWebサイト**です。

Flaskを用いて、  
- 公開ページ  
- 管理画面  
- DBによるデータ管理  

を一通り実装しています。

---

## 想定利用シーン
- コーポレートサイト
- 個人事業主のサービスサイト
- お問い合わせを管理画面で確認・対応したいケース

---

## 主な機能

### 公開ページ
- トップページ
- サービス紹介ページ
- お問い合わせフォーム（DB保存）

### 管理画面
- 管理者ログイン機能（Flask-Login）
- お問い合わせ一覧表示
- お問い合わせ詳細表示
- ステータス変更（未対応 / 対応済）
- お問い合わせ削除

---

## 使用技術
- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLite
- HTML / CSS
- Jinja2

---

## ディレクトリ構成

```text
.
├─ app.py
├─ models.py
├─ instance/
│  └─ app.db
├─ templates/
│  ├─ index.html
│  ├─ about.html
│  ├─ contact.html
│  ├─ login.html
│  └─ admin/
│     ├─ dashboard.html
│     ├─ contacts.html
│     └─ contact_detail.html
└─ static/
   └─ css/
      └─ style.css


---

## 実行方法

```bash
python app.py
ブラウザで以下にアクセスします。

http://127.0.0.1:5000/

http://127.0.0.1:5000/login

http://127.0.0.1:5000/admin

工夫した点

管理画面はログイン必須にしてセキュリティを確保

CRUD操作（一覧・詳細・更新・削除）を一通り実装

SQLiteを使用し、簡単に導入できる構成にした

今後の拡張予定

管理ユーザーのDB管理（ID / パスワード）

バリデーション強化

デザイン改善


メール通知機能

---

## 更新履歴
- 管理画面UI改善、ログイン処理修正（2025/12/16）

