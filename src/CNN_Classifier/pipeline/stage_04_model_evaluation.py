from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.model_evaluation_mlflow import Evaluation
from CNN_Classifier import logger


STAGE_NAME = "Evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(config=eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()



if __name__ == "__main__":
    try:
        logger.info(f"****************")
        logger.info(f">>>>>>> stage {STAGE_NAME} started<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f'>>>>>>> stage {STAGE_NAME} completed <<<<<<')

    except Exception as e:
        logger.exception(e)
        raise e

