class CustomException1(BaseException):
    pass


class CustomException2(BaseException):
    pass


class CustomException3(BaseException):
    pass


class CustomProcessor:
    def process_a_object(self, a_object):
        try:
            a_object.method1("")
        except CustomException1 as e:
            print(f"Error occurred in method1: {e}")

        try:
            a_object.method2(200)
        except CustomException2 as e:
            print(f"Error occurred in method2: {e}")

        try:
            a_object.method3(123)
        except CustomException3 as e:
            print(f"Error occurred in method3: {e}")


class A:
    def method1(self, param):
        if not param:
            raise CustomException1("Parameter is empty.")

    def method2(self, value):
        if value > 100:
            raise CustomException2("Value is too big.")

    def method3(self, data):
        if isinstance(data, int):
            raise CustomException3("Data should be a string.")


a_object = A()
processor = CustomProcessor()

processor.process_a_object(a_object)