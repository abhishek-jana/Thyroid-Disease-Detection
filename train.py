from thyroid_detection.pipeline.training import TrainingPipeline
from thyroid_detection.config.pipeline.training import ThyroidConfig

if __name__=="__main__":
    training_pipeline_config= ThyroidConfig()
    training_pipeline = TrainingPipeline(thyroid_detection_config=training_pipeline_config)
    training_pipeline.start()
