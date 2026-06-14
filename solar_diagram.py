import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(1, 1, figsize=(20, 28))
ax.set_xlim(0, 20)
ax.set_ylim(0, 28)
ax.axis('off')
fig.patch.set_facecolor('#F0F4F8')

# ─────────────────────────────────────────────
# COLORES
# ─────────────────────────────────────────────
COLOR_SOLAR    = '#FFF9C4'
COLOR_INVERSOR = '#E3F2FD'
COLOR_BATERIA  = '#E8F5E9'
COLOR_CARGAS   = '#FFF3E0'
COLOR_GEN      = '#FCE4EC'
COLOR_MON      = '#F3E5F5'
COLOR_RESUMEN  = '#ECEFF1'
BORDER_SOLAR   = '#F9A825'
BORDER_INV     = '#1565C0'
BORDER_BAT     = '#2E7D32'
BORDER_CARGAS  = '#E65100'
BORDER_GEN     = '#B71C1C'
BORDER_MON     = '#6A1B9A'
BORDER_RESUMEN = '#37474F'

def draw_box(ax, x, y, w, h, title, lines, bg, border, title_color='white', title_bg=None):
    if title_bg is None:
        title_bg = border
    # Sombra
    shadow = FancyBboxPatch((x+0.08, y-0.08), w, h,
                             boxstyle="round,pad=0.1",
                             facecolor='#CCCCCC', edgecolor='none', zorder=1)
    ax.add_patch(shadow)
    # Cuerpo
    box = FancyBboxPatch((x, y), w, h,
                          boxstyle="round,pad=0.1",
                          facecolor=bg, edgecolor=border,
                          linewidth=2, zorder=2)
    ax.add_patch(box)
    # Título
    title_box = FancyBboxPatch((x, y+h-0.55), w, 0.55,
                                boxstyle="round,pad=0.05",
                                facecolor=title_bg, edgecolor=border,
                                linewidth=2, zorder=3)
    ax.add_patch(title_box)
    ax.text(x + w/2, y + h - 0.27, title,
            ha='center', va='center', fontsize=9,
            fontweight='bold', color=title_color, zorder=4)
    # Contenido
    line_h = (h - 0.65) / max(len(lines), 1)
    for i, line in enumerate(lines):
        ypos = y + h - 0.65 - line_h * i - line_h * 0.5
        ax.text(x + 0.2, ypos, line,
                ha='left', va='center', fontsize=7.5,
                color='#212121', zorder=4,
                fontfamily='monospace')

def draw_arrow(ax, x1, y1, x2, y2, label='', color='#455A64', lw=2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=lw, connectionstyle='arc3,rad=0.0'))
    if label:
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        ax.text(mx + 0.15, my, label,
                ha='left', va='center', fontsize=7,
                color=color, style='italic',
                bbox=dict(boxstyle='round,pad=0.2',
                          facecolor='white', edgecolor=color,
                          alpha=0.85))

def draw_double_arrow(ax, x1, y1, x2, y2, label='', color='#455A64'):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='<->', color=color,
                                lw=2))
    if label:
        mx = (x1+x2)/2
        my = (y1+y2)/2
        ax.text(mx+0.15, my, label,
                ha='left', va='center', fontsize=7,
                color=color, style='italic',
                bbox=dict(boxstyle='round,pad=0.2',
                          facecolor='white', edgecolor=color,
                          alpha=0.85))

# ─────────────────────────────────────────────
# TÍTULO
# ─────────────────────────────────────────────
title_box = FancyBboxPatch((0.5, 26.8), 19, 1.0,
                            boxstyle="round,pad=0.1",
                            facecolor='#1565C0', edgecolor='#0D47A1',
                            linewidth=3, zorder=2)
ax.add_patch(title_box)
ax.text(10, 27.35, '☀️  SISTEMA SOLAR OFF-GRID — CASITA',
        ha='center', va='center', fontsize=15,
        fontweight='bold', color='white', zorder=3)
ax.text(10, 27.05, 'San Rafael, Mendoza  |  Sistema 48V DC / 220V AC  |  Off-Grid 100%',
        ha='center', va='center', fontsize=9,
        color='#BBDEFB', zorder=3)

# ─────────────────────────────────────────────
# 1. PANELES SOLARES
# ─────────────────────────────────────────────
draw_box(ax, 0.5, 23.2, 19, 3.4,
         '☀️  6x PANELES SOLARES TOPCon Bifaciales 590W  —  3.540W Total',
         [
             '  Panel 1    Panel 2    Panel 3    Panel 4    Panel 5    Panel 6',
             '   590W       590W       590W       590W       590W       590W',
             '',
             '  Potencia Total: 3.540W               Producción estimada: ~18 kWh/día (6 HSP)',
             '  Voc: 51,30V  |  Vmp: 42,67V         Isc: 14,63A  |  Imp: 13,83A',
             '  Eficiencia: 22,8%                    Temp. trabajo: -40°C a +85°C',
         ],
         COLOR_SOLAR, BORDER_SOLAR)

# ─────────────────────────────────────────────
# FLECHA PANELES → INVERSOR
# ─────────────────────────────────────────────
draw_arrow(ax, 10, 23.2, 10, 22.5,
           '  DC 6mm² | MC4 | Fusibles | DPS DC',
           color=BORDER_SOLAR, lw=2.5)

# ─────────────────────────────────────────────
# 2. INVERSOR
# ─────────────────────────────────────────────
draw_box(ax, 0.5, 19.0, 19, 4.0,
         '⚡  GROWATT SPF 6000ES  —  Inversor / Cargador Off-Grid  48V',
         [
             '  ┌── MPPT SOLAR (x2) ──────────┐  ┌── INVERSOR DC→AC ──┐  ┌── CARGADOR AC ───┐',
             '  │  Entrada máx:  8.000W        │  │  Salida: 6.000W    │  │  Entrada: 230VAC  │',
             '  │  Rango MPPT: 120-450V DC     │  │  230V / 50Hz       │  │  Corriente: 80A   │',
             '  │  Voc máx:    500V DC         │  │  Onda senoidal pura│  │  Rango: 170-280V  │',
             '  │  2 MPPT / 16A por MPPT       │  │  Eficiencia: 93%   │  │  Auto-detección   │',
             '  └──────────────────────────────┘  └────────────────────┘  └───────────────────┘',
             '',
             '  Protección pico: 12.000VA   |   Voltaje sistema: 48V DC',
             '  Monitoreo WiFi: ShinePhone   |   Arranque auto generador: Relé contacto seco ✅',
         ],
         COLOR_INVERSOR, BORDER_INV)

# ─────────────────────────────────────────────
# FLECHA INVERSOR → BATERÍA
# ─────────────────────────────────────────────
draw_double_arrow(ax, 4.0, 19.0, 4.0, 17.8,
                  '  48V DC | 50mm² | ANL 150A',
                  color=BORDER_BAT)

# ─────────────────────────────────────────────
# FLECHA INVERSOR → CARGAS
# ─────────────────────────────────────────────
draw_arrow(ax, 15.5, 19.0, 15.5, 17.8,
           '  220V CA | Protec. AC\n  Disyuntor diferencial',
           color=BORDER_CARGAS, lw=2.5)

# ─────────────────────────────────────────────
# 3. BATERÍA
# ─────────────────────────────────────────────
draw_box(ax, 0.5, 13.8, 8.5, 3.8,
         '🔋  PYLONTECH US5000  —  LiFePO4 48V',
         [
             '  Capacidad:       4,8 kWh',
             '  Útil (90% DoD):  4,3 kWh',
             '  Voltaje nominal: 48V',
             '  Corriente:       100Ah',
             '  Ciclos:          ~6.000',
             '  Garantía:        10 años',
             '  Autonomía:       ~8-9h (sin splits)',
             '',
             '  BMS inteligente ✅',
             '  Comunicación: CAN / RS485 → Growatt',
             '  Pre-carga integrada ✅',
             '  Display LED: 🟢🟢🟢🟢🟢 = 100%',
         ],
         COLOR_BATERIA, BORDER_BAT)

# ─────────────────────────────────────────────
# 4. CARGAS
# ─────────────────────────────────────────────
draw_box(ax, 10.5, 13.8, 9.0, 3.8,
         '🏠  CARGAS DE LA CASITA',
         [
             '  💡 Luces LED       100W × 5h  =  0,50 kWh/día',
             '  🖥️  TV + Laptops    220W × 4h  =  0,88 kWh/día',
             '  ❄️  Mini Heladera   100W × 8h  =  0,80 kWh/día',
             '  📱 Celulares/otros  50W × 24h  =  1,20 kWh/día',
             '  🔧 Soldadora Inv.   3.520W  (uso ocasional)',
             '',
             '  ──────────────────────────────────────────',
             '  CONSUMO ESTIMADO SIN SPLITS:  ~3 kWh/día',
             '  CONSUMO ESTIMADO CON 2 SPLITS: ~11 kWh/día',
         ],
         COLOR_CARGAS, BORDER_CARGAS)

# ─────────────────────────────────────────────
# FLECHA GENERADOR → INVERSOR
# ─────────────────────────────────────────────
draw_arrow(ax, 10, 13.4, 10, 14.0,
           '  220V CA | Arranque automático\n  2 hilos contacto seco',
           color=BORDER_GEN, lw=2.5)

# ─────────────────────────────────────────────
# 5. GENERADOR
# ─────────────────────────────────────────────
draw_box(ax, 0.5, 10.0, 19, 3.2,
         '⛽  GENERADOR DE RESPALDO  —  Inverter Naftero 4.500W',
         [
             '  Potencia: 4.500W / 4,5 kVA  |  Tipo: Inverter (onda senoidal pura)  |  Arranque: Eléctrico + Manual',
             '  Voltaje salida: 220V monofásico  |  Arranque automático vía relé Growatt ✅',
             '',
             '  CONFIGURACIÓN AUTOMÁTICA EN GROWATT:',
             '  🔴  Arrancar generador cuando batería llegue a:  25% SoC',
             '  🟢  Apagar  generador cuando batería llegue a:  85% SoC',
             '  ⏱️   Tiempo mínimo de funcionamiento:            30 minutos',
             '  🌙  Horario silencioso (no arrancar):           22:00 — 07:00',
             '  ⏳  Tiempo de carga batería (25% → 85%):        ~5 a 6 horas',
         ],
         COLOR_GEN, BORDER_GEN)

# ─────────────────────────────────────────────
# 6. MODOS DE OPERACIÓN
# ─────────────────────────────────────────────
draw_box(ax, 0.5, 6.8, 9.0, 3.0,
         '🔁  MODOS DE OPERACIÓN',
         [
             '  ☀️  DÍA SOLEADO:',
             '      Paneles → Inversor → Cargas + Carga batería',
             '      Batería llena en ~1,5 horas',
             '',
             '  🌙  NOCHE:',
             '      Batería → Inversor → Cargas (~8-9h)',
             '',
             '  ⛅  DÍA NUBLADO:',
             '      Paneles reducidos + Batería → Cargas',
             '',
             '  ❄️  BATERÍA BAJA (25%):',
             '      Generador arranca SOLO → carga batería',
             '      Se apaga SOLO al llegar al 85%',
         ],
         '#EDE7F6', '#4527A0')

# ─────────────────────────────────────────────
# 7. MONITOREO
# ─────────────────────────────────────────────
draw_box(ax, 10.5, 6.8, 9.0, 3.0,
         '📱  MONITOREO REMOTO  —  ShinePhone App',
         [
             '  Módulo WiFi Growatt Shine (~USD 20)',
             '',
             '  Desde cualquier lugar del mundo:',
             '  ☀️  Generación solar en tiempo real (W)',
             '  🏠  Consumo actual (W)',
             '  🔋  Estado de carga batería (%)',
             '  ⚡  Corriente carga / descarga',
             '  🌡️  Temperatura del inversor',
             '  📊  Historial diario y mensual (kWh)',
             '  🚨  Alertas automáticas',
             '  Sin costo mensual ✅',
         ],
         COLOR_MON, BORDER_MON)

# ─────────────────────────────────────────────
# 8. RESUMEN
# ─────────────────────────────────────────────
draw_box(ax, 0.5, 0.3, 19, 6.3,
         '📋  RESUMEN DE ESPECIFICACIONES DEL SISTEMA',
         [
             '',
             '  COMPONENTE              ESPECIFICACIÓN',
             '  ─────────────────────────────────────────────────────────────────────',
             '  Paneles Solares         6x TOPCon Bifacial 590W = 3.540W total',
             '  Inversor/Cargador       Growatt SPF 6000ES  |  6.000W nominal  |  12.000VA pico',
             '  Batería                 Pylontech US5000  |  LiFePO4 48V  |  4,8 kWh  |  6.000 ciclos',
             '  Generador Respaldo      Inverter Naftero 4.500W  |  Arranque automático',
             '  ─────────────────────────────────────────────────────────────────────',
             '  Generación estimada     ~18 kWh/día  (6 HSP San Rafael, Mendoza)',
             '  Almacenamiento útil     4,3 kWh  (90% DoD)',
             '  Potencia de salida      6.000W nominal  /  12.000W pico',
             '  Autonomía nocturna      ~8 a 9 horas  (sin splits)',
             '  Voltaje del sistema     48V DC',
             '  Voltaje de salida       220V CA  —  Onda Senoidal Pura',
             '  Tipo de sistema         Off-Grid 100%',
             '  Ubicación               San Rafael, Mendoza, Argentina',
             '  Monitoreo               App ShinePhone  (gratuita, acceso remoto)',
         ],
         COLOR_RESUMEN, BORDER_RESUMEN,
         title_color='white', title_bg=BORDER_RESUMEN)

# ─────────────────────────────────────────────
# GUARDAR
# ─────────────────────────────────────────────
plt.tight_layout()
plt.savefig('sistema_solar_casita.png',
            dpi=180, bbox_inches='tight',
            facecolor=fig.get_facecolor())
plt.show()
print("✅ Imagen guardada como: sistema_solar_casita.png")
