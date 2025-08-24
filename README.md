# Armature Tools

Blender用のアドオンで、**Armature（アーマチュア）のボーン操作を便利にするツール**です。  
主な機能は以下の2つです：

1. **Recursive Bone Renamer**  
   - 指定した文字列を含むボーン名を再帰的に置換します。
   - 例：`"Bone_L_001"` → `"Arm_L_001"`  

2. **Delete Child Bones**  
   - 選択したボーンとその子ボーンを再帰的に削除します。

---

## 対応環境

- Blender 4.0 以降
- Python 3.11（Blender付属）
- 開発用: VSCode で補完を使う場合は `fake-bpy-module-4.0` を推奨

---

## インストール方法

1. GitHubリポジトリから **Release の ZIP** をダウンロード  
2. Blenderを開き、`Edit → Preferences → Add-ons → Install...`  
3. ダウンロードした ZIP を選択  
4. アドオン一覧で「Armature Tools」を有効化  

---

## 使い方

### 1. Recursive Bone Renamer
- 3D Viewport → Sidebar → **Armature Tools** タブ
- **Armature** を選択
- **Target String** に置換したい文字列を入力
- **Replace With** に置き換え後の文字列を入力
- **Rename** ボタンを押すと再帰的にボーン名が変更されます

### 2. Delete Child Bones
- 削除したいボーンを選択
- **Delete Children** ボタンを押すと、子ボーンを含めて再帰的に削除されます