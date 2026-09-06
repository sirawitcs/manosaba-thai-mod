from pathlib import Path
import shutil, json, hashlib
root = Path(r'C:/Users/kikik/manosaba_mod')
game = Path(r'C:/Program Files (x86)/Steam/steamapps/common/manosaba_game')
out = root / 'mod'
if out.exists():
    shutil.rmtree(out)
aa_src = game / 'manosaba_Data/StreamingAssets/aa/StandaloneWindows64'
aa_dst = out / 'manosaba_Data/StreamingAssets/aa/StandaloneWindows64'
aa_dst.mkdir(parents=True)
files = list(aa_src.glob('general-localization-zhhans-*.bundle')) + [
    aa_src / 'general-data_assets_all.bundle',
    aa_src / 'general-fonts-sourcehanserifsc_assets_all.bundle',
]
for f in files:
    shutil.copy2(f, aa_dst / f.name)
config = game / 'manosaba_Data/StreamingAssets/config.json'
(out / 'manosaba_Data/StreamingAssets').mkdir(parents=True, exist_ok=True)
shutil.copy2(config, out / 'manosaba_Data/StreamingAssets/config.json')
readme = '''# Manosaba Thai Mod — v1.1.0-beta

ม็อดภาษาไทยสำหรับ Manosaba / 牢屋敷の魔女裁判

สถานะ:
- แปลแล้ว 440 scripts / 34,836 blocks
- ตรวจ `__TH__` marker: 0
- ใช้ locale slot `zh-Hans`
- รวมข้อความไทย ชื่อผู้พูดไทย และฟอนต์ไทย PUA

## วิธีติดตั้ง

1. ปิดเกม
2. สำรองโฟลเดอร์ `manosaba_Data/StreamingAssets`
3. คัดลอกโฟลเดอร์ `manosaba_Data` จากแพ็กนี้ไปวางทับโฟลเดอร์เกม
4. เปิดเกม แล้วเลือกภาษา `简体中文 / zh-Hans`

เกมไม่มี locale `th` ใน catalog จึงใช้ช่อง `zh-Hans` โหลดภาษาไทย

ไฟล์ในแพ็กนี้เป็นไฟล์ม็อดเท่านั้น ไม่รวมไฟล์เกมทั้งหมด

อัปเดต: 2026-09-06
'''
(out / 'README_TH.txt').write_text(readme, encoding='utf8')
manifest = {'files': {}}
for f in out.rglob('*'):
    if f.is_file() and f.name != 'manifest.json':
        rel = f.relative_to(out).as_posix()
        manifest['files'][rel] = hashlib.sha256(f.read_bytes()).hexdigest()
(out / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf8')
print({'files': len(manifest['files']), 'bundles': len(files), 'path': str(out), 'zhhans': len(list(aa_dst.glob('general-localization-zhhans-*.bundle'))), 'font': (aa_dst / 'general-fonts-sourcehanserifsc_assets_all.bundle').exists(), 'data': (aa_dst / 'general-data_assets_all.bundle').exists()})
