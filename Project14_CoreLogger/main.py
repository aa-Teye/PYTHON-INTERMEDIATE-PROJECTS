from core_engine.logger import ProductionLogger, LogError

def main():
    # Instantiate the logger with a professional namespace
    logger = ProductionLogger("SYSTEM_CORE")

    try:
        logger.info("Application initialized successfully.")
        
        # Simulating a system event
        database_connected = False
        
        if not database_connected:
            logger.warning("Database connection failed. Using local cache.")
            
        # Simulating a critical failure
        if 10 > 5: # Example condition
            logger.error("Critical: Disk space below 5% threshold.")

    except LogError as e:
        print(f"FAILED TO LOG DATA: {e}")

if __name__ == "__main__":
    main()