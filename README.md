# 文化祭オーダーシステム
文化祭の模擬店運営を簡単にするために制作したオールインワンシステム。

オーダーもバックヤードもレジも全て一括管理するWebアプリケーション。

## Detail
このシステムの技術仕様について

###　Framework
 - Django
 - Apache

### Database
 - PostgreSQL

### Infrastructure
 - Amazon VPC
 - Amazon EC2
   - Instance: t3a.small
   - EBS: 8GB
 - Amazon RDS
   - Instance: t4g.micro
   - AZ: Single-AZ
   - Storage: 10GB
 - Application Load Balancer
 - AWS Certificate Manager
 - Amazon Route53
   - Host Zone
 - Google Domains

## Features
搭載した機能

### All
 - 管理者権限メンバーを作成

### Backyard
バックヤードを効率的に管理するページ
 - テーブルごとにまとめて表示
 - チェックボタンで提供済み処理
 - オーダー者からのメッセージ表示
 - 個数は右側に青色で表示

### Order
接客担当者が使用するオーダーページ
 - 売り切れの二重確認でバグを阻止
 - バックヤードへのメッセージ

### Register
提供済み商品を精算するレジシステム
 - 提供済みになっている商品のみを表示
 - 別の方の精算分は後に回して別精算
 - バーコード搭載のチケットで簡単値引き処理
 - 手動値引きもページ上で対応
 - お客さんに見やすいように金額表示を回転
 - お釣りの計算もするため、預かった金額も入力
 - 管理者権限メンバーのみ操作可能

### Messages
全てのページ上部で表示されるメッセージ共有
 - 全メンバーが追加や編集・削除可能
 - 優先度ごとにアイコンを追加可能

## Caution
DjangoアプリケーションのデプロイにはApacheにmod_wsgiが必要です。

## Documents
使用などをまとめたPDFは下記リンクから使用できます。
[オーダーシステム 使い方説明]()
