[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=nicole-vqz/MSFBP3)

# Práctica 3 — Modelado y control del sistema musculoesquelético

Repositorio académico de la asignatura **Modelado de Sistemas Fisiológicos**, correspondiente al programa de **Ingeniería Biomédica** del Tecnológico Nacional de México / Instituto Tecnológico de Tijuana. Esta práctica integra modelado mecánico fisiológico, analogías electromecánicas fuerza-voltaje, derivaciones analíticas por principio de superposición, funciones de transferencia, análisis de estabilidad en el plano complejo, sintonización de un controlador PID *in silico*, y simulación computacional comparativa en MATLAB/Simulink, Simscape Electrical y Python.

El caso de estudio analiza un **modelo mecánico viscoelástico musculoesquelético simplificado** (propuesto por Khoo). Se busca evaluar la respuesta dinámico-mecánica de la fuerza transmitida y el desplazamiento en un **individuo sano (control)** contra un **caso simulado de atrofia muscular (caso)** caracterizado por un incremento sustancial en la componente de amortiguamiento viscoso tejido-muscular ($R$). Finalmente, se diseña un esquema de control en lazo cerrado para rehabilitar/reducir la señal de error entre el paciente sintomático y la referencia del control sano.

**Docente:** Dr. Paul Antonio Valle Trujillo  
**Correo:** paul.valle@tectijuana.edu.mx  
**Departamento:** Departamento de Ingeniería Eléctrica y Electrónica  
**Institución:** Tecnológico Nacional de México / Instituto Tecnológico de Tijuana  
**Asignatura:** Modelado de Sistemas Fisiológicos  
**Programa:** Ingeniería Biomédica  
**Estudiante:** Nicole Vazquez Alvear · C20210923 · LC20210923@tijuana.tecnm.mx

**Repositorio de la asignatura:** https://github.com/nicole-vqz/MSFBP3 
**Sede:** Blvd. Alberto Limón Padilla s/n, Tijuana, C. P. 22454, B. C., México.

---

<a id="contenido"></a>
## Contenido

1. [Resumen](#resumen)
2. [Competencia y objetivos](#objetivos)
3. [Relación con el temario](#temario)
4. [Modelo mecánico viscoelástico y analogía electromecánica](#analogia)
5. [Formulación matemática y derivación analítica](#modelo)
6. [Análisis temporal y de estabilidad](#analisis)
7. [Parámetros del sistema: Control vs. Caso (Atrofia)](#parametros)
8. [Implementación en MATLAB, Simulink y Simscape](#matlab)
9. [Control en lazo cerrado y sintonización PID](#pid)
10. [Reproducción en Python (VS Code)](#python)
11. [Diagrama biológico y correlación histofisiológica](#biologico)
12. [Resultados y verificación cruzada](#resultados)
13. [Flujo de trabajo](#flujo)
14. [Actividades del estudiante](#actividades)
15. [Estructura del repositorio](#estructura)
16. [Requisitos](#requisitos)
17. [Reproducibilidad y entregables](#reproducibilidad)
18. [Referencias](#referencias)

---

<a id="resumen"></a>
## Resumen

Esta práctica aborda la representación y análisis dinámico de un compartimento del **sistema musculoesquelético** bajo condiciones normales y patológicas. A partir del modelo de parámetros distribuidos/concentrados de Khoo, se combinan elementos contráctiles activos ($F_0$), compliancias elásticas pasivas en serie ($C_s$) y paralelo ($C_p$), junto con la amortiguación viscosa del tejido muscular ($R$).

Mediante la **analogía electromecánica fuerza-voltaje**, el modelo mecánico se transforma en un circuito eléctrico equivalente donde las fuerzas corresponden a voltajes, las velocidades a corrientes y los desplazamientos a cargas eléctricas. Empleando el **principio de superposición analítica** sobre las fuentes del sistema ($F(t)$ y $F_0(t) = \alpha F(t)$), se obtiene la función de transferencia analítica exacta en el dominio de Laplace $G(s) = \frac{F_s(s)}{F(s)}$ y su relación equivalente en términos de deformación/desplazamiento.

Se analiza analíticamente la posición de los polos del sistema y la respuesta temporal al impulso para la condición de **individuo sano (Control, $R = 100\,\Omega$)** y el **caso simulado de atrofia muscular (Caso, $R = 10\,\mathrm{k}\Omega$)**. Para mitigar el déficit biomecánico de la atrofia, se implementa un sistema de control con retroalimentación negativa que incorpora un **controlador PID** sintonizado en Simulink mediante la herramienta *Tune*, comparando los resultados de manera cruzada mediante **MATLAB/Simulink**, **Simscape Electrical** y código nativo en **Python**.

> **Aviso académico:** La estrategia de control desarrollada durante esta práctica se realiza exclusivamente mediante experimentación *in silico* con propósitos académicos de simulación y no constituye una directriz o estrategia terapéutica clínica real.

**Palabras clave:** sistema musculoesquelético; atrofia muscular; analogía fuerza-voltaje; función de transferencia; principio de superposición; controlador PID; Simscape Electrical; MATLAB; Python; simulación *in silico*.

[Volver al contenido](#contenido)

---

<a id="objetivos"></a>
## Competencia y objetivos

### Competencia a desarrollar

Modelizar sistemas fisiológicos mediante analogías entre sistemas físicos, ecuaciones diferenciales y funciones de transferencia para analizar su comportamiento dinámico, y diseñar estrategias de control mediante técnicas de control clásico. En particular, el estudiante analizará un modelo mecánico simplificado del sistema musculoesquelético, construirá su circuito eléctrico equivalente mediante la analogía fuerza-voltaje, comparará la respuesta de un individuo sano (control) con un caso simulado de atrofia muscular (caso) y diseñará una estrategia de control *in silico* orientada a reducir las diferencias entre ambas respuestas.

### Objetivo general

Formular, simular y controlar *in silico* el modelo dinámico del sistema musculoesquelético mediante su circuito eléctrico equivalente análogo, derivando analíticamente su función de transferencia, evaluando el impacto dinámico del incremento de la amortiguación viscosa por atrofia muscular y diseñando un controlador PID que reduzca la señal de error respecto a la referencia de un individuo sano.

### Objetivos específicos

- Identificar los componentes viscoelásticos y contráctiles del modelo de Khoo ($F_0, F, R, C_s, C_p, x, x_1$).
- Construir el circuito eléctrico equivalente mediante la analogía fuerza-voltaje, respetando la inversión topológica serie-paralelo.
- Formular las ecuaciones integro-diferenciales del circuito y derivar su función de transferencia analítica $G(s)$ utilizando el principio de superposición.
- Evaluar los polos de la planta y la estabilidad para las condiciones de control sano ($R = 100\,\Omega$) y caso patológico ($R = 10\,\mathrm{k}\Omega$).
- Implementar el modelo en MATLAB/Simulink mediante tres enfoques: ecuaciones dinámicas, bloques de función de transferencia y componentes físicos en Simscape Electrical.
- Diseñar y sintonizar un controlador PID en lazo cerrado en Simulink para compensar la respuesta del caso sintomático.
- Reproducir el modelo y el esquema de control en Python mediante Visual Studio Code, realizando una verificación cruzada de resultados.
- Elaborar un diagrama biológico en BioRender que correlacione la estructura histofisiológica del músculo con los elementos mecánicos y eléctricos.

[Volver al contenido](#contenido)

---

<a id="temario"></a>
## Relación con el temario

La práctica integra contenidos pertenecientes a los tres ejes nodales del programa de **Modelado de Sistemas Fisiológicos (IBF-1020)**:

| Unidad | Área | Contenidos aplicados |
|---|---|---|
| I | Sistemas de control retroalimentados | Modelado de señales de error $e(t) = x_{\text{control}}(t) - x_{\text{caso}}(t)$, esquemas de retroalimentación negativa y criterios de estabilidad en el plano complejo |
| II | Modelado matemático | Analogía electromecánica fuerza-voltaje, balance de equilibrio de fuerzas/leyes de Kirchhoff, análisis por superposición y funciones de transferencia |
| III | Controladores | Controlador PID, sintonización de ganancias ($k_P, k_I, k_D$), análisis de respuesta en lazo cerrado ante perturbaciones e impulsos |

[Volver al contenido](#contenido)

---

<a id="analogia"></a>
## Modelo mecánico viscoelástico y analogía electromecánica

El modelo mecánico simplificado del compartimento musculoesquelético de Khoo representa la interacción entre el elemento contráctil activo del sarcómero y las estructuras viscoelásticas pasivas del tejido conjuntivo muscular y tendinoso.

```
                  +-----( F0 )-----+
                  |                |
                  +----[  R  ]-----+---/\/\/\/\----( Pared fija )
                  |      x-x1             Cs
                  |      
   F(t) <---------+                                 x1(t)
   (Fuerza)       |                               <-------
                  +-------------/\/\/\/\-----------( Pared fija )
                                  Cp
                                  
                  <---------------------------------------
                                    x(t)
```

### Elementos del sistema mecánico y su función fisiológica

- **$F_0(t)$:** Fuerza generada activamente por los puentes cruzados de actina-miosina en el elemento contráctil. Se relaciona proporcionalmente con la fuerza total mediante $F_0(t) = \alpha F(t)$, con $0 < \alpha < 1$.
- **$F(t)$:** Fuerza total externa transmitida o aplicada por/hacia el sistema musculoesquelético.
- **$R$:** Coeficiente de amortiguación viscosa inherente al sarcoplasma, matriz extracelular y fluidos tisulares.
- **$C_s$:** Compliancia (elasticidad pasiva en serie), asociada a la elasticidad de los tendones y las aponeurosis.
- **$C_p$:** Compliancia (elasticidad pasiva en paralelo), asociada al sarcolema, epimisio, perimisio y endomisio.
- **$x(t)$:** Desplazamiento global/deformación total del compartimento.
- **$x_1(t)$:** Desplazamiento relativo experimentado por el elemento en serie $C_s$.
- **$x(t) - x_1(t)$:** Deformación relativa sobre el elemento amortiguador viscoso $R$.

### Reglas de la analogía electromecánica Fuerza-Voltaje

De acuerdo con la analogía fuerza-voltaje, las magnitudes mecánicas y eléctricas se relacionan según la siguiente equivalencia:

| Sistema mecánico | Sistema eléctrico equivalente | Unidad en el modelo |
|---|---|---|
| Fuerza $F(t)$ | Voltaje $V(t)$ | $\mathrm{V}$ |
| Velocidad $\dot{x}(t)$ | Corriente $I(t)$ | $\mathrm{A}$ |
| Desplazamiento $x(t)$ | Carga eléctrica $q(t)$ | $\mathrm{C}$ |
| Amortiguador $R$ | Resistencia eléctrica $R$ | $\Omega$ |
| Compliancia mecánica $C_p, C_s$ | Capacitancia eléctrica $C_p, C_s$ | $\mathrm{F}$ |
| Masa $M$ | Inductancia $L$ | $\mathrm{H}$ |

> **Regla de dualidad topológica:** Elementos mecánicos conectados en **paralelo** se convierten en elementos eléctricos en **serie**, mientras que elementos mecánicos en **serie** se transforman en elementos eléctricos conectados en **paralelo**.

[Volver al contenido](#contenido)

---

<a id="modelo"></a>
## Formulación matemática y derivación analítica

A partir de las deducciones analíticas desarrolladas en el documento de trabajo de la práctica (`Sistema musculoesqueletico.pdf`), el circuito equivalente simplificado se resuelve aplicando el **Principio de Superposición** debido a la presencia de la fuente de entrada principal $F(t)$ y la fuente activa dependiente $F_0(t) = \alpha F(t)$.

### 1. Análisis del Circuito 1: Desactivación de la fuente interna $F_0(t) = 0$

Apagando la fuente contráctil activa, el desplazamiento total se descompone en la suma de las contribuciones de las ramas:

$$
x(t) = x_1(t) + x_2(t)
$$

Donde las relaciones constitutivas expresadas en términos del nodo de fuerza $F_{s1}(t)$ satisfacen:

$$
x(t) = C_p \frac{d F_{s1}(t)}{dt}, \quad x_1(t) = C_s \frac{d [F(t) - F_{s1}(t)]}{dt}, \quad x_2(t) = \frac{F(t) - F_{s1}(t)}{R}
$$

Igualando la suma de desplazamientos:

$$
C_p \frac{d F_{s1}(t)}{dt} = C_s \frac{d [F(t) - F_{s1}(t)]}{dt} + \frac{F(t) - F_{s1}(t)}{R}
$$

Aplicando la Transformada de Laplace con condiciones iniciales nulas:

$$
C_p s F_{s1}(s) = C_s s [F(s) - F_{s1}(s)] + \frac{F(s) - F_{s1}(s)}{R}
$$

Reordenando términos en función de $F_{s1}(s)$:

$$
\left( C_p s + C_s s + \frac{1}{R} \right) F_{s1}(s) = \left( C_s s + \frac{1}{R} \right) F(s)
$$

$$
\left[ \frac{R(C_p + C_s)s + 1}{R} \right] F_{s1}(s) = \left[ \frac{C_s R s + 1}{R} \right] F(s)
$$

Despejando la fuerza $F_{s1}(s)$:

$$
F_{s1}(s) = \frac{C_s R s + 1}{R(C_p + C_s)s + 1} F(s)
$$

### 2. Análisis del Circuito 2: Desactivación de la fuente externa $F(t) = 0$

Apagando la fuente externa de fuerza $F(t) = 0$, la fuente dependiente contráctil actúa como $-F_0(t) = -\alpha F(t)$. La compliancia equivalente combinada en serie-paralelo simplifica la rama a $C_p + C_s$.

La ecuación de malla en el dominio del tiempo viene dada por:

$$
-\alpha F(t) = R x(t) + \frac{1}{C_p + C_s} \int x(t) \, dt
$$

Definiendo la contribución a la fuerza en el elemento en serie $F_{s2}(t)$:

$$
F_{s2}(t) = \frac{1}{C_p + C_s} \int x(t) \, dt \implies F_{s2}(s) = \frac{X(s)}{(C_p + C_s)s}
$$

Transformando la ecuación de malla a Laplace:

$$
-\alpha F(s) = R X(s) + \frac{X(s)}{(C_p + C_s)s} = X(s) \left[ \frac{R(C_p + C_s)s + 1}{(C_p + C_s)s} \right]
$$

Despejando la relación de $F(s)$ en función del desplazamiento $X(s)$:

$$
F(s) = -\frac{X(s)}{\alpha} \left[ \frac{R(C_p + C_s)s + 1}{(C_p + C_s)s} \right]
$$

Sustituyendo $X(s)$ para obtener la contribución de fuerza $F_{s2}(s)$:

$$
F_{s2}(s) = \frac{-\alpha F(s)}{R(C_p + C_s)s + 1}
$$

### 3. Función de Transferencia Total $G(s)$

Por el principio de superposición, la fuerza interna resultante $F_s(s)$ es la suma de ambas contribuciones $F_s(s) = F_{s1}(s) + F_{s2}(s)$:

$$
F_s(s) = \left[ \frac{C_s R s + 1}{R(C_p + C_s)s + 1} - \frac{\alpha}{R(C_p + C_s)s + 1} \right] F(s)
$$

$$
\boxed{G(s) = \frac{F_s(s)}{F(s)} = \frac{C_s R s + 1 - \alpha}{R(C_p + C_s)s + 1}}
$$

Expresando el sistema de transferencia considerando el desplazamiento/deformación $X(s)$ como variable principal de salida del compartimento muscular frente a la fuerza $F(s)$:

$$
\boxed{G_x(s) = \frac{X(s)}{F(s)} = \frac{(1-\alpha) C_p s}{R(C_p + C_s)s + 1}}
$$

[Volver al contenido](#contenido)

---

<a id="analisis"></a>
## Análisis temporal y de estabilidad

### 1. Polos del sistema y estabilidad en el plano complejo

La ecuación característica del sistema musculoesquelético viene dada por el denominador de la función de transferencia:

$$
R(C_p + C_s)s + 1 = 0 \implies \boxed{s_1 = -\frac{1}{R(C_p + C_s)}}
$$

- Dado que $R > 0$, $C_p > 0$ y $C_s > 0$, el polo $s_1$ se localiza estrictamente en el **semiplano izquierdo del plano complejo ($\mathrm{Re}\{s\} < 0$)**, garantizando que el sistema es **BIBS (BIBO) Estable** para cualquier condición de amortiguamiento.

### 2. Análisis del error en estado estacionario $e_{ss}$

Ante una entrada tipo escalón unitario de fuerza $F(s) = \frac{1}{s}$, aplicando el Teorema del Valor Final:

$$
x(\infty) = \lim_{s \to 0} s X(s) = \lim_{s \to 0} s \cdot G_x(s) \frac{1}{s} = G_x(0)
$$

Dado que el numerador de $G_x(s)$ posee un cero en el origen ($s=0$), el valor final en estado estacionario para el desplazamiento ante escalón constante de fuerza se anula ($x(\infty) = 0$), representando la disipación pasiva completa de la deformación elástica.

[Volver al contenido](#contenido)

---

<a id="parametros"></a>
## Parámetros del sistema: Control vs. Caso (Atrofia)

Para la experimentación *in silico*, el modelo de atrofia muscular se induce mediante un **incremento de 100 veces en la componente de amortiguamiento viscoso ($R$)**, simulando el endurecimiento, fibrosis y pérdida de plasticidad del tejido muscular atrófico:

| Parámetro | Símbolo | Individuo Sano (Control) | Caso Atrofia Muscular (Caso) | Unidad eléctrica |
|---|---|---:|---:|---|
| Fuerza de entrada aplicada | $F(t)$ | $1$ | $1$ | $\mathrm{V}$ |
| Coeficiente contráctil activo | $\alpha$ | $0.25$ | $0.25$ | Adimensional |
| Compliancia pasiva en serie | $C_s$ | $10 \times 10^{-6}$ ($10\,\mu\mathrm{F}$) | $10 \times 10^{-6}$ ($10\,\mu\mathrm{F}$) | $\mathrm{F}$ |
| Compliancia pasiva en paralelo | $C_p$ | $100 \times 10^{-6}$ ($100\,\mu\mathrm{F}$) | $100 \times 10^{-6}$ ($100\,\mu\mathrm{F}$) | $\mathrm{F}$ |
| Amortiguamiento viscoso | $R$ | **$100$** | **$10\,000$ ($10\,\mathrm{k}\Omega$)** | $\Omega$ |

### Evaluación de los polos numéricos

- **Polo Control (Sano):**
  $$s_{\text{control}} = -\frac{1}{100 \cdot (100\,\mu\mathrm{F} + 10\,\mu\mathrm{F})} = -\frac{1}{100 \cdot 110 \times 10^{-6}} = -90.91\,\mathrm{rad/s}$$
  *Respuesta dinámica rápida con constante de tiempo $\tau_{\text{control}} \approx 11\,\mathrm{ms}$.*

- **Polo Caso (Atrofia):**
  $$s_{\text{caso}} = -\frac{1}{10\,000 \cdot (110 \times 10^{-6})} = -0.9091\,\mathrm{rad/s}$$
  *Respuesta dinámica severamente ralentizada con constante de tiempo $\tau_{\text{caso}} \approx 1.1\,\mathrm{s}$.*

[Volver al contenido](#contenido)

---

<a id="matlab"></a>
## Implementación en MATLAB, Simulink y Simscape

En el entorno MATLAB/Simulink se construyen tres representaciones equivalentes para validar la consistencia del modelado:

```
               +---------------------------------------------------+
               |  1. Modelo por Ecuaciones Integro-diferenciales  |
  Entrada F(t) |---> 2. Modelo por Función de Transferencia G(s)   |---> Salida x(t)
               |  3. Circuito Eléctrico Simscape Electrical        |
               +---------------------------------------------------+
```

1. **Ecuaciones de estado/integro-diferenciales:** Implementación mediante bloques continuos de integración, suma y ganancias de Simulink.
2. **Función de transferencia:** Bloques `Transfer Fcn` cargados con los coeficientes analíticos derivados por superposición.
3. **Simscape Electrical:** Red física integrada por fuentes de voltaje, resistores, capacitores y sensores de corriente/voltaje para emular la topología real del circuito análogo.

### Ejecución del script principal de MATLAB

```matlab
% Parámetros del modelo
alpha = 0.25;
Cs = 10e-6;    % 10 uF
Cp = 100e-6;   % 100 uF
R_control = 100;     % 100 Ohm (Sano)
R_caso = 10e3;       % 10 kOhm (Atrofia)

% Funciones de Transferencia de Desplazamiento Gx(s)
num_control = [(1-alpha)*Cp 0];
den_control = [R_control*(Cp+Cs) 1];
Gx_control = tf(num_control, den_control);

num_caso = [(1-alpha)*Cp 0];
den_caso = [R_caso*(Cp+Cs) 1];
Gx_caso = tf(num_caso, den_caso);

% Polos
p_control = pole(Gx_control);
p_caso = pole(Gx_caso);
```

[Volver al contenido](#contenido)

---

<a id="pid"></a>
## Control en lazo cerrado y sintonización PID

Para rehabilitar el comportamiento del caso simulado con atrofia muscular y forzar a que su respuesta siga el patrón dinámico de un individuo sano, se establece un esquema de retroalimentación negativa:

```
         +---------+   e(t)   +---------+  u(t)  +----------+  x_caso(t)
Ve(t) -->| Control |--(+)---->|   PID   |------->| Paciente |----+----> [Scope]
         +---------+   | -    +---------+        |  (Caso)  |    |
          (Sano)       +-------------------------+----------+    |
                       |                                         |
                       +-----------------------------------------+
```

### Definición de la señal de error

$$
e(t) = x_{\text{control}}(t) - x_{\text{caso}}(t)
$$

### Controlador PID

La ley de control sintonizada actúa según:

$$
u(t) = k_P e(t) + k_I \int_0^t e(\tau)\,d\tau + k_D \frac{de(t)}{dt}
$$

### Sintonización mediante PID Tuner

Utilizando la herramienta automática `Tune` del bloque `PID Controller` de Simulink sobre la planta del Caso, se obtienen las ganancias optimizadas ($k_P, k_I, k_D$) para lograr un seguimiento estable, con mínimo sobreimpulso y rápida anulación del error de atrofia.

[Volver al contenido](#contenido)

---

<a id="python"></a>
## Reproducción en Python (VS Code)

El script de Python `musculoesqueletico.py` reproduce computacionalmente la respuesta temporal del sistema utilizando la biblioteca `scipy.signal` y `matplotlib`.

```python
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Parámetros del sistema
alpha = 0.25
Cs = 10e-6
Cp = 100e-6
R_ctrl = 100.0
R_caso = 10000.0

# Funciones de transferencia: G(s) = X(s)/F(s)
# Numerador: (1-alpha)*Cp * s
# Denominador: R*(Cp+Cs) * s + 1

num_ctrl = [(1 - alpha) * Cp, 0]
den_ctrl = [R_ctrl * (Cp + Cs), 1]
sys_ctrl = signal.TransferFcn(num_ctrl, den_ctrl)

num_caso = [(1 - alpha) * Cp, 0]
den_caso = [R_caso * (Cp + Cs), 1]
sys_caso = signal.TransferFcn(num_caso, den_caso)

# Respuesta al impulso unitario t in [0, 10] s
t = np.linspace(0, 10, 1000)
t_ctrl, y_ctrl = signal.impulse(sys_ctrl, T=t)
t_caso, y_caso = signal.impulse(sys_caso, T=t)

# Gráfica comparativa
plt.figure(figsize=(8, 5))
plt.plot(t_ctrl, y_ctrl, 'b-', label='Control (Individuo Sano)')
plt.plot(t_caso, y_caso, 'r--', label='Caso (Atrofia Muscular)')
plt.title('Respuesta al Impulso del Sistema Musculoesquelético')
plt.xlabel('Tiempo [s]')
plt.ylabel('Desplazamiento x(t)')
plt.grid(True)
plt.legend()
plt.savefig('impulse_python.pdf')
plt.show()
```

[Volver al contenido](#contenido)

---

<a id="biologico"></a>
## Diagrama biológico y correlación histofisiológica

Mediante herramientas de ilustración científica (BioRender), se establece la equivalencia biológica entre las estructuras micro/macroscópicas del músculo esquelético y los componentes del modelo formal:

```
+-----------------------------------+-----------------------+-----------------------+
| Estructura Biológica Real         | Elemento Mecánico     | Análogo Eléctrico     |
+-----------------------------------+-----------------------+-----------------------+
| Puentes cruzados de Actina-Miosina| Fuente activa F0(t)   | Fuente de tensión V0  |
| Fuerza total de contracción m.    | Fuerza externa F(t)   | Fuente de tensión V(t)|
| Tendón de inserción / Aponeurosis | Compliancia serie Cs  | Capacitancia Cs       |
| Sarcolema / Epimisio / Endomisio  | Compliancia par. Cp   | Capacitancia Cp       |
| Sarcoplasma y matriz viscosa      | Amortiguador R        | Resistencia R         |
| Deformación / Acortamiento m.     | Desplazamiento x(t)   | Carga eléctrica q(t)  |
+-----------------------------------+-----------------------+-----------------------+
```

[Volver al contenido](#contenido)

---

<a id="resultados"></a>
## Resultados y verificación cruzada

Se realiza una validación cruzada rigurosa entre las cinco herramientas de simulación e implementación:

1. Ecuaciones integro-diferenciales en Simulink.
2. Bloques de función de transferencia en Simulink.
3. Circuito eléctrico en Simscape Electrical.
4. Cuaderno computacional de MATLAB (`.mlx`).
5. Código independiente en Python.

---

<a id="flujo"></a>
## Flujo de trabajo

```mermaid
flowchart TD
    A[Modelo Mecanico de Khoo] --> B[Analogia Electromecanica Fuerza-Voltaje]
    B --> C[Ecuaciones Integro-diferenciales]
    C --> D[Analisis por Superposicion de Fuentes]
    D --> E[Funcion de Transferencia Gs Analitica]
    E --> F[Analisis de Polos y Estabilidad]
    
    E --> G[Simulacion en Simulink: Bloques Gs]
    C --> H[Simulacion en Simulink: Ecuaciones]
    B --> I[Simulacion en Simscape Electrical]
    
    G --> J[Comparacion Lazo Abierto: Control vs Caso Atrofia]
    H --> J
    I --> J
    
    J --> K[Diseno de Retroalimentacion Negativa e(t)]
    K --> L[Sintonizacion de Controlador PID con Tune]
    L --> M[Simulacion Lazo Cerrado en MATLAB]
    
    E --> N[Script de Python en VS Code]
    L --> N
    
    M --> O[Verificacion Cruzada de Resultados]
    N --> O
    O --> P[Diagrama Biologico BioRender]
    P --> Q[Documentacion Final en Repository GitHub]
```

[Volver al contenido](#contenido)

---

<a id="actividades"></a>
## Actividades del estudiante

- [ ] **1. Identificación:** Analizar el modelo mecánico e identificar la función de cada elemento ($F_0, F, R, C_s, C_p, x, x_1$).
- [ ] **2. Analogía:** Construir el circuito eléctrico equivalente respetando las conversiones serie-paralelo.
- [ ] **3. Ecuaciones:** Formular las ecuaciones integro-diferenciales y verificar su equivalencia en Laplace.
- [ ] **4. Superposición:** Derivar analíticamente la función de transferencia $G(s) = \frac{F_s(s)}{F(s)}$ y $G_x(s) = \frac{X(s)}{F(s)}$.
- [ ] **5. Estabilidad:** Calcular analíticamente los polos para $R = 100\,\Omega$ y $R = 10\,\mathrm{k}\Omega$.
- [ ] **6. Simulink:** Implementar los modelos por ecuaciones, función de transferencia y Simscape Electrical.
- [ ] **7. Lazo abierto:** Simular la respuesta al impulso en el intervalo $t \in [0, 10]\,\mathrm{s}$ y contrastar Control vs. Caso.
- [ ] **8. Control PID:** Construir el lazo cerrado en Simulink, definir $e(t) = x_{\text{control}}(t) - x_{\text{caso}}(t)$ y sintonizar $k_P, k_I, k_D$.
- [ ] **9. Python:** Implementar las funciones de transferencia en Python (VS Code) y reproducir las gráficas.
- [ ] **10. Verificación cruzada:** Comprobar que todas las plataformas muestren consistencia numérica exacta.
- [ ] **11. Diagrama biológico:** Elaborar en BioRender la correspondencia histofisiológica del modelo.
- [ ] **12. Reporte GitHub:** Publicar el código, las figuras en PDF, el archivo `CITATION.cff` y redactar este `README.md`.

[Volver al contenido](#contenido)

---

<a id="estructura"></a>
## Estructura del repositorio

```text
.
├── README.md                                      # Reporte principal y guía de práctica
├── CITATION.cff                                   # Archivo de citación bibliográfica del autor
├── Analisis De Circuito Por Superposicion NVA.pdf # Cálculos analíticos por superposición
├── vazquezC20210923.mlx                           # Cuaderno computacional de MATLAB
 vazqeuezC20210923.pdf                             # Cuaderno computacional de MATLAB en formato pdf
├── P3.slx                                         # Diagramas de Simulink y Simscape Electrical
├── vazquezC20210923.py                            # Script de simulación independiente en Python
├── Sistema Musculoesqueletico.png                 # Diagrama de correlación biológica (BioRender)
├── EDOsysmatlab.pdf                               # Gráfica de respuesta en MATLAB
├── simulinkmatlab.pdf                             # Gráfica de respuesta  en MATLAB
├── figura 1 python.png                            # Gráfica de respuesta Python
├── Respuestamatlab.pdf                           # Gráfica de respuesta en MATLAB
   parametros..jpg                              
```

[Volver al contenido](#contenido)

---

<a id="requisitos"></a>
## Requisitos

### Software

- **MATLAB** (R2021a o superior) con **Simulink** y **Control System Toolbox**.
- **Simscape / Simscape Electrical** para la simulación física del circuito.
- **Python 3.8+** con las librerías `numpy`, `scipy` y `matplotlib`.
- **Visual Studio Code** configurado para entorno Python.
- **Git** y cuenta activa en **GitHub**.

[Volver al contenido](#contenido)

---

<a id="reproducibilidad"></a>
## Reproducibilidad y entregables

1. Clonar el repositorio localmente mediante `git clone`.
2. Abrir MATLAB y ejecutar el cuaderno `musculoesqueletico.mlx` para cargar las variables en el Workspace.
3. Simular el modelo `musculoesqueletico.slx` en Simulink.
4. Ejecutar el script `musculoesqueletico.py` desde VS Code.
5. Verificar que las figuras `.pdf` generadas en ambos entornos sean idénticas.

[Volver al contenido](#contenido)

---

<a id="referencias"></a>
## Referencias

[1] M. C. Khoo, *Physiological Control Systems: Analysis, Simulation, and Estimation*, 2nd ed., IEEE Press, 2018.

[2] F. C. Hoppensteadt y C. S. Peskin, *Modeling and Simulation in Medicine and the Life Sciences*, Springer.

[3] J. E. Hall, *Guyton and Hall Textbook of Medical Physiology*, 14th ed., Elsevier, 2021.

[4] K. Ogata, *Ingeniería de Control Moderna*, 5.ª ed., Pearson Educación, 2010.

[5] N. S. Nise, *Control Systems Engineering*, 8th ed., John Wiley & Sons, 2020.

[6] P. A. Valle, *Syllabus para Modelado de Sistemas Fisiológicos*, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B. C., México, 2026.

[7] Tecnológico Nacional de México, *Programa de estudio de la asignatura Modelado de Sistemas Fisiológicos, IBF-1020*.

---

## Uso académico

Este repositorio constituye la evidencia documental y computacional de la práctica **5.5 Modelado y control del sistema musculoesquelético**. Todo el desarrollo ha sido formulado con fines didácticos para la carrera de Ingeniería Biomédica.
