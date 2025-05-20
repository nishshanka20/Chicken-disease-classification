from chicken_disease_prediction.config.configuration import ConfigurationManager
from chicken_disease_prediction.components.prepare_base_model import PrepareBaseModel
from chicken_disease_prediction import logger

STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        prepare_base_model_config=config.get_prepare_base_model_config()
        prepare_base_model=PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        logger.info(f"{STAGE_NAME} completed successfully.")
    
if __name__=="__main__":
    try:
        logger.info(f"*************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        prepare_base_model_training_pipeline=PrepareBaseModelTrainingPipeline()
        prepare_base_model_training_pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    
    except Exception as e:
        logger.exception(e)
        raise e