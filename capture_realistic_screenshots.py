import os
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8', errors='replace', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_path = r's:\01_ACADEMIC_STUDY\UoPeople as Student\01_ACTIVE_COURSES\CS4406-Computer_Graphics\04_Unit 3_ Viewing and Projection\coursework\realistic_campus\index.html'
out_dir = r's:\01_ACADEMIC_STUDY\UoPeople as Student\01_ACTIVE_COURSES\CS4406-Computer_Graphics\04_Unit 3_ Viewing and Projection\coursework\realistic_campus\screenshots'
os.makedirs(out_dir, exist_ok=True)

modes = ['overview', 'walkthrough', 'perspective', 'orthographic', 'clipping', 'depth_error', 'depth_fixed']

for m in modes:
    url = f'file:///{html_path.replace(os.sep, "/")}?mode={m}'
    out_png = os.path.join(out_dir, f'{m}.png')
    cmd = f'"{edge}" --headless --use-gl=angle --virtual-time-budget=4000 --window-size=1280,720 --screenshot="{out_png}" "{url}"'
    print(f'Capturing realistic campus mode: {m}...')
    subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if os.path.exists(out_png):
        print(f'  [OK] {out_png} ({os.path.getsize(out_png)} bytes)')
    else:
        print(f'  [FAIL] {out_png}')

print("Completed capturing realistic campus screenshots!")
