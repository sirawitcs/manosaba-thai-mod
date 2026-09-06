# 泰语MOD制作工具 - Manosaba Game Thai Mod Toolkit

## 📋 项目概述

这是一个为游戏《Manosaba》(牢屋敷的魔女裁判)制作泰语翻译MOD的工具包。

### 游戏信息
- **游戏名称**: Manosaba (牢屋敷の魔女裁判)
- **游戏类型**: 视觉小说 / 推理解谜
- **引擎**: Unity (IL2CPP)
- **文本系统**: Naninovel Visual Novel Engine
- **支持语言**: 日语 (ja), 简体中文 (zh-Hans)

### MOD状态
✅ **已完成**:
- 游戏文本提取 (440个脚本, 36,000+条对话)
- 中文本地化文件解析
- MOD基础设施搭建
- 游戏配置更新 (添加泰语支持)
- 15个泰语本地化bundle创建

⚠️ **需要完成**:
- 完整的泰语翻译 (当前仅有示例翻译)

---

## 🛠️ 使用方法

### 1. 安装MOD
```bash
# 运行安装脚本
python install_mod.py
```

### 2. 选择语言
1. 启动游戏
2. 进入设置/语言选项
3. 选择 "ไทย" (泰语)

---

## 📁 文件结构

```
manosaba_mod/
├── backup/                          # 原始文件备份
│   ├── config.json.backup
│   └── *.bundle.backup
├── thai_bundles/                    # 泰语本地化bundle
│   └── general-localization-th-scripts-*.bundle
├── zh_localization.json             # 中文本地化数据
├── thai_localization.json           # 泰语本地化数据
├── extracted_japanese.json          # 提取的日语文本
├── unique_dialogues.txt             # 唯一对话列表
├── thai_translation_sample.txt      # 泰语翻译示例
└── *.py                             # 工具脚本
```

---

## 🔧 工具脚本说明

### 1. `extract_all_full.py`
从游戏bundle中提取所有日语文本。

### 2. `extract_zh_all.py`
解析中文本地化文件，提取翻译模板。

### 3. `create_thai_translation.py`
创建泰语翻译文件 (需要添加翻译内容)。

### 4. `build_thai_proper.py`
构建泰语本地化bundle。

### 5. `install_mod.py`
安装MOD到游戏目录。

---

## 📝 翻译指南

### 本地化文件格式
Naninovel使用以下格式的本地化文件：

```
; 日本語 <ja> to ไทย <th> localization document for 'ScriptPath' Naninovel scenario script

# VoiceLineID
; > Character: |#VoiceLineID|
; 原始日语文本
泰语翻译文本

# VoiceLineID2
; > Character: |#VoiceLineID2|
; 原始日语文本2
泰语翻译文本2
```

### 翻译注意事项
1. 保持 `<br>` 换行标签不变
2. 保持 `<link="...">` 链接标签不变
3. 保持 `【】` 括号内的关键词
4. 角色名称音译:
   - エマ → เอ็มม่า
   - シェリー → เชอร์ลี่
   - ハンナ → ฮันน่า
   - メルル → เมอร์รู
   - レイア → เรย์ย่า
   - マーゴ → มาร์โก้
   - ミリア → มิเรีย
   - ココ → โคโค่
   - アリサ → อะริสะ
   - アンアン → อันอัน
   - ナノカ → นานกะ

---

## 🎮 游戏内容结构

### 章节结构
- **Act 01**: 第一幕 (5个章节)
  - Chapter 01-05: 每章包含Adv(冒险)、Trial(审判)、Bad(坏结局)路线
- **Act 02**: 第二幕 (6个章节)
  - Chapter 01-06: 同上

### 脚本类型
- **Adv**: 冒险/探索部分
- **Trial**: 审判/推理部分
- **Bad**: 坏结局路线
- **Common**: 通用场景
- **System**: 系统文本
- **Debug**: 调试文本

---

## ⚠️ 重要提示

1. **备份原始文件**: 安装MOD前请备份游戏文件
2. **Steam验证**: 如遇问题可通过Steam验证游戏文件完整性
3. **翻译完整性**: 当前MOD仅包含示例翻译，需要完成全部翻译才能获得完整体验

---

## 📊 翻译进度

| 脚本数量 | 已翻译 | 待翻译 | 完成度 |
|---------|-------|-------|-------|
| 440 | 1 (示例) | 439 | 0.2% |

### 翻译优先级
1. **System** (系统文本) - 4个脚本
2. **Common** (通用场景) - 13个脚本
3. **Trial** (审判部分) - ~100个脚本
4. **Adv** (冒险部分) - ~300个脚本
5. **Debug** (调试文本) - 16个脚本 (可选)

---

## 🔗 相关资源

- **Naninovel文档**: https://naninovel.com/
- **UnityPy**: https://github.com/K0lb3/UnityPy
- **游戏Steam页面**: (请自行搜索)

---

## 📧 联系方式

如有问题或建议，请通过GitHub Issues反馈。

---

**最后更新**: 2026年8月27日
**版本**: 1.0.0 (Beta)
"# manosaba-thai-mod" 
