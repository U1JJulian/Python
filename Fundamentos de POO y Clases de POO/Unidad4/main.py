import asyncio
import random
import time

class SistemaReservas:
    def __init__(self, capacidad_total=10, solicitudes_concurrentes=3):
        """
        Inicializa el Sistema de Reservas.

        Argumentos:
        - capacidad_total: Número máximo de reservas permitidas.
        - solicitudes_concurrentes: Número máximo de solicitudes que pueden procesarse a la vez.
        """
        self.capacidad_total = capacidad_total
        self.reservas_actuales = 0
        self.semaforo = asyncio.Semaphore(solicitudes_concurrentes)  # Controla cuántas solicitudes pueden pasar al mismo tiempo
        self.lock = asyncio.Lock()  # Asegura que las reservas no se modifiquen al mismo tiempo
    
    async def procesar_solicitudes(self, id_cliente):
        """
        Procesa una solicitud de reserva.

        Argumento:
        - id_cliente: Identificador único del cliente.

        Retorna:
        - bool: True si la reserva fue exitosa, False en caso contrario.
        """
        async with self.semaforo:
            print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente}: Procesando solicitud...")
            await asyncio.sleep(random.uniform(0.5, 2))  # Simula tiempo de procesamiento
            
            async with self.lock:  # Solo uno puede acceder a modificar las reservas a la vez
                if self.reservas_actuales < self.capacidad_total:
                    self.reservas_actuales += 1
                    disponibilidad_restante = self.capacidad_total - self.reservas_actuales
                    print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente}: Reserva CONFIRMADA. Disponibilidad restante: {disponibilidad_restante}/{self.capacidad_total}")
                    return True
                else:
                    print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente}: Reserva RECHAZADA por falta de disponibilidad.")
                    return False

    async def cancelar_reserva(self, id_cliente):
        """
        Cancela una reserva ya hecha por un cliente.

        Argumento:
        - id_cliente: Identificador único del cliente.
        """
        await asyncio.sleep(random.uniform(0.3,1))
        
        async with self.lock:
            if self.reservas_actuales > 0:
                self.reservas_actuales -=1
                print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente}: Reserva CANCELADA. Disponibilidad ahora: {self.capacidad_total - self.reservas_actuales}/{self.capacidad_total}")
            else:
                print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente}: No hay reservas para cancelar.")
    
    async def cliente(sistema, id_cliente):
        """
        Simula el comportamiento de un cliente que intenta hacer una reserva.

        Argumento:
                 -sistema: Instancia de SistemaReservas
                 -id_cliente: Identificador unico del cliente
        """

        try:
            print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente}: Intentando realizar reserva.")
            reserva_exitosa = await sistema.procesar_solicitudes(id_cliente)
            if reserva_exitosa:
                if random.random() < 0.3:
                    await asyncio.sleep(random.uniform(1,3))
                    await sistema.cancelar_reserva(id_cliente)
            else:
                if random.random() < 0.5:
                    espera = random.uniform(0.5,3)
                    print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente}: Esperando para volver a intentar.")
                    await asyncio.sleep(espera)
                    print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente}: Reintentando reserva.")
                    await sistema.procesar_solicitudes(id_cliente)
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] Cliente {id_cliente}: Error: {e}.")

async def main():
    sistema = SistemaReservas(capacidad_total=10,solicitudes_concurrentes=3)
    cliente = [SistemaReservas.cliente(sistema,i)for i in range(1,16)] #15 clientes
    await asyncio.gather(*cliente)
    print(f"[{time.strftime('%H:%M:%S')}] Todas las solicitudes han sido procesadas.")
    print(f"[{time.strftime('%H:%M:%S')}] Reservas actuales: {sistema.reservas_actuales}/{sistema.capacidad_total}")          

if __name__ == "__main__":
    print("Iniciando el sistema de reservas...")
    asyncio.run(main())