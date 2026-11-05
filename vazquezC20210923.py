"""
Práctica 3: Sistema Musculoesqueletico

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Nicole Vazquez Alvear
Número de control: C20210923
Correo institucional: lC20210923@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Instalar librerias en consola
#!pip install control
#!pip install slycot


# Librerías para cálculo numérico y generación de gráficas
import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd
 
# Datos de la simulación 
x0, t0, tend, dt, w, h = 0, 0, 10, 1E-3, 10, 5
N = int(tend/dt) + 1
t = np.linspace(t0, tend, N)
u2 = np.zeros(N)
u2[round(1/dt):round(2/dt)] = 1

# Control
num_ctrl = [100*10e-6, 1-0.25]
den_ctrl = [100*(100e-6+10e-6), 1]
sys_ctrl = ctrl.tf(num_ctrl, den_ctrl)
print(f"FT Control: {sys_ctrl}\n")

# Caso
num_caso = [10e3*10e-6, 1-0.25]
den_caso = [10e3*(100e-6+10e-6), 1]
sys_caso = ctrl.tf(num_caso, den_caso)
print(f"FT Caso: {sys_caso}\n")

# Controlador
kP, kI = 0.22157, 3595.7467
Cr = 1E-6
Re = 1/(Cr*kI)
Rr = kP*Re

print(f"Cr = {Cr} F")
print(f"Re = {Re:.4f} Ω")
print(f"Rr = {Rr:.4f} Ω\n")

numPID = [Rr*Cr, 1]
denPID = [Re*Cr, 0]
PI = ctrl.tf(numPID, denPID)
print(f"FT Controlador PI: {PI}\n")

# Lazo cerrado
sys_caso_LC = ctrl.feedback(ctrl.series(PI, sys_caso), 1, sign=-1)
print(f"FT Caso LC: {sys_caso_LC}\n")

# Respuestas
_, F_ctrl   = ctrl.forced_response(sys_ctrl, t, u2, x0)
_, F_caso   = ctrl.forced_response(sys_caso, t, u2, x0)
_, PID_caso = ctrl.forced_response(sys_caso_LC, t, F_ctrl, x0)

# Colores
clr_1 = np.array([0, 63, 92]) / 255  
clr_2 = np.array([139, 0, 0]) / 255  
clr_3 = np.array([0, 100, 0]) / 255  
clr_4 = np.array([74, 21, 75]) / 255

# Gráfica
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']

# Figura 1:
fg1 = plt.figure(1, figsize=(w, h), facecolor='white')

plt.plot(t, u2,         '-',  linewidth=1.0, color=clr_1, label=r'$F(t)$')
plt.plot(t, F_ctrl,     '--', linewidth=1.2, color=clr_2,   label=r'$F_s(t)$: Control')
plt.plot(t, F_caso,     '--', linewidth=1.2, color=clr_3,  label=r'$F_s(t)$: Caso')
plt.plot(t, PID_caso,   ':',  linewidth=1.5, color=clr_4,   label=r'$PID(t)$: Tratamiento')

plt.gca().set_facecolor('white')
plt.grid(False)
plt.box(True)

plt.xlim(0, 10)
plt.xticks(np.arange(0, 11, 1))
plt.ylim(-0.1, 1.1)
plt.yticks(np.round(np.arange(-0.1, 1.11, 0.1), 1))

plt.xlabel('t [s]')
plt.ylabel('F(t) [V]')

plt.legend(bbox_to_anchor=(0.5, 1.08), loc='center', ncol=4, frameon=False, fontsize=10)

plt.show()