# Manosaba Thai Mod

ม็อดภาษาไทยสำหรับ **Manosaba / 牢屋敷の魔女裁判**

## สถานะล่าสุด

- เวอร์ชันม็อด: **1.1.0-beta**
- แปลบทสนทนาแล้ว: **440 scripts / 34,836 blocks**
- ตรวจ marker `__TH__`: **0**
- ใช้ locale slot: **`zh-Hans`**
- รวมชื่อผู้พูดภาษาไทย
- รวมฟอนต์ไทยและ PUA glyph สำหรับสระ/วรรณยุกต์
- รวม localization bundle สำหรับ Act01, Act02, Common, Debug และ System
- เกลาสำนวนแล้วหลายจุด โดยคงความหมายเดิมและโครงสร้าง Naninovel

> เนื้อหาแปลครบตามไฟล์เกมที่ตรวจพบแล้ว แต่การเกลาสำนวนยังอาจมีจุดย่อยที่ต้องปรับเพิ่มในรุ่นถัดไป

## ติดตั้งม็อด

1. ปิดเกม Manosaba
2. สำรองโฟลเดอร์ `manosaba_Data/StreamingAssets`
3. เปิดโฟลเดอร์ `mod/`
4. คัดลอกโฟลเดอร์ `manosaba_Data` จากม็อดไปวางทับโฟลเดอร์เกม
5. เปิดเกม
6. เลือกภาษา **简体中文 / zh-Hans** ในเมนูภาษา

เกมใช้ช่องภาษา `zh-Hans` เพื่อโหลดข้อความไทย เพราะ catalog ของเกมไม่มี locale `th`

## ถอนการติดตั้ง

ใช้ Steam ตรวจสอบไฟล์เกม หรือกู้คืนไฟล์จาก backup ที่ทำไว้ก่อนติดตั้ง

## โครงสร้างแพ็ก

```text
mod/
├── README_TH.txt
├── manifest.json
└── manosaba_Data/
    └── StreamingAssets/
        ├── config.json
        └── aa/StandaloneWindows64/
            ├── general-localization-zhhans-*.bundle
            ├── general-data_assets_all.bundle
            └── general-fonts-sourcehanserifsc_assets_all.bundle
```

## กฎการแปล

- คง ID, metadata, voice ID และคำสั่ง Naninovel
- คง `<br>`, `<link>`, `<ruby>` และ markup เดิม
- คงชื่อ `AuthorId` ภายในระบบ เช่น `Ema`, `Alisa`
- ชื่อที่แสดงใช้ภาษาไทยจาก `AuthorData` ของ locale `zh-Hans`
- ฟอนต์ใช้ PUA glyph เพื่อรองรับสระและวรรณยุกต์ใน runtime ที่ไม่จัดรูปภาษาไทยเอง

## เครื่องมือสร้างม็อด

ไฟล์สำคัญ:

- `package_mod.py` — สร้างแพ็กแจกจ่ายจากไฟล์เกมที่ติดตั้ง
- `build_mod_full.py` — build localization bundle
- `apply_thai_pua.py` — แปลงชุดสระ/วรรณยุกต์เป็น PUA
- `patch_pua_font_bundle.py` — แพตช์ฟอนต์เข้า bundle

## ลิงก์

- เกม: Manosaba / 牢屋敷の魔女裁判
- Naninovel: https://naninovel.com/
- UnityPy: https://github.com/K0lb3/UnityPy

## ใบอนุญาตและข้อควรระวัง

ม็อดนี้เป็นงานแปลแฟนเมด ไม่แจกไฟล์เกมต้นฉบับทั้งหมด ใช้กับเกมที่ซื้อถูกต้องเท่านั้น

**เวอร์ชัน:** 1.1.0-beta  
**อัปเดต:** 2026-09-06
