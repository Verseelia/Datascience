from src.datascience import logger
from src.datascience .pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.valida import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation import DataTransformationTrainingPipeline
from src.datascience.pipeline.trainer_pipeline import ModelTrainerTrainingPipeline
from src.datascience.pipeline.data_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME="Data Ingestion Stage"

try:
            logger.info(f">>>>>stage {STAGE_NAME} started <<<<<")
            data_ingestion=DataIngestionTrainingPipeline()
            data_ingestion.initiate_data_ingestion()
            logger.info(f">>>>>stage {STAGE_NAME} completed <<<<<")
except Exception as e:
             logger.exception(e)
             raise e

STAGE_NAME="Data Validation Stage"

try:
            logger.info(f">>>>>stage {STAGE_NAME} started <<<<<")
            data_validation=DataValidationTrainingPipeline()
            data_validation.initiate_data_validation()
            logger.info(f">>>>>stage {STAGE_NAME} completed <<<<<")
except Exception as e:
             logger.exception(e)
             raise e
STAGE_NAME="Data Transformation Stage"

try:
            logger.info(f">>>>>stage {STAGE_NAME} started <<<<<")
            data_transformation=DataTransformationTrainingPipeline()
            data_transformation.initiate_data_transformation()
            logger.info(f">>>>>stage {STAGE_NAME} completed <<<<<")
except Exception as e:
             logger.exception(e)
             raise e

STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.initiate_model_training()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

   
        
        