"""Expand confirmed derivative shorthand; retain layer labels such as u_t."""
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
replacements={
 '\\bar\\theta_z':'\\frac{\\partial\\bar\\theta}{\\partial z}',
 r'\Phi_{\ln p}':r'\frac{\partial\Phi}{\partial\ln p}',
 r'\partial u_g/\partial\ln p':r'\frac{\partial u_g}{\partial\ln p}',
 r'\partial v_g/\partial\ln p':r'\frac{\partial v_g}{\partial\ln p}',
 r'\bar T_y':r'\frac{\partial\bar T}{\partial y}',
 r'\bar T_x':r'\frac{\partial\bar T}{\partial x}',
 r'\partial_tT':r'\frac{\partial T}{\partial t}',
 r'uT_x+vT_y':r'u\frac{\partial T}{\partial x}+v\frac{\partial T}{\partial y}',
 r'\omega T_p':r'\omega\frac{\partial T}{\partial p}',
 r'\frac{\kappa T}{p}-T_p':r'\frac{\kappa T}{p}-\frac{\partial T}{\partial p}',
 r'\omega_p':r'\frac{\partial\omega}{\partial p}',
 r'\Phi_p':r'\frac{\partial\Phi}{\partial p}',
 r'\partial_i\dot\theta':r'\frac{\partial\dot\theta}{\partial x_i}',
 r'\partial_i u_j':r'\frac{\partial u_j}{\partial x_i}',
 r'\partial_iw':r'\frac{\partial w}{\partial x_i}',
 r'\theta_z':r'\frac{\partial\theta}{\partial z}',
}
count=0
def normalize(m):
 global count
 s=m[0]
 for a,b in replacements.items():
  count+=s.count(a);s=s.replace(a,b)
 return s
for p in (root/'每日内容').glob('D*.md'):
 s=p.read_text(encoding='utf-8')
 s=re.sub(r'\$\$[\s\S]*?\$\$|(?<!\\)\$(?!\$)[^$]+?(?<!\\)\$',normalize,s)
 p.write_text(s,encoding='utf-8')
print('Expanded derivative shorthand:',count)
