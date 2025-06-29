from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.TextSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline


stage_name = "Data Ingestion Stage"
try:
    logger.info(f"{stage_name} initiated")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{stage_name} completed")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = "Data Transformation Stage"
try:
    logger.info(f"{stage_name} initiated")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"{stage_name} completed")
except Exception as e:
    logger.exception(e)
    raise e