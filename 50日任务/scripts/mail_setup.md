## 每日邮件配置

工作流已安排每日北京时间10:30。GitHub Actions可能延迟，不保证分钟级准点。仅在2026-10-29至2026-12-17发送对应内容，结束后不发信。今天时段已过，可在Actions手动指定day=1补发。

在仓库 Settings → Secrets and variables → Actions 填入 Secrets：

- SMTP_HOST：支持SSL的SMTP服务器，例如QQ邮箱为smtp.qq.com。
- SMTP_PORT：465。
- SMTP_USER：实际发件邮箱。
- SMTP_PASSWORD：邮件服务授权码，不是网页登录密码。
- MAIL_TO：收件邮箱（已设置）。

完成后设置 Repository variable `MAIL_ENABLED` 为 `true`。当前默认关闭，避免凭据不全反复失败。手动执行工作流可指定day 1—50；手动重试会再次发送，发信成功后不要重复运行。

邮件附完整Markdown文件和GitHub阅读链接。邮件正文不执行数学脚本；公式需在GitHub或Obsidian阅读视图中查看。源资料含未审校与疑题标记，本任务保留这些限制；专题选题为关键词辅助整理，仍宜按个人错题调整。生成脚本依赖PyMuPDF和原始PDF，发信脚本仅使用Python标准库。
