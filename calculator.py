class MetricCalculator:
    def __init__(self):
        self.results = []

    def calculate_mean(self, data):
        if not isinstance(data, list):
            raise TypeError('输入格式必须为列表')
        if len(data) == 0:
            return 0
        return sum(data) / len(data)

    def calculate_accuracy(self, y_true, y_pred):
        if not isinstance(y_true, list) or not isinstance(y_pred, list):
            raise TypeError("y_true和y_pred的格式必须为列表")
        if len(y_true) != len(y_pred):
            return None
        if len(y_true) == 0:
            return 0

        correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        return correct / len(y_true)

    def add_metric(self, name, value):
        self.results.append((name, value))

    def get_results(self):
        return self.results
