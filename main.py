import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def job():
    print("Tâche exécutée")

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(job, 'interval', seconds=5)  # Exécute job toutes les 5 secondes
    scheduler.start()

    # Garde la boucle en vie
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
