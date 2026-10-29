import datetime, json, os, smtplib, ssl
from email.message import EmailMessage
from pathlib import Path
from urllib.parse import quote
from zoneinfo import ZoneInfo
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'manifest.json').read_text(encoding='utf-8'))
day=os.environ.get('DAY','').strip()
today=datetime.datetime.now(ZoneInfo('Asia/Shanghai')).date().isoformat()
items=[m for m in manifest if (m['day']==int(day) if day else m['date']==today)]
if not items:
 print('No lesson scheduled today.'); raise SystemExit(0)
m=items[0]; path=root/m['file']
url='https://github.com/0183ty2512/lao-san-yang/blob/main/'+quote('50日任务/'+m['file'])
msg=EmailMessage(); msg['Subject']=f"D{m['day']:02} 大气科学复习 · {m['title']}"
msg['From']=os.environ['SMTP_USER']; msg['To']=os.environ['MAIL_TO']
msg.set_content(f"今天的学习内容：{m['title']}\n\n点击阅读（支持数学公式）：{url}\n\n完整学习包见附件。Markdown附件可在Obsidian阅读模式打开。参考答案为学习整理版，不是官方评分标准。")
msg.add_attachment(path.read_bytes(),maintype='text',subtype='markdown',filename=path.name)
if os.environ.get('DRY_RUN')=='1':
 print('Validated lesson',m['day'],'attachment bytes',path.stat().st_size); raise SystemExit(0)
with smtplib.SMTP_SSL(os.environ['SMTP_HOST'],int(os.environ.get('SMTP_PORT','465')),context=ssl.create_default_context(),timeout=45) as smtp:
 smtp.login(os.environ['SMTP_USER'],os.environ['SMTP_PASSWORD']); smtp.send_message(msg)
print('Sent lesson',m['day'])
