import logging

from ai.logging_setup import setup_logging
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from datasets import load_dataset

setup_logging()

DATA_SET_NAME = 'IMDB'
MODEL_NAME = 'google-bert/bert-base-uncased'

def sentiment_test():
    logging.info(f'[开始] 下载数据集 {DATA_SET_NAME} ...')
    dataset = load_dataset(DATA_SET_NAME).shuffle()
    logging.info(f'[完成] 下载数据集 {DATA_SET_NAME}')

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)

    inputs = tokenizer(dataset['train']['text'][:10], truncation=True, padding=True, return_tensors="pt")
    outputs = model(**inputs)

    predictions = outputs.logits.argmax(dim=-1)
    labels = dataset['train']['label'][:10]

    logging.info(f'predictions 大小为 {predictions.size()}, labels 大小为 {len(labels)}')

    for (i, (prediction, label)) in enumerate(zip(predictions, labels)):
        prediction_value = prediction #.item()
        prediction_label = '正面' if prediction_value == 1 else '负面'
        actual_label = '正面' if label == 1 else '负面'
        logging.info(f'样本[{i}]: 预测：{prediction_label}, 实际: {actual_label}')


if __name__ == '__main__':
    sentiment_test()
