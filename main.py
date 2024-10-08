from Chicken_Disease_Classification import logger
from Chicken_Disease_Classification.pipeline.stage_01_data_ingestion import DataIngestionTarinigPipeline
from Chicken_Disease_Classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainigPipeline
from Chicken_Disease_Classification.pipeline.stage_03_training import ModelTrainingPipeline
from Chicken_Disease_Classification.pipeline.stage_04_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f"Starting {STAGE_NAME}")
        data_ingestion = DataIngestionTarinigPipeline()
        data_ingestion.main()
        logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
        logger.error(f"{STAGE_NAME} failed! Error: {str(e)}")
        raise e                                 

STAGE_NAME = "Prepare Base Model"
try:
        logger.info(f"Starting {STAGE_NAME}")
        obj = PrepareBaseModelTrainigPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
        logger.error(f"{STAGE_NAME} failed! Error: {str(e)}")
        raise e

STAGE_NAME = "Training"
try:
        logger.info(f"Starting {STAGE_NAME}")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
        logger.error(f"{STAGE_NAME} failed! Error: {str(e)}")
        raise e


STAGE_NAME = "Evaluation"
try:
        logger.info(f"Starting {STAGE_NAME}")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
        logger.error(f"{STAGE_NAME} failed! Error: {str(e)}")
        raise e