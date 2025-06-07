from chicken_disease_prediction.config.configuration import ConfigurationManager
from chicken_disease_prediction import logger
from chicken_disease_prediction.components.evaluation import Evaluation

STAGE_NAME = "Evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == "__main__":
    try:
        logger.info(f"*************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        evaluation_pipeline = EvaluationPipeline()
        evaluation_pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    
    except Exception as e:
        logger.exception(e)
        raise e
