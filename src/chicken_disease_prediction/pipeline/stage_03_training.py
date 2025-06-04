from chicken_disease_prediction.config.configuration import ConfigurationManager
from chicken_disease_prediction import logger
from chicken_disease_prediction.components.training import Training
from chicken_disease_prediction.components.prepare_callbacks import PrepareCallback

STAGE_NAME = "Training Stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()


        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )
    
if __name__ == "__main__":
    try:
        logger.info(f"*************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_training_pipeline = ModelTrainingPipeline()
        model_training_pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    
    except Exception as e:
        logger.exception(e)
        raise e