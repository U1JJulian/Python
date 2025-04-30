import aiohttp
import asyncio
import time
import random
 
async def make_request(session, url, request_id):
    """Función individual para hacer una petición"""
    # Parámetros aleatorios para la prueba
    params = {
        'min_delay': random.uniform(0.05, 0.2),
        'max_delay': random.uniform(0.2, 1.0),
        'error_prob': random.choice([0, 0, 0, 0.1, 0.2])  # 20% de prob. de error
    }
   
    start_time = time.monotonic()
    try:
        async with session.get(url, params=params) as response:
            response_data = await response.json()
            elapsed = time.monotonic() - start_time
           
            result = {
                'id': request_id,
                'status': response.status,
                'time': f"{elapsed:.3f}s",
                'success': response.status == 200,
                'response': response_data if elapsed < 1.0 else "TRUNCATED"
            }
           
            # Mostrar algunos resultados en consola
            if not result['success'] or random.random() < 0.1:
                print(f"Request {request_id}: Status {result['status']} - Time {result['time']}")
           
            return result
    except Exception as e:
        return {
            'id': request_id,
            'error': str(e),
            'time': f"{time.monotonic() - start_time:.3f}s"
        }
 
async def run_load_test(url, total_requests, concurrency):
    """Ejecuta la prueba de carga"""
    connector = aiohttp.TCPConnector(limit=concurrency)
    timeout = aiohttp.ClientTimeout(total=10)
   
    results = []
    start_time = time.time()
   
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        # Crear grupos de tareas para controlar la concurrencia
        for i in range(0, total_requests, concurrency):
            tasks = []
            for j in range(concurrency):
                if i + j >= total_requests:
                    break
                request_id = i + j
                task = asyncio.create_task(make_request(session, url, request_id))
                tasks.append(task)
           
            batch_results = await asyncio.gather(*tasks)
            results.extend(batch_results)
           
            # Pequeña pausa entre batches
            await asyncio.sleep(0.1)
   
    total_time = time.time() - start_time
   
    # Estadísticas
    successful = sum(1 for r in results if r.get('success', False))
    failed = total_requests - successful
   
    print(f"\n{'='*50}")
    print(f"PRUEBA COMPLETADA")
    print(f"Total peticiones: {total_requests}")
    print(f"Concurrencia máxima: {concurrency}")
    print(f"Tiempo total: {total_time:.2f} segundos")
    print(f"Peticiones exitosas: {successful}")
    print(f"Peticiones fallidas: {failed}")
    print(f"Rendimiento: {total_requests/total_time:.2f} req/seg")
    print(f"{'='*50}")
   
    return results
 
if __name__ == '__main__':
    # Configuración
    ENDPOINT_URL = "http://localhost:8080/api/test"
    TOTAL_REQUESTS = 200
    CONCURRENCY = 50  # Número máximo de peticiones simultáneas
   
    # Ejecutar prueba
    asyncio.run(run_load_test(ENDPOINT_URL, TOTAL_REQUESTS, CONCURRENCY))