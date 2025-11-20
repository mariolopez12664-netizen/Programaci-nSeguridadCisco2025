import time
import random

# Aqui vamos a usar las --- Estructuras de Datos ---
HOSTS = []
REPORTE_VULNERABILIDADES = {}

# Aqui vamos a usar las --- Funciones ---

def RegistrarHost(ip: str):
    """Registra un host y lo inicializa en el reporte."""
    if ip not in HOSTS:
        HOSTS.append(ip)
        REPORTE_VULNERABILIDADES[ip] = []
        print(f"✅ Host {ip} registrado.")
    else:
        print(f"⚠️ Host {ip} ya existe.")

def AnalizarVulnerabilidades(ip: str):
    """Simula el escaneo y registra vulnerabilidades aleatorias."""
    if ip not in HOSTS:
        print(f"❌ Host {ip} no encontrado.")
        return

    print(f"\n--- 🔎 Escaneando {ip} ---")
    servicios_abiertos = ['SSH (22)', 'HTTP (80)', 'FTP (21)']
    
    # Prueva de la Simulación 
    for servicio in servicios_abiertos:
        if random.choice([True, False, False]): # 33% de probabilidad de vulnerabilidad
            riesgo = random.choice(['ALTO', 'MEDIO', 'BAJO'])
            
            v = {
                'servicio': servicio,
                'riesgo': riesgo,
                'desc': f"Vulnerabilidad en {servicio} detectada.",
                'fecha': time.strftime("%Y-%m-%d")
            }
            # Registrar la vulnerabilidad
            REPORTE_VULNERABILIDADES[ip].append(v)
            print(f"🚨 Vulnerabilidad encontrada en {servicio} (Riesgo: {riesgo})")
            
    print(f"✅ Escaneo de {ip} completado.")

def MostrarReporte(ip: str):
    """Muestra el reporte consolidado de un host."""
    print(f"\n--- 📄 REPORTE DE {ip} ({time.strftime('%H:%M:%S')}) ---")
    
    if not REPORTE_VULNERABILIDADES.get(ip):
        print("ℹ️ Sin vulnerabilidades registradas.")
        return

    vulnerabilidades = REPORTE_VULNERABILIDADES[ip]
    print(f"**Total de hallazgos:** {len(vulnerabilidades)}")

    # Bucle y Condicional: Mostrar el detalle y calcular el riesgo
    puntaje_riesgo = sum(3 if v['riesgo'] == 'ALTO' else 2 if v['riesgo'] == 'MEDIO' else 1 for v in vulnerabilidades)
    
    for v in vulnerabilidades:
        print(f"[{v['riesgo']}] {v['desc']} - Servicio: {v['servicio']}")

    print(f"--- RIESGO CONSOLIDADO: **{puntaje_riesgo} Puntos** ---")

# ----------------------------------------------------------------------
# --- PRUEBA (Ejecución) ---
# ----------------------------------------------------------------------
RegistrarHost("192.168.1.1")
RegistrarHost("10.0.0.5")

AnalizarVulnerabilidades("192.168.1.1")
AnalizarVulnerabilidades("10.0.0.5")

MostrarReporte("192.168.1.1")
MostrarReporte("10.0.0.5")